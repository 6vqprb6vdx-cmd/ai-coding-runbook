---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=fr
fetched_at: 2026-06-29T05:29:44.781791+00:00
title: "Utiliser des outils avec l'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Utiliser des outils avec l'API Gemini

Les outils étendent les capacités des modèles Gemini, ce qui leur permet d'agir dans le monde réel, d'accéder à des informations en temps réel et d'effectuer des tâches de calcul complexes. Les modèles peuvent utiliser des outils dans les interactions standard de demande et de réponse, ainsi que dans les sessions de streaming en temps réel à l'aide de l'[API Live](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr).

Les outils sont des fonctionnalités spécifiques (comme la recherche Google ou l'exécution de code) qu'un modèle peut utiliser pour répondre aux requêtes. L'API Gemini fournit une suite d'outils intégrés entièrement gérés. Vous pouvez également définir des outils personnalisés à l'aide de l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).

Pour créer des systèmes orientés objectif et à plusieurs étapes, consultez la [présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr).

## Outils intégrés disponibles

| Outil | Description | Cas d'utilisation |
| --- | --- | --- |
| [La recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) | Ancrez les réponses dans l'actualité et les faits du Web pour réduire les hallucinations. | \- Répondre à des questions sur des événements récents   \- Vérifier des faits à l'aide de sources diverses |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr) | Créez des assistants utilisant la détection de la position qui peuvent trouver des lieux, obtenir des itinéraires et fournir un contexte local riche. | - Planifier des itinéraires de voyage avec plusieurs arrêts   - Trouver des établissements locaux en fonction des critères de l'utilisateur |
| [Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) | Permettez au modèle d'écrire et d'exécuter du code Python pour résoudre des problèmes mathématiques ou traiter des données avec précision. | \- Résoudre des équations mathématiques complexes   \- Traiter et analyser des données textuelles avec précision |
| [Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) | Demandez au modèle de lire et d'analyser le contenu de pages Web ou de documents spécifiques. | \- Répondre à des questions basées sur des URL ou des documents spécifiques   \- Récupérer des informations sur différentes pages Web |
| [Utilisation de l'ordinateur (aperçu)](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr) | Activez Gemini pour qu'il puisse afficher un écran et générer des actions pour interagir avec les UI des navigateurs Web (exécution côté client). | \- Automatiser les workflows Web répétitifs   \- Tester les interfaces utilisateur des applications Web |
| [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr) | Indexez et recherchez vos propres documents pour activer la génération augmentée par récupération (RAG). | \- Recherche dans des manuels techniques   \- Réponses à des questions sur des données propriétaires |

Pour en savoir plus sur les coûts associés à des outils spécifiques, consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#pricing_for_tools).

## Fonctionnement de l'exécution des outils

Les outils permettent au modèle de demander des actions au cours d'une conversation. Le flux diffère selon que l'outil est intégré (géré par Google) ou personnalisé (géré par vous).

### Flux d'outil intégré

Pour les outils intégrés (recherche Google, Google Maps, contexte d'URL, recherche de fichiers, exécution de code), l'ensemble du processus se déroule en un seul appel d'API :

1. **Vous** envoyez une requête : "Quelle est la racine carrée du dernier cours de l'action GOOG ?"
2. **Gemini** décide qu'il a besoin d'outils et les exécute sur les serveurs de Google (par exemple, il recherche le cours de l'action, puis exécute du code Python pour calculer la racine carrée).
3. **Gemini** renvoie la réponse finale basée sur les résultats de l'outil.

### Flux d'outil personnalisé (appel de fonction)

Pour les outils personnalisés et l'utilisation de l'ordinateur, votre application gère l'exécution :

1. **Vous** envoyez un prompt avec des déclarations de fonctions (outils).
2. **Gemini** peut renvoyer un code JSON structuré pour appeler une fonction spécifique (par exemple, `{"name": "get_order_status", "args": {"order_id": "123"}}`), toujours avec un `id` unique.
3. **Vous** exécutez la fonction dans votre application ou votre environnement.
4. **Vous** renvoyez les résultats de la fonction à Gemini, avec le même `id` que l'appel de fonction.
5. **Gemini** utilise les résultats pour générer une réponse finale ou un autre appel d'outil.

Pour en savoir plus, consultez le [guide sur les appels de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).

### Combiner des outils intégrés et personnalisés

Pour les requêtes qui combinent des outils intégrés et des outils personnalisés (appels de fonction), le modèle utilise la [circulation du contexte d'outil](https://ai.google.dev/gemini-api/docs/toold-combination?hl=fr) pour coordonner l'exécution dans différents environnements :

1. **Vous** envoyez une requête et déclarez les outils intégrés et les fonctions personnalisées que vous souhaitez activer, en définissant un indicateur pour activer la prise en charge des combinaisons.
2. **Gemini** exécute les outils intégrés et cède la place à l'utilisateur si des appels de fonction côté client sont générés (l'exécution en premier dépend de la requête et de ce que le modèle décide). Il renvoie une réponse avec :
   - Confirmation de l'appel d'outil
   - Résultats de la réponse de l'outil (ils peuvent être placés après le JSON si le modèle a généré deux appels de fonction parallèles)
   - JSON structuré pour appeler votre fonction
   - Signatures de pensée chiffrées pour préserver le contexte
3. **Vous** exécutez la fonction dans votre application ou votre environnement.
4. **Vous** renvoyez toutes les parties de la réponse de Gemini, ainsi que les résultats de votre appel de fonction.
5. **Gemini** génère la réponse finale à l'aide de l'ensemble du contexte combiné.

Consultez le [guide sur la combinaison d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr) pour découvrir comment activer la prise en charge de la combinaison d'outils intégrés et personnalisés, et obtenir des exemples de circulation du contexte.

## Sorties structurées et appels de fonction

Gemini propose deux méthodes pour générer des résultats structurés. Utilisez l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) lorsque le modèle doit effectuer une étape intermédiaire en se connectant à vos propres outils ou systèmes de données. Utilisez les [sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) lorsque vous avez absolument besoin que la réponse finale du modèle respecte un schéma spécifique, par exemple pour afficher une UI personnalisée.

## Sorties structurées avec des outils

Vous pouvez combiner les [sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) avec des outils intégrés pour vous assurer que les réponses du modèle ancrées dans des données externes ou des calculs respectent toujours un schéma strict.

Pour obtenir des exemples de code, consultez [Sorties structurées avec des outils](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=fr#structured_outputs_with_tools).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/04/29 (UTC)."],[],[]]
