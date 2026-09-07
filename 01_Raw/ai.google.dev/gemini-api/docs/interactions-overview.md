---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr
fetched_at: 2026-09-07T05:37:36.661481+00:00
title: "API Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# API Interactions

L'API Interactions est le meilleur moyen de créer avec les modèles et les agents Gemini. Depuis juin 2026, elle est disponible pour tous et recommandée pour tous les nouveaux projets. Bien qu'elle soit désormais considérée comme une API héritée, l'API d'origine
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=fr)
reste entièrement compatible.

## Pourquoi utiliser l'API Interactions ?

- **Interface universelle pour toutes les applications** : conçue comme l'interface standard
  pour tous les cas d'utilisation, y compris la génération de texte en une seule étape,
  la compréhension multimodale, les sorties structurées, l'orchestration d'outils et
  les workflows d'agent.
- **Une seule API pour les modèles et les agents** : un point de terminaison et un modèle unifiés pour
  appeler directement les modèles Gemini standards, ainsi que des agents spécialisés (tels que
  Deep Research et les agents gérés personnalisés).
- **Nouvelles fonctionnalités prêtes à l'emploi** : fonctionnalités telles que l'état de conversation côté serveur facultatif à l'aide de `previous_interaction_id`, les étapes d'exécution observables pour le débogage et le rendu de l'interface utilisateur, et [l'exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) pour les tâches de longue durée à l'aide de `background=true`.
- **Coût inférieur avec des taux de succès de cache plus élevés** : lorsque vous utilisez des conversations multitours, la gestion de l'état côté serveur facultative permet une mise en cache plus efficace du contexte entre les tours, ce qui réduit les coûts liés aux jetons.
- **Lancement de nouvelles fonctionnalités** : à l'avenir, tous les nouveaux modèles, fonctionnalités multimodales
  fonctionnalités, outils et fonctionnalités d'agent seront lancés sur l'API Interactions.

Par défaut, l'API Interactions stocke les requêtes afin que vous puissiez exploiter les fonctionnalités de gestion de l'état côté serveur à l'aide de `previous_interaction_id`. Vous pouvez choisir un comportement sans état en définissant `store=false`. Pour en savoir plus, consultez la section sur la [conservation des données](#data-storage-retention) pour
plus de détails.

## Premiers pas

- **Configurer votre agent de codage** : connectez-vous au **MCP Gemini Docs** et installez
  la compétence `gemini-api-dev` pour donner à votre assistant un accès direct aux
  dernières documentations pour les développeurs et aux bonnes pratiques. Pour obtenir des instructions détaillées, consultez le
  [guide Configurer votre agent de codage](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr).
- **Migrer depuis `generateContent`** : si vous disposez d'une intégration existante,
  suivez le [guide de migration](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=fr) pour
  passer à l'API Interactions.
