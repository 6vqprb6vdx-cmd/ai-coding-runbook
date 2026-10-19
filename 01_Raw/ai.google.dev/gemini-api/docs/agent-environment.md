---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr
fetched_at: 2026-10-19T05:31:03.157374+00:00
title: "Y\u00f6netilen arac\u0131lar\u0131n ortamlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yönetilen aracıların ortamları

Ortamlar, Linux'ta yönetilen sanal alanlardır. Bu alanlar, ajanlara kodu yürütmek ve dosyaları kalıcı hale getirmek için yalıtılmış bir yer sağlar. Etkileşim bağlamından bağımsız oldukları için aynı ortamı birden fazla etkileşimde yeniden kullanabilir veya istediğiniz zaman sıfırdan başlayabilirsiniz.

Aşağıdaki örnekte, yeni bir uzak ortamla nasıl etkileşim oluşturulacağı ve bu ortamın kimliğinin nasıl alınacağı gösterilmektedir:

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

## `environment` parametresi

`environment` parametresi üç biçimi kabul eder:

| Form | Örnek | Ne zaman kullanılır? |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | Yeni bir sanal alan sağlayın. |
| Ortam Kimliği | `environment="env_abc123"` | Tüm dosyaları ve paketleriyle birlikte mevcut bir sanal ortamı yeniden kullanın. |
| Yapılandırma nesnesi | `environment={...}` | Kaynaklar, ağ kuralları, ortam değişkenleri veya bunların bir kombinasyonuyla yeni bir korumalı alan sağlayın. |

Aşağıdaki örneklerde `environment`
parametresinin üç kullanım şekli gösterilmektedir.

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

## Ortam yapılandırma

Bir ortam oluşturmanın bir yolu, ajana hangi yazılımların yüklenmesi gerektiğini söylemektir.
Bağımlılık çözümünü ve sorun gidermeyi yönetir. Ortam hazır olduğunda `environment_id` dosyasını kaydedin ve yeniden kullanın.

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

### Bir kaynaktan bağlama

Temsilcinin hangi dosyalara ihtiyacı olduğunu tam olarak biliyorsanız yineleme yapmak yerine dosyaları tek bir çağrıda bağlayın. `environment` yapılandırma nesnesi, üç tür içeren bir `sources` dizisi kabul eder:

| Kaynak türü | `type` değer | Açıklama | Sınır |
| --- | --- | --- | --- |
| Git kod deposu | `repository` | Bir URL'den alınan depoyu `target` konumundaki sanal alana kopyalar. | 500 MB |
| Cloud Storage | `gcs` | Cloud Storage'daki bir dosyayı veya dizini `target` konumundaki sanal ortama kopyalar. | 2 GB |
| Satır içi içerik | `inline` | Ham metin içeriğini `target` konumundaki sanal alanda bir dosyaya yazar. | Dosya başına 1 MB, toplam 2 MB |

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

Her iki yaklaşımı da birleştirebilirsiniz: Bilinen kaynakları bildirimli olarak bağlayın, ardından paketleri yüklemek veya kurulum komut dosyalarını çalıştırmak için takip etkileşimleriyle yineleme yapın. Özel kaynak eklerken hedef olarak kök (`/`) ayarlayamazsınız, her zaman bir alt dizin belirtmeniz gerekir.

### Dikkat çekici girişler

Ayrıca, araçlar her yürütüldüğünde güvenlik sınırlarını zorunlu kılmak veya otomatik doğrulamalar çalıştırmak için `.agents/hooks.json` yapılandırma dosyası ve özel yakalama komut dosyalarını korumalı alana monte edebilirsiniz. Şema tanımları ve kod örnekleri için [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=tr) başlıklı makaleyi inceleyin.

### Özel kaynaklar

Ayrıca, ağ yapılandırmasında kaynak alanını doğrulayarak özel GitHub depolarından veya özel Cloud Storage kovalarından da indirebilirsiniz.

Bir seçenek, kimliğe göre referans verilen depolanmış bir [kimlik bilgisidir](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr). Bu nedenle, gizli anahtarı bir kez depolarsınız ve bu kaynağa ihtiyaç duyan her ortam, gizli anahtara referans verebilir:

```
"network": {
    "allowlist": [
        { "domain": "github.com", "credential": "github-production" },
        { "domain": "*" }
    ]
}
```

