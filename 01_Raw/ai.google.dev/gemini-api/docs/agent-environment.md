---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=de
fetched_at: 2026-08-17T02:19:49.594983+00:00
title: "Umgebungen in verwalteten KI-Agenten \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Umgebungen in verwalteten KI-Agenten

Umgebungen sind verwaltete Linux-Sandboxes, in denen Agents Code ausführen und Dateien speichern können. Sie sind vom Interaktionskontext entkoppelt, sodass Sie dieselbe Umgebung für mehrere Interaktionen wiederverwenden oder jederzeit neu beginnen können.

Das folgende Beispiel zeigt, wie eine Interaktion mit einer neuen Remote-Umgebung erstellt und ihre ID abgerufen wird:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
    input: "Install pandas and matplotlib, verify the imports, and print the versions.",
    environment: "remote",
});

console.log(`Environment ID: ${interaction.environment_id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## Der Parameter `environment`

Der Parameter `environment` kann drei Formen annehmen:

| Formular | Beispiel | Anwendung |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | Stellen Sie eine neue Sandbox bereit. |
| Umgebungs-ID | `environment="env_abc123"` | Eine vorhandene Sandbox mit allen Dateien und Paketen wiederverwenden. |
| Konfigurationsobjekt | `environment={...}` | Stellen Sie eine neue Sandbox mit Quellen, Netzwerkregeln oder beidem bereit. |

Die folgenden Beispiele veranschaulichen die drei Möglichkeiten zur Verwendung des Parameters `environment`.

### Python

```
from google import genai

client = genai.Client()

# Fresh sandbox
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a hello world script.",
    environment="remote",
)

# Reuse an existing sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Modify the script to accept a name argument.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# New sandbox with sources
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
    input: "Write a hello world script.",
    environment: "remote",
});

// Reuse an existing sandbox
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Modify the script to accept a name argument.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

// New sandbox with sources
const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
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

### REST

```
# Fresh sandbox
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
}"

# New sandbox with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

## Umgebung konfigurieren

Eine Möglichkeit, eine Umgebung einzurichten, besteht darin, dem Agenten mitzuteilen, was installiert werden muss.
Es kümmert sich um die Auflösung von Abhängigkeiten und die Fehlerbehebung. Sobald die Umgebung bereit ist, speichern Sie die `environment_id` und verwenden Sie sie wieder.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment="remote",
)

# Reuse the configured environment
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# Reuse the configured environment
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment: "remote",
});

const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Using the tools in /workspace/tools, list the files.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction2.id,
});
console.log(interaction.output_text);
```

### REST

```
# Create interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### Von einer Quelle bereitstellen

Wenn Sie genau wissen, welche Dateien der Agent benötigt, stellen Sie sie in einem einzigen Aufruf bereit, anstatt sie zu iterieren. Das Konfigurationsobjekt `environment` akzeptiert ein `sources`-Array mit drei Typen:

| Quelltyp | `type` Wert | Beschreibung | Limit |
| --- | --- | --- | --- |
| Git-Repository | `repository` | Klonen eines Repositorys aus einer URL in die Sandbox unter `target`. | 500 MB |
| Cloud Storage | `gcs` | Kopiert eine Datei oder ein Verzeichnis aus Cloud Storage in die Sandbox unter `target`. | 2 GB |
| Inline-Inhalte | `inline` | Schreibt Rohtextinhalte in eine Datei in der Sandbox unter `target`. | 1 MB pro Datei, insgesamt 2 MB |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
# Create interaction with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

Sie können beide Ansätze kombinieren: Binden Sie bekannte Quellen deklarativ ein und installieren Sie dann mit Folgeinteraktionen Pakete oder führen Sie Einrichtungs-Scripts aus. Sie können beim Hinzufügen einer benutzerdefinierten Quelle nicht das Stammverzeichnis (`/`) als Ziel festlegen, sondern müssen immer ein Unterverzeichnis angeben.

### Private Quellen

Sie können auch aus privaten GitHub-Repositories oder privaten Cloud Storage-Buckets herunterladen, indem Sie die Anmeldedaten in der Netzwerkkonfiguration hinzufügen:

Für **private Git-Repositories** verwenden Sie die `Basic`-Authentifizierung mit Ihrem [persönlichen GitHub-Zugriffstoken (Personal Access Token, PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
Codieren Sie das Token mit `x-oauth-basic` als Nutzernamen:

```
echo -n "x-oauth-basic:ghp_YourPATHere" | base64
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

Verwenden Sie für **private Cloud Storage-Buckets** ein standardmäßiges OAuth 2.0-Inhabertoken:

