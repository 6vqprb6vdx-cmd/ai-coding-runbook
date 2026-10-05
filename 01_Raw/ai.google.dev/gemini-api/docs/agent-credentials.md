---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr
fetched_at: 2026-10-05T06:29:11.093134+00:00
title: "Y\u00f6netilen arac\u0131lardaki kimlik bilgileri \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yönetilen aracılardaki kimlik bilgileri

Kimlik bilgileri, sunucu tarafından yönetilen ve gizli anahtarın hiçbir zaman aracının ortamına girmediği üçüncü taraf hizmetlerine erişmesine olanak tanıyan gizli anahtarlardır. Kimlik bilgisini bir kez saklar, kimliğe göre referans verirsiniz. Çıkış proxy'si, istek sırasında kimlik bilgisini çözümler ve ekler.

Gizli değerler yalnızca yazılabilir. Depolandıktan sonra hiçbir uç nokta tarafından döndürülmezler. Bu nedenle, güvenliği ihlal edilmiş bir aracı, kullandığı jetonları geri okuyamaz.

Kimlik bilgisini kullandığınız birincil yer, [`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr) üzerindeki ağ izin verilenler listesidir. Önce sırrı saklayın:

### Python

```
from google import genai

client = genai.Client()

credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});

console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:    "github-production",
            Token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Credential ID: %s, Status: %v\n", res.Credential.ID, res.Credential.GetStatus())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

Ardından, kimliğini doğruladığı alana ekleyin:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Triage the open issues in my-org/my-repo.",
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
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Triage the open issues in my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ],
        },
    },
});
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
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Triage the open issues in my-org/my-repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
                    Allowlist: []interactions.AllowlistEntry{
                        {Domain: "api.github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "*"},
                    },
                }))),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Triage the open issues in my-org/my-repo.",
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

Aracı artık `api.github.com` için kimliği doğrulanmış istekler gönderiyor ve jeton hiçbir zaman sanal alan içinde bulunmuyor.

## Yeterlilik belgesi türleri

Her kimlik bilgisinin, hangi alanları kabul edeceğini ve proxy'nin bunu nasıl uygulayacağını belirleyen bir `type` vardır.

| Tür | Kullanım alanı | Davranış |
| --- | --- | --- |
| `bearer_token` | Kişisel erişim jetonları, bot jetonları, statik API anahtarları | Proxy, jetonu istek başlığı olarak yerleştirir. Yenileme mantığı yoktur. |
| `oauth2` | OAuth uygulamaları ve kullanıcı tarafından temsil edilen akışlar | Proxy, yenileme jetonunu erişim jetonlarıyla değiştirir ve süreleri doldukça bunları yeniler. |
| `environment_variable` | Gizli dizileri işlem ortamından okuyan istemci SDK'ları | Temsilcinin ortamı bir yer tutucu alır. Proxy, giden isteklerde gerçek sırrın yerine geçer. |

## Ağın izin verilenler listesindeki kimlik bilgilerini kullanma

İzin verilenler listesi kuralına `credential` eklediğinizde proxy, bu alana yapılan her giden isteğin kimliğini doğrular. Bu yöntem, bir temsilciye özel API'ye, özel depoya veya özel pakete erişim vermek için önerilir.

