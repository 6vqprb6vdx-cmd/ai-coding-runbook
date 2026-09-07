---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl
fetched_at: 2026-09-07T05:36:51.938295+00:00
title: "Tworzenie agent\u00f3w zarz\u0105dzanych \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tworzenie agentów zarządzanych

Zarządzane agenty w Gemini API umożliwiają rozszerzenie agenta Antigravity o własne instrukcje, umiejętności i dane. Możesz [dostosować agenta w tekście](#customize-inline) w czasie interakcji lub [zapisać konfigurację](#save-agent) jako zarządzanego agenta, którego wywołujesz za pomocą identyfikatora.

## Dostosowywanie agenta Antigravity

Najszybszym sposobem na utworzenie agenta niestandardowego jest przekazanie konfiguracji w tekście podczas tworzenia nowej interakcji bez konieczności rejestracji. Agenta możesz rozszerzyć na kilka sposobów:

- **[Wybór modelu](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#model-selection)**: wybierz model Gemini bazowy za pomocą parametru `agent_config` (domyślnie **Gemini 3.7 Flash**).
- **Instrukcje systemowe**: przekaż tekst w tekście za pomocą parametru `system_instruction`, aby kształtować zachowanie.
- **Narzędzia**: zastąp domyślne narzędzia (wykonywanie kodu, wyszukiwanie, kontekst adresu URL), zarejestruj zdalne serwery MCP lub zdefiniuj funkcje niestandardowe (wywoływanie funkcji).
- **Pliki i umiejętności**: zamontuj pliki takie jak `AGENTS.md` i `SKILL.md` w środowisku.

Oto przykład przekazywania wszystkich 3 elementów w tekście:

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

Wszystko jest zdefiniowane w czasie interakcji. Nie musisz niczego rejestrować. Uprząż agenta Antigravity zapewnia środowisko wykonawcze (wykonywanie kodu, zarządzanie plikami, dostęp do internetu) i warstwy konfiguracji.

### Narzędzia i instrukcje systemowe

Zachowanie i możliwości agenta w przypadku konkretnej interakcji możesz dostosować za pomocą parametrów `system_instruction` i `tools`.

- **Instrukcje systemowe**: użyj parametru `system_instruction`, aby przekazać tekst w tekście, który kształtuje zachowanie agenta. Jest to idealne rozwiązanie w przypadku szybkich zmian, które chcesz wprowadzić w każdej rozmowie. Parametry `system_instruction` i `AGENTS.md` są addytywne. Oba mają zastosowanie, gdy są obecne.
- **Narzędzia**: domyślnie agent Antigravity ma dostęp do narzędzi `code_execution`, `google_search` i `url_context`. Tę listę możesz zastąpić, przekazując parametr `tools` w czasie interakcji. Możesz też zarejestrować [zdalne serwery MCP](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#mcp-servers) lub zdefiniować [funkcje niestandardowe (wywoływanie funkcji)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#function-calling), aby połączyć agenta z własnymi interfejsami API i bazami danych. Szczegółowe informacje o dostępnych narzędziach znajdziesz w artykule [Agent Antigravity: obsługiwane narzędzia](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#supported-tools).

### Dostosowywanie na podstawie plików

#### Struktura katalogu agenta

Konfigurację możesz przekazać w tekście, ale zalecamy uporządkowanie plików agenta w uporządkowanym katalogu. Ułatwia to zarządzanie, kontrolę wersji i montowanie w środowisku agenta.

Typowy katalog projektu agenta wygląda tak:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Środowisko wykonawcze Antigravity skanuje te pliki w katalogu `.agents/` (i w katalogu głównym środowiska).

#### AGENTS.md

Podczas uruchamiania agent automatycznie wczytuje plik `.agents/AGENTS.md` (lub `/.agents/AGENTS.md`) ze środowiska jako instrukcje systemowe. Użyj pliku `AGENTS.md` do definiowania długich opisów person, szczegółowych wytycznych i instrukcji, które chcesz kontrolować za pomocą kontroli wersji wraz z kodem.

Zamontuj plik `AGENTS.md` za pomocą źródła w tekście:

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

#### Umiejętności: SKILL.md

Umiejętności to pliki, które rozszerzają możliwości agenta. Umieść je w katalogu `.agents/skills/<skill-name>/SKILL.md`, a platforma automatycznie je wykryje i zarejestruje.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Zamontuj umiejętność za pomocą źródła w tekście:

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

Umiejętności wczytane z katalogów `.agents/skills/` i `/.agents/skills/` są wykrywane automatycznie.

## Tworzenie zarządzanego agenta

Po przejrzeniu konfiguracji możesz utworzyć ją jako zarządzanego agenta za pomocą polecenia `agents.create`. Dzięki temu możesz wywoływać agenta za pomocą identyfikatora bez konieczności powtarzania konfiguracji.

Określony podczas tworzenia zarządzanego agenta `id` musi być unikalny w Twoim projekcie i nie może zaczynać się od zarezerwowanych prefiksów (np. `google-`, `gemini-`). Pełną listę zastrzeżonych prefiksów znajdziesz w sekcji [Ograniczenia dotyczące identyfikatora agenta](#agent-id-restrictions).

### Ze źródeł

Określ `base_agent`, `id`, `agent_config`, `system_instruction` i `base_environment` ze źródłami. Platforma udostępnia nową piaskownicę z Twoimi plikami przy każdym wywołaniu. Dostępne typy źródeł (Git, GCS, w tekście) znajdziesz w sekcji [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.7-flash",
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
        model: "gemini-3.7-flash",
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
        "model": "gemini-3.7-flash"
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

### Z istniejącego środowiska (fork)

Pracuj z podstawowym agentem Antigravity, aż środowisko będzie odpowiednie (zainstalowane pakiety, pliki na miejscu), a następnie utwórz z niego zarządzanego agenta.

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

### Z regułami sieciowymi

Podczas zapisywania zarządzanego agenta możesz zablokować dostęp wychodzący lub wstawić dane logowania. Pełny schemat listy dozwolonych, wzorce danych logowania i symbole wieloznaczne znajdziesz w sekcji [Środowiska: konfiguracja sieci](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#network-configuration).

Poniższy przykład tworzy agenta `issue-resolver`, który może uzyskiwać dostęp tylko do GitHuba i PyPI, z danymi logowania wstawionymi do GitHuba:

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

## Wywoływanie agenta

Wywołaj zarządzanego agenta za pomocą jego identyfikatora, tworząc nową interakcję. Każde wywołanie tworzy kopię środowiska podstawowego, więc każde uruchomienie zaczyna się od nowa.

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

Informacje o rozmowach wieloetapowych i przesyłaniu strumieniowym znajdziesz w [krótkim wprowadzeniu](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl). Te same wzorce `previous_interaction_id` i `environment` mają zastosowanie do zarządzanych agentów.

Zarządzani agenci obsługują też wykonywanie w tle i anulowanie. Szczegółowe informacje i przykłady kodu znajdziesz w artykule [Agent Antigravity: wykonywanie w tle](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#background-execution).

## Zastępowanie konfiguracji podczas wywołania

Podczas tworzenia interakcji możesz zastąpić domyślną konfigurację sieci `system_instruction`, `tools` i `environment` agenta. Dzięki temu możesz modyfikować zachowanie, możliwości lub dane logowania agenta w przypadku konkretnego uruchomienia bez zmiany zapisanej definicji agenta.

### Zastępowanie instrukcji systemowych i narzędzi

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

### Zastępowanie konfiguracji sieci (odświeżanie danych logowania)

Jeśli zarządzany agent ma dane logowania do sieci wbudowane w `base_environment`, możesz je zastąpić podczas wywołania, aby odświeżyć wygasłe tokeny lub zmienić klucze API. Przekaż obiekt `environment` z nową konfiguracją `network`. Nowe reguły sieciowe całkowicie zastępują poprzednie w przypadku tej interakcji. Źródła środowiska podstawowego (pliki, repozytoria) są zachowywane.

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

## Zarządzanie agentami

Możesz wyświetlać listę agentów, pobierać ich i usuwać.

### Wyświetlenie listy agentów

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

### Pobieranie agenta

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

### Usuwanie agenta

Usunięcie powoduje usunięcie konfiguracji. Nie ma to wpływu na istniejące środowiska i interakcje utworzone przez agenta.

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

## Informacje o definicji agenta

| Pole | Typ | Wymagane | Opis |
| --- | --- | --- | --- |
| `id` | tekst | Tak | Unikalny identyfikator agenta w projekcie w chmurze Google. Używany do wywoływania agenta. Nie może używać zarezerwowanych prefiksów. Więcej informacji znajdziesz w sekcji [Ograniczenia dotyczące identyfikatora agenta](#agent-id-restrictions). |
| `description` | tekst | Nie | Zrozumiały dla człowieka opis agenta. |
| `base_agent` | tekst | Tak | Identyfikator agenta podstawowego (np. `antigravity-preview-05-2026`). |
| `agent_config` | obiekt | Nie | Konfiguracja agenta podstawowego, w tym wybór modelu (`{"type": "antigravity", "model": "gemini-3.7-flash"}`). Jeśli ten parametr zostanie pominięty, domyślnie używany jest model `gemini-3.7-flash`. W przypadku nazwanych agentów nie można go zastąpić w czasie interakcji. |
| `system_instruction` | tekst | Nie | Prompt systemowy definiujący zachowanie i personę. |
| `tools` | tablica | Nie | Narzędzia, których może używać agent. Jeśli ten parametr zostanie pominięty, domyślnie używane są narzędzia `code_execution`, `google_search` i `url_context`. Obsługiwane narzędzia to `code_execution`, `google_search`, `url_context`, `mcp_server` i definicje niestandardowych `function`. |
| `base_environment` | tekst lub obiekt | Nie | `"remote"`, `environment_id` lub obiekt konfiguracji z parametrami `sources` i `network`. Więcej informacji znajdziesz w sekcji Środowiska. |

### Ograniczenia dotyczące identyfikatora agenta

Podczas tworzenia zarządzanego agenta określony identyfikator `id` musi spełniać te wymagania:

- Musi być unikalny w Twoim projekcie Google Cloud.
- **Nie może** zaczynać się od żadnego z tych zarezerwowanych prefiksów (bez uwzględniania wielkości liter), w przeciwnym razie utworzenie się nie powiedzie:
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

## Przepływ pracy iteracji

1. **Prototyp** z podstawowym agentem Antigravity. Przekaż instrukcje systemowe i źródła środowiska w tekście. Interaktywnie testuj instrukcje, umiejętności i konfigurację środowiska.
2. **Stabilizuj** środowisko. Zainstaluj pakiety, zamontuj źródła i sprawdź, czy wszystko działa.
3. **Utrwal** jako zarządzanego agenta, tworząc nowego agenta ze źródeł lub przez utworzenie kopii środowiska.
4. **Zaktualizuj** definicję agenta. Zmień instrukcje systemowe, zamień umiejętności lub dodaj źródła. Następne wywołanie spowoduje użycie nowej konfiguracji.

## Ograniczenia

- **Sprawdź, w jakim stopniu spełniasz wymagania**: zarządzani agenci są dostępni w wersji zapoznawczej. Funkcje i schematy mogą ulec zmianie.
- **Agent podstawowy i modele**: jako `base_agent` obsługiwany jest tylko agent `antigravity-preview-05-2026`. Obsługiwane opcje modelu w `agent_config` to `gemini-3.7-flash` (domyślny), `gemini-3.6-flash`, `gemini-3.5-flash` i `gemini-3.5-flash-lite`. W przypadku nazwanych agentów nie można zastąpić modelu w czasie interakcji.
- **Brak obsługi wersji**: obsługa wersji agentów i przywracanie poprzedniej wersji nie są jeszcze dostępne.
- **Brak zagnieżdżania subagentów**: delegowanie subagentów nie jest jeszcze obsługiwane.
- Możesz mieć maksymalnie 1000 zarządzanych agentów.

## Co dalej?

- [Omówienie agentów](https://ai.google.dev/gemini-api/docs/agents?hl=pl): poznaj podstawowe koncepcje zarządzanych agentów.
- [Krótkie wprowadzenie](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl): zacznij tworzyć rozmowy wieloetapowe i przesyłanie strumieniowe.
- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl): poznaj możliwości, narzędzia i ceny domyślnego agenta.
- [Środowiska agentów](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl): konfiguruj piaskownice, źródła i sieć.
- [Zarządzane agenty API w Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=pl): do tworzenia agentów z wbudowanym zarządzaniem organizacją.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-19 UTC."],[],[]]