```
gcloud auth print-access-token
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

## Vorinstallierte Software

Die Sandbox wird unter Ubuntu ausgeführt und enthält vorinstallierte Runtimes und gängige Pakete. Der Agent kann zur Laufzeit zusätzliche Pakete mit `pip
install` oder `npm install` installieren. Pakete, die während einer Interaktion installiert werden, bleiben erhalten, wenn Sie dieselbe `environment_id` wiederverwenden.

| Kategorie | Vorinstallierte Pakete |
| --- | --- |
| **UNIX-Tools** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## Netzwerkkonfiguration

Standardmäßig haben Umgebungen uneingeschränkten ausgehenden Netzwerkzugriff. Verwenden Sie das Feld `network`, um ausgehenden Traffic auf bestimmte Domains zu beschränken. Jede Regel gibt ein `domain`- und ein optionales `transform`-Objekt an, in das Header in übereinstimmende Anfragen eingefügt werden sollen. Diese Header können für jede Interaktion eindeutig sein und Sie können sie für dieselbe Umgebung aktualisieren.

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `domain` | `string` | Abzugleichende Domain. Verwenden Sie einen genauen Hostnamen oder `*` für alle Domains. |
| `transform` | `object` | Objekt mit einfachen Schlüssel/Wert-Paaren, die Header darstellen, die in übereinstimmende Anfragen eingefügt werden sollen, z.B. `{"Authorization": "Bearer ..."}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

Wenn eine Zulassungsliste festgelegt ist, sind nur Anfragen an explizit aufgeführte Domains zulässig. Sie können Platzhalter verwenden, um Subdomains abzugleichen (z. B. `{"domain":
"*.example.com"}`). Beachten Sie jedoch, dass die Stammdomain `example.com` nicht abgeglichen wird. Sie muss separat hinzugefügt werden. Wenn Sie allen anderen Datenverkehr zulassen möchten, z. B. das Weiterleiten nicht aufgeführter Domains ohne eingefügte Header, fügen Sie `{"domain": "*"}` als Catch-all-Eintrag hinzu.

### Anmeldedaten

Sie können Anmeldedaten für Ihren Agent hinzufügen, indem Sie Header-Transformationen hinzufügen. Die Anmeldedaten werden von einem Egress-Proxy in die entsprechenden HTTP-Header eingefügt. Sie werden in der Sandbox niemals als Umgebungsvariablen oder Dateien verfügbar gemacht.

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
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

### Netzwerkzugriff deaktivieren

