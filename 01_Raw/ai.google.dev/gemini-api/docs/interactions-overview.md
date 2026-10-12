---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr
fetched_at: 2026-10-12T07:10:12.713008+00:00
title: "API Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# API Interactions

L'API Interactions est le meilleur moyen de créer des applications avec les modèles et les agents Gemini. Depuis juin 2026, il est en disponibilité générale et recommandé pour tous les nouveaux projets. Bien qu'elle soit désormais considérée comme ancienne, l'API [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=fr) d'origine reste entièrement compatible.

## Pourquoi utiliser l'API Interactions ?

- **Interface universelle pour toutes les applications** : conçue comme interface standard pour tous les cas d'utilisation, y compris la génération de texte en un tour, la compréhension multimodale, les sorties structurées, l'orchestration d'outils et les workflows agentiques.
- **Une seule API pour les modèles et les agents** : un point de terminaison et un modèle unifiés pour appeler directement les modèles Gemini standards ainsi que les agents spécialisés (comme Deep Research et les agents gérés personnalisés).
- **Nouvelles fonctionnalités prêtes à l'emploi** : fonctionnalités telles que l'état de conversation côté serveur facultatif à l'aide de `previous_interaction_id`, les étapes d'exécution observables pour le débogage et le rendu de l'UI, et l'[exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) pour les tâches de longue durée à l'aide de `background=true`.
- **Coût réduit avec des taux de succès de cache plus élevés** : lorsque vous utilisez des conversations multitours, la gestion facultative de l'état côté serveur permet une mise en cache du contexte plus efficace entre les tours, ce qui réduit les coûts en jetons.
- **Où les nouvelles fonctionnalités seront-elles lancées ?** À l'avenir, tous les nouveaux modèles, outils, fonctionnalités multimodales et agentiques seront lancés sur l'API Interactions.

Par défaut, l'API Interactions stocke les requêtes afin que vous puissiez exploiter les fonctionnalités de gestion de l'état côté serveur à l'aide de `previous_interaction_id`. Vous pouvez activer le comportement sans état en définissant `store=false`. Pour en savoir plus, consultez la section [Conservation des données](#data-storage-retention).

## Commencer

