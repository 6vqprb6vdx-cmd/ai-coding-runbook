---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa
fetched_at: 2026-11-02T07:23:03.432023+00:00
title: "\u0627\u0639\u062a\u0628\u0627\u0631\u0646\u0627\u0645\u0647\u200c\u0647\u0627 \u062f\u0631 \u0639\u0627\u0645\u0644\u200c\u0647\u0627\u06cc \u0645\u062f\u06cc\u0631\u06cc\u062a\u200c\u0634\u062f\u0647 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# اعتبارنامه‌ها در عامل‌های مدیریت‌شده

اعتبارنامه‌ها اسرار مدیریت‌شده توسط سرور هستند که به نمایندگان شما امکان می‌دهند بدون اینکه این اسرار وارد محیط نماینده شود، به سرویس‌های طرف سوم دسترسی پیدا کنند. اطلاعات اعتباری را یک‌بار ذخیره می‌کنید، با شناسه به آن ارجاع می‌دهید، و پراکسی خروجی آن را در زمان درخواست حل و تزریق می‌کند.

مقادیر رمز فقط نوشتنی هستند. پس‌از ذخیره شدن، هیچ‌گاه توسط هیچ پایانی برگردانده نمی‌شوند، بنابراین کارگزار درمعرض خطر نمی‌تواند نشان‌هایی را که استفاده می‌کند بازخوانی کند.

