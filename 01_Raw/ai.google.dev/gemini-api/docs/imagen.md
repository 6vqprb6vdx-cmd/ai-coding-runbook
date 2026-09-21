---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=fr
fetched_at: 2026-09-21T05:46:37.081309+00:00
title: "G\u00e9n\u00e9rer des images \u00e0 l'aide d'Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)

Envoyer des commentaires

# Générer des images à l'aide d'Imagen

Imagen est l'ancien modèle de génération d'images de Google. Il a été arrêté et n'est plus disponible dans l'API Gemini.

## Migrer vers Nano Banana

Migrer vers Nano Banana pour la génération d'images :

- **Nom du modèle** : utilisez `gemini-2.5-flash-image` (ou les modèles Nano Banana 2 tels que `gemini-3.1-flash-image`) au lieu des noms de modèles Imagen.
- **Méthode** : utilisez `client.models.generate_content` à la place de `client.models.generate_images`.
- **Gestion des réponses** : Nano Banana renvoie des parties de contenu contenant des données d'image au lieu d'un objet de réponse d'image spécifique.

Pour en savoir plus et obtenir des exemples, consultez le [guide de génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/18 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/18 (UTC)."],[],[]]