- **Premiers pas** : suivez les étapes décrites dans le guide [Premiers pas avec l'API Interactions
  guide](https://ai.google.dev/gemini-api/docs/get-started?hl=fr).

### Guides des fonctionnalités

Découvrez les fonctionnalités spécifiques de l'API Interactions grâce à ces guides. Vous pouvez utiliser le bouton bascule sur ces pages pour passer de l'API generateContent à l'API Interactions :

- [Génération de texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr)
- [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)
- [Compréhension d'images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr)
- [Compréhension audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr)
- [Compréhension des vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr)
- [Traitement de documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr)
- [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
- [Sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)
- [Agent Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr)
- [Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)
- [Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)

## Fonctionnement de l'API Interactions

L'API Interactions est axée sur une ressource principale : [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=fr#Resource:Interaction). Une `Interaction` représente une étape complète dans une conversation ou une tâche. Elle fait office d'enregistrement de session, contenant l'historique complet d'une interaction sous forme de séquence chronologique d'**étapes d'exécution**. Ces étapes incluent les réflexions du modèle, les appels d'outils côté serveur ou client et les résultats (tels que `function_call` et `function_result`), ainsi que la `model_output` finale. La ressource stockée (récupérée via `interactions.get`) inclut également des étapes `user_input` pour un contexte complet, bien que la réponse `interactions.create` ne renvoie que les étapes générées par le modèle.

Lorsque vous effectuez un appel à
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=fr#CreateInteraction), vous
créez une nouvelle ressource `Interaction`.

### Gestion de l'état côté serveur

Vous pouvez utiliser le `id` d'une interaction terminée dans un appel ultérieur à l'aide du
`previous_interaction_id` paramètre pour poursuivre la conversation. Le serveur utilise cet ID pour récupérer l'historique des conversations, ce qui vous évite d'avoir à renvoyer l'intégralité de l'historique des discussions.

Le paramètre `previous_interaction_id` ne conserve que l'historique des conversations (entrées et sorties) à l'aide de `previous_interaction_id`. Les autres paramètres sont **limités à l'interaction** et ne s'appliquent qu'à l'interaction spécifique que vous générez actuellement :

- `tools`
- `system_instruction`
- `generation_config` (y compris `thinking_level`, `temperature`, etc.)

Cela signifie que vous devez spécifier à nouveau ces paramètres dans chaque nouvelle interaction si vous souhaitez qu'ils s'appliquent. Cette gestion de l'état côté serveur est facultative. Vous pouvez également fonctionner en mode sans état en envoyant l'intégralité de l'historique des conversations dans chaque requête.

### Stockage et conservation des données

Par défaut, l'API stocke tous les objets Interaction (`store=true`) afin de
simplifier l'utilisation des fonctionnalités de gestion de l'état côté serveur (avec
`previous_interaction_id`), [l'exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) (à l'aide de `background=true`) et
à des fins d'observabilité.

- **Niveau payant** : le système conserve les interactions pendant **55 jours**.
- **Niveau sans frais** : le système conserve les interactions pendant **un jour**.

Si vous ne le souhaitez pas, vous pouvez définir `store=false` dans votre requête. Cette commande est distincte de la gestion de l'état. Vous pouvez désactiver le stockage pour n'importe quelle interaction. Toutefois, notez que
`store=false` est incompatible avec [l'exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) et empêche l'utilisation de
`previous_interaction_id` pour les étapes suivantes.

Pour les projets de niveau payant, vous pouvez configurer la période de conservation dans
[AI Studio](https://aistudio.google.com/logs?hl=fr) afin de marquer automatiquement les journaux à supprimer du stockage du projet après 7, 14, 28 ou 55 jours. Une période de conservation plus courte peut affecter la récupération des conversations passées.

Vous pouvez supprimer les interactions stockées à tout moment à l'aide de la [`delete`](https://ai.google.dev/api/interactions-api?hl=fr#deleteInteraction) méthode par programmation, qui
nécessite l'ID d'interaction. Vous pouvez également afficher et gérer les journaux d'interactions stockées, y compris la suppression du stockage du projet, dans
[AI Studio](https://aistudio.google.com/logs?hl=fr).

Une fois la période de conservation expirée, vos données seront automatiquement supprimées.

Les objets Interactions sont traités conformément aux [conditions d'utilisation](https://ai.google.dev/gemini-api/terms?hl=fr).

### Afficher les interactions dans AI Studio

L'API stocke les requêtes de l'API Interactions exécutées avec `store=true` pour les projets de niveau payant. Vous pouvez les afficher directement depuis la page
["Journaux" de Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=fr). Pour en savoir plus, consultez le
[guide des journaux](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr).

## Bonnes pratiques

- **Taux de succès de cache** : la mise en cache implicite est compatible avec les modes avec état et
  sans état (voir le
  [guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/get-started?hl=fr#4_multi-turn_conversations)). L'utilisation de `previous_interaction_id` (avec état) pour poursuivre les conversations permet au système d'utiliser plus facilement la mise en cache implicite pour l'historique des conversations, ce qui améliore les performances et réduit les coûts.
- **Mélange d'interactions** : vous pouvez mélanger et associer des interactions d'agent et de
  modèle au sein d'une conversation. Par exemple, vous pouvez utiliser un agent spécialisé, tel que l'agent Deep Research, pour la collecte initiale de données, puis utiliser un modèle Gemini standard pour les tâches de suivi telles que la synthèse ou le reformatage, en liant ces étapes avec `previous_interaction_id`.

## Modèles et agents compatibles

| Nom du modèle | Type | ID du modèle |
| --- | --- | --- |
| Gemini 3.8 Flash | Modèle | `gemini-3.8-flash` |
| Gemini 3.7 Flash | Modèle | `gemini-3.7-flash` |
| Gemini 3.6 Flash | Modèle | `gemini-3.6-flash` |
| Gemini 3.5 Flash | Modèle | `gemini-3.5-flash` |
| Preview Gemini 3.1 Pro | Modèle | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Modèle | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Modèle | `gemini-3.1-flash-lite` |
| Preview Gemini 3 Flash | Modèle | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modèle | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modèle | `gemini-2.5-flash` |
| Gemini 2.5 Flash-Lite | Modèle | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modèle | `gemini-3-pro-image` |
| Image Gemini 3.1 Flash | Modèle | `gemini-3.1-flash-image` |
| Preview Gemini 3.1 Flash TTS | Modèle | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Modèle | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modèle | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Modèle | `lyria-3.5` |
| Preview Lyria 3 Clip | Modèle | `lyria-3-clip-preview` |
| Preview Lyria 3 Pro | Modèle | `lyria-3-pro-preview` |
| Preview Deep Research | Agent | `deep-research-preview-04-2026` |
| Preview Deep Research Max | Agent | `deep-research-max-preview-04-2026` |
| Preview Antigravity | Agent | `antigravity-preview-05-2026` |

## SDK

Vous pouvez utiliser la dernière version des SDK Google GenAI pour accéder à l'API Interactions.

- Dans Python, il s'agit du package `google-genai` à partir de la version `2.3.0`.
- Dans JavaScript, il s'agit du package `@google/genai` à partir de la version `2.3.0`.

Pour en savoir plus sur l'installation des SDK, consultez la page
[Bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr).

## Limites

- **MCP à distance** : Gemini 3 n'est pas compatible avec le MCP à distance, mais cette fonctionnalité sera bientôt disponible.
- **Compatibilité des modèles en plusieurs étapes** : lorsque vous mélangez différents modèles dans une
  conversation (avec ou sans état), les modèles suivants doivent être compatibles avec les modalités de sortie des modèles précédents en tant qu'entrée. Par exemple, si vous générez une image à l'aide de `gemini-3.1-flash-image`, vous ne pouvez pas poursuivre cette conversation avec un modèle qui n'accepte pas les entrées d'image (comme un modèle de texte uniquement ou un modèle de génération de musique comme Lyria).

Les fonctionnalités suivantes sont compatibles avec l'API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=fr), mais **ne sont pas encore
disponibles** dans l'API Interactions :

- **[API par lot](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**
- **[Appel de fonction automatique (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=fr#automatic_function_calling_python_only)**
- **[Mise en cache explicite](https://ai.google.dev/gemini-api/docs/caching?hl=fr)** : notez que la mise en cache implicite côté serveur est disponible dans l'API Interactions
  via `previous_interaction_id`.
- **[Paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr)** : les paramètres de sécurité personnalisés ne sont pas compatibles avec l'API Interactions.

## Commentaires

Vos commentaires sont essentiels au développement de l'API Interactions.
Partagez vos commentaires, signalez des bugs ou demandez des fonctionnalités sur notre
[forum de la communauté des développeurs Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=fr).

## Étape suivante

- Essayez le [notebook de démarrage rapide de l'API Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=fr).
- En savoir plus sur l'[agent Deep Research de Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/04 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/04 (UTC)."],[],[]]