Ayrıca, aşağıdaki örneklerde olduğu gibi başlığı `transform` ile satır içi olarak da ayarlayabilirsiniz. Çıkış proxy'si her iki formu da aynı şekilde uygular ve hiçbir durumda gizli anahtar korumalı alanın içine yerleştirilmez.

**Özel Git depoları** için `Basic` kimlik doğrulamasını [GitHub kişisel erişim jetonunuzla (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) kullanın.
Kullanıcı adı olarak `x-oauth-basic` değerini kullanarak jetonu kodlayın:

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
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            )))
            .build()
    ))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
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

**Özel Cloud Storage paketleri** için standart bir OAuth 2.0 Bearer jetonu kullanın:

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
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("*.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer YOUR_GCS_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            )))
            .build()
    ))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "*.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer YOUR_GCS_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
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

## Önceden yüklenmiş yazılım

Sandbox, Ubuntu üzerinde çalışır ve çalışma zamanları ile yaygın paketler önceden yüklenmiş olarak gelir. Aracı, `pip
install` veya `npm install` kullanarak çalışma zamanında ek paketler yükleyebilir. Etkileşim sırasında yüklenen paketler, aynı `environment_id`'yı yeniden kullandığınızda kalıcı olur.

| Kategori | Önceden yüklenmiş paketler |
| --- | --- |
| **UNIX araçları** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite` ve `typescript` |

## Ortam değişkenleri

Korumalı alanda ortam değişkenlerini ayarlamak için `env` alanını kullanın. Her giriş, bir değişken adını yapılandırma için değişmez bir dizeyle veya bir sır için depolanmış [kimlik bilgisine](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr) yapılan bir referansla eşler. Ajan, bunları herhangi bir kabukta olduğu gibi görür. Bu nedenle, işlem ortamından okuyan araçlar ve komut dosyaları bunları ek kablolama olmadan alır.

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `env` | `object` | Değişken adının değerle eşlemesi. Değer, `string` değişmezi veya `{"credential": "credential-id"}` biçiminde bir kimlik bilgisi referansıdır. |

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

Değişkenler, kabuk komutları, derleme adımları ve başlattığı tüm işlemler dahil olmak üzere temsilcinin bu etkileşimde çalıştırdığı her komut için geçerlidir.

Bu iki değer türü farklı şekilde davranır. Değişken olmayan bir dize, kapsayıcıya düz metin olarak yazılır. Kimlik bilgisi referansı: değişken bir yer tutucu alır ve çıkış proxy'si, gerçek sırrı yalnızca bu kimlik bilgisinin güvenilir alanlarına yapılan giden isteklerde değiştirir. Bu işlemin nasıl çalıştığını öğrenmek için [Kimlik bilgilerini ortam değişkeni olarak kullanma](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr#environment-variables) başlıklı makaleyi inceleyin.

## Ağ yapılandırması

Varsayılan olarak, ortamların sınırsız giden ağ erişimi vardır. Giden trafiği belirli alan adlarıyla kısıtlamak için `network` alanını kullanın. Her kural, `domain` değerinin yanı sıra depolanmış bir sır yerleştirmek için isteğe bağlı bir `credential` ve eşleşen isteklere başlık yerleştirmek için isteğe bağlı bir `transform` nesnesi belirtir.
Bu başlıklar etkileşim başına benzersiz olabilir ve aynı ortam için güncellenebilir.

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `domain` | `string` | Eşleştirilecek alan. Tüm alanlar için tam ana makine adı veya `*` kullanın. |
| `credential` | `string` | Depolanan [kimlik bilgisinin](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr) kimliği. Çıkış proxy'si bunu çözer ve istek sırasında kimlik doğrulama başlığını ekler. |
| `transform` | `object` | Eşleşen isteklere yerleştirilecek başlıkları temsil eden düz anahtar/değer çiftlerini içeren nesne (ör. `{"Authorization": "Bearer ..."}`). |

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
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_your_github_token"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build(),
                AllowlistEntry.builder().domain("*").build()
            )))
            .build()
    ))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
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
            })),
        })),
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

İzin verilenler listesi ayarlandığında yalnızca açıkça listelenen alanlara yapılan isteklere izin verilir. Alt alan adlarını eşleştirmek için joker karakterler (ör. `{"domain":
"*.example.com"}`) kullanabilirsiniz ancak bunun, ayrı olarak eklenmesi gereken kök alanla
`example.com` eşleşmediğini unutmayın. Diğer tüm trafiğe (ör. eklenmiş üstbilgiler olmadan listelenmemiş alanları yönlendirme) izin vermek için `{"domain": "*"}` öğesini genel bir giriş olarak ekleyin.

### Kimlik bilgileri

Giden trafiğin kimliğini doğrulamanın iki yolu vardır: kimliğe göre referans verilen depolanmış bir kimlik bilgisi ve izin verilenler listesi kuralında satır içi `transform`. Çıkış proxy'si hem kablolu hem de kablosuz bağlantılarda geçerli olduğundan gizli anahtar hiçbir zaman sanal ortama girmez ve etkileşim yüklerinizde görünmez.

Gizliyi bir kez depolayıp yeniden kullanmak istediğinizde [yönetilen kimlik bilgisi](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr) kullanmanız gerekir. Projenizdeki her ortam, aracı ve tetikleyici aynı kimliğe başvurabilir ve bu kimliği tek bir yerden döndürebilirsiniz.

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

`oauth2` kimlik bilgisi, erişim jetonunu kendi başına da yeniler. Böylece, jetonun süresi dolduğunda uzun süren etkileşim kesintiye uğramaz. Kimlik bilgisi türlerinin ve yönetim işlemlerinin tam listesi için [Kimlik bilgileri](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr) başlıklı makaleye bakın.

Üstbilgileri `transform` ile satır içi olarak da ayarlayabilirsiniz. Bu, değer tek bir çağrıya ait olduğunda (ör. etkileşimi oluşturmadan hemen önce oluşturduğunuz bir jeton) uygundur. Bu şekilde ayarlanan başlıklar aynı çıkış proxy'si tarafından yerleştirilir.
Bunlar, ortam değişkenleri veya dosyalar olarak korumalı alanda hiçbir zaman kullanıma sunulmaz.

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
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer " + gcloudToken
                    )))
                    .build()
            )))
            .build()
    ))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer " + gcloudToken,
                    })),
                },
            })),
        })),
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

`credential` ve `transform` aynı kuralda görünebilir. Öncelikle kimlik bilgisi uygulanır ve `transform` üstte birleştirilir. Bu nedenle, her ikisi de aynı anahtarı ayarlarsa açık bir `transform` başlığı kazanır. Yaygın bir kalıp, kimlik doğrulama üstbilgisi için bir kimlik bilgisi ve hizmetin yanında beklediği ek üstbilgiler için bir `transform` içerir.

### Ağ erişimini devre dışı bırakma

Tüm giden ağ erişimini engellemek için `network` değerini `disabled` olarak ayarlayın:

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

### Kimlik bilgilerini yenileme

Erişim jetonları ve kısa ömürlü API anahtarları gibi satır içi jetonların süresi dolar.
Mevcut `environment_id` ile birlikte yeni bir `network` yapılandırmasını bir sonraki etkileşimde ileterek bunları yenileyebilirsiniz. Yeni ağ kuralları, önceki kuralların yerini tamamen alırken ortamın dosya sistemi durumu (yüklü paketler, dosyalar, depolar) korunur.

Bunun yerine depolanmış bir [kimlik bilgisi](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr) kullanıyorsanız bu bilgiye ihtiyacınız yoktur. `oauth2` kimlik bilgisi kendi kendini yeniler ve herhangi bir kimlik bilgisinin döndürülmesi, izin verilenler listesindeki her kuralı etkilemeden kimlik bilgisinde `PATCH` işlemidir.

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
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer INITIAL_TOKEN"
                    )))
                    .build()
            )))
            .build()
    ))
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
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer REFRESHED_TOKEN"
                    )))
                    .build()
            )))
            .build()
    ))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer INITIAL_TOKEN",
                    })),
                },
            })),
        })),
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer REFRESHED_TOKEN",
                    })),
                },
            })),
        })),
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

## Ortam yaşam döngüsü

Ortamlar şu yaşam döngüsünü izler:

| Eyalet | Davranış |
| --- | --- |
| **Oluşturuldu** | Bir etkileşimde `environment: "remote"` veya bir yapılandırma nesnesi belirtildiğinde sağlanır. |
| **Etkin** | Bir etkileşim devam ederken çalıştırılır. |
| **Boşta** | Otomatik anlık görüntü alma ve 15 dakika işlem yapılmadığında durdurulur. |
| **Çevrimdışı** | Son etkinliğin üzerinden 7 gün geçene kadar saklanır. Kimliği iletilerek devam ettirilebilir. |
| **Silindi** | 7 günlük TTL saklama süresi dolduktan sonra veya manuel olarak silindiğinde sistemden otomatik olarak kaldırılır. |

## Environments API

Sandbox oturumlarını programatik olarak yönetmek için Environments API'yi kullanabilirsiniz.
Ortamları numaralandırarak etkin oturum kimliklerini keşfedebilir ve uzun süren bir görev sırasında istemci bağlantısı sonlanırsa durumu kurtarabilirsiniz. Ayrıca, iş akışları tamamlandığında oturum meta verilerini inceleyebilir ve ortamları açıkça silebilirsiniz. Bunun için otomatik TTL süresinin dolmasını beklemeniz gerekmez.

### Ortamları listeleme

Projenize ait etkin ortamları listeler. Yanıt grup boyutunu kontrol etmek için sayfalama parametrelerini kullanın.

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

Yanıt, aşağıdakine benzer şekilde görünür:

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

### Ortam alma

Belirli bir ortamın meta verilerini ve yapılandırma ayrıntılarını kaynak adına göre alın.

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

Yanıt, aşağıdakine benzer şekilde görünür:

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

### Ortam silme

Görevleriniz veya işlem hatlarınız tamamlandığında sandbox kaynaklarını temizlemek için bir ortamı açıkça sonlandırın ve silin.

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

## Ortamdaki dosyaları yönetme

Temsilci, yürütme sırasında sanal ortamda dosyalar oluşturur ve değiştirir. Dizin içeriklerine göz atabilir, dosya meta verilerini alabilir, tek tek dosyaları veya dizinlerin tamamını tar arşivleri olarak indirebilir ve dosyaları doğrudan ortama yükleyebilir ya da arşivleri ayıklayabilirsiniz. Korumalı alan ortamlarındaki depolama alanı, adil kullanım sınırlarına tabidir.

### Bir dizindeki dosyaları listeleme

Ortamdaki bir dizinin içeriğini listeler. Varsayılan olarak kök dizini listeler.

#### Sorgu parametreleri

| Parametre | Tür | Açıklama |
| --- | --- | --- |
| `recursive` | boole | `true` kullanıldığında tüm dosyalar ve dizinler tekrar tekrar listelenir. Varsayılan: `false`. |

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

Yanıt, her girişin meta verilerini içeren bir `files` dizisi döndürür:

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

#### Dosya giriş alanları

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `name` | dize | Dosya veya dizin adı. |
| `path` | dize | Ortam köküne göre tam yol. |
| `type` | dize | `FILE` veya `DIRECTORY` |
| `size_bytes` | dize | Dosyanın bayt cinsinden boyutu (yalnızca dosyalar). |
| `mime_type` | dize | MIME türü (yalnızca dosyalar). |
| `created` | dize | ISO 8601 oluşturma zaman damgası. |
| `modified` | dize | ISO 8601 son değiştirilme zaman damgası. |

### Dosya meta verilerini alma

Belirli bir dosyanın meta verilerini yola göre alın.

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

Yanıt, `files` dizisine sarılmış dosya meta verilerini döndürür:

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

Dosya mevcut değilse API `404` hatası döndürür:

```
{
  "error": {
    "message": "Path 'nonexistent.txt' not found in environment 'ENV_ID'.",
    "code": "not_found"
  }
}
```

### Tek bir dosyayı indirme

Belirli bir dosyanın içeriğini indirme SDK'larda `download()` yöntemini kullanın. REST isteklerinde, `?alt=media` sorgu parametresini dosya yoluna ekleyin. Sunucu, `200 OK` ile yanıt verir ve işlenmemiş dosya içeriğini yayınlar.

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

### Dizini tar arşivi olarak indirme

Dizin yolunu `?alt=media` ile isteyerek dizinin tamamını tar arşivi olarak indirin. Bu işlem, POSIX tar dosyası (gziplenmemiş) döndürür. İç içe yerleştirilmiş alt dizinleri dahil etmek için `recursive=true` öğesini kullanın.

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

#### Davranış matrisi

Aşağıdaki davranış matrisi, dosya ve dizin uç noktaları, HTTP yöntemleri ve sorgu parametreleri genelinde beklenen yanıt ve arşiv davranışını özetlemektedir:

| İstek | `alt` | `recursive` | `extract` | `overwrite` | Yanıt |
| --- | --- | --- | --- | --- | --- |
| `GET /files` | (hiçbiri) | (hiçbiri) | - | - | Kök dizinin JSON listesi |
| `GET /files/{path}` (dosya) | (hiçbiri) | - | - | - | Dosyanın JSON meta verileri |
| `GET /files/{path}` (dir) | (hiçbiri) | `false` | - | - | Alt öğelerin JSON listesi |
| `GET /files/{path}` (dir) | (hiçbiri) | `true` | - | - | Tüm alt öğelerin JSON listesi |
| `GET /files/{path}?alt=media` (dosya) | `media` | - | - | - | Ham dosya içeriği |
| `GET /files/{path}?alt=media` (dir) | `media` | `false` | - | - | Dizindeki dosyaların tar arşivi |
| `GET /files/{path}?alt=media` (dir) | `media` | `true` | - | - | Tüm dosyaların tar arşivini yinelemeli olarak oluşturur. |
| `GET /files?alt=media` | `media` | `false` | - | - | Yalnızca kök düzeyindeki dosyaların tar arşivi |
| `PUT /files/{path}` (dosya) | - | - | `false` | `false` | Dosyayı yola yazar. Zaten varsa `409 Conflict` değerini döndürür. |
| `PUT /files/{path}?overwrite=true` | - | - | `false` | `true` | Yoldaki dosyayı yazar veya üzerine yazar. |
| `PUT /files/{path}?extract=true` | - | - | `true` | `false` | Arşivi hedef dizine açar. Herhangi bir hedef dosya varsa `409 Conflict` değerini döndürür. |
| `PUT /files/{path}?extract=true&overwrite=true` | - | - | `true` | `true` | Arşivi açar ve mevcut dosyaları değiştirir. |

### Ortama dosya yükleme

HTTP `PUT` kullanarak tek tek dosyaları veya dizin arşivlerini doğrudan mevcut bir ortam sandbox'ına yükleyin. Üst dizinler mevcut değilse otomatik olarak oluşturulur. Ortamlardaki depolama alanı, adil kullanım sınırlarına tabidir.

#### Tek bir dosya yükleme

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

Yanıt, yüklenen dosyanın meta verilerini döndürür. Bu meta veriler, liste ve get uç noktalarıyla tutarlılık sağlamak için `files` dizisine sarılır:

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

#### Dizin arşivi yükleme ve çıkarma

Tek bir istekte kod tabanının veya dizin yapısının tamamını başlatmak için `extract=true` ile `.tar` veya `.tar.gz` arşivi yükleyin.

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

Yanıt, arşiv tarafından yazılan her dosyayı listeler:

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

#### Devam ettirilebilir oturumla büyük dosyaları yükleme

Büyük yükler için veya güvenilir olmayan bir bağlantı üzerinden yükleme yaparken tüm gövdeyi tek bir istekte göndermek yerine devam ettirilebilir bir oturum kullanın. Devam ettirilebilir yükleme, aktarımı ayrı ayrı yeniden denenebilecek parçalara böler. Bu nedenle, yarıda kalan bir yükleme işlemi baştan başlamanıza neden olmaz.

`uploadType=resumable` ile oturumu başlatarak başlayın. Boş bir gövde gönderin ve yüklemek istediğiniz yükün medya türünü ve toplam boyutunu bildirmek için `X-Upload-Content-Type` ve `X-Upload-Content-Length` üstbilgilerini kullanın:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable HTTP/1.1
Host: generativelanguage.googleapis.com
X-Upload-Content-Type: application/octet-stream
X-Upload-Content-Length: 20971520
Content-Length: 0
x-goog-api-key: $GEMINI_API_KEY
```