Aynı izin verilenler listesinde kimliği doğrulanmış ve doğrulanmamış kuralları birlikte kullanabilirsiniz:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Sync the open Jira issues into the tracking sheet in my repo.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app",
            }
        ],
        "network": {
            "allowlist": [
                {"domain": "github.com", "credential": "github-production"},
                {"domain": "api.atlassian.com", "credential": "jira-oauth"},
                {"domain": "*.googleapis.com"},
            ]
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Sync the open Jira issues into the tracking sheet in my repo.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app",
            },
        ],
        network: {
            allowlist: [
                { domain: "github.com", credential: "github-production" },
                { domain: "api.atlassian.com", credential: "jira-oauth" },
                { domain: "*.googleapis.com" },
            ],
        },
    },
});
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
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Sync the open Jira issues into the tracking sheet in my repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Sources: []interactions.Source{
                    {
                        Type:   interactions.SourceTypeRepository.ToPointer(),
                        Source: genai.Ptr("https://github.com/your-org/backend"),
                        Target: genai.Ptr("/backend-app"),
                    },
                },
                Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
                    Allowlist: []interactions.AllowlistEntry{
                        {Domain: "github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "api.atlassian.com", Credential: genai.Ptr("jira-oauth")},
                        {Domain: "*.googleapis.com"},
                    },
                }))),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Sync the open Jira issues into the tracking sheet in my repo.",
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
                { "domain": "github.com", "credential": "github-production" },
                { "domain": "api.atlassian.com", "credential": "jira-oauth" },
                { "domain": "*.googleapis.com" }
            ]
        }
    }
}'
```

Proxy, kimlik bilgisini istek başına çözdüğünden `oauth2` kimlik bilgisi, erişim jetonunu şeffaf bir şekilde yeniler. Uzun süren bir etkileşim, erişim jetonunun süresi dolduğunda kesintiye uğramaz.

### `credential` ve `transform`'ı birleştirme

İzin verilenler listesi kuralları, doğrudan kuralda başlıkları ayarlayan satır içi [`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#private-sources) nesnesini de kabul eder. Her iki mekanizma da kablodaki çıkış proxy'si tarafından uygulanır. Bu nedenle, her iki durumda da üstbilgi değeri hiçbir zaman sanal alan içinde bulunmaz. Her iki alan da aynı kuralda görünebilir.

| Kural yapılandırması | Davranış |
| --- | --- |
| Yalnızca `credential` | Proxy, kimlik bilgisini çözer ve alanla ilgili her isteğe başlığını ekler. |
| Yalnızca `transform` | Statik başlık yerleştirme. Yazdığınız başlıklar olduğu gibi gönderilir. |
| Her ikisi de | Önce kimlik bilgisi uygulanır, ardından `transform` üstte birleştirilir. Her ikisi de aynı anahtarı ayarlarsa açık bir `transform` başlığı öncelikli olur. |
| Hiçbiri | Alana izin verilir ve herhangi bir başlık eklenmez. |

Bir sırrı bir kez saklamak ve projenizdeki her ortamda, aracıda ve tetikleyicide buna referans vermek istediğinizde ve erişim jetonu yenileme ve döndürme işlemlerinin sizin için yapılmasını istediğinizde kimlik bilgisi kullanmak mantıklıdır. Satır içi `transform`, değer tek bir çağrıya ait olduğunda (ör. etkileşimi oluşturmadan hemen önce kendiniz oluşturduğunuz bir jeton) uygundur.

İkisinin bir arada kullanılması yaygındır. Kimlik bilgisi, kimlik doğrulama üstbilgisini taşır ve `transform`, aynı istekte yukarı akış hizmetinin beklediği diğer her şeyi ekler:

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

Bir sırrı satır içi `transform` öğesinden kimlik bilgisine taşımak için `POST /credentials` ile birlikte saklayın, `transform` öğesindeki kimlik doğrulama başlığını `"credential": "<id>"` ile değiştirin ve `transform` nesnesinin geri kalanını olduğu gibi bırakın.

## MCP sunucularıyla kimlik bilgilerini kullanma

