---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=fr
fetched_at: 2026-09-21T05:47:53.462997+00:00
title: "Combiner les outils int\u00e9gr\u00e9s et l'appel de fonction \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Combiner les outils intégrés et l'appel de fonction

Gemini permet de combiner des [outils intégrés](https://ai.google.dev/gemini-api/docs/tools?hl=fr), tels
que `google_search`, et l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
(également appelé *outils personnalisés*) en une seule génération en préservant et en exposant
l'historique du contexte des appels d'outils. Les combinaisons d'outils intégrés et personnalisés permettent de créer des workflows complexes et autonomes où, par exemple, le modèle peut s'appuyer sur des données Web en temps réel avant d'appeler votre logique métier spécifique.

Voici un exemple qui active les combinaisons d'outils intégrés et personnalisés avec `google_search` et une fonction personnalisée `getWeather` :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.getGenerativeModel({
        model: "gemini-3.6-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.6-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## Fonctionnement

Les modèles Gemini 3 utilisent la *circulation du contexte d'outil* pour activer les combinaisons d'outils intégrés et personnalisés. La circulation du contexte d'outil permet de préserver et d'exposer le contexte des outils intégrés, et de le partager avec des outils personnalisés dans le même appel, d'un tour à l'autre.

### Activer la combinaison d'outils

- Vous devez définir l'option `include_server_side_tool_invocations` sur `true` pour activer la circulation du contexte d'outil.
- Incluez les [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#function-declarations), ainsi que les
  outils intégrés que vous souhaitez utiliser, pour déclencher le comportement de combinaison.
  - Si vous n'incluez pas `function_declarations`, la circulation du contexte d'outil agira toujours sur les outils intégrés inclus, tant que l'option est définie.

### L'API renvoie des parties

Dans une seule réponse, l'API renvoie les parties `toolCall` et `toolResponse` pour l'appel d'outil intégré. Pour l'appel de fonction (outil personnalisé), l'API renvoie la partie d'appel `functionCall`, à laquelle l'utilisateur fournit la partie `functionResponse` au tour suivant.

- `toolCall` et `toolResponse` : l'API renvoie ces parties pour préserver le contexte des outils exécutés côté serveur et le résultat de leur exécution pour le tour suivant.
- `functionCall` et `functionResponse` : l'API envoie l'appel de fonction à
  l'utilisateur pour qu'il le remplisse, et l'utilisateur renvoie le résultat dans la
  réponse de la fonction (ces parties sont standards pour tous les [appels de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) de l'API Gemini, et ne sont pas propres à la
  fonctionnalité de combinaison d'outils).
- ([Outil d'exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) uniquement)
  `executableCode` et `codeExecutionResult` :
  Lorsque vous utilisez l'outil d'exécution de code, au lieu de `functionCall` et
  `functionResponse`, l'API renvoie `executableCode` (le code généré
  par le modèle qui doit être exécuté) et `codeExecutionResult` (le
  résultat du code exécutable).

Vous devez renvoyer toutes les parties, y compris tous les [champs](#critical-fields) qu'elles
contiennent, au modèle à chaque tour pour conserver le contexte et activer les combinaisons
d'outils.

### Champs essentiels dans les parties renvoyées

Certaines [parties renvoyées par l'API](#api-returns-parts) incluent les champs `id`,
`tool_type` et `thought_signature`. Ces champs sont essentiels pour conserver le contexte de l'outil (et donc pour les combinaisons d'outils). Vous devez renvoyer toutes les parties *telles qu'elles sont indiquées dans la réponse* dans vos requêtes suivantes.

- `id` : identifiant unique qui mappe un appel à sa réponse. `id` est **défini sur
  toutes les réponses d'appel de fonction**, quelle que soit la circulation du contexte d'outil.
  Vous *devez* fournir le même `id` dans la réponse de la fonction que celui fourni par l'API dans l'appel de fonction. Les outils intégrés partagent automatiquement l'`id` entre l'appel d'outil et la réponse de l'outil.
  - Présent dans toutes les parties liées à l'outil : `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: identifie l'outil spécifique utilisé ; le nom littéral de l'outil intégré ou (par exemple, `URL_CONTEXT`) ou de la fonction (par exemple, `getWeather`).
  - Présent dans les parties `toolCall` et `toolResponse`.
- `thought_signature`: contexte chiffré réel intégré dans **chaque partie renvoyée par l'API**. Le contexte ne peut pas être reconstruit sans les signatures de pensée. Si vous ne renvoyez pas les signatures de pensée pour toutes les parties à chaque tour, le modèle générera une erreur.
  - Présent dans *toutes* les parties.

### Données spécifiques à l'outil

Certains outils intégrés renvoient des arguments de données visibles par l'utilisateur, spécifiques au type d'outil.

| Outil | Arguments d'appel d'outil visibles par l'utilisateur (le cas échéant) | Réponse de l'outil visible par l'utilisateur (le cas échéant) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL à parcourir | `urls_metadata` `retrieved_url` : URL parcourues `url_retrieval_status` : état de la navigation |
| **FILE\_SEARCH** | Aucun | Aucun |

## Exemple de structure de requête de combinaison d'outils

La structure de requête suivante montre la structure de requête de l'invite : "Quelle est la ville la plus au nord des États-Unis ? Quel temps fait-il aujourd'hui ?". Elle combine trois outils : les outils Gemini intégrés `google_search` et `code_execution`, ainsi qu'une fonction personnalisée `get_weather`.

```
{
  "model": "models/gemini-3.6-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## Jetons et tarifs

Notez que les parties `toolCall` et `toolResponse` des requêtes sont comptabilisées dans `prompt_token_count`. Étant donné que ces étapes intermédiaires de l'outil sont désormais visibles et vous sont renvoyées, elles font partie de l'historique des conversations. Cela n'est le
cas que pour les *requêtes*, et non pour les *réponses*.

L'outil Recherche Google est une exception à cette règle. La recherche Google applique déjà son propre modèle de tarification au niveau de la requête. Les jetons ne sont donc pas facturés deux fois (consultez la page [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr)).

Pour en savoir plus, consultez la page [Jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr).

## Limites

- Par défaut, le mode `VALIDATED` est utilisé (le mode `AUTO` n'est pas compatible) lorsque l'option `include_server_side_tool_invocations` est activée.
- Les outils intégrés tels que `google_search` s'appuient sur des informations de localisation et d'heure actuelles. Par conséquent, si votre `system_instruction` ou `function_declaration.description` contient des informations de localisation et d'heure conflictuelles, la fonctionnalité de combinaison d'outils risque de ne pas fonctionner correctement.

## Outils compatibles

La circulation standard du contexte d'outil s'applique aux outils côté serveur (intégrés).
L'exécution de code est également un outil côté serveur, mais il dispose de sa propre solution intégrée pour la circulation du contexte. L'utilisation de l'ordinateur et l'appel de fonction sont des outils côté client, et disposent également de solutions intégrées pour la circulation du contexte.

| Outil | Côté exécution | Compatibilité avec la circulation du contexte |
| --- | --- | --- |
| [Recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) | Côté serveur | Compatible |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr) | Côté serveur | Compatible |
| [Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) | Côté serveur | Compatible |
| [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr) | Côté serveur | Compatible |
| [Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) | Côté serveur | Compatible (intégré, utilise les parties `executableCode` et `codeExecutionResult`) |
| [Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr) | Côté client | Compatible (intégré, utilise les parties `functionCall` et `functionResponse`) |
| [Fonctions personnalisées](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) | Côté client | Compatible (intégré, utilise les parties `functionCall` et `functionResponse`) |

## Étape suivante

- En savoir plus sur l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) dans l'API Gemini.
- Découvrez les outils compatibles :
  - [Recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)
  - [Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)
  - [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/12 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/12 (UTC)."],[],[]]
