---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl
fetched_at: 2026-05-25T12:57:58.591598+00:00
title: "Szybki start z zarz\u0105dzanymi agentami \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Szybki start z zarządzanymi agentami

Z tego przewodnika dowiesz się, jak tworzyć i używać zarządzanych agentów w interfejsie Gemini API na przykładzie [agenta Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=pl). Nawiążesz pierwsze połączenie z agentem, będziesz kontynuować wieloetapową rozmowę, przesyłać strumieniowo odpowiedź, pobierać pliki z piaskownicy i pracować z zarządzanym agentem Antigravity.

## Przeprowadź pierwszą interakcję z agentem

Pojedyncze wywołanie [interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) udostępnia piaskownicę Linuksa, uruchamia pętlę agenta i zwraca wynik. Zdefiniujesz 3 parametry:

- Przekaż `agent` jako `"antigravity-preview-05-2026",`, czyli obecną wersję naszego predefiniowanego agenta zarządzanego ogólnego przeznaczenia.
- Zdefiniuj `environment="remote"`, aby udostępnić nowe, świeże środowisko piaskownicy.
- Utwórz dane wejściowe, określając, co ma robić agent.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

Odpowiedź zwraca obiekt `Interaction`. Zapisz `interaction.id` i `interaction.environment_id`, aby kontynuować rozmowę w tym samym środowisku piaskownicy. Użyj `interaction.output_text`, aby uzyskać dostęp do ostatecznej odpowiedzi agenta. `interaction.steps` zawiera listę wszystkich kroków podjętych przez agenta (rozumowanie, wywołania narzędzi, wykonanie kodu);

## Kontynuowanie rozmowy (wieloetapowej)

Interfejs API śledzi 2 niezależne wymiary stanu:

- **Kontekst rozmowy:** historia czatu, ślad rozumowania, korzystanie z narzędzi, używanie `previous_interaction_id`.
- [**Stan środowiska:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl) pliki, zainstalowane pakiety i stan piaskownicy, przy użyciu `environment`.

Przekaż oba w odpowiednich miejscach, aby wznowić:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Pliki z tury 1 (`fibonacci.txt`) są zachowywane w turze 2. Agent zachowuje też kontekst rozmowy.

Możesz je łączyć i dopasowywać niezależnie od siebie:

- **Wyczyść rozmowę, zachowaj pliki:** pomiń `previous_interaction_id`, przekaż tylko identyfikator środowiska za pomocą `environment`, aby rozpocząć nową rozmowę w tym samym obszarze roboczym.
- **Zachowaj rozmowę, nowy obszar roboczy:** przekaż `previous_interaction_id`, ustaw `environment="remote"`, aby utworzyć nowe środowisko testowe.

### Automatyczne kompresowanie kontekstu

W długich rozmowach wieloetapowych historia kroków rozumowania, wywołań narzędzi i zawartości dużych plików może szybko się rozrastać i zajmować dużo miejsca w kontekście. Aby zapobiec błędom związanym z limitem tokenów i utrzymać koncentrację agenta (zapobiec „rozmyciu kontekstu”), interfejs Managed Agents API zawiera natywny krok kompresji kontekstu przy około 135 tys. tokenów. Dzieje się to automatycznie.

## Przesyłanie odpowiedzi strumieniowo

W przypadku długotrwałych zadań możesz przesyłać strumieniowo odpowiedź, aby zobaczyć, jak agent pracuje w czasie rzeczywistym:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Strumieniowanie zwraca iterowalną listę zmian kroków, które są przyrostowymi aktualizacjami tekstu, tokenów uzasadnienia i wywołań narzędzi. Więcej informacji o strumieniowaniu odpowiedzi znajdziesz w [przewodniku po strumieniowaniu](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=pl).

## Pobieranie plików ze środowiska

Gdy agent tworzy pliki w piaskownicy. Pobierz je za pomocą interfejsu Files API za pomocą bezpośredniego żądania HTTP (nie ma jeszcze metody SDK):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

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
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Zapisywanie agenta zarządzanego

W poprzednich krokach użyliśmy domyślnego agenta Antigravity i dostosowaliśmy go w tekście. Po wprowadzeniu zmian w konfiguracji (instrukcje, umiejętności i środowisko) możesz zapisać ją jako zarządzanego agenta. Dzięki temu możesz wywołać go za pomocą identyfikatora bez powtarzania konfiguracji.

Podczas zapisywania agenta definiujesz `base_environment` (ze źródeł lub przez rozwidlenie istniejącego środowiska). Agent będzie używać tego środowiska w przypadku każdej nowej interakcji.

**Ze źródeł:** zdefiniuj źródła w tekście lub z innych źródeł, takich jak GitHub czy Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Wywoływanie agenta zarządzanego

Po zapisaniu zarządzanego agenta możesz go wywołać za pomocą identyfikatora. Każde wywołanie rozwidla środowisko bazowe, więc każde uruchomienie zaczyna się od czystego stanu:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Co dalej?

- [Antigravity Agent:](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl) funkcje, obsługiwane narzędzia, multimodalne wprowadzanie danych, ceny i ograniczenia.
- [Tworzenie zarządzanych agentów:](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl) rozszerzaj Antigravity o własne instrukcje, umiejętności i dane.
- [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl): źródła, sieci, cykl życia, limity zasobów.
- [Interfejs API interakcji:](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) podstawowy interfejs API dla modeli i agentów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-20 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-20 UTC."],[],[]]