Uzak MCP sunucuları aynı `credential` alanını alır. `mcp_server` aracında ayarlayın. Proxy, kimlik doğrulama üst bilgisini bu sunucuya yapılan her isteğe ekler:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Create a new issue in my-org/my-repo",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "github",
        "url": "https://api.githubcopilot.com/mcp",
        "credential": "github-production",
    }],
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Create a new issue in my-org/my-repo",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "github",
        url: "https://api.githubcopilot.com/mcp",
        credential: "github-production",
    }],
});
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
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Create a new issue in my-org/my-repo"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
                    Allowlist: []interactions.AllowlistEntry{
                        {Domain: "api.githubcopilot.com", Credential: genai.Ptr("github-production")},
                    },
                }))),
            })),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("github"),
                    URL:  genai.Ptr("https://api.githubcopilot.com/mcp"),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Create a new issue in my-org/my-repo",
    "environment": "remote",
    "tools": [
        {
            "type": "mcp_server",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp",
            "credential": "github-production"
        }
    ]
}'
```

`credential` ve `headers`, izin verilenler listesiyle aynı öncelik kuralına tabidir.
Kimlik bilgisi önce uygulanır ve `headers` üstte birleştirilir. Bu nedenle, her ikisi de aynı anahtarı ayarlarsa açık bir başlık kazanır:

```
{
    "type": "mcp_server",
    "name": "jira",
    "url": "https://jira.atlassian.com/mcp",
    "credential": "jira-oauth",
    "headers": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

Bir sırrı satır içi `headers` öğesinden kimlik bilgisine taşımak için `POST /credentials` ile saklayın ve `headers` öğesindeki kimlik doğrulama girişini `credential` ile değiştirin.
Diğer başlıkları olduğu gibi bırakın.

## Kimlik bilgilerini ortam değişkeni olarak kullanma

Bazı istemci kitaplıkları, sırları istek üstbilgisi olarak kabul etmek yerine işlem ortamından okur. Soket modu ve uzun anket istemcileri yaygın olarak kullanılır.

`environment_variable` kimlik bilgisini `environment.env` altındaki bir değişken adına bağlayın:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the sync script and check notifications.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": {"credential": "slack-bot-token"},
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the sync script and check notifications.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            SLACK_BOT_TOKEN: { credential: "slack-bot-token" },
        },
    },
});
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
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Run the sync script and check notifications."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Env: genai.Ptr(interactions.NewEnv(map[string]interactions.EnvVar{
                    "NODE_ENV":        {Value: genai.Ptr("production")},
                    "SLACK_BOT_TOKEN": {Credential: genai.Ptr("slack-bot-token")},
                })),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Run the sync script and check notifications.",
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": { "credential": "slack-bot-token" }
        }
    }
}'
```

`env`, değişmez dizeleri ve kimlik bilgisi referanslarını yan yana kabul eder. Dize değişmezi, kapsayıcıya normal bir düz metin değişkeni olarak yerleştirilir.

Kimlik bilgisi referansı değildir. Değişken, yer tutucuyu (`__GEMINI_CRED_<credential-id>__`) alır ve proxy, yalnızca kimlik bilgilerinin `trusted_domains` bölümündeki bir alana giden giden istekler için gerçek gizliyi değiştirir. Başka bir alana yapılan istekler reddedilir. Böylece, gizli anahtar hiçbir zaman sınırın dışına çıkmaz ve yerine yer tutucu gönderilmez.

Her `environment_variable` kimlik bilgisinde `trusted_domains` ayarlayın. Bu, sırrın kullanılabileceği kapsamları belirleyen kontroldür.

## Kimlik bilgisi oluşturma

Her oluşturma isteği için `type` ve bu türün gerektirdiği alanlar gerekir.

REST doğrudan çağrıldığında tüm alan adları snake\_case kullanır. camelCase
alanı göndermek `400` döndürür.

### Hamiline ait jeton

Bir taşıyıcı jeton kimlik bilgisinin yalnızca `token` olması gerekir:

### Python

```
credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:    "github-production",
            Token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

Yanıt yalnızca meta verileri döndürür, jetonu asla döndürmez:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

Proxy varsayılan olarak `Authorization: Bearer <token>` gönderir. Başka bir şey bekleyen bir hizmeti hedeflemek için `header_name` ve `prefix` değerlerini geçersiz kılın:

### Python

```
credential = client.credentials.create(
    id="my-api-key",
    type="bearer_token",
    token="key_xxxxxxxxxxxx",
    header_name="x-goog-api-key",
    prefix="",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "my-api-key",
    type: "bearer_token",
    token: "key_xxxxxxxxxxxx",
    header_name: "x-goog-api-key",
    prefix: "",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:         "my-api-key",
            Token:      "key_xxxxxxxxxxxx",
            HeaderName: genai.Ptr("x-goog-api-key"),
            Prefix:     genai.Ptr(""),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "my-api-key",
    "type": "bearer_token",
    "token": "key_xxxxxxxxxxxx",
    "header_name": "x-goog-api-key",
    "prefix": ""
}'
```

Bu yapılandırma, `x-goog-api-key: key_xxxxxxxxxxxx` başlığını oluşturur.

Aşağıdaki tabloda `header_name` ve `prefix` değerlerinin nasıl birleştiği gösterilmektedir:

| Yapılandırma | Yerleştirilmiş üstbilgi |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

