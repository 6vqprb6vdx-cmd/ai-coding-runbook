---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr
fetched_at: 2026-08-24T02:31:25.452280+00:00
title: "Journaux et ensembles de donn\u00e9es \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Journaux et ensembles de données

Ce guide explique comment afficher les journaux d'utilisation de l'API Gemini dans le tableau de bord Google AI Studio pour mieux comprendre le comportement des modèles et la façon dont les utilisateurs interagissent avec vos applications. Utilisez la journalisation pour observer, déboguer et *partager éventuellement des commentaires sur l'utilisation
avec Google afin d'améliorer Gemini dans les cas d'utilisation des développeurs*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=fr)

Tous les appels d'API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` et les appels d'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr), à l'exception des Managed Agents, sont compatibles. Cela inclut les appels effectués via
[des points de terminaison de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr).

## Configurer la journalisation des projets

Par défaut, l'API stocke tous les objets d'interaction (`store=true`) afin de simplifier l'utilisation des fonctionnalités de gestion de l'état côté serveur. En revanche, l'API Generate Content ne stocke pas les requêtes par défaut et nécessite que le stockage soit activé par requête ou au niveau du projet à partir d'AI Studio.

Dans Google [AI Studio](https://aistudio.google.com/logs?hl=fr), vous pouvez activer ou
désactiver la journalisation pour tous les projets ou pour des projets spécifiques, et modifier ces
préférences à tout moment via le panneau **Paramètres** de la page
[Journaux et ensembles de données](https://aistudio.google.com/logs?hl=fr). La journalisation peut être activée ou désactivée
indépendamment pour l'API `generateContent` et l'
[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr)
afin de modifier le comportement de stockage par défaut d'un projet.

### Journalisation au niveau des requêtes

Le comportement de stockage et de journalisation diffère selon l'API :

- **[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr):** stocke les requêtes par défaut (`store=true`) pour simplifier la gestion de l'état côté serveur.
- **API Generate Content (`generateContent`)** : ne stocke pas les requêtes par défaut (`store=false`).

Voici comment définir la propriété `store` :

**API GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**API Interactions**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## Afficher les journaux de projet dans AI Studio

1. Accédez à la page "Journaux" dans [AI Studio](https://aistudio.google.com/logs?hl=fr).
2. Sélectionnez un projet dans la liste déroulante.
3. Les journaux s'affichent dans le tableau dans l'ordre chronologique inverse pour l'API Interactions, s'ils existent.
4. Pour observer les journaux de projet de l'API Generate Content, activez d'abord cette option dans le [panneau des paramètres](#configure-logging).

Cliquez sur une entrée pour obtenir un aperçu de la charge utile. Vous pouvez inspecter le prompt et la réponse complets de Gemini, ainsi que le contexte des tours précédents. Pour les requêtes de l'**API Interactions**, les journaux incluent également un lien direct vers `previous_interaction_id`.

## Configurer la période de conservation du stockage des projets

Les journaux expirent et sont marqués pour suppression après une période de conservation par défaut de
55 jours (sauf s'ils sont [enregistrés dans un ensemble de données](#create), qui n'expire pas).
Vous pouvez configurer la période de conservation des journaux d'un projet sur 7, 14, 28 ou 55 jours maximum.

## Créer et partager des ensembles de données

Vous pouvez enregistrer des journaux dans des ensembles de données pour les organiser et les exporter plus efficacement.

- Sur la page [Journaux](https://aistudio.google.com/logs?hl=fr), recherchez la barre de filtres
  en haut de la page pour sélectionner une propriété à filtrer.
- Dans votre vue filtrée, utilisez les cases à cocher pour sélectionner tous les journaux ou des journaux individuels.
- Cliquez sur le bouton **Créer un ensemble de données** qui s'affiche en haut de la liste.
- Attribuez un nom à votre nouvel ensemble de données et ajoutez une description facultative.
- L'ensemble de données que vous venez de créer s'affiche avec l'ensemble de journaux organisé.
- Exportez votre ensemble de données pour une analyse plus approfondie au format CSV, JSONL ou dans Google Sheets.

Les ensembles de données peuvent être utiles dans différents cas d'utilisation.

- **Organiser des ensembles de défis** : générez des améliorations futures ciblant les domaines dans lesquels vous souhaitez que votre IA s'améliore.
- **Organiser des ensembles d'échantillons** : par exemple, un échantillon d'utilisation réelle pour générer des réponses à partir d'un autre modèle, ou une collection de cas extrêmes pour des vérifications de routine avant le déploiement.
- **Ensembles d'évaluation** : ensembles représentatifs de l'utilisation réelle des fonctionnalités importantes, pour la comparaison entre d'autres modèles ou itérations d'instructions système.

Vous pouvez contribuer à la recherche et au développement de Gemini en choisissant de partager vos ensembles de données avec Google à titre d'exemples de démonstration.

## Limites

La journalisation n'est actuellement pas compatible avec les éléments suivants :

- Modèles Imagen et Veo
- Modèles d'embedding Gemini
- Modèle Gemini Robotics
- Entrées contenant des vidéos, des GIF ou des PDF
- Agents en préversion publique dans l'API Gemini

## Étape suivante

- **Créer un prototype avec l'historique des sessions** : utilisez [AI Studio Build](https://aistudio.google.com/apps?hl=fr) pour coder des applications et ajoutez votre clé API afin d'activer un historique des journaux de l'API Gemini pour les fonctionnalités d'IA.
- **Exécuter à nouveau les journaux avec l'API Gemini Batch** : utilisez des ensembles de données pour l'échantillonnage des réponses
  et l'évaluation des modèles ou de la logique d'application en exécutant à nouveau les journaux avec l'
  [API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/22 (UTC)."],[],[]]
