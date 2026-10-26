---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=he
fetched_at: 2026-10-26T05:48:45.900789+00:00
title: "\u05e4\u05e8\u05d8\u05d9 \u05db\u05e0\u05d9\u05e1\u05d4 \u05d1\u05e1\u05d5\u05db\u05e0\u05d9\u05dd \u05de\u05e0\u05d5\u05d4\u05dc\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# פרטי כניסה בסוכנים מנוהלים

פרטי הכניסה הם סודות שמנוהלים על ידי השרת ומאפשרים לסוכנים שלכם לגשת לשירותי צד שלישי בלי שהסודות יגיעו לסביבת הסוכן. אתם מאחסנים את פרטי הכניסה פעם אחת, מפנים אליהם באמצעות מזהה, ופרוקסי היציאה מזהה אותם ומכניס אותם בזמן הבקשה.

ערכי סוד הם לקריאה בלבד. אחרי שהם מאוחסנים, אף נקודת קצה לא מחזירה אותם, כך שסוכן שנפרץ לא יכול לקרוא את הטוקנים שהוא משתמש בהם.

המקום העיקרי שבו משתמשים בפרטי כניסה הוא רשימת ההיתרים של הרשת ב-[`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he). קודם מאחסנים את הסוד:

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

לאחר מכן מצרפים אותו לדומיין שהוא מאמת:

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

הסוכן שולח עכשיו בקשות מאומתות אל `api.github.com`, והטוקן אף פעם לא נמצא בארגז החול.

## סוגי פרטי כניסה

לכל אמצעי אימות יש `type` שקובע אילו שדות הוא מקבל ואיך ה-proxy מחיל אותו.

| סוג | תרחיש שימוש | התנהגות |
| --- | --- | --- |
| `bearer_token` | טוקנים של גישה אישית, טוקנים של בוטים, מפתחות סטטיים של API | שרת ה-proxy מוסיף את הטוקן כ-request header. אין לוגיקה לרענון. |
| `oauth2` | אפליקציות OAuth ותהליכים שמוקצים למשתמשים | הפרוקסי מחליף את אסימון הרענון באסימוני גישה ומרענן אותם כשתוקף שלהם פג. |
| `environment_variable` | ערכות SDK ללקוח שקוראות סודות מסביבת התהליך | סביבת הנציג מקבלת placeholder. ה-proxy מחליף את הסוד האמיתי בבקשות יוצאות. |

## שימוש בפרטי הכניסה ברשימת ההיתרים של הרשת

מוסיפים את `credential` לכלל ברשימת ההיתרים, והפרוקסי מאמת כל בקשה יוצאת לדומיין הזה. זו הדרך המומלצת לתת לסוכן גישה ל-API פרטי, למאגר פרטי או לדלי פרטי.

אפשר לשלב כללים מאומתים ולא מאומתים באותה רשימת היתרים:

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

מכיוון שהפרוקסי פותר את פרטי הכניסה לכל בקשה, פרטי כניסה מסוג `oauth2` מרעננים את אסימון הגישה שלהם באופן שקוף. אינטראקציה ארוכה לא תיפסק כשפג תוקף טוקן הגישה.

### שילוב של `credential` ו-`transform`

כללי הרשימה הלבנה מקבלים גם אובייקט [`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he#private-sources) מוטבע שמגדיר כותרות ישירות בכלל. שני המנגנונים מופעלים על ידי שרת ה-proxy של היציאה (egress) בחיבור, כך שבשני המקרים ערך הכותרת אף פעם לא קיים בתוך ארגז החול. שני השדות יכולים להופיע באותו כלל.

| הגדרת הכלל | התנהגות |
| --- | --- |
| `credential` בלבד | הפרוקסי מפענח את פרטי הכניסה ומוסיף את הכותרת שלהם לכל בקשה לדומיין. |
| `transform` בלבד | החדרה סטטית של כותרות. הכותרות שאתם כותבים נשלחות כמו שהן. |
| שניהם | פרטי הכניסה מוחלים קודם, ואז `transform` מתמזגים מעל. אם שני סוגי הכותרות מגדירים את אותו מפתח, הכותרת `transform` מנצחת. |
| אין לי דעה לכאן או לכאן | הדומיין מותר ולא מוחדרות כותרות. |

כדאי להשתמש באמצעי אימות כשרוצים לאחסן סוד פעם אחת ולהפנות אליו מכל סביבה, סוכן וטריגר בפרויקט, וכשרוצים שהמערכת תטפל ברענון וברוטציה של אסימוני הגישה. `transform` מתאים כשמדובר בערך ששייך לקריאה יחידה, למשל טוקן שיוצרים בעצמכם ממש לפני יצירת האינטראקציה.

שילוב של שתי השיטות הוא נפוץ. פרטי הכניסה כוללים את כותרת האימות, ו-`transform` מוסיף את כל מה שהשירות במעלה הזרם מצפה לקבל באותה בקשה:

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

כדי להעביר סוד מתוך `transform` מוטבע אל תוך פרטי כניסה, מאחסנים אותו באמצעות `POST /credentials`, מחליפים את כותרת האימות ב-`transform` ב-`"credential": "<id>"` ומשאירים את שאר האובייקט `transform` ללא שינוי.

## שימוש בפרטי כניסה עם שרתי MCP

שרתי MCP מרוחקים מקבלים את אותו שדה `credential`. מגדירים אותו בכלי `mcp_server`, ושרת ה-proxy מוסיף את כותרת האימות לכל בקשה לשרת הזה:

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

`credential` ו-`headers` פועלים לפי אותו כלל עדיפות כמו רשימת ההיתרים.
האישורים מוחלים קודם ו`headers` מתמזג מעל, כך שכותרת מפורשת מנצחת אם שניהם מגדירים את אותו מפתח:

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

כדי להוציא סוד מתוך `headers` ולהעביר אותו לפרטי כניסה, מאחסנים אותו באמצעות `POST /credentials` ומחליפים את רשומת האימות ב-`headers` ב-`credential`.
משאירים את הכותרות האחרות במקומן.

## שימוש בפרטי כניסה כמשתני סביבה

חלק מספריות הלקוח קוראות סודות מסביבת התהליך במקום לקבל אותם ככותרות של בקשות. בדרך כלל, הלקוחות הם במצב Socket או במצב Long-polling.

מקשרים פרטי כניסה מסוג `environment_variable` לשם משתנה בקטע `environment.env`:

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

‫`env` מקבל מחרוזות מילוליות והפניות לפרטי כניסה זו לצד זו. מחרוזת מילולית מוזרקת למאגר כמשתנה רגיל של טקסט פשוט.

הפניה לפרטי כניסה לא. המשתנה מקבל את ה-placeholder‏ `__GEMINI_CRED_<credential-id>__`, והפרוקסי מחליף אותו בסוד האמיתי רק בבקשות יוצאות שמופנות לדומיין ב-`trusted_domains` של פרטי הכניסה. בקשה לכל דומיין אחר נדחית, כך שהסוד אף פעם לא יוצא מגבולות הגזרה וה-פלייסהולדר לא נשלח במקומו.

מגדירים את `trusted_domains` בכל אישורי `environment_variable`. הוא קובע את ההיקף שבו אפשר להשתמש בסוד.

## יצירת פרטי כניסה

כל בקשת יצירה צריכה לכלול `type`, בנוסף לשדות שנדרשים עבור הסוג הזה.

כשקוראים ישירות ל-REST, כל שמות השדות הם בפורמט snake\_case. שליחת שדה בפורמט camelCase מחזירה `400`.

### טוקן למוכ"ז

פרטי כניסה של טוקן bearer צריכים לכלול רק את `token`:

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

התגובה מחזירה רק מטא-נתונים, אף פעם לא את הטוקן:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

כברירת מחדל, ה-proxy שולח `Authorization: Bearer <token>`. החלפת הערך של `header_name` ושל `prefix` כדי לטרגט שירות שמצפה למשהו אחר:

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

ההגדרה הזו יוצרת את הכותרת `x-goog-api-key: key_xxxxxxxxxxxx`.

בטבלה הבאה אפשר לראות איך `header_name` ו-`prefix` משולבים:

| הגדרות אישיות | כותרת שהוחדרה |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

פרטי כניסה מסוג OAuth2 דורשים `client_id`, `client_secret`, `refresh_token` ו-`token_url`. השדה `scopes` הוא אופציונלי:

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

יצירת פרטי כניסה של OAuth2 מבצעת החלפת אסימונים בזמן אמת מול `token_url` כדי לוודא שההגדרה פועלת. האישורים נשמרים רק אם הספק מחזיר תגובה מוצלחת של אסימון שמכילה `access_token`. המערכת מקבלת תגובות בפורמט JSON וגם בפורמט form-urlencoded.

כלומר, צריך שיהיה לכם טוקן רענון תקף שלא פג התוקף שלו בזמן היצירה. אם הספק דוחה את ההמרה, השגיאה מוחזרת אליכם:

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

אחרי שהם נשמרים, ה-proxy מרענן את אסימוני הגישה כשהתוקף שלהם פג. אם הספק מבצע רוטציה של טוקנים לרענון ומחזיר טוקן חדש במהלך רענון, הטוקן החדש מחליף את הטוקן השמור באופן אוטומטי.

### משתנה הסביבה

פרטי כניסה של `environment_variable` דורשים `value` ו-`injection_location`:

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

השדה `injection_location` מציין לשרת ה-Proxy איפה בבקשה היוצאת להחליף את הסוד. היא מקבלת את הערכים `header`,‏ `query` או `body`, כמחרוזת אחת או כמערך אם שירות מסוים צריך יותר מאחד:

```
"injection_location": ["header", "query"]
```

ההחלפה מתבצעת רק במיקומים שציינתם. בקשה שכוללת את ה-placeholder במקום אחר נדחית ולא נשלחת.

במאמר [שימוש בפרטי כניסה כמשתני סביבה](#environment-variables) מוסבר איך לקשר את פרטי הכניסה לשם של משתנה.

### מזהים שנוצרו

השדה `id` הוא אופציונלי. משמיטים אותו והשירות יוצר UUID:

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

אתם יכולים לספק מזהה משלכם אם אתם רוצים הפניה קבועה וקריאה לשימוש באינטראקציות. המזהה מופיע בנתיב המשאב, ולכן מומלץ להשתמש באותיות קטנות, בספרות, במקפים או בקווים תחתונים.

## הצגת רשימה של פרטי כניסה

מציגים ברשימה את פרטי הכניסה ששייכים לפרויקט. אפשר להשתמש בפרמטרים של חלוקה לדפים כדי לשלוט בגודל אצווה של התגובות.

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

התשובה מכילה מטא-נתונים בלבד:

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

מעבירים את `next_page_token` בחזרה כ-`page_token` כדי לאחזר את הדף הבא. השדה
מושמט כשאין תוצאות נוספות.

| פרמטר | סוג | תיאור |
| --- | --- | --- |
| `page_size` | מספר שלם | המספר המקסימלי של פרטי כניסה בכל דף. |
| `page_token` | מחרוזת | טוקן מתוך `next_page_token` של תשובה קודמת. |

## קבלת פרטי כניסה

אחזור מטא-נתונים של פרטי כניסה ספציפיים לפי המזהה שלהם.

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

התגובה אמורה להיראות כך:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

בקשה של פרטי כניסה שלא קיימים מחזירה את השגיאה `404`:

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## עדכון של פרטי הכניסה

להחליף סוד בלי לשנות כלל ברשימת ההיתרים, הגדרת כלי או משתנה סביבתי שמפנה אליו. הרוטציה נכנסת לתוקף ברזולוציית ה-proxy הבאה.

הבקשה צריכה לכלול את `type`, בנוסף לשדות שרוצים לשנות. הערכים הנוכחיים של השדות שלא מציינים נשמרים.

סיבוב של אסימון למוכ"ז:

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

החלפת טוקן רענון של OAuth2:

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

התשובה משקפת את `update_time` החדש:

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

הערך של `type` בפרטי כניסה נקבע בזמן היצירה. כדי לשנות את האישורים, צריך למחוק אותם וליצור אישורים חדשים.

## מחיקת פרטי כניסה

למחוק פרטי כניסה ואת הסוד שמאוחסן בהם כשאין בהם יותר צורך.

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

אם המחיקה בוצעה בהצלחה, מוחזר אובייקט ריק:

```
{}
```

כל כלל, כלי או משתנה סביבה ברשימת ההיתרים שמפנים עדיין למזהה לא יפעלו, ולכן צריך לעדכן אותם קודם.

## הפניה לשדה

שדות שמשותפים לכל פרטי הכניסה:

| שדה | סוג | נדרש | תיאור |
| --- | --- | --- | --- |
| `id` | מחרוזת | לא | מזהה ייחודי. אם לא מציינים ערך, המערכת יוצרת מזהה ייחודי אוניברסלי (UUID). |
| `type` | מחרוזת | כן | אחד מהערכים `bearer_token`, `oauth2`, `environment_variable`. |
| `status` | מחרוזת | קריאה בלבד | הסטטוס הנוכחי של פרטי הכניסה. |
| `create_time` | מחרוזת | קריאה בלבד | חותמת הזמן של היצירה בפורמט RFC 3339. |
| `update_time` | מחרוזת | קריאה בלבד | חותמת הזמן של העדכון האחרון בפורמט RFC 3339. |

שדות ל-`bearer_token`:

| שדה | סוג | נדרש | תיאור |
| --- | --- | --- | --- |
| `token` | מחרוזת | כן | כתיבה בלבד. ערך הטוקן. |
| `header_name` | מחרוזת | לא | הכותרת להחדרה. ברירת המחדל היא `Authorization`. |
| `prefix` | מחרוזת | לא | קידומת ערך. ברירת המחדל היא `Bearer`. אם לא רוצים להגדיר אף אחד מהם, בוחרים באפשרות `""`. |

שדות ל-`oauth2`:

| שדה | סוג | נדרש | תיאור |
| --- | --- | --- | --- |
| `client_id` | מחרוזת | כן | מזהה לקוח ב-OAuth2. |
| `client_secret` | מחרוזת | כן | כתיבה בלבד. סוד לקוח OAuth2. |
| `refresh_token` | מחרוזת | כן | כתיבה בלבד. אסימון רענון שמשמש להשגת טוקנים של גישה. |
| `token_url` | מחרוזת | כן | נקודת הקצה של הטוקן של הספק. |
| `scopes` | מערך | לא | היקפי הרשאות OAuth לבקשה. |

שדות ל-`environment_variable`:

| שדה | סוג | נדרש | תיאור |
| --- | --- | --- | --- |
| `value` | מחרוזת | כן | כתיבה בלבד. ערך הסוד. |
| `injection_location` | מחרוזת או מערך | כן | איפה להחליף את הסוד. אחת או יותר מהאפשרויות הבאות: `header`, `query`, `body`. |
| `trusted_domains` | מערך | לא | תבניות דומיין שמורשות להחלפה. |

## שגיאות

שגיאות מחזירות אובייקט JSON עם `message` ו-`code`:

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| סטטוס HTTP | `code` | סיבה |
| --- | --- | --- |
| 400 | `invalid_request` | שדה חובה חסר, שדה לא ידוע, `type` לא נתמך או אימות OAuth2 נכשל. |
| 404 | `not_found` | לא נמצאו פרטי כניסה עם המזהה הזה. |
| 409 | `aborted` | כבר קיימים פרטי כניסה עם המזהה הזה. |

שדות לא מוכרים נדחים ולא מתעלמים מהם, והשגיאה מציינת את השדה:

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## המאמרים הבאים

- [סביבות](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he): מידע על האופן שבו סוכנים מריצים קוד ושומרים קבצים.
- [סקירה כללית על סוכנים](https://ai.google.dev/gemini-api/docs/agents?hl=he): מידע על המושגים המרכזיים של סוכנים מנוהלים.
- [יצירת סוכנים בהתאמה אישית](https://ai.google.dev/gemini-api/docs/custom-agents?hl=he): הגדרת סוכנים משלכם באמצעות `AGENTS.md` ו-`SKILL.md`.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-07 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-07 (שעון UTC)."],[],[]]