OAuth2 kimlik bilgisi için `client_id`, `client_secret`, `refresh_token` ve `token_url` gerekir. `scopes` alanı isteğe bağlıdır:

### Python

```
credential = client.credentials.create(
    id="jira-oauth",
    type="oauth2",
    client_id="my-client-id",
    client_secret="my-client-secret",
    token_url="https://auth.atlassian.com/oauth/token",
    refresh_token="rt_xxxxxxxxxxxxxxxxxxxx",
    scopes=["read:jira-work", "write:jira-work"],
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "jira-oauth",
    type: "oauth2",
    client_id: "my-client-id",
    client_secret: "my-client-secret",
    token_url: "https://auth.atlassian.com/oauth/token",
    refresh_token: "rt_xxxxxxxxxxxxxxxxxxxx",
    scopes: ["read:jira-work", "write:jira-work"],
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.OAuth2Config{
            ID:           "jira-oauth",
            ClientID:     "my-client-id",
            ClientSecret: "my-client-secret",
            TokenURL:     "https://auth.atlassian.com/oauth/token",
            RefreshToken: "rt_xxxxxxxxxxxxxxxxxxxx",
            Scopes:       []string{"read:jira-work", "write:jira-work"},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created OAuth2 credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "jira-oauth",
    "type": "oauth2",
    "client_id": "my-client-id",
    "client_secret": "my-client-secret",
    "token_url": "https://auth.atlassian.com/oauth/token",
    "refresh_token": "rt_xxxxxxxxxxxxxxxxxxxx",
    "scopes": ["read:jira-work", "write:jira-work"]
}'
```

OAuth2 kimlik bilgisi oluşturmak, yapılandırmanın çalıştığını onaylamak için `token_url` ile canlı jeton değişimi gerçekleştirir. Kimlik bilgisi yalnızca sağlayıcı, `access_token` içeren başarılı bir jeton yanıtı döndürürse saklanır. Hem JSON hem de form-urlencoded yanıtları kabul edilir.

Bu, oluşturma sırasında geçerli ve süresi dolmamış bir yenileme jetonuna ihtiyacınız olduğu anlamına gelir. Sağlayıcı, değişimi reddederse hata size döndürülür:

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

Depolandıktan sonra proxy, erişim jetonlarının süresi doldukça bunları yeniler. Sağlayıcı, yenileme jetonlarını döndürürse ve yenileme sırasında yeni bir jeton döndürürse yeni jeton, depolanan jetonun yerini otomatik olarak alır.

### Ortam değişkeni

`environment_variable` kimlik bilgisi için `value` ve `injection_location` gerekir:

### Python

```
credential = client.credentials.create(
    id="slack-bot-token",
    type="environment_variable",
    value="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains=["*.slack.com", "slack.com"],
    injection_location="header",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "slack-bot-token",
    type: "environment_variable",
    value: "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains: ["*.slack.com", "slack.com"],
    injection_location: "header",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.EnvironmentVariableConfig{
            ID:                "slack-bot-token",
            Value:             "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
            TrustedDomains:    []string{"*.slack.com", "slack.com"},
            InjectionLocation: credentials.NewEnvironmentVariableConfigInjectionLocation(credentials.InjectionLocationEnumHeader),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created environment variable credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "slack-bot-token",
    "type": "environment_variable",
    "value": "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    "trusted_domains": ["*.slack.com", "slack.com"],
    "injection_location": "header"
}'
```

`injection_location` alanı, proxy'ye giden istekte sırrın nerede değiştirileceğini bildirir. Bir hizmetin birden fazla değere ihtiyacı olduğunda `header`, `query` veya `body` değerlerini tek bir dize ya da dizi olarak kabul eder:

```
"injection_location": ["header", "query"]
```

Yerine koyma işlemi yalnızca listelediğiniz konumlarda gerçekleşir. Yer tutucuyu başka bir yerde taşıyan istekler, iletilmek yerine reddedilir.