مکان اصلی که از اطلاعات اعتباری استفاده می‌کنید فهرست مجاز شبکه در
[`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa) است. ابتدا رمز را ذخیره کنید:

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

### رفتن

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

سپس آن را به دامنه‌ای که اصالت‌سنجی می‌کند پیوست کنید:

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

### رفتن

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
                Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
                    Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                        {Domain: "api.github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "*"},
                    })),
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

اکنون عامل درخواست‌های اصالت‌سنجی‌شده را به `api.github.com` ارسال می‌کند و کد
هرگز در جعبه ایمنی وجود ندارد.

## انواع اعتبارنامه

هر مدرک اعتباری `type` دارد که تعیین می‌کند کدام فیلدها را می‌پذیرد و کارگزار چگونه آن را اعمال می‌کند.

| نوع | کاربرد | رفتار |
| --- | --- | --- |
| `bearer_token` | کدهای دسترسی شخصی، کدهای روبات، کلیدهای API ثابت | کارگزار وکالتی کد را به‌عنوان سرایند درخواست تزریق می‌کند. منطق بازآوری وجود ندارد. |
| `oauth2` | برنامه‌های OAuth و جریان‌های واگذارشده کاربر | کارگزار جانشین، کد بازآوری را با کدهای دسترسی مبادله می‌کند و آن‌ها را با انقضایشان بازآوری می‌کند. |
| `environment_variable` | کیت‌های توسعه نرم‌افزار کارخواهی که رمزها را از محیط فرایند می‌خوانند | محیط کارگزار جای‌بانی دریافت می‌کند. کارگزار جانشین رمز واقعی در درخواست‌های خروجی می‌شود. |

## استفاده از اعتبارنامه‌ها در فهرست مجاز شبکه

‫`credential` را به قانون فهرست مجاز اضافه کنید و پراکسی هر درخواست خروجی به آن دامنه را اصالت‌سنجی کند. این روش توصیه‌شده برای دادن دسترسی نماینده به
میانای برنامه‌سازی کاربردی خصوصی، مخزن خصوصی، یا سطل خصوصی است.

می‌توانید قوانین اصالت‌سنجی‌شده و اصالت‌سنجی‌نشده را در یک فهرست مجاز ترکیب کنید:

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

### رفتن

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
                Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
                    Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                        {Domain: "github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "api.atlassian.com", Credential: genai.Ptr("jira-oauth")},
                        {Domain: "*.googleapis.com"},
                    })),
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

ازآنجایی‌که پراکسی اعتبارنامه را برای هر درخواست حل‌وفصل می‌کند، اعتبارنامه `oauth2`
به‌طور شفاف رمز دسترسی خود را بازآوری می‌کند. تعامل طولانی‌مدت با انقضای
توکن دسترسی قطع نمی‌شود.

### درحال ترکیب `credential` و `transform`

قوانین فهرست مجاز همچنین شیء درون‌خطی
[`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa#private-sources) را می‌پذیرند که
سرصفحه‌ها را مستقیماً روی قانون تنظیم می‌کند. هر دو سازوکار توسط پراکسی خروجی در سیم اعمال می‌شوند، بنابراین در هر دو مورد مقدار سرایند هرگز در محیط امن وجود ندارد. هر دو فیلد می‌توانند در یک قانون ظاهر شوند.

| پیکربندی قانون | رفتار |
| --- | --- |
| فقط `credential` | کارگزار وکالتی اطلاعات اعتباری را حل‌وفصل می‌کند و سرایند آن را در هر درخواست به دامنه تزریق می‌کند. |
| فقط `transform` | تزریق سرصفحه ایستا. سرایندهایی که می‌نویسید همان‌گونه که هست ارسال می‌شود. |
| هر دو | ابتدا اطلاعات اعتباری اعمال می‌شود، سپس `transform` در بالا ادغام می‌شود. اگر هر دو سرایند کلید یکسانی را تنظیم کنند، سرایند `transform` صریح برنده است. |
| هیچ‌کدام | دامنه مجاز است و هیچ سرایندی تزریق نمی‌شود. |

وقتی می‌خواهید رمز را یک‌بار ذخیره کنید و از هر محیط، عامل، و راه‌انداز در پروژه‌تان به آن ارجاع دهید، و وقتی می‌خواهید بازآوری و چرخش کد دسترسی برایتان مدیریت شود، استفاده از اطلاعات اعتباری ارزشمند است. `transform` درون‌خطی زمانی مناسب است که مقدار متعلق به یک تماس واحد باشد، برای مثال، کد شناسایی‌ای که درست قبل‌از ایجاد تعامل خودتان تولید می‌کنید.

ترکیب این دو رایج است. این اطلاعات اعتباری سرصفحه اصالت‌سنجی را حمل می‌کند
و `transform` هر چیز دیگری را که سرویس بالادستی در همان
درخواست انتظار دارد اضافه می‌کند:

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

برای انتقال یک رمز از `transform` درون‌خطی به اطلاعات اعتباری، آن را با `POST /credentials` ذخیره کنید، سرصفحه اصالت‌سنجی را در `transform` با `"credential": "<id>"` جایگزین کنید، و بقیه شیء `transform` را دست نخورده بگذارید.

## استفاده از اعتبارنامه‌ها با سرورهای MCP

سرورهای MCP راه دور همان فیلد `credential` را می‌گیرند. آن را در `mcp_server`
ابزاری تنظیم کنید و پراکسی سرایند اصالت‌سنجی را در هر درخواست به آن سرور تزریق می‌کند:

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

### رفتن

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
                Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
                    Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                        {Domain: "api.githubcopilot.com", Credential: genai.Ptr("github-production")},
                    })),
                })),
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

`credential` و `headers` از همان قانون تقدم فهرست مجاز پیروی می‌کنند.
ابتدا اطلاعات اعتباری اعمال می‌شود و `headers` در بالا ادغام می‌شود، بنابراین اگر هر دو کلید یکسانی را تنظیم کنند، سرایند صریح برنده است:

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

برای انتقال رمز از درون‌خط `headers` به اطلاعات اعتباری، آن را با
`POST /credentials` ذخیره کنید و ورودی اصالت‌سنجی را در `headers` با `credential` جایگزین کنید.
سایر سرایندها را در جای خود نگه دارید.

## استفاده از اطلاعات اعتباری به‌عنوان متغیرهای محیط

