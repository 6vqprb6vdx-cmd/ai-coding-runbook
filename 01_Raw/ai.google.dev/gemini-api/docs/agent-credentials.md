---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr
fetched_at: 2026-09-28T06:15:58.588662+00:00
title: "Identifiants dans les agents g\u00e9r\u00e9s \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Identifiants dans les agents gérés

Les identifiants sont des secrets gérés par le serveur qui permettent à vos agents d'accéder à des services tiers sans que le secret n'entre dans l'environnement de l'agent. Vous stockez un identifiant une seule fois, vous y faites référence par son ID, et le proxy de sortie le résout et l'injecte au moment de la requête.

Les valeurs secrètes sont en écriture seule. Une fois stockés, ils ne sont jamais renvoyés par aucun point de terminaison. Par conséquent, un agent piraté ne peut pas relire les jetons qu'il utilise.

Vous utilisez principalement un identifiant dans la liste d'autorisation du réseau sur [`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr). Stockez d'abord le secret :

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

Associez-le ensuite au domaine qu'il authentifie :

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

L'agent effectue désormais des requêtes authentifiées vers `api.github.com`, et le jeton n'existe jamais dans le bac à sable.

## Types d'identifiants

Chaque identifiant possède un `type` qui détermine les champs qu'il accepte et la façon dont le proxy l'applique.

| Type | Cas d'utilisation | Comportement |
| --- | --- | --- |
| `bearer_token` | Jetons d'accès personnels, jetons de bot, clés API statiques | Le proxy injecte le jeton en tant qu'en-tête de requête. Aucune logique d'actualisation. |
| `oauth2` | Applications OAuth et flux délégués par l'utilisateur | Le proxy échange le jeton d'actualisation contre des jetons d'accès et les actualise lorsqu'ils expirent. |
| `environment_variable` | SDK clients qui lisent les secrets de l'environnement de processus | L'environnement de l'agent reçoit un espace réservé. Le proxy remplace le secret réel dans les requêtes sortantes. |

## Utiliser des identifiants dans la liste d'autorisation du réseau

Ajoutez `credential` à une règle de liste d'autorisation. Le proxy authentifie alors chaque requête sortante vers ce domaine. Il s'agit de la méthode recommandée pour accorder à un agent l'accès à une API privée, un dépôt privé ou un bucket privé.

Vous pouvez combiner des règles authentifiées et non authentifiées dans la même liste d'autorisation :

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

Étant donné que le proxy résout les identifiants pour chaque requête, un identifiant `oauth2` actualise son jeton d'accès de manière transparente. Une interaction de longue durée ne s'interrompt pas lorsque le jeton d'accès expire.

### Combiner `credential` et `transform`

Les règles de liste d'autorisation acceptent également un objet [`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#private-sources) intégré qui définit les en-têtes directement sur la règle. Les deux mécanismes sont appliqués par le proxy de sortie sur le réseau. Dans les deux cas, la valeur de l'en-tête n'existe donc jamais dans le bac à sable. Les deux champs peuvent apparaître dans la même règle.

| Configuration de la règle | Comportement |
| --- | --- |
| `credential` uniquement | Le proxy résout les identifiants et injecte leur en-tête dans chaque requête envoyée au domaine. |
| `transform` uniquement | Injection d'en-tête statique. Les en-têtes que vous rédigez sont envoyés tels quels. |
| Les deux | L'identifiant est appliqué en premier, puis `transform` est fusionné par-dessus. Un en-tête `transform` explicite est prioritaire si les deux définissent la même clé. |
| Ni l'un, ni l'autre | Le domaine est autorisé et aucun en-tête n'est injecté. |

Il est intéressant d'utiliser un identifiant lorsque vous souhaitez stocker un secret une seule fois et y faire référence depuis chaque environnement, agent et déclencheur de votre projet, et lorsque vous souhaitez que l'actualisation et la rotation des jetons d'accès soient gérées pour vous. Un `transform` intégré est adapté lorsque la valeur appartient à un seul appel, par exemple un jeton que vous générez vous-même juste avant de créer l'interaction.

Il est courant de combiner les deux. Les identifiants comportent l'en-tête d'authentification, et `transform` ajoute tout ce que le service en amont attend de la même requête :

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

Pour déplacer un secret d'un `transform` intégré vers un identifiant, stockez-le avec `POST /credentials`, remplacez l'en-tête d'authentification dans `transform` par `"credential": "<id>"` et laissez le reste de l'objet `transform` tel quel.

## Utiliser des identifiants avec les serveurs MCP

