---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=fr
fetched_at: 2026-09-14T05:35:40.250811+00:00
title: "Nouveaut\u00e9s de Gemini\u00a03.8 Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)

Envoyer des commentaires

# Nouveautés de Gemini 3.8 Flash

[Voir tous les modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr)

Gemini 3.8 Flash (`gemini-3.8-flash`) est disponible pour tous les utilisateurs et prêt à être utilisé en production. Il s'agit de notre modèle Flash le plus intelligent, conçu pour l'ingénierie logicielle à long terme, les agents autonomes et les workflows d'entreprise complexes.

Ce guide explique les nouveautés de Gemini 3.8 Flash, les modifications apportées à l'API, des exemples de code et des conseils de migration.

## Nouveau modèle

| Modèle | ID du modèle | Niveau de raisonnement par défaut | Tarifs | Description |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash est disponible jusqu'à la fin de l'année au prix de lancement de 0,75 $/1 M de jetons d'entrée et de 3,75 $/1 M de jetons de sortie. Pour en savoir plus, consultez les [tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr). | Notre modèle Flash le plus intelligent, conçu pour l'ingénierie logicielle à long terme, les agents autonomes et les workflows d'entreprise complexes. |

Gemini 3.8 Flash est compatible avec une fenêtre de contexte d'un million de jetons, 64 000 jetons de sortie maximum, des niveaux de raisonnement réglables (`low`, `medium`, `high`) et la même suite complète d'outils intégrés.

Pour obtenir les spécifications complètes, consultez la [page du modèle Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fr). Pour en savoir plus sur les tarifs de lancement, consultez la [section Tarifs](#pricing) ci-dessous ou la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-3.8-flash).

## Guide de démarrage rapide

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
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
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## Nouveautés de Gemini 3.8 Flash

- **Ingénierie logicielle à long terme** : obtient des résultats de pointe sur des benchmarks de codage réels, des refactorisations complexes de plusieurs fichiers et une exécution déterministe des outils. Pour en savoir plus, consultez la [méthodologie d'évaluation](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=fr).
- **Agents autonomes** : vous permet de créer des workflows de planification et d'orchestration d'outils en plusieurs étapes résilients, ce qui réduit considérablement les boucles et les erreurs.
- **Workflows d'entreprise complexes** : offre une précision supérieure, un raisonnement approfondi et une rigueur factuelle élevée pour les tâches de domaine exigeantes et les pipelines de données à grande échelle.
- **Modèle par défaut pour les agents gérés** : l'agent par défaut pour les agents gérés, l'agent [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr), utilise désormais Gemini 3.8 Flash. Le [SDK Antigravity](https://antigravity.google/docs/sdk/overview/?hl=fr) utilise également Gemini 3.8 Flash par défaut.
- **Tarifs de lancement** : Gemini 3.8 Flash est disponible au tarif de lancement de 0,75 $/1 M de jetons d'entrée et de 3,75 $/1 M de jetons de sortie jusqu'au 31 décembre 2026. Les tarifs standards de 1,50 $/1 M de jetons d'entrée et de 7,50 $/1 M de jetons de sortie entreront en vigueur le 1er janvier 2027.

Gemini 3.8 Flash peut utiliser plus de jetons pour les tâches plus longues et complexes, par conception. Pour fournir des résultats de meilleure qualité sur des objectifs difficiles en plusieurs étapes, le modèle effectue des étapes de raisonnement plus petites, appelle les outils de manière itérative et vérifie son travail en cours de route. Tous les workflows n'ont pas besoin de ce niveau de vérification. Pour les tâches quotidiennes, vous pouvez réduire l'effort de [raisonnement](#understanding-reasoning-levels) afin de diminuer la consommation de jetons. Vous pouvez également continuer à utiliser Gemini 3.7 Flash, qui reste entièrement compatible.

## Comprendre les niveaux de raisonnement

Gemini 3.8 Flash vous offre un contrôle flexible sur la latence et l'intelligence en ajustant le niveau de raisonnement du modèle :

- **Faible effort de raisonnement** : réduit le délai de réponse pour les tâches critiques en termes de latence, telles que les pipelines de réponse aux incidents, le chat en temps réel, la rédaction de brouillons et l'analyse de données rapide.
- **Moyen (par défaut)** : meilleure qualité pour la plupart des tâches. Recommandé pour le code complexe et les cas d'utilisation agentiques, offrant une plus grande précision dès la première passe.
- **Effort de raisonnement élevé** : maximise les capacités de raisonnement et d'orchestration d'outils du modèle. Idéal pour le raisonnement approfondi, les mathématiques et les tâches complexes en plusieurs étapes.

L'exemple suivant définit `thinking_level` sur `medium` pour une demande d'analyse de code complexe :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
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
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Agent Antigravity mis à jour

Grâce à ses performances et à son raisonnement améliorés, l'agent [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr) dans Gemini Managed Agents est désormais conçu avec Gemini 3.8 Flash par défaut.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
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
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

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
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

Le modèle Gemini sous-jacent [peut être configuré](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr#model-selection) à l'aide de `agent_config`.

## Checklist de migration

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Migrer vers gemini-3.8-flash

- **Mettre à jour l'ID du modèle** : remplacez la chaîne de votre modèle cible par `gemini-3.8-flash`.
- **Supprimer les paramètres d'échantillonnage obsolètes**
  - Supprimez `temperature`, `top_p` et `top_k` des configurations de génération.
  - Remplacez `thinking_budget` par l'énumération de chaîne `thinking_level`. Notez que `minimal` n'est pas compatible avec 3.8 Flash.
  - Supprimez `candidate_count` (non compatible avec Gemini 3 et versions ultérieures).
- **Appliquer les règles de validation des tours**
  - Standardisez les conversations multitours sur `previous_interaction_id` côté serveur.
  - Supprimez les tours de modèle préremplis.
- **Auditer l'appel de fonction**
  - Placez les éléments multimodaux dans la charge utile de la réponse.
  - Mettez en forme les instructions intégrées à l'aide de `\n\n`.
  - Si vous voyez des erreurs `Malformed_Function_Call` liées au texte pré-outil, consultez [Solutions de contournement pour les exigences concernant le texte pré-outil](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#workarounds-for-pre-tool-text-requirements).
  - Uniquement si vous utilisez l'API generateContent : assurez-vous que tous les objets `FunctionResponse` incluent `call_id` et `name`.
- **Exigences de base de Gemini 3** : pour les mises à jour du SDK et la conservation de la signature de pensée, consultez la [checklist de migration Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=fr#migration).

## Tarifs

Profitez des tarifs de lancement dans Google AI Studio et Gemini Enterprise Agent Platform jusqu'au 31 décembre 2026 pour Gemini 3.8 Flash, Gemini 3.7 Flash et Gemini 3.6 Flash. Les tarifs standards entreront en vigueur le 1er janvier 2027. Pour connaître les niveaux de tarification complets, consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-3.8-flash).

## Étapes suivantes

- Consultez les spécifications de l'API dans la [présentation des modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).
- Découvrez l'orchestration multi-agent dans la [présentation de l'API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr).
- Testez et affinez les prompts dans [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/10 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/10 (UTC)."],[],[]]
