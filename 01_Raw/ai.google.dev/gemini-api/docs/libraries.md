---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=fr
fetched_at: 2026-06-01T19:38:50.105635+00:00
title: "Biblioth\u00e8ques API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Bibliothèques API Gemini

Lorsque vous créez des applications avec l'API Gemini, nous vous recommandons d'utiliser le **SDK Google GenAI**.
Il s'agit des bibliothèques officielles prêtes pour la production que nous développons et gérons pour les langages les plus courants. Elles sont en [disponibilité générale](https://ai.google.dev/gemini-api/docs/libraries?hl=fr#new-libraries) et sont utilisées dans toute notre documentation et nos exemples officiels.

Si vous débutez avec l'API Gemini, suivez notre [guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/quickstart?hl=fr) pour commencer.

## Compatibilité linguistique et installation

Le SDK Google GenAI est disponible pour les langages Python, JavaScript/TypeScript, Go et Java. Vous pouvez installer la bibliothèque de chaque langage à l'aide de gestionnaires de paquets ou consulter ses dépôts GitHub pour en savoir plus :

### Python

- Bibliothèque : [`google-genai`](https://pypi.org/project/google-genai)
- Dépôt GitHub : [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Installation: `pip install google-genai`

### JavaScript

- Bibliothèque : [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Dépôt GitHub : [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Installation: `npm install @google/genai`

### Go

- Bibliothèque : [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Dépôt GitHub : [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Installation: `go get google.golang.org/genai`

### Java

- Bibliothèque : `google-genai`
- Dépôt GitHub : [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Installation : si vous utilisez Maven, ajoutez les éléments suivants à vos dépendances :

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Bibliothèque : `Google.GenAI`
- Dépôt GitHub : [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Installation: `dotnet add package Google.GenAI`

## Disponibilité générale

Depuis mai 2025, le SDK Google GenAI est en disponibilité générale sur toutes les plates-formes compatibles et constitue la bibliothèque recommandée pour accéder à l'API Gemini.
Il est stable, entièrement compatible avec une utilisation en production et activement géré.
Il donne accès aux dernières fonctionnalités et offre les meilleures performances avec Gemini.

Si vous utilisez l'une de nos anciennes bibliothèques, nous vous recommandons vivement de migrer pour pouvoir accéder aux dernières fonctionnalités et obtenir les meilleures performances avec Gemini. Pour en savoir plus, consultez la section [Anciennes bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr#previous-sdks).

## Anciennes bibliothèques et migration

Si vous utilisez l'une de nos anciennes bibliothèques, nous vous recommandons de
[migrer vers les nouvelles](https://ai.google.dev/gemini-api/docs/migrate?hl=fr).

Les anciennes bibliothèques ne donnent pas accès aux fonctionnalités récentes (telles que
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=fr) et [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr)) et sont
obsolètes depuis le 30 novembre 2025.

L'état de compatibilité de chaque ancienne bibliothèque varie, comme indiqué dans le tableau suivant :

| Langue | Ancienne bibliothèque | Compatibilité | Bibliothèque recommandée |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Non gérée activement | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Non gérée activement | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Non gérée activement | `google.golang.org/genai` |
| **Dart et Flutter** | `google_generative_ai` | Non gérée activement | Utiliser [Genkit Dart](https://genkit.dev/docs/dart/get-started/) ou [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Non gérée activement | Utiliser [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=fr) |
| **Android** | `generative-ai-android` | Non gérée activement | Utiliser [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=fr) |

**Remarque pour les développeurs Java** : Il n'existait pas d'ancien SDK Java fourni par Google pour l'API Gemini. Aucune migration depuis une ancienne bibliothèque Google n'est donc requise. Vous
pouvez commencer directement avec la nouvelle bibliothèque dans la
[section Compatibilité linguistique et installation](#install).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/28 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/28 (UTC)."],[],[]]