برخی‌از کتابخانه‌های مشتری رمزها را از محیط فرایند می‌خوانند نه اینکه آن‌ها را به‌عنوان سرصفحه‌های درخواست بپذیرند. کاربران حالت سوکت و نظرسنجی طولانی حالت رایج هستند.

اطلاعات اعتباری `environment_variable` را به نام متغیری در زیر
`environment.env` پیوند دهید:

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

### رفتن

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

‫`env` رشته‌های تحت‌اللفظی و ارجاع‌های اطلاعات اعتباری را در کنار هم می‌پذیرد. رشته‌ای
حرف‌به‌حرف به‌عنوان متغیر نوشتار ساده معمولی به محتوی تزریق می‌شود.

مرجع اعتبارنامه نیست. متغیر جای‌بان `__GEMINI_CRED_<credential-id>__` را دریافت می‌کند و کارگزار فقط برای درخواست‌های خروجی که به دامنه‌ای در `trusted_domains` اطلاعات اعتباری می‌روند، رمز واقعی را جایگزین می‌کند. درخواست به هر دامنه دیگری رد می‌شود، بنابراین رمز هرگز از محیط
خارج نمی‌شود و جای‌بان در جای آن ارسال نمی‌شود.

‫`trusted_domains` را در هر `environment_variable` اطلاعات اعتباری تنظیم کنید. این کنترل محدوده‌ای را که می‌توان از راز استفاده کرد تعیین می‌کند.

## ایجاد اطلاعات اعتباری

هر درخواست ایجاد به `type`، به‌علاوه هر فیلدی که آن نوع نیاز دارد، نیاز دارد.

هنگام تماس مستقیم با REST، همه نام‌های فیلد از snake\_case استفاده می‌کنند. ارسال فیلد camelCase
باعث برگرداندن `400` می‌شود.

### کد حامل

اطلاعات اعتباری نمودار اصالت‌سنجی فقط به `token` نیاز دارد:

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

### رفتن

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

پاسخ فقط فراداده برمی‌گرداند، هرگز نشان:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

به‌طور پیش‌فرض، پراکسی `Authorization: Bearer <token>` را ارسال می‌کند. برای هدف‌یابی سرویسی که چیز دیگری انتظار دارد،
`header_name` و `prefix` را ملغی کنید:

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

### رفتن

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

این پیکربندی سرایند `x-goog-api-key: key_xxxxxxxxxxxx` را تولید می‌کند.

جدول زیر نحوه ترکیب `header_name` و `prefix` را نشان می‌دهد:

| پیکربندی | سرایند تزریق‌شده |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

اعتبارنامه OAuth2 به `client_id`،‏ `client_secret`،‏ `refresh_token`،
و `token_url` نیاز دارد. فیلد `scopes` اختیاری است:

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

### رفتن

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

ایجاد کردن اطلاعات اعتباری OAuth2 تبادل زنده کد اصالت‌سنجی را دربرابر
`token_url` انجام می‌دهد تا تأیید کند پیکربندی کار می‌کند. اطلاعات اعتباری فقط درصورتی ذخیره می‌شود که ارائه‌دهنده پاسخ رمز موفقیت‌آمیزی حاوی `access_token` برگرداند. پاسخ‌های JSON و form-urlencoded پذیرفته می‌شوند.

این یعنی در زمان ایجاد، باید یک کد نوسازی معتبر و منقضی‌نشده داشته باشید. اگر ارائه‌دهنده تبادل را رد کند، خطا به شما برگردانده می‌شود:

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

پس‌از ذخیره شدن، پراکسی با منقضی شدن کدهای دسترسی آن‌ها را بازآوری می‌کند. اگر ارائه‌دهنده
توکن‌های بازآوری را چرخش دهد و توکن جدیدی را درطول بازآوری برگرداند، توکن جدید
به‌طور خودکار جایگزین توکن ذخیره‌شده می‌شود.

### متغیر محیط