- **Configurez votre agent de codage** : connectez-vous au **MCP Gemini Docs** et installez la compétence `gemini-api-dev` pour donner à votre assistant un accès direct aux dernières documentations pour les développeurs et aux bonnes pratiques. Pour obtenir la procédure détaillée, consultez le [guide de configuration de votre agent de programmation](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr).
- **Migrer depuis `generateContent`** : si vous disposez d'une intégration existante, suivez le [guide de migration](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=fr) pour passer à l'API Interactions.
- **Premiers pas** : suivez les étapes du [guide de démarrage de l'API Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=fr).

### Guides des fonctionnalités

Découvrez les fonctionnalités spécifiques de l'API Interactions grâce à ces guides. Vous pouvez utiliser le bouton bascule sur ces pages pour passer de l'API generateContent à l'API Interactions :

- [Génération de texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr)
- [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)
- [Compréhension des images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr)
- [Compréhension audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr)
- [Compréhension des vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr)
- [Traitement de documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr)
- [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
- [Sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)
- [Agent Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr)
- [Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)
- [Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)

## Fonctionnement de l'API Interactions

L'API Interactions est axée sur une ressource principale : [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=fr#Resource:Interaction). Un `Interaction` représente un tour complet dans une conversation ou une tâche. Il sert d'enregistrement de session et contient l'intégralité de l'historique d'une interaction sous forme de séquence chronologique d'**étapes d'exécution**. Ces étapes incluent les réflexions du modèle, les appels et les résultats d'outils côté serveur ou côté client (comme `function_call` et `function_result`), ainsi que le `model_output` final. La ressource stockée (récupérée via `interactions.get`) inclut également des étapes `user_input` pour un contexte complet, bien que la réponse `interactions.create` ne renvoie que les étapes générées par le modèle.

Lorsque vous appelez [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=fr#CreateInteraction), vous créez une ressource `Interaction` :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### Gestion de l'état côté serveur

Vous pouvez utiliser le `id` d'une interaction terminée dans un appel ultérieur à l'aide du paramètre `previous_interaction_id` pour poursuivre la conversation. Le serveur utilise cet ID pour récupérer l'historique des conversations, ce qui vous évite d'avoir à renvoyer l'intégralité de l'historique des discussions :

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
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

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

Le paramètre `previous_interaction_id` ne conserve que l'historique des conversations (entrées et sorties) à l'aide de `previous_interaction_id`. Les autres paramètres sont **de portée interaction** et ne s'appliquent qu'à l'interaction spécifique que vous générez actuellement :

- `tools`
- `system_instruction`
- `generation_config` (y compris `thinking_level`, `temperature`, etc.)

Cela signifie que vous devez spécifier à nouveau ces paramètres dans chaque nouvelle interaction si vous souhaitez qu'ils s'appliquent. Cette gestion de l'état côté serveur est facultative. Vous pouvez également fonctionner en mode sans état en envoyant l'intégralité de l'historique des conversations dans chaque requête.

### Stockage et conservation des données

Par défaut, l'API stocke tous les objets Interaction (`store=true`) afin de simplifier l'utilisation des fonctionnalités de gestion de l'état côté serveur (avec `previous_interaction_id`), de l'[exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) (à l'aide de `background=true`) et à des fins d'observabilité.

- **Niveau payant** : le système conserve les interactions pendant **55 jours**.
- **Niveau sans frais** : le système conserve les interactions pendant **un jour**.

Si vous ne le souhaitez pas, vous pouvez définir `store=false` dans votre demande. Cette commande est distincte de la gestion de l'état. Vous pouvez désactiver le stockage pour n'importe quelle interaction. Notez toutefois que `store=false` n'est pas compatible avec l'[exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) et empêche l'utilisation de `previous_interaction_id` pour les tours suivants.

Pour les projets de niveau payant, vous pouvez configurer la période de conservation dans [AI Studio](https://aistudio.google.com/logs?hl=fr) afin de marquer automatiquement les journaux pour suppression du stockage du projet après 7, 14, 28 ou 55 jours. Une durée de conservation plus courte peut affecter la récupération des conversations passées.

Vous pouvez supprimer les interactions stockées à tout moment à l'aide de la méthode [`delete`](https://ai.google.dev/api/interactions-api?hl=fr#deleteInteraction) par programmation, qui nécessite l'ID d'interaction. Vous pouvez également afficher et gérer les journaux des interactions stockées, y compris les supprimer du stockage du projet, dans [AI Studio](https://aistudio.google.com/logs?hl=fr).

Une fois la période de conservation expirée, vos données seront automatiquement supprimées.

Les objets d'interaction sont traités conformément aux [Conditions d'utilisation](https://ai.google.dev/gemini-api/terms?hl=fr).

### Afficher les interactions dans AI Studio

L'API stocke les requêtes de l'API Interactions exécutées avec `store=true` pour les projets du forfait payant. Vous pouvez les consulter directement sur la [page "Journaux" de Google AI Studio](https://aistudio.google.com/logs?hl=fr). Pour en savoir plus, consultez le [guide des journaux](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr).

## Bonnes pratiques

- **Taux de succès de cache** : la mise en cache implicite est compatible avec les modes avec état et sans état (voir [Démarrage rapide](https://ai.google.dev/gemini-api/docs/get-started?hl=fr#4_multi-turn_conversations)). L'utilisation de `previous_interaction_id` (avec état) pour poursuivre les conversations permet au système d'utiliser plus facilement la mise en cache implicite pour l'historique des conversations, ce qui améliore les performances et réduit les coûts.
- **Mélanger les interactions** : vous pouvez mélanger les interactions avec l'agent et le modèle au sein d'une même conversation. Par exemple, vous pouvez utiliser un agent spécialisé, comme l'agent Deep Research, pour la collecte initiale de données, puis utiliser un modèle Gemini standard pour les tâches de suivi telles que la synthèse ou le reformatage, en associant ces étapes à l'`previous_interaction_id`.

## Modèles et agents compatibles

| Nom du modèle | Type | ID du modèle |
| --- | --- | --- |
| Gemini 3.8 Flash | Modèle | `gemini-3.8-flash` |
| Gemini 3.6 Flash | Modèle | `gemini-3.6-flash` |
| Preview Gemini 3.1 Pro | Modèle | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Modèle | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Modèle | `gemini-3.1-flash-lite` |
| Preview Gemini 3 Flash | Modèle | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modèle | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modèle | `gemini-2.5-flash` |
| Gemini 2.5 Flash-Lite | Modèle | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modèle | `gemini-3-pro-image` |
| Image Gemini 3.1 Flash | Modèle | `gemini-3.1-flash-image` |
| Preview Gemini 3.1 Flash TTS | Modèle | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B-it | Modèle | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modèle | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Modèle | `lyria-3.5` |
| Aperçu de clip Lyria 3 | Modèle | `lyria-3-clip-preview` |
| Preview Lyria 3 Pro | Modèle | `lyria-3-pro-preview` |
| Aperçu de Deep Research | Agent | `deep-research-preview-04-2026` |
| Aperçu de Deep Research | Agent | `deep-research-max-preview-04-2026` |
| Aperçu d'Antigravity | Agent | `antigravity-preview-09-2026` |

## SDK

Vous pouvez utiliser la dernière version des SDK Google GenAI pour accéder à l'API Interactions.

- Sur Python, il s'agit du package `google-genai` à partir de la version `2.3.0`.
- Sur JavaScript, il s'agit du package `@google/genai` à partir de la version `2.3.0`.
- Sur Go, il s'agit du package `google.golang.org/genai`.
- Sur Java, il s'agit du package `com.google.genai:google-genai`.

Pour savoir comment installer les SDK, consultez la page [Bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr).

## Limites

- **MCP à distance** : Gemini 3 n'est pas compatible avec le MCP à distance. Cette fonctionnalité sera bientôt disponible.
- **Compatibilité des modèles multitours** : lorsque vous combinez différents modèles dans une conversation (avec ou sans état), les modèles suivants doivent accepter les modalités de sortie des modèles précédents en tant qu'entrée. Par exemple, si vous générez une image à l'aide de `gemini-3.1-flash-image`, vous ne pouvez pas poursuivre cette conversation avec un modèle qui n'accepte pas les entrées d'image (comme un modèle de texte uniquement ou un modèle de génération de musique comme Lyria).

Les fonctionnalités suivantes sont compatibles avec l'API [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=fr), mais **ne sont pas encore disponibles** dans l'API Interactions :

- **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**
- **[Appel de fonction automatique (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=fr#automatic_function_calling_python_only)**
- **[Mise en cache explicite](https://ai.google.dev/gemini-api/docs/caching?hl=fr)** : notez que la mise en cache implicite côté serveur est disponible dans l'API Interactions via `previous_interaction_id`.
- **[Paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr)** : les paramètres de sécurité personnalisés ne sont pas compatibles avec l'API Interactions.

## Commentaires

Vos commentaires sont essentiels au développement de l'API Interactions.
Partagez vos commentaires, signalez des bugs ou demandez des fonctionnalités sur notre [forum de la communauté des développeurs Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=fr).

## Étape suivante

- Essayez le [notebook de démarrage rapide de l'API Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=fr).
- En savoir plus sur l'[agent Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/09 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/09 (UTC)."],[],[]]
