---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr
fetched_at: 2026-06-29T05:28:05.878478+00:00
title: "Agent Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Agent Antigravity

L'agent Antigravity est un agent géré à usage général sur l'API Gemini. Un seul appel d'API vous donne un agent qui raisonne, exécute du code, gère des fichiers et navigue sur le Web dans votre propre bac à sable Linux sécurisé, hébergé par Google.

Il est alimenté par Gemini 3.5 Flash et utilise le même harnais que l'IDE Antigravity. Disponible via l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) et [Google AI Studio](https://aistudio.google.com?hl=fr).

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
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Capacités

Chaque appel peut provisionner un bac à sable Linux et démarrer une boucle d'utilisation d'outil. L'agent planifie, agit, observe les résultats et répète l'opération jusqu'à ce que la tâche soit terminée.

- **Exécution de code** : exécutez des commandes Bash, Python et Node.js. Installez des packages, exécutez des tests et créez des applications.
- **Gestion des fichiers** : lisez, écrivez, modifiez, recherchez et listez des fichiers dans le bac à sable. Les fichiers sont conservés entre les interactions.
- **Accès Web** : recherche Google et récupération d'URL pour les données.
- **Compactage du contexte** : compactage automatique du contexte (déclenché à environ 135 000 jetons) pour prendre en charge les sessions de longue durée et multitours sans perdre le contexte ni atteindre les limites de jetons.

Pour en savoir plus sur l'utilisation multitour et le streaming, consultez le [Quickstart](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr).

## Outils compatibles

Par défaut, l'agent a accès à `code_execution`, `google_search` et `url_context`. Les outils de système de fichiers sont activés automatiquement lorsque vous spécifiez le paramètre `environment`. Vous pouvez également définir des **fonctions personnalisées** pour connecter l'agent à vos propres API et outils. Vous n'avez besoin de spécifier le paramètre `tools` que lorsque vous personnalisez ou limitez l'ensemble par défaut, ou lorsque vous ajoutez des fonctions personnalisées.

| Outil | Valeur du type | Description |
| --- | --- | --- |
| Exécution du code | `code_execution` | Exécutez des commandes shell (bash, Python, Node) avec capture stdout/stderr. |
| Recherche Google | `google_search` | Recherchez sur le Web public. |
| Contexte de l'URL | `url_context` | Récupérez et lisez des pages Web. |
| Système de fichiers | *(activé via `environment`)* | Lisez, écrivez, modifiez, recherchez et listez des fichiers dans le bac à sable. Aucun type d'outil distinct ; activé automatiquement lorsque `environment` est défini. |
| Fonctions personnalisées | `function` | Définissez des fonctions personnalisées que l'agent peut demander à exécuter. Consultez [Appel de fonction](#function-calling). |
| Serveur MCP distant | `mcp_server` | Enregistrez des serveurs MCP (Model Context Protocol) externes en tant qu'outils. Consultez [Serveurs MCP](#mcp-servers). |

Pour limiter l'agent à des outils spécifiques, ne transmettez que ceux dont vous avez besoin :

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

## Requêtes multimodales

L'agent Antigravity est compatible avec les requêtes multimodales. Actuellement, seules les requêtes `text` et `image` sont acceptées. Les images doivent être fournies sous forme de chaînes encodées en base64 intégrées (`data`).

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

## Appel de fonction

L'appel de fonction vous permet de connecter l'agent Antigravity à des API et des bases de données externes en définissant des outils personnalisés que l'agent peut appeler. Pour en savoir plus sur les concepts généraux, consultez [Appel de fonction avec l'API Gemini](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=fr).

L'exemple suivant illustre une interaction en deux tours. L'agent demande d'abord un appel de fonction `get_weather` personnalisé, puis le client l'exécute et renvoie le résultat au deuxième tour.

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

## Serveurs MCP

Vous pouvez connecter l'agent Antigravity à des outils externes en enregistrant des serveurs MCP (Model Context Protocol) distants. L'agent est compatible avec les serveurs MCP distants via HTTP diffusable.

Lorsque vous enregistrez un serveur MCP, vous devez spécifier les champs suivants dans le tableau `tools` :

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `type` | chaîne | Oui | Doit être `"mcp_server"`. |
| `name` | chaîne | Oui | Identifiant unique du serveur. Doit être strictement en minuscules et alphanumérique (correspondant à `^[a-z0-9_-]+$`). |
| `url` | chaîne | Oui | URL du point de terminaison du serveur MCP distant. |
| `headers` | objet | Non | En-têtes personnalisés (par exemple, authentification) envoyés avec les requêtes. |
| `allowed_tools` | tableau | Non | Liste des noms d'outils autorisés à être exécutés. Si cette option est omise, tous les outils sont autorisés. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
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
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Personnaliser l'agent

Vous pouvez étendre l'agent Antigravity en personnalisant ses instructions, ses outils et son environnement. L'agent est compatible avec une approche native du système de fichiers pour la personnalisation : vous pouvez installer des fichiers tels que `AGENTS.md` pour les instructions et les compétences sous `.agents/skills/` directement dans le bac à sable, ou transmettre la configuration en ligne au moment de l'interaction. Vous pouvez itérer sur votre configuration en ligne, puis l'enregistrer en tant qu'agent géré lorsque vous êtes prêt.

Pour en savoir plus sur la création d'agents personnalisés, consultez [Créer des agents gérés](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr).

## Exécution en arrière-plan

