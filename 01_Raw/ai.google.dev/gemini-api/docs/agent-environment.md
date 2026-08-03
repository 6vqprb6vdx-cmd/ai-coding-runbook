---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl
fetched_at: 2026-08-03T04:31:37.543443+00:00
title: "\u015arodowiska w\u00a0przypadku zarz\u0105dzanych agent\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Środowiska w przypadku zarządzanych agentów

Środowiska to zarządzane piaskownice Linux, które zapewniają agentom odizolowane miejsce do wykonywania kodu i przechowywania plików. Są one oddzielone od kontekstu interakcji, dzięki czemu możesz ponownie użyć tego samego środowiska w wielu interakcjach lub w dowolnym momencie zacząć od nowa.

Poniższy przykład pokazuje, jak utworzyć interakcję z nowym środowiskiem zdalnym i pobrać jego identyfikator:

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

## Parametr `environment`

Parametr `environment` może przyjmować 3 formy:

| Formularz | Przykład | Kiedy używać |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | Utwórz nową piaskownicę. |
| Identyfikator środowiska | `environment="env_abc123"` | Użyj ponownie istniejącej piaskownicy ze wszystkimi jej plikami i pakietami. |
| Obiekt konfiguracji | `environment={...}` | Utwórz nową piaskownicę ze źródłami, regułami sieciowymi lub oboma tymi elementami. |

Poniższe przykłady pokazują 3 sposoby użycia parametru `environment`.

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

## Konfigurowanie środowiska

Jednym ze sposobów konfigurowania środowiska jest poinformowanie agenta, co ma zainstalować.
Zajmuje się on rozwiązywaniem zależności i problemów. Gdy środowisko będzie gotowe, zapisz `environment_id` i użyj go ponownie.

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

### Montowanie ze źródła

Jeśli wiesz dokładnie, jakich plików potrzebuje agent, zamontuj je w jednym wywołaniu zamiast iterować. Obiekt konfiguracji `environment` akceptuje tablicę `sources` z 3 typami:

| Typ źródła | Wartość `type` | Opis | Limit |
| --- | --- | --- | --- |
| Repozytorium Git | `repository` | Klonuje repozytorium z adresu URL do piaskownicy w `target`. | 500 MB |
| Cloud Storage | `gcs` | Kopiuje plik lub katalog z Cloud Storage do piaskownicy w `target`. | 2 GB |
| Treść w tekście | `inline` | Zapisuje surową treść tekstową w pliku w piaskownicy w `target`. | 1 MB na plik, 2 MB łącznie |

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

Możesz połączyć oba podejścia: zamontować znane źródła deklaratywnie, a następnie iterować z interakcjami uzupełniającymi, aby zainstalować pakiety lub uruchomić skrypty konfiguracji. Podczas dodawania źródła niestandardowego nie możesz ustawić katalogu głównego (`/`) jako miejsca docelowego. Zawsze musisz określić podkatalog.

### Źródła prywatne

Możesz też pobierać dane z prywatnych repozytoriów GitHub lub prywatnych zasobników Cloud Storage, dodając dane logowania w konfiguracji sieci:

W przypadku **prywatnych repozytoriów Git** użyj uwierzytelniania `Basic` z
[osobistym tokenem dostępu GitHub
(PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
Zakoduj token, używając `x-oauth-basic` jako nazwy użytkownika:

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

W przypadku **prywatnych zasobników Cloud Storage** użyj standardowego tokena OAuth 2.0 Bearer:

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

## Wstępnie zainstalowane oprogramowanie

Piaskownica działa w systemie Ubuntu i ma wstępnie zainstalowane środowiska wykonawcze oraz popularne pakiety. Agent może instalować dodatkowe pakiety w czasie działania za pomocą `pip
install` lub `npm install`. Pakiety zainstalowane podczas interakcji są zachowywane, gdy ponownie użyjesz tego samego `environment_id`.

| Kategoria | Zainstalowane pakiety |
| --- | --- |
| **Narzędzia UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## Konfiguracja sieci

Domyślnie środowiska mają nieograniczony dostęp do sieci wychodzącej. Użyj pola `network`, aby ograniczyć ruch wychodzący do określonych domen. Każda reguła określa `domain` i opcjonalny obiekt `transform`, aby wstawiać nagłówki do pasujących żądań. Te nagłówki mogą być unikalne dla każdej interakcji i możesz je aktualizować w tym samym środowisku.

| Pole | Typ | Opis |
| --- | --- | --- |
| `domain` | `string` | Domena do dopasowania. Użyj dokładnej nazwy hosta lub `*` dla wszystkich domen. |
| `transform` | `object` | Obiekt zawierający płaskie pary klucz-wartość reprezentujące nagłówki do wstawienia do pasujących żądań, np. `{"Authorization": "Bearer ..."}`. |

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

Gdy ustawiona jest lista dozwolonych, dozwolone są tylko żądania do domen wymienionych na tej liście. Możesz używać symboli wieloznacznych do dopasowywania subdomen (np. `{"domain":
"*.example.com"}`), ale pamiętaj, że nie pasuje to do domeny głównej
`example.com`, którą należy dodać osobno. Aby zezwolić na cały inny ruch, np.
na kierowanie na domeny nieznajdujące się na liście bez wstawionych nagłówków, dodaj `{"domain": "*"}` jako wpis
obejmujący wszystkie przypadki.

### Dane logowania

Aby agent mógł korzystać z danych logowania, możesz dodać transformacje nagłówków. Dane logowania są wstawiane do odpowiednich nagłówków HTTP przez serwer proxy ruchu wychodzącego. Nigdy nie są one udostępniane w piaskownicy jako zmienne środowiskowe ani pliki.

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

### Wyłączanie dostępu do sieci

Aby zablokować cały dostęp do sieci wychodzącej, ustaw `network` na `disabled`:

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

### Odświeżanie danych logowania

Dane logowania, takie jak tokeny dostępu i krótkotrwałe klucze API, wygasają.
Możesz je odświeżyć, przekazując istniejący `environment_id` wraz z nową konfiguracją `network` podczas następnej interakcji. Nowe reguły sieciowe całkowicie zastępują poprzednie, a stan systemu plików środowiska (zainstalowane pakiety, pliki, repozytoria) jest zachowywany.

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

## Cykl życia środowiska

Środowiska mają następujący cykl życia:

| Stan | Zachowanie |
| --- | --- |
| **Utworzono** | Utworzone, gdy interakcja określa `environment: "remote"` lub obiekt konfiguracji. |
| **Aktywne** | Działające podczas interakcji. |
| **– bezczynny(-a)** | Automatycznie tworzy migawkę i zatrzymuje się po 15 minutach bezczynności. |
| **Offline** | Przechowywane przez 7 dni od ostatniej aktywności. Można je wznowić, przekazując jego identyfikator. |
| **Usunięto** | Automatycznie usuwane z systemu po upływie 7-dniowego okresu TTL lub po ręcznym usunięciu. |

## Environments API

Za pomocą interfejsu Environments API możesz programowo zarządzać sesjami piaskownicy.
Wyliczanie środowisk pozwala wykrywać aktywne identyfikatory sesji i przywracać stan, jeśli połączenie klienta zostanie przerwane podczas długotrwałego zadania. Możesz też sprawdzać metadane sesji i jawnie usuwać środowiska po zakończeniu przepływów pracy, zamiast czekać na automatyczne wygaśnięcie TTL.

### Wyświetlanie listy środowisk

Wyświetl listę aktywnych środowisk należących do Twojego projektu. Użyj parametrów stronicowania, aby kontrolować wielkość wsadu odpowiedzi.

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

Odpowiedź będzie wyglądać mniej więcej tak:

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

### Pobieranie środowiska

Pobierz metadane i szczegóły konfiguracji konkretnego środowiska według jego nazwy zasobu.

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

Odpowiedź będzie wyglądać mniej więcej tak:

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

### Usuwanie środowiska

Jawnie zakończ i usuń środowisko, aby zwolnić miejsce w zasobach piaskownicy po zakończeniu zadań lub potoków.

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

## Pobieranie plików ze środowiska

Podczas wykonywania agent tworzy pliki w piaskownicy. Za pomocą interfejsu Files API możesz pobrać pełną migawkę środowiska jako plik tar:

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

## Ceny i zasoby

Każde środowisko działa z przydzielonymi zasobami:

| Zasób | Wartość |
| --- | --- |
| **CPU** | 4 rdzenie |
| **Pamięć** | 16 GB |

W okresie korzystania z wersji testowej **nie są naliczane opłaty** za zasoby obliczeniowe środowiska (CPU, pamięć, wykonywanie w piaskownicy). Koszty tokenów agenta znajdziesz w sekcji
[Ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents).

## Ograniczenia

- **Stan wersji testowej:** środowiska i agenci zarządzani są w wersji testowej. Funkcje i schematy mogą ulec zmianie.
- **Rozmiar źródła w tekście:** źródła w tekście są ograniczone do 1 MB na plik i 2 MB łącznie we wszystkich plikach.
- **Rozmiar źródła**: repozytoria Git są ograniczone do 500 MB, a repozytoria Cloud Storage do 2 GB.
- **Uruchamianie środowiska:** utworzenie nowego środowiska trwa do ok. 5 sekund. Duże repozytoria źródłowe mogą wydłużyć ten czas.
- **Wygasanie środowiska:** nieaktywne środowiska offline są przechowywane przez 7 dni, a następnie usuwane za pomocą automatycznego czyszczenia TTL. Przekazanie wygasłego lub nieprawidłowego identyfikatora środowiska powoduje zwrócenie błędu `404 Not Found`.
- **Obsługa plików:** agent może obecnie odczytywać tylko pliki tekstowe i obrazy. Obsługa plików binarnych nie jest jeszcze dostępna.
- **Brak montowania z katalogu głównego:** podczas dodawania źródła niestandardowego nie możesz ustawić katalogu głównego (`/`) jako miejsca docelowego. Zawsze musisz określić podkatalog.

## Co dalej?

- [Omówienie agentów](https://ai.google.dev/gemini-api/docs/agents?hl=pl): poznaj podstawowe koncepcje agentów zarządzanych.
- [Krótkie wprowadzenie](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl): zacznij tworzyć aplikacje z wieloetapowymi rozmowami i przesyłaniem strumieniowym.
- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl): poznaj możliwości, narzędzia, wybór modelu i ceny domyślnego agenta.
- [Tworzenie agentów niestandardowych](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl): definiuj własnych agentów za pomocą plików `AGENTS.md` i `SKILL.md`.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-23 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-23 UTC."],[],[]]