Yanıt, `Location` üstbilgisinde oturum URL'sini taşır. Bu URL zaten `upload_id` içerdiğinden API anahtarına tekrar ihtiyaç duymaz:

```
HTTP/1.1 200 OK
Location: https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY
Content-Length: 0
```

Yükü bu URL'ye parçalar halinde yükleyin. Her parça, bayt aralığını ve toplam boyutu `Content-Range` başlığıyla bildirir:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 0-10485759/20971520
Content-Length: 10485760

<10 MB binary payload>
```

Son parça hariç her parça `308 Resume Incomplete` değerini döndürür. `Range` üstbilgisi, sunucunun kaç baytlık yer ayırdığını gösterir. Bir parça başarısız olursa bu noktadan devam edersiniz:

```
HTTP/1.1 308 Resume Incomplete
Range: bytes=0-10485759
Content-Length: 0
```

Kalan parçaları da aynı şekilde gönderin:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 10485760-20971519/20971520
Content-Length: 10485760

<remaining 10 MB binary payload>
```

Son parça, yükleme işlemini tamamlar ve dosya meta verilerini tek seferlik yüklemeyle aynı `files` zarf içinde döndürür:

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

Devam ettirilebilir oturumlar `extract` ve `overwrite` ile de çalışır. Bu sorgu parametrelerini tek tek parçalarda değil, başlatma isteğinde ayarlayın.

