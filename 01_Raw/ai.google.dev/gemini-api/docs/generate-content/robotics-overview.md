---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=fr
fetched_at: 2026-11-02T07:30:47.744738+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Gemini Robotics ER

Les modèles Gemini Robotics ER (raisonnement incarné) sont des modèles de vision-langage (VLM) qui permettent aux robots de percevoir le monde physique et d'interagir avec lui. Ils interprètent les données visuelles, effectuent des raisonnements spatiaux et temporels, planifient des tâches en plusieurs étapes, et orchestrent les robots et les outils.

## Modèles

Le modèle Gemini Robotics ER 2 est le dernier modèle de Gemini Robotics.
Il s'agit de notre modèle de raisonnement mis à jour, qui permet aux robots de comprendre précisément leur environnement. Il est spécialisé dans les capacités de raisonnement incarné, telles que l'orchestration agentique de robots (par exemple, à l'aide de VLA), la compréhension vidéo des robots, y compris la compréhension de la progression et la détection des réussites, la lecture d'instruments, le pointage et le raisonnement spatial.

Le modèle Gemini Robotics ER 2 introduit deux points de terminaison de modèle :

- **`gemini-robotics-er-2-preview`** : modèle ER 2 standard. S'appuie sur Gemini 3.5 Flash avec un raisonnement spatial amélioré, la recherche de moments vidéo, la classification de la progression vidéo, l'orchestration multirobot et l'utilisation d'outils en plusieurs étapes.
- **`gemini-robotics-er-2-streaming-preview`** : optimisé pour le streaming en temps réel via l'[API Live](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr). Utilisez ce modèle pour les agents robotiques à faible latence qui traitent des entrées audio et vidéo continues.

Si vous utilisez Gemini Robotics ER 1.6, passez à Gemini Robotics ER 2 en remplaçant `model="gemini-robotics-er-1.6-preview"` par `model="gemini-robotics-er-2-preview"` ou `model="gemini-robotics-er-2-streaming-preview"` dans vos appels d'API. Notez que le modèle Gemini Robotics ER 1.6 sera arrêté [fin août](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr#robotics-models).

[Essayer Gemini Robotics ER 2 dans Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=fr)

## Fonctionnalités de robotique

Gemini Robotics ER est compatible avec un éventail de capacités de raisonnement incarné.
Sélectionnez une fonctionnalité pour en savoir plus :

| Capacité | Description | Guide |
| --- | --- | --- |
| Raisonnement spatial | Pointez des objets, suivez-les dans une vidéo, détectez-les avec des cadres de délimitation et planifiez des trajectoires. | [Raisonnement spatial](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=fr) |
| Vision agentique | Utilisez l'exécution de code pour améliorer d'autres fonctionnalités en exploitant des outils de manipulation d'images. | [Vision agentique](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=fr) |
| Orchestration des tâches | Combinez le raisonnement spatial avec des API de robot personnalisées pour effectuer des tâches à long horizon. | [Orchestration des tâches](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=fr) |
| Streaming (point de terminaison de streaming Gemini Robotics ER 2 uniquement) | Streaming bidirectionnel pour les agents robotiques en temps réel avec appel de fonction à faible latence. | [Streaming pour la robotique](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr) |
| Progression de la vidéo (Gemini Robotics ER 2 uniquement) | Détection de moments et classification de la progression à partir de flux vidéo continus. | [Compréhension des vidéos](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=fr) |

## Premiers pas

L'exemple suivant recherche des objets dans une image et renvoie leurs coordonnées 2D normalisées et leurs étiquettes. Vous pouvez transmettre ce résultat directement à une API de robotique ou à un modèle VLA pour générer des actions de robot.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

Le résultat sera un tableau JSON contenant des objets, chacun avec un `point` (coordonnées `[y, x]` normalisées) et un `label` identifiant l'objet.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

L'image suivante montre comment ces points peuvent être affichés :

![Exemple affichant les points des objets dans une image](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=fr)

## Fonctionnement

Gemini Robotics ER accepte des images, des vidéos ou des fichiers audio en entrée avec des requêtes en langage naturel. Il identifie les objets, raisonne sur le contexte de la scène et les relations spatiales, et renvoie une sortie structurée, comme des coordonnées ou des cadres de délimitation.

Gemini Robotics ER est également agentique : il décompose les tâches complexes en sous-tâches et les exécute en appelant vos fonctions de robot ou en exécutant le code généré. Par exemple, "mettre la pomme dans le bol" devient une séquence d'étapes de localisation, de saisie et de placement.

Consultez [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=fr#how-it-works) pour savoir comment Gemini exécute les appels d'outils.

## Sécurité

Bien que Gemini Robotics ER ait été conçu dans un souci de sécurité, il est de votre responsabilité de maintenir un environnement sûr autour du robot. Les modèles d'IA générative peuvent faire des erreurs, et les robots physiques peuvent causer des dommages. Pour en savoir plus, consultez la [page sur la sécurité de la robotique de Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=fr).

## Bonnes pratiques

1. Utilisez un langage simple et naturel. Décrivez ce que vous voulez que le robot fasse, comme vous le feriez avec une personne. Si un terme ne fonctionne pas, essayez un synonyme courant.
2. Optimisez l'entrée visuelle. Recadrez ou zoomez sur les objets petits ou peu clairs avant d'envoyer l'image. La luminosité et un faible contraste des couleurs peuvent affecter la détection.
3. Décomposez les tâches complexes en étapes. Envoyez chaque étape sous la forme d'une requête distincte pour que le modèle reste concentré et pour améliorer la précision.
4. Interrogez plusieurs fois et calculez la moyenne des résultats pour les tâches de haute précision. Cette approche consensuelle réduit la variance des résultats spatiaux.

## Limites

Tenez compte des limites suivantes lorsque vous développez avec Gemini Robotics ER :

- **Restrictions des clés API** : l'API Gemini n'accepte pas les requêtes provenant de clés API sans restriction et renvoie une erreur `403 Forbidden`. Sécurisez votre clé API en ajoutant des restrictions dans [AI Studio](https://aistudio.google.com/api-keys?hl=fr).
  Pour en savoir plus, consultez [Sécuriser les clés API sans restriction](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#secure-unrestricted-keys).
- **Latence et performances** : les requêtes complexes, les entrées haute résolution ou les niveaux de réflexion élevés peuvent entraîner des temps de traitement plus longs. Pour le niveau de réflexion, utilisez "Moyen" pour un bon équilibre entre latence et performances.
- **Hallucinations** : comme tous les grands modèles de langage, les modèles Gemini Robotics ER peuvent parfois "halluciner" ou fournir des informations incorrectes, en particulier pour les requêtes ambiguës ou les entrées hors distribution.
- **Dépendance à la qualité du prompt** : la qualité de la sortie dépend de la clarté du prompt d'entrée. Utilisez des prompts spécifiques et bien structurés.
- **Coût de calcul** : l'exécution du modèle, en particulier avec des entrées vidéo ou un `thinking_budget` élevé, consomme des ressources de calcul et entraîne des coûts.
  Pour en savoir plus, consultez la page [Réflexion](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=fr).
- **Types d'entrée** : consultez les rubriques suivantes pour en savoir plus sur les limites de chaque mode.
  - [Entrées d'image](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=fr#technical-details-image)
  - [Entrées vidéo](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=fr#supported-formats)
  - [Entrées audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=fr#supported-formats)

## Avis de confidentialité

Vous reconnaissez que les modèles référencés dans ce document (les "modèles robotiques") exploitent des données vidéo et audio pour faire fonctionner et déplacer votre matériel conformément à vos instructions. Vous pouvez donc utiliser les Modèles robotiques de manière à ce que des données de personnes identifiables, telles que des données vocales, des images et des données de ressemblance ("Données à caractère personnel"), soient collectées par les Modèles robotiques. Si vous choisissez d'utiliser les Modèles robotiques d'une manière qui collecte des Données à caractère personnel, vous acceptez de ne pas autoriser les personnes identifiables à interagir avec les Modèles robotiques ou à être présentes dans la zone qui les entoure, à moins que ces personnes identifiables n'aient été suffisamment informées et n'aient consenti au fait que leurs Données à caractère personnel puissent être fournies à Google et utilisées par Google, comme indiqué dans les Conditions d'utilisation supplémentaires de l'API Gemini disponibles à l'adresse [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=fr) (les "Conditions"), y compris conformément à la section intitulée "Comment Google utilise vos données". Vous devez vous assurer que cet avis autorise la collecte et l'utilisation des Données à caractère personnel comme indiqué dans les Conditions, et vous devez déployer des efforts commercialement raisonnables pour minimiser la collecte et la distribution des Données à caractère personnel en utilisant des techniques telles que le floutage des visages et en utilisant les Modèles robotiques dans des zones ne contenant pas de personnes identifiables, dans la mesure du possible.

## Tarifs

Pour en savoir plus sur les tarifs et les régions disponibles, consultez la page [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Points de terminaison de modèles

### Gemini Robotics ER 2 Preview

| Propriété | Description |
| --- | --- |
| id\_cardCode du modèle | `gemini-robotics-er-2-preview` |
| saveTypes de données acceptés | **Entrées**  Texte, images, vidéo, audio  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  131 072  **Limite de jetons de sortie**  65 536 |
| handymanFonctionnalités | **[Génération d'audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)**  Not supported  **[Mise en cache](https://ai.google.dev/gemini-api/docs/caching?hl=fr)**  Compatible  **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**  Compatible  **[Utilisation d'un ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)**  Compatible  **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)**  Compatible  **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)**  Compatible  **[Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)**  Compatible  **[Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)**  Not supported  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)**  Not supported  **[Ancrage avec la recherche](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)**  Compatible  **[Sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)**  Compatible  **[Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)**  Compatible  **[Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)**  Compatible |
| speedOptions de consommation | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**  Compatible  **[Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)**  Not supported  **[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)**  Not supported |
| 123 versions | Pour en savoir plus, consultez les [modèles de version de modèle](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions).  - Aperçu : `gemini-robotics-er-2-preview` |
| calendar\_monthDernière mise à jour | Juillet 2026 |
| id\_cardFiche de modèle | [fiche de modèle](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=fr) |
| paid Tarifs | [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-robotics-er-2) |

### Aperçu du streaming Gemini Robotics ER 2

| Propriété | Description |
| --- | --- |
| id\_cardCode du modèle | `gemini-robotics-er-2-streaming-preview` |
| saveTypes de données acceptés | **Entrées**  Texte, images, vidéo, audio  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  131 072  **Limite de jetons de sortie**  65 536 |
| handymanFonctionnalités | **[Génération d'audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)**  Not supported  **[Mise en cache](https://ai.google.dev/gemini-api/docs/caching?hl=fr)**  Not supported  **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**  Not supported  **[Utilisation d'un ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)**  Not supported  **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)**  Not supported  **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)**  Compatible  **[Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)**  Not supported  **[Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)**  Not supported  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)**  Compatible  **[Ancrage avec la recherche](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)**  Compatible  **[Sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)**  Not supported  **[Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)**  Compatible  **[Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)**  Not supported |
| speedOptions de consommation | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**  Not supported  **[Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)**  Not supported  **[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)**  Not supported |
| 123 versions | Pour en savoir plus, consultez les [modèles de version de modèle](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions).  - Aperçu : `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthDernière mise à jour | Juillet 2026 |
| id\_cardFiche de modèle | [fiche de modèle](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=fr) |
| paid Tarifs | [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-robotics-er-2-streaming) |

### Gemini Robotics ER 1.6 Preview

| Propriété | Description |
| --- | --- |
| id\_cardCode du modèle | `gemini-robotics-er-1.6-preview` |
| saveTypes de données acceptés | **Entrées**  Texte, images, vidéo, audio  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  131 072  **Limite de jetons de sortie**  65 536 |
| handymanFonctionnalités | **[Génération d'audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)**  Not supported  **[Mise en cache](https://ai.google.dev/gemini-api/docs/caching?hl=fr)**  Compatible  **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**  Compatible  **[Utilisation d'un ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)**  Compatible  **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)**  Compatible  **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)**  Compatible  **[Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)**  Compatible  **[Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)**  Not supported  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)**  Not supported  **[Ancrage avec la recherche](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)**  Compatible  **[Sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)**  Compatible  **[Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)**  Compatible  **[Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)**  Compatible |
| speedOptions de consommation | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**  Compatible  **[Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)**  Not supported  **[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)**  Not supported |
| 123 versions | Pour en savoir plus, consultez les [modèles de version de modèle](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions).  - Arrêt : `gemini-robotics-er-1.6-preview` |
| calendar\_monthDernière mise à jour | Décembre 2025 |
| cognition\_2Date limite des connaissances (ou "knowledge cutoff") | Janvier 2025 |

## Étape suivante

- [Raisonnement spatial](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=fr) : pointage, suivi, cadres de délimitation, trajectoires.
- [Capacités agentiques](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=fr) : exécution de code, lecture d'instruments, annotation d'images.
- [Orchestration des tâches](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=fr) : tâches à long horizon avec des API de robot personnalisées.
- [Robotique avec streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr) : streaming bidirectionnel en temps réel (Gemini Robotics ER 2 uniquement).
- [Compréhension des vidéos](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=fr) : identification des moments et classification de la progression (Gemini Robotics ER 2 uniquement).
- [Sécurité de la robotique Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=fr) : recherche sur la sécurité derrière la famille de modèles.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/29 (UTC)."],[],[]]
