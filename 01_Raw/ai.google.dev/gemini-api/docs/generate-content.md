---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=fr
fetched_at: 2026-11-02T07:28:31.501909+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

# Gemini API

Passez rapidement d'un prompt à des applications et des agents de production avec l'API Gemini.
Gérez des tâches de codage complexes et un raisonnement multimodal avec Gemini, ou confiez des tâches en plusieurs étapes à un agent géré. Diffusez de la voix et de la vidéo en streaming avec l'API Live, ou générez des images avec Nano Banana, des vidéos avec Gemini Omni et de la musique avec Lyria.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-4-argon",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-4-argon",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-4-argon", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[À vos briques](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)

---

## Découvrez les modèles

[Tout afficher](https://ai.google.dev/gemini-api/docs/models?hl=fr)

[auto\_awesome
Gemini 4 Argon
Nouveau

Notre modèle de raisonnement phare avec une fenêtre de contexte partagée de 1 million de jetons et des décodages longs jusqu'à 1 million de jetons.](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fr)
[spark
Gemini 3.6 Flash
Nouveau

Notre dernier modèle, qui offre un bon équilibre entre vitesse et intelligence pour des performances optimales dans les tâches agentiques et multimodales.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr)
[graphic\_eq
Gemini 3.8 Flash TTS
Nouveau

Modèle de synthèse vocale de qualité studio avec jeu d'acteur expressif, conception de voix personnalisée et réplication vocale.](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr)
[spark
Gemini 3.5 Flash-Lite
Nouveau

Modèle à haut volume et sensible aux coûts, optimisé pour les tâches de sous-agents à haut débit et à faible latence.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fr)
[spark
Gemini 3.1 Flash-Lite

Modèle à volume élevé et sensible aux coûts, offrant les performances et la qualité de la série Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr)
[spark
Gemini 3 Flash

Des performances de pointe rivalisant avec celles de modèles plus grands, pour un coût bien inférieur.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr)
[🍌
Nano Banana

Modèles de pointe pour la génération et la retouche d'images.](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)
[video\_library
Gemini Omni Flash

Notre modèle de pointe pour la génération et la retouche de vidéos.](https://ai.google.dev/gemini-api/docs/omni?hl=fr)
[spark
Gemini Robotics

Un modèle de vision-langage (VLM) qui apporte les capacités agentiques de Gemini à la robotique et permet un raisonnement avancé dans le monde physique.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr)

## Découvrir les fonctionnalités

[imagesmode

Génération d'images native (Nano Banana)

Générez et retouchez des images hautement contextuelles de manière native avec Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)
[article

Contexte long

Saisissez des millions de jetons dans les modèles Gemini et tirez des enseignements d'images, de vidéos et de documents non structurés.](https://ai.google.dev/gemini-api/docs/long-context?hl=fr)
[code

Sorties structurées

Limitez Gemini à répondre au format JSON, un format de données structuré adapté au traitement automatisé.](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)
[functions

Appel de fonction

Créer des workflows agentifs en connectant Gemini à des API et des outils externes](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
[videocam

Génération de vidéos avec Gemini Omni Flash

Créez des contenus vidéo de haute qualité à partir de prompts contenant du texte ou des images avec notre modèle de pointe.](https://ai.google.dev/gemini-api/docs/video?hl=fr)
[android\_recorder

Agents vocaux avec l'API Live

Créez des applications et des agents vocaux en temps réel avec l'API Live.](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)
[build

Outils

Connectez Gemini au monde grâce à des outils intégrés tels que la recherche Google, le contexte d'URL, Google Maps, l'exécution de code et l'utilisation de l'ordinateur.](https://ai.google.dev/gemini-api/docs/tools?hl=fr)
[stacks

Compréhension des documents

Traitez jusqu'à 1 000 pages de fichiers PDF avec une compréhension multimodale complète ou d'autres types de fichiers textuels.](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr)
[cognition\_2

Raisonnement

Découvrez comment les capacités de réflexion améliorent le raisonnement pour les tâches et les agents complexes.](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)

[Google AI Studio

Testez des requêtes, gérez vos clés API, surveillez l'utilisation et créez des prototypes.](https://aistudio.google.com?hl=fr)
[group

Communauté de développeurs

Posez des questions et trouvez des solutions auprès d'autres développeurs et d'ingénieurs Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=fr)
[menu\_book

Documentation de référence de l'API

Vous trouverez des informations détaillées sur l'API Gemini dans la documentation de référence officielle.](https://ai.google.dev/api?hl=fr)
[sensors

État

Vérifiez l'état de l'API Gemini, de Google AI Studio et de nos services de modèles.](https://aistudio.google.com/status?hl=fr)

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/26 (UTC).

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/26 (UTC)."],[],[]]