Les tâches de l'agent qui impliquent un raisonnement en plusieurs étapes, l'exécution de code ou des opérations sur les fichiers peuvent prendre plusieurs minutes. Utilisez `background=True` pour exécuter l'interaction de manière asynchrone. L'API renvoie immédiatement un ID d'interaction que vous interrogez jusqu'à ce que l'état soit `completed` ou `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

L'exécution en arrière-plan nécessite `store=True`, qui est la valeur par défaut. Pour obtenir des mises à jour en temps réel de la progression lors de l'exécution en arrière-plan, consultez [Diffuser des interactions en arrière-plan](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=fr#streaming-background).

Vous pouvez annuler une interaction en arrière-plan en cours d'exécution à l'aide de la méthode `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel({ id: "INTERACTION_ID" });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Multitour avec exécution en arrière-plan**

Lorsqu'une interaction en arrière-plan implique des outils avec état (comme l'exécution de code dans un bac à sable), utilisez l'`environment_id` de l'interaction terminée pour continuer dans le même environnement. Cela permet à l'agent de reprendre là où il s'était arrêté, avec tous les fichiers et l'état intacts.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Environnements

Chaque appel crée ou réutilise un bac à sable Linux. Le paramètre `environment` prend trois formes :

| Formulaire | Description |
| --- | --- |
| `"remote"` | Provisionnez un nouveau bac à sable avec les paramètres par défaut. |
| `"env_abc123"` | Réutilisez un environnement existant par ID, en conservant tous les fichiers et l'état. |
| `{...}` | `EnvironmentConfig` complet avec des sources personnalisées et des règles réseau. |

Pour en savoir plus sur les sources (Git, GCS, en ligne), la mise en réseau, le cycle de vie et les limites de ressources, consultez [Environnements](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr).

## Disponibilité et prix

L'agent Antigravity est disponible en preview via l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) dans Google AI Studio et l'API Gemini.

La tarification suit un [modèle de paiement à l'usage](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#pricing-for-agents) basé sur les jetons du modèle Gemini sous-jacent et les outils utilisés par l'agent. Contrairement à une requête de chat standard qui produit une seule sortie, une interaction Antigravity est un workflow agentique. Une seule requête déclenche une boucle autonome de raisonnement, d'exécution d'outil, d'exécution de code et de gestion de fichiers.

### Coûts estimés

Les coûts varient en fonction de la complexité de la tâche. L'agent détermine de manière autonome le nombre d'appels d'outils, d'exécutions de code et d'opérations sur les fichiers nécessaires. Les estimations suivantes sont basées sur les exécutions.

| Catégorie de tâche | Jetons d'entrée | Jetons de sortie | Coût habituel |
| --- | --- | --- | --- |
| **Recherche et synthèse d'informations** | 100 000 à 500 000 | 10 000 à 40 000 | 0,30 $ à 1,00 $ |
| **Génération de documents et de contenu** | 100 000 à 500 000 | 15 000 à 50 000 | 0,30 $ à 1,30 $ |
| **Conception de processus et de systèmes** | 100 000 à 400 000 | 10 000 à 30 000 | 0,25 $ à 0,80 $ |
| **Traitement et analyse des données** | 300 000 à 3 000 000 | 30 000 à 150 000 | 0,70 $ à 3,25 $ |

50 à 70% des jetons d'entrée sont généralement mis en cache. Les workflows agentiques complexes avec de nombreux appels d'outils peuvent accumuler 3 à 5 millions de jetons dans une seule interaction, avec des coûts allant jusqu'à environ 5 $.

Le **calcul de l'environnement** (processeur, mémoire, exécution du bac à sable) **n'est pas facturé** pendant la période de preview.

## Limites

- **État de la preview** : l'agent Antigravity et l'API Interactions. Les fonctionnalités et les schémas peuvent changer.
- **Configuration de génération non compatible** : les paramètres suivants ne sont pas compatibles et renvoient une erreur 400 : `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Sortie structurée** : l'agent Antigravity n'est pas compatible avec les sorties structurées.
- **Outils non disponibles** : `file_search`, `computer_use` et `google_maps` ne sont pas encore compatibles.
- **Limites du MCP distant** : le transport des événements envoyés par le serveur (SSE) n'est pas compatible (utilisez HTTP diffusable). De plus, le `name` du serveur doit être strictement en minuscules et alphanumérique (l'utilisation de lettres majuscules déclenche une erreur générique `400 Bad Request`).
- **Outil de système de fichiers** : aucun outil de système de fichiers n'est disponible pour le moment. Il fait partie de l'`environment`.
- **Exigence de stockage** : l'exécution de l'agent à l'aide de `background=True` nécessite `store=True`.
- **Appel de fonction avec état uniquement** : l'appel de fonction n'est compatible qu'en mode avec état. Vous devez utiliser `previous_interaction_id` pour continuer le tour ; la reconstruction manuelle de l'historique (mode sans état) n'est pas compatible.
- **Types multimodaux non compatibles**. Les entrées audio, vidéo et de documents ne sont pas compatibles pour le moment. Seuls le texte et les images sont autorisés.

## Étape suivante

- [Guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr) : conversations multitours et diffusion en streaming.
- [Créer des agents personnalisés](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr) : instructions, compétences et enregistrement d'agents personnalisés.
- [Environnements](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr) : configuration du bac à sable, sources, mise en réseau.
- [Agent de recherche approfondie](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) : tâches de recherche de longue durée.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) : l'API sous-jacente.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/26 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/26 (UTC)."],[],[]]