Kimliği bir değişken adına bağlamak için [Kimlikleri ortam değişkeni olarak kullanma](#environment-variables) başlıklı makaleyi inceleyin.

### Oluşturulan kimlikler

`id` alanı isteğe bağlıdır. Bu parametreyi atladığınızda hizmet bir UUID oluşturur:

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

Etkileşimlerde kullanmak üzere sabit ve okunabilir bir referans istediğinizde kendi kimliğinizi sağlayın. Kimlik, kaynak yolunda göründüğünden kısa çizgi veya alt çizgi içeren küçük alfanümerik karakterler tercih edilir.

## Kimlik bilgilerini listeleme

Projenize ait kimlik bilgilerini listeleyin. Yanıt grup boyutunu kontrol etmek için sayfalama parametrelerini kullanın.

### Python

```
response = client.credentials.list(page_size=10)
for credential in response.credentials:
    print(f"Credential ID: {credential.id}, Type: {credential.type}")
```

### JavaScript

```
const response = await client.credentials.list({ page_size: 10 });
for (const credential of response.credentials) {
    console.log(`Credential ID: ${credential.id}, Type: ${credential.type}`);
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.List(ctx, operations.ListCredentialsRequest{
        PageSize: genai.Ptr(10),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, cred := range res.CredentialListResponse.Credentials {
        fmt.Printf("Credential ID: %s, Type: %v\n", cred.ID, cred.GetType())
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials?page_size=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

Yanıtta yalnızca meta veriler var:

```
{
  "credentials": [
    {
      "id": "github-production",
      "type": "bearer_token",
      "status": "active",
      "create_time": "2026-07-15T10:00:00.000000000Z",
      "update_time": "2026-07-15T10:00:00.000000000Z"
    },
    {
      "id": "jira-oauth",
      "type": "oauth2",
      "status": "active",
      "create_time": "2026-07-15T10:05:00.000000000Z",
      "update_time": "2026-07-15T10:05:00.000000000Z"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

Sonraki sayfayı getirmek için `next_page_token` değerini `page_token` olarak geri iletin. Başka sonuç olmadığında alan atlanır.

| Parametre | Tür | Açıklama |
| --- | --- | --- |
| `page_size` | tam sayı | Sayfa başına maksimum kimlik bilgisi sayısı. |
| `page_token` | dize | Önceki bir yanıttaki `next_page_token` jetonu. |

## Yeterlilik belgesi edinme

Belirli bir kimlik bilgisinin meta verilerini kimliğine göre alma

### Python

```
credential = client.credentials.get(id="github-production")
print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
const credential = await client.credentials.get("github-production");
console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Get(ctx, operations.GetCredentialRequest{
        ID: "github-production",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Credential ID: %s, Status: %v\n", res.Credential.ID, res.Credential.GetStatus())
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

Yanıt, aşağıdakine benzer şekilde görünür:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

Mevcut olmayan bir kimlik bilgisi istenirse `404` döndürülür:

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## Kimlik bilgisini döndürme

İzin verilenler listesi kuralına, araç tanımına veya ona referans veren ortam değişkenine dokunmadan bir sırrı değiştirin. Rotasyon, bir sonraki proxy çözümünde geçerli olur.

İstek, `type` ve değiştirmek istediğiniz alanları içermelidir. Atladığınız alanlar mevcut değerlerini korur.

Hamiline ait jetonu döndürme:

### Python

```
credential = client.credentials.update(
    id="github-production",
    type="bearer_token",
    token="ghp_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("github-production", {
    type: "bearer_token",
    token: "ghp_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Update(ctx, operations.UpdateCredentialRequest{
        ID: "github-production",
        Body: credentials.NewCredentialUpdate(credentials.HTTPBearerUpdateConfig{
            Token: genai.Ptr("ghp_new_xxxxxxxxxxxxxxxxxxxx"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Updated credential %s at %v\n", res.Credential.ID, res.Credential.GetUpdateTime())
}
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "bearer_token",
    "token": "ghp_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

OAuth2 yenileme jetonunu döndürme:

### Python

```
credential = client.credentials.update(
    id="jira-oauth",
    type="oauth2",
    refresh_token="rt_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("jira-oauth", {
    type: "oauth2",
    refresh_token: "rt_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Update(ctx, operations.UpdateCredentialRequest{
        ID: "jira-oauth",
        Body: credentials.NewCredentialUpdate(credentials.OAuth2UpdateConfig{
            RefreshToken: genai.Ptr("rt_new_xxxxxxxxxxxxxxxxxxxx"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Updated credential %s at %v\n", res.Credential.ID, res.Credential.GetUpdateTime())
}
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/jira-oauth" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "oauth2",
    "refresh_token": "rt_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

Yanıt, yeni `update_time`'ı yansıtıyor:

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

Kimlik bilgilerinin `type` oluşturma sırasında sabitlenir. Değiştirmek için kimlik bilgisini silip yenisini oluşturun.

## Kimlik bilgisini silme

Artık ihtiyaç duyulmayan kimlik bilgilerini ve depolanmış sırlarını silin.

### Python

```
client.credentials.delete(id="github-production")
```

### JavaScript

```
await client.credentials.delete("github-production");
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Credentials.Delete(ctx, operations.DeleteCredentialRequest{
        ID: "github-production",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

Başarılı bir silme işlemi boş bir nesne döndürür:

```
{}
```

Kimliğe hâlâ referans veren tüm izin verilenler listesi kuralları, araçları veya ortam değişkenleri çözümlenemez. Bu nedenle, önce bunları güncelleyin.

## Alan referansı

Her kimlik bilgisi için ortak olan alanlar:

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `id` | dize | Hayır | Benzersiz tanımlayıcı. Atlandığında UUID olarak oluşturulur. |
| `type` | dize | Evet | Şunlardan biri: `bearer_token`, `oauth2`, `environment_variable`. |
| `status` | dize | Salt okunur | Kimlik bilgisinin mevcut durumu. |
| `create_time` | dize | Salt okunur | RFC 3339 oluşturma zaman damgası. |
| `update_time` | dize | Salt okunur | Son güncellemenin RFC 3339 zaman damgası. |

`bearer_token` için alanlar:

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `token` | dize | Evet | Salt yazma. Jeton değeri. |
| `header_name` | dize | Hayır | Eklenecek üstbilgi. Varsayılan olarak `Authorization` değerine ayarlanır. |
| `prefix` | dize | Hayır | Değer öneki. Varsayılan olarak `Bearer` değerine ayarlanır. Hiçbiri için `""` olarak ayarlayın. |

`oauth2` için alanlar:

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `client_id` | dize | Evet | OAuth2 istemci kimliği. |
| `client_secret` | dize | Evet | Salt yazma. OAuth2 istemci gizli anahtarı. |
| `refresh_token` | dize | Evet | Salt yazma. Erişim jetonları almak için kullanılan yenileme jetonu. |
| `token_url` | dize | Evet | Sağlayıcı jeton uç noktası. |
| `scopes` | dizi | Hayır | İstek yapılacak OAuth kapsamları. |

`environment_variable` için alanlar:

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `value` | dize | Evet | Salt yazma. Gizli anahtar değeri. |
| `injection_location` | dize veya dizi | Evet | Gizli anahtarın yerine ne yazılacağı. `header`, `query`, `body` değerlerinden biri veya daha fazlası. |
| `trusted_domains` | dizi | Hayır | Değiştirme için yetkilendirilmiş alan adları. |

## Hatalar

Hatalar, `message` ve `code` içeren bir JSON nesnesi döndürür:

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| HTTP durumu | `code` | Neden |
| --- | --- | --- |
| 400 | `invalid_request` | Zorunlu alan eksik, bilinmeyen alan, desteklenmeyen `type` veya başarısız OAuth2 doğrulama. |
| 404 | `not_found` | Bu kimliğe sahip kimlik bilgisi yok. |
| 409 | `aborted` | Bu kimliğe sahip bir kimlik bilgisi zaten var. |

Bilinmeyen alanlar yoksayılmak yerine reddedilir ve hata, alanı adlandırır:

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## Sırada ne var?

- [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr): Aracıların kodu nasıl çalıştırdığını ve dosyaları nasıl kalıcı hale getirdiğini öğrenin.
- [Ajanlara Genel Bakış](https://ai.google.dev/gemini-api/docs/agents?hl=tr): Yönetilen ajanların temel kavramları hakkında bilgi edinin.
- [Özel Ajanlar Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr): `AGENTS.md` ve `SKILL.md` kullanarak kendi ajanlarınızı tanımlayın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-24 UTC."],[],[]]
