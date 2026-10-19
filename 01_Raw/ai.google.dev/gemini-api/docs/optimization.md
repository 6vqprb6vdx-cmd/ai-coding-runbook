---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=fr
fetched_at: 2026-10-19T05:44:26.668766+00:00
title: "Optimisation et inf\u00e9rence de l'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Optimisation et inférence de l'API Gemini

L'API Gemini propose différents mécanismes d'optimisation pour vous aider à équilibrer la vitesse, le coût et la fiabilité en fonction des besoins spécifiques de votre charge de travail.
Que vous créiez des bots conversationnels en temps réel ou que vous exécutiez des pipelines de traitement de données hors connexion lourds, le choix du bon paradigme peut réduire considérablement les coûts ou améliorer les performances.

| Fonctionnalité | Standard | Flex | Priorité | Lot | Mise en cache |
| --- | --- | --- | --- | --- | --- |
| **Tarifs** | Plein tarif | 50% de remise | 75 à 100 % de plus que le tarif standard | 50% de remise | 90% de remise + stockage des jetons au prorata |
| **Latence** | Quelques secondes à quelques minutes | Quelques minutes (1 à 15 minutes) | Quelques secondes | Jusqu'à 24 heures | Délai d'émission du premier jeton plus rapide |
| **Fiabilité** | Élevée / Modérée à élevée | Optimisation limitée (supprimable) | Élevée (non supprimable) | Élevée (pour le débit) | N/A |
| **Interface** | Synchrone | Synchrone | Synchrone | Asynchrone | État enregistré |
| **Cas d'utilisation recommandé** | Workflows d'application généraux | Chaînes séquentielles non urgentes | Applications de production visibles par l'utilisateur | Ensembles de données volumineux, évaluations hors connexion | Requêtes récurrentes sur le même fichier |

## Niveaux de service d'inférence (synchrone)

Vous pouvez passer d'un trafic synchrone optimisé pour la fiabilité à un trafic synchrone optimisé pour les coûts en transmettant le paramètre `service_tier` dans vos appels de génération standards.

### Inférence standard (par défaut)

Le niveau standard est l'option par défaut pour la génération de contenu séquentiel.
Il offre des temps de réponse normaux sans frais supplémentaires ni mise en file d'attente importante.

- **Fiabilité** : criticité standard
- **Prix** : tarifs standards.
- **Recommandé pour** : la plupart des applications interactives quotidiennes.

### Inférence prioritaire (optimisée pour la latence)

[Le traitement](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)
prioritaire achemine vos requêtes vers des files d'attente de calcul à criticité élevée.
Ce trafic est strictement non supprimable (il n'est jamais préempté par d'autres niveaux) et offre la plus haute fiabilité. Si vous dépassez les limites dynamiques de priorité, le système rétrogradera gracieusement la requête vers un traitement standard au lieu d'échouer avec une erreur.

- **Fiabilité** : criticité la plus élevée
- **Prix** : 75 à 100 % de plus que les tarifs standards.
- **Recommandé pour** : les chatbots clients, la détection de fraudes en temps réel et les copilotes essentiels à l'entreprise.

### Inférence Flex (optimisée pour les coûts)

[L'inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr) offre une remise de 50% par rapport aux tarifs standards en utilisant
une capacité de calcul opportuniste en dehors des heures de pointe. Les requêtes sont traitées de manière synchrone, ce qui signifie que vous n'avez pas besoin de réécrire le code pour gérer les objets par lot.
Comme il s'agit d'un trafic "supprimable", les requêtes peuvent être préemptées si le système connaît des pics de trafic standards.

- **Fiabilité** : criticité non garantie et supprimable
- **Prix** : 50% du tarif standard (facturé par jeton).
- **Recommandé pour** : les workflows agentifs en plusieurs étapes où l'appel N+1 dépend de la sortie de l'appel N, les mises à jour CRM en arrière-plan et les évaluations hors connexion.

## API Batch (Bulk, asynchrone)

[L'API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr) est conçue pour traiter de grands volumes
de requêtes de manière asynchrone à
50% du coût standard. Vous pouvez envoyer des requêtes sous forme de dictionnaires intégrés ou à l'aide d'un fichier d'entrée JSONL (jusqu'à 2 Go). Elle traite les requêtes à l'aide de files d'attente de débit en arrière-plan avec un délai de traitement cible de 24 heures.

- **Fiabilité** : supprimable, mais avec des nouvelles tentatives automatisées et un système de mise en file d'attente de 24 heures
- **Prix** : 50% du tarif standard.
- **Recommandé pour** : le prétraitement d'ensembles de données volumineux, l'exécution de suites de tests de régression périodiques et la génération d'images ou d'intégrations à volume élevé.

## Mise en cache de contexte (réduction des coûts d'entrée)

[La mise en cache de contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) est utilisée lorsqu'un contexte initial important
est référencé à plusieurs reprises par des requêtes plus courtes.

- **Mise en cache implicite** : activée automatiquement sur Gemini 2.5 et les modèles plus récents.
  Le système répercute les économies si votre requête atteint des caches existants en fonction des préfixes d'invite courants.
- **Mise en cache explicite** : vous pouvez créer manuellement un objet de cache avec une valeur TTL (Time-To-Live) spécifique. Une fois créé, vous référencez les jetons mis en cache pour les requêtes suivantes afin d'éviter de transmettre plusieurs fois la même charge utile de corpus. La mise en cache explicite n'est pas compatible avec Gemini 4 Argon et les versions ultérieures.
- **Prix** : facturé en fonction du nombre de jetons mis en cache et de la durée de stockage (TTL).
- **Recommandé pour** : les chatbots avec des instructions système détaillées, l'analyse répétitive de longs fichiers vidéo ou les requêtes sur des ensembles de documents volumineux.

## Réduire les coûts d'entrée vidéo grâce au traitement agentif

Pour les contenus vidéo longs (plus de 5 à 10 minutes) ou les requêtes ciblées, le traitement agentif peut réduire les coûts des jetons d'entrée jusqu'à 88% tout en améliorant la qualité des réponses. Par défaut, tous les modèles (y compris Gemini 4) utilisent le [traitement statique](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#agentic-video-understanding) pour extraire des frames à 1 FPS. Avec la compréhension vidéo agentique, le modèle inspecte d'abord la transcription vidéo et charge dynamiquement les segments visuels à des fréquences d'images et des résolutions plus élevées uniquement lorsque cela est nécessaire. Pour les clips courts (moins de 5 minutes) ou les résumés vidéo complets, conservez le mode de traitement statique par défaut pour un délai d'émission du premier jeton plus rapide et une surcharge de jetons inférieure. Le mode agentif entraîne un raisonnement interne (`total_thought_tokens`) et des allers-retours d'outils (`total_tool_use_tokens`) lors de la navigation dans la chronologie.

Pour utiliser le traitement agentif avec Gemini 4 Argon, 3.8 Flash, 3.6 Flash ou 3.5 Flash Lite,
définissez `processing: "agentic"` (API Interactions) ou
`media_processing: "AGENTIC"` (API GenerateContent) sur votre entrée vidéo. Si le modèle n'est pas compatible avec le traitement agentif, il renverra une erreur.

Pour en savoir plus, consultez la section
[Compréhension vidéo agentive](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#agentic-video-understanding).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/13 (UTC)."],[],[]]