Les serveurs MCP distants acceptent le même champ `credential`. Définissez-le sur un outil `mcp_server`. Le proxy injecte l'en-tête d'authentification dans chaque requête envoyée à ce serveur :

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

`credential` et `headers` suivent la même règle de priorité que la liste d'autorisation.
Les identifiants sont appliqués en premier, et `headers` est fusionné par-dessus. Par conséquent, un en-tête explicite est prioritaire si les deux définissent la même clé :

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

Pour déplacer un secret hors de `headers` intégré et dans un identifiant, stockez-le avec `POST /credentials` et remplacez l'entrée d'authentification dans `headers` par `credential`.
Conservez les autres en-têtes à leur emplacement.

## Utiliser des identifiants comme variables d'environnement

Certaines bibliothèques clientes lisent les secrets à partir de l'environnement de processus au lieu de les accepter comme en-têtes de requête. Les clients en mode Socket et en mode Long-Polling sont les plus courants.

Associez un identifiant `environment_variable` à un nom de variable sous `environment.env` :

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

`env` accepte les chaînes littérales et les références d'identifiants côte à côte. Une chaîne littérale est injectée dans le conteneur en tant que variable en texte brut normale.

Une référence d'identifiant ne l'est pas. La variable reçoit l'espace réservé `__GEMINI_CRED_<credential-id>__`, et le proxy remplace le secret réel uniquement pour les requêtes sortantes adressées à un domaine dans le `trusted_domains` des identifiants. Toute requête adressée à un autre domaine est rejetée. Le secret ne quitte donc jamais le périmètre et l'espace réservé n'est pas envoyé à sa place.

Définissez `trusted_domains` sur chaque identifiant `environment_variable`. Il s'agit du contrôle qui définit l'étendue d'utilisation du secret.

## Créer un identifiant

Chaque requête de création nécessite un `type`, ainsi que les champs requis par ce type.

Lorsque vous appelez REST directement, tous les noms de champs utilisent snake\_case. L'envoi d'un champ camelCase renvoie un `400`.

### Jeton de support

Un identifiant de jeton de support n'a besoin que de `token` :

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

La réponse ne renvoie que des métadonnées, jamais le jeton :

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

Par défaut, le proxy envoie `Authorization: Bearer <token>`. Remplacez `header_name` et `prefix` pour cibler un service qui attend autre chose :

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

Cette configuration génère l'en-tête `x-goog-api-key: key_xxxxxxxxxxxx`.

Le tableau suivant montre comment `header_name` et `prefix` se combinent :

| Configuration | En-tête injecté |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

Un identifiant OAuth2 nécessite `client_id`, `client_secret`, `refresh_token` et `token_url`. Le champ `scopes` est facultatif :

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

La création d'un identifiant OAuth2 effectue un échange de jetons en direct avec `token_url` pour confirmer que la configuration fonctionne. L'identifiant n'est stocké que si le fournisseur renvoie une réponse de jeton réussie contenant un `access_token`. Les réponses JSON et form-urlencoded sont acceptées.

Cela signifie que vous avez besoin d'un jeton d'actualisation valide et non expiré au moment de la création. Si le fournisseur refuse l'échange, l'erreur vous est renvoyée :

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

Une fois stocké, le proxy actualise les jetons d'accès lorsqu'ils expirent. Si le fournisseur effectue une rotation des jetons d'actualisation et en renvoie un nouveau lors d'une actualisation, le nouveau jeton remplace automatiquement celui stocké.

### Variable d'environnement

Un identifiant `environment_variable` nécessite `value` et `injection_location` :

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

Le champ `injection_location` indique au proxy où remplacer le secret dans la requête sortante. Il accepte `header`, `query` ou `body`, sous forme de chaîne unique ou de tableau lorsqu'un service en a besoin de plusieurs :

```
"injection_location": ["header", "query"]
```

La substitution n'a lieu que dans les emplacements que vous indiquez. Une requête contenant le code de substitution ailleurs est refusée au lieu d'être envoyée.