Wenn Sie den gesamten ausgehenden Netzwerkzugriff blockieren möchten, setzen Sie `network` auf `disabled`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
    input: "Analyze the local files only.",
    environment: {
        type: "remote",
        network: "disabled",
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
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

### Anmeldedaten aktualisieren

Anmeldedaten wie Zugriffstokens und kurzlebige API-Schlüssel laufen ab.
Sie können sie aktualisieren, indem Sie beim nächsten Aufruf das vorhandene `environment_id` zusammen mit einer neuen `network`-Konfiguration übergeben. Die neuen Netzwerkregeln ersetzen die vorherigen vollständig, während der Dateisystemstatus der Umgebung (installierte Pakete, Dateien, Repositorys) beibehalten wird.

### Python

```
from google import genai

client = genai.Client()

# First interaction: use an initial token
first = client.interactions.create(
    agent="antigravity-preview-05-2026",
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
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
# Use the environment_id from a previous interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
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

## Umgebungslebenszyklus

Umgebungen folgen diesem Lebenszyklus:

| Bundesland | Verhalten |
| --- | --- |
| **Erstellt** | Wird bereitgestellt, wenn in einer Interaktion `environment: "remote"` oder ein Konfigurationsobjekt angegeben ist. |
| **Aktiv** | Laufen während einer Interaktion |
| **Inaktiv** | Automatische Momentaufnahme und Stopp nach 15 Minuten Inaktivität. |
| **Offline** | Die Daten werden seit der letzten Aktivität 7 Tage lang aufbewahrt. Kann durch Übergabe der ID fortgesetzt werden. |
| **Gelöscht** | Sie werden automatisch aus dem System entfernt, wenn die Aufbewahrungsdauer von 7 Tagen abläuft, oder bei manueller Löschung. |

## Environments API

Mit der Environments API können Sie Sandbox-Sitzungen programmatisch verwalten.
Durch das Aufzählen von Umgebungen können Sie aktive Sitzungs-IDs ermitteln und den Status wiederherstellen, wenn eine Clientverbindung während einer lang andauernden Aufgabe beendet wird. Sie können auch Sitzungsmetadaten prüfen und Umgebungen explizit löschen, wenn Workflows abgeschlossen sind, anstatt auf den automatischen TTL-Ablauf zu warten.

### Umgebungen auflisten

Aktive Umgebungen für Ihr Projekt auflisten Verwenden Sie Paginierungsparameter, um die Batchgröße der Antwort zu steuern.

### Python

```
from google import genai

client = genai.Client()

for env in client.environments.list(page_size=10):
    print(f"Environment ID: {env.environment_id}, Type: {env.type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.list({ pageSize: 10 });
for (const env of response.environments) {
    console.log(`Environment ID: ${env.environment_id}, Type: ${env.type}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

Die Antwort sieht dann ungefähr so aus:

```
{
  "environments": [
    {
      "environment_id": "140128b2a13c12c00a5a0d8cf7af9469",
      "type": "remote"
    },
    {
      "environment_id": "362b738275a1d74af6f1c62bc050da73",
      "type": "remote"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

### Umgebung abrufen

Metadaten und Konfigurationsdetails für eine bestimmte Umgebung anhand des Ressourcennamens abrufen.

### Python

```
from google import genai

client = genai.Client()

env = client.environments.get(name="environments/YOUR_ENVIRONMENT_ID")
print(f"Environment ID: {env.environment_id}, Type: {env.type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const env = await client.environments.get({ name: "environments/YOUR_ENVIRONMENT_ID" });
console.log(`Environment ID: ${env.environment_id}, Type: ${env.type}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

Die Antwort sieht dann ungefähr so aus:

```
{
  "environment_id": "140128b2a13c12c00a5a0d8cf7af9469",
  "type": "remote",
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

### Umgebung löschen

Beenden und löschen Sie eine Umgebung explizit, um Sandbox-Ressourcen zu bereinigen, wenn Ihre Aufgaben oder Pipelines abgeschlossen sind.

### Python

```
from google import genai

client = genai.Client()

client.environments.delete(name="environments/YOUR_ENVIRONMENT_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

await client.environments.delete({ name: "environments/YOUR_ENVIRONMENT_ID" });
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Dateien aus der Umgebung herunterladen

Der Agent erstellt während der Ausführung Dateien in der Sandbox. Sie können den vollständigen Umgebungs-Snapshot als TAR-Datei über die Files API herunterladen:

### Python

```
import os
import requests
import tarfile
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a file environments_test.txt with content 'Environments' inside the sandbox.",
    environment="remote",
)

env_id = interaction.environment_id
api_key = os.environ.get("GEMINI_API_KEY")

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot_env.tar", "wb") as f:
    f.write(response.content)

os.makedirs("extracted_env_snapshot", exist_ok=True)
with tarfile.open("snapshot_env.tar") as tar:
    tar.extractall(path="extracted_env_snapshot")

print(os.listdir("extracted_env_snapshot"))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { execSync } from "child_process";
import * as fs from "fs";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a file environments_test.txt with content 'Environments' inside the sandbox.",
    environment: "remote",
});

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot_env.tar", buffer);

if (!fs.existsSync("extracted_env_snapshot")) {
    fs.mkdirSync("extracted_env_snapshot");
}
execSync("tar -xf snapshot_env.tar -C extracted_env_snapshot");

console.log(fs.readdirSync("extracted_env_snapshot"));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a file environments_test.txt with content '\''Environments'\'' inside the sandbox.",
    "environment": "remote"
}'
# Step 2: Download snapshot (reusing environment ID from Step 1)
# curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
#   -H "x-goog-api-key: $API_KEY" \
#   -o snapshot.tar
```

## Preise und Ressourcen

Jede Umgebung wird mit festen Ressourcenzuweisungen ausgeführt:

| Ressource | Wert |
| --- | --- |
| **CPU** | 4 Kerne |
| **Arbeitsspeicher** | 16 GB |

Die Rechenleistung der Umgebung (CPU, Arbeitsspeicher, Sandbox-Ausführung) wird während des Vorschauzeitraums **nicht in Rechnung gestellt**. Informationen zu den Kosten für Agent-Tokens finden Sie unter [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de#pricing-for-agents).

## Beschränkungen

- **Vorschaustatus**:Umgebungen und verwaltete Agents sind in der Vorschau verfügbar. Funktionen und Schemas können sich ändern.
- **Größe von Inline-Quellen**:Inline-Quellen sind auf 1 MB pro Datei und insgesamt 2 MB für alle Dateien begrenzt.
- **Quellgröße**: Git-Repositories sind auf 500 MB und Cloud Storage-Repositories auf 2 GB begrenzt.
- **Umgebungsstart**:Das Bereitstellen einer neuen Umgebung dauert bis zu 5 Sekunden. Bei großen Quell-Repositories kann diese Zeit länger dauern.
- **Ablauf von Umgebungen**:Inaktive Offlineumgebungen werden 7 Tage lang aufbewahrt, bevor sie durch die automatische TTL-Bereinigung ablaufen. Wenn Sie eine abgelaufene oder ungültige Umgebungs-ID übergeben, wird der Fehler `404 Not Found` zurückgegeben.
- **Unterstützung von Dateien**:Der Agent kann derzeit nur Text- und Bilddateien lesen. Die Unterstützung von Binärdateien ist noch nicht verfügbar.
- **Keine Einbindung über das Stammverzeichnis**:Sie können beim Hinzufügen einer benutzerdefinierten Quelle nicht das Stammverzeichnis (`/`) als Ziel festlegen, sondern müssen immer ein Unterverzeichnis angeben.

## Nächste Schritte

- [Übersicht über Agents](https://ai.google.dev/gemini-api/docs/agents?hl=de): Hier finden Sie Informationen zu den wichtigsten Konzepten von verwalteten Agents.
- [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de): Multi-Turn-Unterhaltungen und Streaming nutzen
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de): Hier finden Sie Informationen zu Funktionen, Tools, Modellauswahl und Preisen für den Standard-Agent.
- [Benutzerdefinierte KI-Agenten erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de): Definieren Sie Ihre eigenen KI-Agenten mit `AGENTS.md` und `SKILL.md`.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-23 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-23 (UTC)."],[],[]]