اطلاعات اعتباری `environment_variable` به `value` و `injection_location` نیاز دارد:

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

### رفتن

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

فیلد `injection_location` به پراکسی می‌گوید که در درخواست خروجی،
رمز را در کجا جایگزین کند. ‫`header`،‏ `query`، یا `body` را می‌پذیرد، چه به‌صورت
رشته تکی چه به‌صورت آرایه وقتی سرویسی به بیش‌از یک مورد نیاز دارد:

```
"injection_location": ["header", "query"]
```

جایگزینی فقط در مکان‌هایی که فهرست می‌کنید اتفاق می‌افتد. درخواستی که
جای‌بان را در هر جای دیگری داشته باشد به‌جای ارسال شدن، رد می‌شود.

برای پیوند دادن اعتبارنامه به نام متغیر، به
[استفاده از اعتبارنامه‌ها به‌عنوان متغیرهای محیطی](#environment-variables) مراجعه کنید.

### شناسه‌های تولیدشده

فیلد `id` اختیاری است. آن را حذف کنید و سرویس یک UUID تولید می‌کند:

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

وقتی می‌خواهید مرجع پایدار و خوانایی برای استفاده در تعاملات داشته باشید، شناسه خودتان را ارائه دهید. ازآنجایی‌که شناسه در مسیر منبع نشان داده می‌شود،
حروف الفباعددی کوچک با خط تیره یا زیرخط را ترجیح دهید.

## فهرست اعتبارنامه‌ها

اعتبارنامه‌های متعلق به پروژه‌تان را فهرست کنید. از پارامترهای صفحه‌بندی برای کنترل اندازه دسته‌ای پاسخ استفاده کنید.

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

### رفتن

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

پاسخ فقط حاوی فراداده است:

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

‫`next_page_token` را به‌عنوان `page_token` برگردانید تا صفحه بعدی واکشی شود. وقتی نتیجه دیگری وجود نداشته باشد، این فیلد
حذف می‌شود.

| پارامتر | نوع | شرح |
| --- | --- | --- |
| `page_size` | عدد صحیح | حداکثر تعداد اعتبارنامه‌ها در هر صفحه. |
| `page_token` | رشته | نشانه از `next_page_token` پاسخ قبلی. |

## دریافت اطلاعات اعتباری

فراداده‌های یک مدرک اعتباری خاص را براساس شناسه آن بازیابی کنید.

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

### رفتن

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

پاسخ شبیه به این است:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

درخواست اطلاعات اعتباری که وجود ندارد `404` را برمی‌گرداند:

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## چرخاندن اعتبارنامه

بدون دست زدن به هیچ قانون فهرست مجاز، تعریف ابزار، یا متغیر محیطی که به آن ارجاع می‌دهد، رمز را جایگزین کنید. گردش در وضوح پراکسی بعدی اعمال می‌شود.

درخواست باید شامل `type` و همچنین فیلدهایی باشد که می‌خواهید تغییر دهید. فیلدهایی که
حذف می‌کنید مقادیر کنونی‌شان را حفظ می‌کنند.

چرخاندن کد حامل:

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

### رفتن

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

چرخاندن کد بازآوری OAuth2:

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

### رفتن

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

پاسخ نشان‌دهنده `update_time` جدید است:

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

‫`type` اطلاعات اعتباری هنگام ایجاد ثابت است. برای تغییر آن، اطلاعات اعتباری را حذف کنید
و اطلاعات اعتباری جدیدی ایجاد کنید.

## حذف اطلاعات اعتباری

وقتی دیگر به اطلاعات اعتباری و رمز ذخیره‌شده آن نیاز نیست، آن‌ها را حذف کنید.

### Python

```
client.credentials.delete(id="github-production")
```

### JavaScript

```
await client.credentials.delete("github-production");
```

### رفتن

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

حذف موفق یک شیء خالی برمی‌گرداند:

```
{}
```

هر قانون فهرست مجاز، ابزار، یا متغیر محیطی که هنوز به شناسه ارجاع می‌دهد
در حل کردن ناموفق خواهد بود، بنابراین ابتدا آن‌ها را به‌روز کنید.

## مرجع فیلد

فیلدهای مشترک در همه اطلاعات اعتباری:

| فیلد | نوع | الزامی | شرح |
| --- | --- | --- | --- |
| `id` | رشته | نه | شناسه یکتا. وقتی حذف شود، به‌عنوان UUID تولید می‌شود. |
| `type` | رشته | بله | یکی از `bearer_token`،‏ `oauth2`،‏ `environment_variable`. |
| `status` | رشته | فقط خواندنی | وضعیت فعلی اطلاعات اعتباری. |
| `create_time` | رشته | فقط خواندنی | مُهر زمان ایجاد RFC 3339. |
| `update_time` | رشته | فقط خواندنی | مُهر زمان RFC 3339 آخرین به‌روزرسانی. |

فیلدهای `bearer_token`:

| فیلد | نوع | الزامی | شرح |
| --- | --- | --- | --- |
| `token` | رشته | بله | فقط نوشتن. مقدار کد. |
| `header_name` | رشته | نه | سرایندی که باید تزریق شود. پیش‌فرض `Authorization` است. |
| `prefix` | رشته | نه | پیشوند مقدار. پیش‌فرض `Bearer` است. برای هیچ‌کدام، روی `""` تنظیم کنید. |

فیلدهای `oauth2`:

| فیلد | نوع | الزامی | شرح |
| --- | --- | --- | --- |
| `client_id` | رشته | بله | شناسه کارخواه OAuth2. |
| `client_secret` | رشته | بله | فقط نوشتن. رمز کارخواه OAuth2. |
| `refresh_token` | رشته | بله | فقط نوشتن. از کد بازآوری برای دریافت کدهای دسترسی استفاده می‌شود. |
| `token_url` | رشته | بله | نقطه پایان کد ارائه‌دهنده. |
| `scopes` | آرایه | نه | محدوده‌های OAuth برای درخواست. |

فیلدهای `environment_variable`:

| فیلد | نوع | الزامی | شرح |
| --- | --- | --- | --- |
| `value` | رشته | بله | فقط نوشتن. مقدار رمز. |
| `injection_location` | رشته یا آرایه | بله | محل جایگزینی رمز. یک یا چند مورد از `header`،‏ `query`،‏ `body`. |
| `trusted_domains` | آرایه | نه | الگوهای دامنه برای جایگزینی مجاز است. |

## خطاها

خطاها شیء JSON را با `message` و `code` برمی‌گردانند:

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| وضعیت HTTP | `code` | علت |
| --- | --- | --- |
| ۴۰۰ | `invalid_request` | فیلد الزامی وجود ندارد، فیلد ناشناس است، `type` پشتیبانی نمی‌شود، یا اعتبارسنجی OAuth2 ناموفق بود. |
| 404 | `not_found` | اطلاعات اعتباری با این شناسه وجود ندارد. |
| 409 | `aborted` | اطلاعات اعتباری با این شناسه ازقبل وجود دارد. |

فیلدهای ناشناخته به‌جای نادیده گرفته شدن رد می‌شوند و خطا نام فیلد را ذکر می‌کند:

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## قدم بعدی چیست

- [محیط‌ها](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa): با نحوه اجرای کد و ماندگاری فایل‌ها توسط عامل‌ها آشنا شوید.
- [نمای کلی عامل‌ها](https://ai.google.dev/gemini-api/docs/agents?hl=fa): با مفاهیم اصلی عامل‌های مدیریت‌شده آشنا شوید.
- [ساختن عامل‌های سفارشی](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fa): بااستفاده از `AGENTS.md` و `SKILL.md`، عامل‌های خودتان را تعریف کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی."],[],[]]