#### Üzerine yazma koruması

Varsayılan olarak `overwrite`, `false`'dir. Hedef yol zaten varsa istek `409 Conflict` hatası döndürür ve hiçbir şey yazılmaz:

```
{
  "error": {
    "message": "Requested entity already exists",
    "code": "aborted"
  }
}
```

Mevcut bir dosyayı veya dizini değiştirmek için `overwrite=true` değerini ayarlayın (veya REST'te `?overwrite=true` değerini ekleyin). `extract=true` ile çakışma kontrolü, arşivdeki her dosya için geçerli olur. Bu nedenle, herhangi bir hedef dosya varsa istek başarısız olur.

### Tam anlık görüntüyü indir (kullanımdan kaldırıldı)

Mevcut kodu ortam dosyaları API'sine taşımak için:

- **Python**: Eski dosya indirme isteklerini aşağıdakilerle değiştirin:

  ```
  archive = client.environments.files.download(
      environment="YOUR_ENVIRONMENT_ID",
      path="workspace",
  )
  with open("snapshot.tar", "wb") as f:
      f.write(archive)
  ```
- **JavaScript**: Eski dosya indirme isteklerini aşağıdakilerle değiştirin:

  ```
  const bytes = await client.environments.files.download({
      environment: "YOUR_ENVIRONMENT_ID",
      path: "workspace",
  });
  fs.writeFileSync("snapshot.tar", Buffer.from(bytes));
  ```
- **REST**: `GET /v1beta/files/environment-$ENV_ID:download?alt=media` yerine şunu kullanın:

  ```
  curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -o snapshot.tar
  ```

## Fiyatlandırma ve kaynaklar

Her ortam, sabit kaynak ayırmalarıyla çalışır:

| Kaynak | Değer |
| --- | --- |
| **CPU** | 4 çekirdek |
| **Bellek** | 16 GB |

Önizleme döneminde ortam işlem (CPU, bellek, korumalı alan yürütme) için **ücret alınmaz**. Aracı jetonu maliyetleri için
[Fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing-for-agents) bölümüne bakın.

## Sınırlamalar

- **Önizleme durumu:** Ortamlar ve yönetilen aracılar önizleme aşamasındadır. Özellikler ve şemalar değişebilir.
- **Satır içi kaynak boyutu:** Satır içi kaynaklar, dosya başına 1 MB ve tüm dosyalar için toplamda 2 MB ile sınırlıdır.
- **Kaynak boyutu**: Git depoları 500 MB, Cloud Storage depoları ise 2 GB ile sınırlıdır.
- **Ortam başlatma:** Yeni bir ortamın sağlanması yaklaşık 5 saniye sürer. Büyük kaynak depoları bu süreyi uzatabilir.
- **Ortamın süresinin dolması:** Etkin olmayan çevrimdışı ortamlar, otomatik TTL temizliği kullanılarak süreleri dolmadan önce 7 gün boyunca saklanır. Süresi dolmuş veya geçersiz bir ortam kimliği iletildiğinde `404 Not Found` hatası döndürülür.
- **Dosya desteği:** Ajan şu anda metin ve resim dosyalarını okumakla sınırlıdır. İkili program dosyası desteği henüz kullanılamamaktadır.
- **Kökten bağlama yok:** Özel kaynak eklerken hedef olarak kökü (`/`) ayarlayamazsınız, her zaman bir alt dizin belirtmeniz gerekir.

## Sırada ne var?

- [Ajanlara Genel Bakış](https://ai.google.dev/gemini-api/docs/agents?hl=tr): Yönetilen ajanların temel kavramları hakkında bilgi edinin.
- [Hızlı başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr): Çok aşamalı etkileşimler ve akışla geliştirmeye başlayın.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr): Varsayılan aracın özelliklerini, araçlarını, model seçimini ve fiyatlandırmasını keşfedin.
- [Özel Ajanlar Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr): `AGENTS.md` ve `SKILL.md` kullanarak kendi ajanlarınızı tanımlayın.
- [Kancalar](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=tr): Güvenlik korumalarını zorunlu kılın ve korumalı alan içinde yan etki doğrulamaları çalıştırın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-07 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-07 UTC."],[],[]]
