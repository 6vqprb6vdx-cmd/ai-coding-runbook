---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=fr
fetched_at: 2026-08-03T04:35:51.999116+00:00
title: "Mise en cache du contexte \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Mise en cache du contexte

Dans un workflow d'IA typique, vous pouvez transmettre les mêmes jetons d'entrée à un modèle à plusieurs reprises. L'API Gemini propose une mise en cache implicite pour optimiser les performances et les coûts.

## Mise en cache implicite

La mise en cache implicite est activée par défaut pour tous les modèles Gemini 2.5 et versions ultérieures. Elle est
compatible avec les modes de conversation [avec état](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#multi-turn-conversations) (à l'aide de `previous_interaction_id`)
et [sans état](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#stateless-conversations).
Nous répercutons automatiquement les économies de coûts si votre requête atteint les caches. Aucune action n'est requise de votre part pour activer cette fonctionnalité. Le nombre minimal de jetons d'entrée pour la mise en cache du contexte est indiqué dans le tableau suivant pour chaque modèle :

| Modèle | Limite minimale de jetons |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Preview Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Pour augmenter les chances d'atteindre un succès de cache implicite :

- Essayez de placer des contenus volumineux et courants au début de votre invite.
- Essayez d'envoyer des requêtes avec un préfixe similaire dans un court laps de temps.

Vous pouvez voir le nombre de jetons qui ont été mis en cache dans le champ `usage.total_cached_tokens` (Python et JavaScript) de l'objet de réponse.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
