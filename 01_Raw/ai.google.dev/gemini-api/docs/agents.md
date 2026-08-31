---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=fr
fetched_at: 2026-08-31T06:28:42.435777+00:00
title: "Pr\u00e9sentation des agents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Présentation des agents

Les agents gérés de l'API Gemini vous offrent un harnais d'agent configurable. Un seul appel d'API provisionne un bac à sable Linux dans lequel l'agent raisonne, exécute du code, gère des fichiers et navigue sur le Web de manière autonome.

[rocket\_launch

Guide de démarrage rapide

Effectuez votre premier appel d'agent, diffusez des réponses et créez un agent personnalisé.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr)
[smart\_toy

Agent Antigravity

Fonctionnalités, outils, entrée multimodale et tarifs de l'agent par défaut.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr)
[experiment

Agents dans AI Studio

Terrain de jeu visuel pour prototyper des agents sans écrire de code.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=fr)

## Agents gérés disponibles

- **[Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr)** : à usage général
  agent géré basé sur Gemini 3.7 Flash. Exécute du code, gère des fichiers et effectue des recherches sur le Web dans un bac à sable Linux sécurisé hébergé par Google. Vous pouvez
  configurer le modèle sous-jacent (par exemple, Gemini 3.7 Flash, Gemini 3.6 Flash ou Gemini 3.5 Flash)
  à l'aide de `agent_config`, et l'étendre avec vos propres instructions, compétences et données pour
  [créer un agent personnalisé](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr)** : agent de recherche autonome
  qui planifie, exécute et synthétise des tâches de recherche en plusieurs étapes pour des cas d'utilisation
  tels que l'analyse de marché, la diligence raisonnable et les revues de littérature.

## Sécurité et bonnes pratiques

Chaque agent s'exécute dans un environnement de bac à sable isolé au niveau du système d'exploitation.
Par défaut, le bac à sable dispose d'un accès réseau sortant illimité. Vous pouvez limiter ou désactiver l'accès réseau à l'aide d'une liste d'autorisation.

### Accès au réseau

Par défaut, les environnements disposent d'un accès réseau sortant illimité. Utilisez une liste d'autorisation `network` pour limiter le trafic sortant à des domaines spécifiques ou à des modèles génériques. Pour plus d'informations sur la configuration, consultez
[Liste d'autorisation réseau](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=fr#network_allow_list) (AI
Studio) ou [Règles réseau](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr#with_network_rules)
(API).

### Outils et API externes

Vous pouvez connecter des outils et des API externes pour étendre l'agent. N'utilisez que des outils provenant de sources fiables et limitez les autorisations au minimum requis. Les identifiants peuvent être injectés de manière sécurisée via des transformations d'en-tête de proxy de sortie et ne sont jamais exposés dans le bac à sable. L'agent peut utiliser n'importe quel identifiant auquel il a accès. Ne fournissez donc que les identifiants dont vous êtes prêt à accorder la portée complète.

- Utilisez des comptes de service ou des clés API basés sur le principe du moindre privilège.
- Préférez les jetons à courte durée de vie aux clés à longue durée de vie.
- Ne fournissez que les identifiants dont vous êtes prêt à accorder la portée complète.
- Effectuez une rotation régulière des identifiants.

Pour en savoir plus sur la configuration des transformations d'en-tête, consultez
[Identifiants](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#credentials).

### Supervision humaine

Vérifiez toujours les sorties (code généré, transformations de données, modifications de configuration) avant de les déployer, en particulier pour les tâches qui modifient des données ou interagissent avec des systèmes externes.

## Tarifs

Les agents gérés utilisent un [modèle de paiement à l'usage](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#pricing-for-agents) basé sur les jetons de modèle Gemini et l'utilisation des outils. Une seule interaction peut déclencher plusieurs boucles de raisonnement, consommant généralement entre 100 000 et 3 millions de jetons. Le calcul de l'environnement **n'est pas facturé** pendant la version Preview. Consultez les [coûts estimés](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr#availability-and-pricing)
pour les répartitions par tâche. Les agents gérés sont également disponibles dans le niveau sans frais avec une limite de débit et un quota d'utilisation sans frais.

## Limites

| Limite | Description |
| --- | --- |
| **Durée de vie de l'environnement** | Les environnements sont définitivement supprimés après sept jours d'inactivité. |
| **Arrêt de la VM** | Les VM s'éteignent après une brève période d'inactivité pour économiser des ressources. La requête suivante restaure l'état (avec un démarrage à froid). |
| **Logiciel pré-installé** | Environnement basé sur Ubuntu avec Python 3.12 et Node.js 22. Pour en savoir plus sur l'image de base de l'environnement, consultez [Logiciel pré-installé](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#pre-installed-software). |
| **Nombre maximal d'agents** | Vous pouvez avoir jusqu'à 1 000 agents gérés. |

## Frameworks d'agents

Vous pouvez également créer des agents avec Gemini à l'aide des frameworks et SDK suivants :

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=fr) : créez des flux d'applications complexes avec état et des systèmes multi-agents à l'aide de structures de graphiques.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=fr) : connectez les agents Gemini à
  vos données privées pour des workflows améliorés par RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=fr) : orchestrez des agents d'IA autonomes collaboratifs,
  et de jeu de rôle.
- [**SDK Vercel AI**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=fr) : créez des interfaces utilisateur et des agents basés sur l'IA en JavaScript/TypeScript.
- [**\*\*Google ADK\*\***](https://google.github.io/adk-docs/get-started/python/) : An
  open-source framework for building and orchestrating interoperable AI
  agents.
- [**SDK Antigravity**](https://antigravity.google/product/antigravity-sdk?hl=fr) : créez
  des agents d'IA autonomes à l'aide des mêmes outils, boucle d'agent et gestion du contexte
  que Google Antigravity, programmable en Python.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/08/19 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/08/19 (UTC)."],[],[]]
