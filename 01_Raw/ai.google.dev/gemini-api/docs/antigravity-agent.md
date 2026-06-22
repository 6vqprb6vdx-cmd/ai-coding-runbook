---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl
fetched_at: 2026-06-22T06:28:26.147915+00:00
title: "Agent Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agent Antigravity

Agent Antigravity to agent do zwykłych obciążeń zarządzany w Gemini API. Pojedyncze wywołanie interfejsu API zapewnia dostęp do agenta, który rozumuje, wykonuje kod, zarządza plikami i przegląda internet w bezpiecznej piaskownicy Linux hostowanej przez Google.

Jest on oparty na modelu Gemini 3.5 Flash i korzysta z tego samego szkieletu co Antigravity IDE. Jest dostępny za pomocą [interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) i [Google AI Studio](https://aistudio.google.com?hl=pl).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Uprawnienia

Każde wywołanie może udostępnić piaskownicę Linux i uruchomić pętlę korzystania z narzędzi. Agent planuje, działa, obserwuje wyniki i powtarza te czynności, aż zadanie zostanie wykonane.

- **Wykonywanie kodu:** uruchamiaj polecenia Bash, Python i Node.js. Instaluj pakiety, przeprowadzaj testy i twórz aplikacje.
- **Zarządzanie plikami:** odczytuj, zapisuj, edytuj, wyszukuj i wyświetlaj pliki w piaskownicy. Pliki są zachowywane między interakcjami.
- **Dostęp do internetu:** wyszukiwarka Google i pobieranie adresów URL na potrzeby danych.
- **Kompaktowanie kontekstu:** automatyczne kompaktowanie kontekstu (wyzwalane przy ok. 135 tys. tokenów) w celu obsługi długotrwałych sesji wieloetapowych bez utraty kontekstu i przekroczenia limitów tokenów.

Więcej informacji o korzystaniu z sesji wieloetapowych i streamingu znajdziesz w [krótkim wprowadzeniu](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl).

## Obsługiwane narzędzia

Domyślnie agent ma dostęp do narzędzi `code_execution`, `google_search` i `url_context`. Narzędzia systemu plików są włączane automatycznie, gdy określisz parametr `environment`. Możesz też zdefiniować **funkcje niestandardowe** , aby połączyć agenta z własnymi interfejsami API i narzędziami. Parametr `tools` musisz określić tylko wtedy, gdy dostosowujesz lub ograniczasz domyślny zestaw narzędzi albo dodajesz funkcje niestandardowe.

| Narzędzie | Wartość typu | Opis |
| --- | --- | --- |
| Wykonywanie kodu | `code_execution` | Uruchamiaj polecenia powłoki (Bash, Python, Node) z przechwytywaniem stdout/stderr. |
| Wyszukiwarka Google | `google_search` | Szukaj w sieci publicznej. |
| Kontekst adresu URL | `url_context` | Pobieraj i odczytuj strony internetowe. |
| System plików | *(włączone przez `environment`)* | Odczytuj, zapisuj, edytuj, wyszukuj i wyświetlaj pliki w piaskownicy. Brak osobnego typu narzędzia. Włączane automatycznie, gdy ustawiony jest parametr `environment`. |
| Funkcje niestandardowe | `function` | Zdefiniuj funkcje niestandardowe, które agent może wywoływać. Zobacz [Wywoływanie funkcji](#function-calling). |

Aby ograniczyć agenta do określonych narzędzi, przekaż tylko te, których potrzebujesz:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Wielomodalne dane wejściowe

Agent Antigravity obsługuje wielomodalne dane wejściowe. Obecnie obsługiwane są tylko dane wejściowe `text` i `image`. Obrazy muszą być podawane jako ciągi tekstowe z kodowaniem Base64 (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Wywoływanie funkcji

Wywoływanie funkcji umożliwia połączenie agenta Antigravity z zewnętrznymi interfejsami API i bazami danych przez zdefiniowanie niestandardowych narzędzi, które agent może wywoływać. Ogólne informacje znajdziesz w artykule [Wywoływanie funkcji za pomocą Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl).

Poniższy przykład przedstawia interakcję 2-etapową. Najpierw agent prosi o wywołanie funkcji niestandardowej `get_weather`, a klient ją wykonuje i zwraca wynik w drugim etapie.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## Dostosowywanie agenta

Możesz rozszerzyć możliwości agenta Antigravity, dostosowując jego instrukcje, narzędzia i środowisko. Agent obsługuje natywne dla systemu plików podejście do dostosowywania: możesz zamontować pliki, takie jak `AGENTS.md`, z instrukcjami i umiejętnościami w katalogu `.agents/skills/` bezpośrednio w piaskownicy lub przekazać konfigurację w tekście podczas interakcji. Możesz iterować konfigurację w tekście, a potem zapisać ją jako agenta zarządzanego.

Szczegółowe informacje o tworzeniu agentów niestandardowych znajdziesz w artykule [Tworzenie agentów zarządzanych](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl).

## Środowiska

Każde wywołanie tworzy lub ponownie wykorzystuje piaskownicę Linux. Parametr `environment` może przyjmować 3 formy:

| Pozycja | Opis |
| --- | --- |
| `"remote"` | Udostępnij nową piaskownicę z ustawieniami domyślnymi. |
| `"env_abc123"` | Ponownie wykorzystaj istniejące środowisko według identyfikatora, zachowując wszystkie pliki i stan. |
| `{...}` | Pełna konfiguracja `EnvironmentConfig` ze źródłami niestandardowymi i regułami sieci. |

Szczegółowe informacje o źródłach (Git, GCS, w tekście), sieci, cyklu życia i limitach zasobów znajdziesz w artykule [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).

## Dostępność i ceny

Agent Antigravity jest dostępny w wersji testowej za pomocą interfejsu [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) w Google AI Studio i Gemini API.

Ceny są oparte na modelu [płatności według wykorzystania](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents) i zależą od tokenów modelu Gemini oraz narzędzi używanych przez agenta. W przeciwieństwie do standardowego żądania czatu, które generuje pojedyncze dane wyjściowe, interakcja z agentem Antigravity to przepływ pracy oparty na agentach. Pojedyncze żądanie wywołuje autonomiczny cykl rozumowania, wykonywania narzędzi, uruchamiania kodu i zarządzania plikami.

### Szacunkowy koszt

Koszty zależą od złożoności zadania. Agent autonomicznie określa, ile wywołań narzędzi, wykonań kodu i operacji na plikach jest potrzebnych. Poniższe szacunki są oparte na uruchomieniach.

| Kategoria zadania | Tokeny wejściowe | Tokeny wyjściowe | Typowy koszt |
| --- | --- | --- | --- |
| **Badania i synteza informacji** | 100 tys.–500 tys. | 10 tys.–40 tys. | 0,30–1,00 USD |
| **Generowanie dokumentów i treści** | 100 tys.–500 tys. | 15 tys.–50 tys. | 0,30–1,30 USD |
| **Projektowanie procesów i systemów** | 100 tys.–400 tys. | 10 tys.–30 tys. | 0,25–0,80 USD |
| **Przetwarzanie i analiza danych** | 300 tys.–3 mln | 30 tys.–150 tys. | 0,70–3,25 USD |

Zazwyczaj w pamięci podręcznej jest przechowywanych 50–70% tokenów wejściowych. Złożone przepływy pracy oparte na agentach z wieloma wywołaniami narzędzi mogą gromadzić 3–5 milionów tokenów w jednej interakcji, a koszty mogą sięgać ok. 5 USD.

W okresie korzystania z wersji testowej **nie są naliczane opłaty** za **obliczenia w środowisku** (procesor, pamięć, wykonywanie w piaskownicy).

## Ograniczenia

- **Stan wersji testowej:** agent Antigravity i interfejs Interactions API są w wersji testowej. Funkcje i schematy mogą ulec zmianie.
- **Nieobsługiwana konfiguracja generowania:** te parametry nie są obsługiwane i zwracają błąd 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Uporządkowane dane wyjściowe:** agent Antigravity nie obsługuje uporządkowanych danych wyjściowych.
- **Niedostępne narzędzia:** narzędzia `file_search`, `computer_use`, `google_maps` i `mcp` nie są jeszcze obsługiwane.
- **Narzędzie systemu plików:** obecnie nie ma narzędzia systemu plików. Jest ono częścią `environment`.
- **Tło:** agent nie obsługuje używania `background=True` i wymaga `store=True`.
- **Wywoływanie funkcji tylko w trybie stanowym:** wywoływanie funkcji jest obsługiwane tylko w trybie stanowym. Aby kontynuować etap, musisz użyć `previous_interaction_id`. Ręczne odtwarzanie historii (tryb bezstanowy) nie jest obsługiwane.
- **Nieobsługiwane typy multimodalne.** Obecnie nie są obsługiwane dane wejściowe audio, wideo i dokumenty. Dozwolone są tylko tekst i obraz.

## Co dalej?

- [Krótkie wprowadzenie](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl): rozmowy wieloetapowe i streaming.
- [Tworzenie agentów niestandardowych](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl): instrukcje niestandardowe, umiejętności i zapisywanie agentów.
- [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl): konfiguracja piaskownicy, źródła, sieć.
- [Agent Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=pl): zadania badawcze o długim formacie.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl): podstawowy interfejs API.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-17 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-17 UTC."],[],[]]