Pour associer les identifiants à un nom de variable, consultez [Utiliser des identifiants comme variables d'environnement](#environment-variables).

### ID générés

Le champ `id` est facultatif. Si vous l'omettez, le service génère un UUID :

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

Fournissez votre propre ID lorsque vous souhaitez disposer d'une référence stable et lisible à utiliser dans les interactions. Étant donné que l'ID apparaît dans le chemin d'accès à la ressource, préférez les caractères alphanumériques en minuscules avec des traits d'union ou des traits de soulignement.

## Lister les identifiants

Répertoriez les identifiants appartenant à votre projet. Utilisez les paramètres de pagination pour contrôler la taille du lot de réponses.

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

La réponse ne contient que des métadonnées :

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

Transmettez `next_page_token` en tant que `page_token` pour récupérer la page suivante. Ce champ est omis lorsqu'il n'y a plus de résultats.

| Paramètre | Type | Description |
| --- | --- | --- |
| `page_size` | entier | Nombre maximal d'identifiants par page. |
| `page_token` | chaîne | Jeton provenant du `next_page_token` d'une réponse précédente. |

## Obtenir un identifiant

Récupérez les métadonnées d'un identifiant spécifique à l'aide de son ID.

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

La réponse ressemble à ce qui suit :

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

Si vous demandez un identifiant qui n'existe pas, le code d'erreur `404` est renvoyé :

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## Faire tourner un identifiant

Remplacez un secret sans modifier les règles de la liste d'autorisation, la définition de l'outil ni les variables d'environnement qui y font référence. La rotation prend effet lors de la prochaine résolution du proxy.

La requête doit inclure `type`, ainsi que les champs que vous souhaitez modifier. Les champs que vous omettez conservent leurs valeurs actuelles.

Faire pivoter un jeton de support :

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

Faire pivoter un jeton d'actualisation OAuth2 :

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

La réponse reflète le nouveau `update_time` :

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

Le `type` d'un identifiant est fixe lors de la création. Pour le modifier, supprimez l'identifiant et créez-en un autre.

## Supprimer un identifiant

Supprimez un identifiant et son secret stocké lorsqu'ils ne sont plus nécessaires.

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

Une suppression réussie renvoie un objet vide :

```
{}
```

Toute règle, tout outil ou toute variable d'environnement de la liste d'autorisation qui fait encore référence à l'ID ne pourra pas être résolue. Mettez-les donc à jour en premier.

## Référence de champ

Champs communs à tous les identifiants :

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `id` | chaîne | Non | Identifiant unique. Généré sous forme d'UUID lorsqu'il est omis. |
| `type` | chaîne | Oui | à savoir `bearer_token`, `oauth2` ou `environment_variable`. |
| `status` | chaîne | Lecture seule | État actuel du certificat. |
| `create_time` | chaîne | Lecture seule | Code temporel de création au format RFC 3339. |
| `update_time` | chaîne | Lecture seule | Code temporel RFC 3339 de la dernière mise à jour. |

Champs pour `bearer_token` :

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `token` | chaîne | Oui | Écriture seule. Valeur du jeton. |
| `header_name` | chaîne | Non | En-tête à injecter. La valeur par défaut est `Authorization`. |
| `prefix` | chaîne | Non | Préfixe de la valeur. La valeur par défaut est `Bearer`. Définissez la valeur sur `""` pour qu'il n'y ait pas de traînée. |

Champs pour `oauth2` :

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `client_id` | chaîne | Oui | ID client OAuth2. |
| `client_secret` | chaîne | Oui | Écriture seule. Code secret du client OAuth2. |
| `refresh_token` | chaîne | Oui | Écriture seule. Jeton d'actualisation utilisé pour obtenir des jetons d'accès. |
| `token_url` | chaîne | Oui | Point de terminaison du jeton du fournisseur. |
| `scopes` | tableau | Non | Champs d'application OAuth à demander. |

Champs pour `environment_variable` :

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `value` | chaîne | Oui | Écriture seule. Valeur du secret. |
| `injection_location` | chaîne ou tableau | Oui | Où remplacer le secret. Une ou plusieurs des valeurs suivantes : `header`, `query`, `body`. |
| `trusted_domains` | tableau | Non | Schémas de domaine autorisés pour la substitution. |

## Erreurs

Les erreurs renvoient un objet JSON avec un `message` et un `code` :

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| État HTTP | `code` | Cause |
| --- | --- | --- |
| 400 | `invalid_request` | Champ obligatoire manquant, champ inconnu, `type` non accepté ou validation OAuth2 ayant échoué. |
| 404 | `not_found` | Aucun identifiant ne correspond à cet ID. |
| 409 | `aborted` | Un identifiant associé à cet ID existe déjà. |

Les champs inconnus sont rejetés plutôt qu'ignorés, et l'erreur indique le nom du champ :

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## Étape suivante

- [Environnements](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr) : découvrez comment les agents exécutent du code et conservent les fichiers.
- [Présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) : découvrez les concepts de base des agents gérés.
- [Créer des agents personnalisés](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr) : définissez vos propres agents à l'aide de `AGENTS.md` et `SKILL.md`.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
