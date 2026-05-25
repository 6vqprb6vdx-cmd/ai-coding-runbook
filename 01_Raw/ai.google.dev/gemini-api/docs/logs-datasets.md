---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr
fetched_at: 2026-05-25T13:05:28.455375+00:00
title: "Journaux et ensembles de donn\u00e9es \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Journaux et ensembles de données

Ce guide contient tout ce dont vous avez besoin pour commencer à activer la journalisation pour vos applications Gemini API existantes. Dans ce guide, vous allez apprendre à afficher les journaux d'une application existante ou nouvelle dans le tableau de bord Google AI Studio pour mieux comprendre le comportement du modèle et la façon dont les utilisateurs interagissent avec vos applications. Utilisez la journalisation pour observer, déboguer et *partager éventuellement des commentaires sur l'utilisation avec Google afin d'améliorer Gemini pour les cas d'utilisation des développeurs*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=fr)

Tous les appels d'API `GenerateContent` et `StreamGenerateContent` sont acceptés, y compris ceux effectués via les points de terminaison de [compatibilité avec OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr).

## 1. Activer la journalisation dans Google AI Studio

Avant de commencer, assurez-vous de disposer d'un projet dont vous êtes propriétaire et pour lequel la facturation est activée.

1. Ouvrez la page des journaux dans Google [AI Studio](https://aistudio.google.com/logs?hl=fr).
2. Sélectionnez votre projet dans le menu déroulant, puis appuyez sur le bouton "Activer" pour activer la journalisation de toutes les requêtes par défaut.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=fr)

Vous pouvez activer ou désactiver la journalisation pour tous les projets ou pour des projets spécifiques, et modifier ces préférences à tout moment dans Google AI Studio.

## 2. Afficher les journaux dans AI Studio

1. Accédez à [AI Studio](https://aistudio.google.com/logs?hl=fr).
2. Sélectionnez le projet pour lequel vous avez activé la journalisation.
3. Vos journaux devraient s'afficher dans le tableau, dans l'ordre chronologique inverse.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Cliquez sur une entrée pour afficher la paire requête/réponse en plein écran. Vous pouvez examiner le prompt complet, la réponse complète de Gemini et le contexte du tour précédent. Notez que chaque projet dispose d'une limite de stockage par défaut de 1 000 journaux maximum. Les journaux non enregistrés dans des ensembles de données expirent au bout de 55 jours. Si votre projet atteint sa limite de stockage, vous serez invité à supprimer des journaux.

## 3. Organiser et partager des ensembles de données

- Dans le tableau des journaux, recherchez la barre de filtres en haut de la page pour sélectionner une propriété à filtrer.
- Dans la vue filtrée des journaux, utilisez les cases à cocher pour sélectionner tous les journaux ou certains d'entre eux.
- Cliquez sur le bouton "Créer un ensemble de données" qui s'affiche en haut de la liste.
- Attribuez un nom descriptif et éventuellement une description à votre nouvel ensemble de données.
- L'ensemble de données que vous venez de créer s'affiche avec l'ensemble de journaux sélectionnés.
- Exportez votre ensemble de données pour une analyse plus approfondie au format CSV ou JSONL, ou vers Google Sheets.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Les ensembles de données peuvent être utiles pour différents cas d'utilisation.

- **Organisez des ensembles de défis** : favorisez les améliorations futures dans les domaines où vous souhaitez que votre IA progresse.
- **Organisez des ensembles d'échantillons** : par exemple, un échantillon d'utilisation réelle pour générer des réponses à partir d'un autre modèle, ou une collection de cas extrêmes pour les vérifications de routine avant le déploiement.
- **Ensembles d'évaluation** : ensembles représentatifs de l'utilisation réelle des fonctionnalités importantes, permettant de comparer les modèles ou les itérations d'instructions système.

Vous pouvez contribuer à faire progresser la recherche sur l'IA, l'API Gemini et Google AI Studio en choisissant de partager vos ensembles de données comme exemples de démonstration. Cela nous permet d'affiner nos modèles dans divers contextes et de créer des systèmes d'IA qui restent utiles aux développeurs dans de nombreux domaines et applications.

## Étapes suivantes et éléments à tester

Maintenant que vous avez activé la journalisation, voici quelques opérations à essayer :

- **Prototyper avec l'historique des sessions** : utilisez [AI Studio Build](https://aistudio.google.com/apps?hl=fr) pour créer des applications avec le vibe coding et ajoutez votre clé API pour activer un historique des journaux utilisateur.
- **Réexécuter les journaux avec l'API Gemini Batch** : utilisez des ensembles de données pour l'échantillonnage des réponses et l'évaluation des modèles ou de la logique d'application en réexécutant les journaux via l'[API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Compatibilité

La journalisation n'est actuellement pas disponible pour les éléments suivants :

- Modèles Imagen et Veo
- Modèle d'embedding Gemini
- Entrées contenant des vidéos, des GIF ou des PDF

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/04/29 (UTC)."],[],[]]
