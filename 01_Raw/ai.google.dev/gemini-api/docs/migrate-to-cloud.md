---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=fr
fetched_at: 2026-08-03T04:31:52.011126+00:00
title: "API Gemini\u00a0Developer et Gemini\u00a0Enterprise Agent\u00a0Platform \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# API Gemini Developer et Gemini Enterprise Agent Platform

Lorsque vous développez des solutions d'IA générative avec Gemini, Google propose deux produits API :
l'[API Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=fr) et l'[API Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=fr).

L'API Gemini Developer est le moyen le plus rapide de créer, de mettre en production et de faire évoluer des applications basées sur Gemini. La plupart des développeurs devraient utiliser l'API Gemini Developer, sauf s'ils ont besoin de commandes d'entreprise spécifiques.

Gemini Enterprise Agent Platform offre un écosystème complet de fonctionnalités et de services prêts à l'emploi pour créer et déployer des applications d'IA générative basées sur Google Cloud Platform.

Nous avons récemment simplifié la migration entre ces services. L'API Gemini
Developer et l'API Gemini Enterprise Agent Platform sont désormais accessibles via le SDK Google Gen AI unifié
.

## Comparaison de code

Cette page présente des comparaisons de code côte à côte entre les guides de démarrage rapide de l'API Gemini Developer et de Gemini Enterprise Agent Platform pour la génération de texte.

### Python

Vous pouvez accéder aux services de l'API Gemini Developer et de Gemini Enterprise Agent Platform via la bibliothèque `google-genai`. Consultez la page des [bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr)
pour savoir comment installer `google-genai`.

### API Gemini Developer

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### API Gemini Enterprise Agent Platform

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript et TypeScript

Vous pouvez accéder aux services de l'API Gemini Developer et de Gemini Enterprise Agent Platform via la bibliothèque `@google/genai`. Consultez la page des [bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr) pour savoir comment
installer `@google/genai`.

### API Gemini Developer

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### API Gemini Enterprise Agent Platform

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Vous pouvez accéder aux services de l'API Gemini Developer et de Gemini Enterprise Agent Platform via la bibliothèque `google.golang.org/genai`. Consultez la page des [bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr) pour savoir comment
installer `google.golang.org/genai`.

### API Gemini Developer

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### API Gemini Enterprise Agent Platform

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Autres cas d'utilisation et plates-formes

Pour d'autres plates-formes et cas d'utilisation, consultez les guides spécifiques aux cas d'utilisation de la documentation de l'API [Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=fr)
et de la documentation de [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=fr).

## Considérations sur la migration

Lors de la migration :

- Vous devrez utiliser des comptes de service Google Cloud pour vous authentifier. Pour en savoir plus, consultez la documentation de [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=fr).
- Vous pouvez utiliser votre projet Google Cloud existant
  (celui utilisé pour générer votre clé API) ou vous pouvez
  [créer un nouveau projet Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=fr).
- Les régions compatibles peuvent différer entre l'API Gemini Developer et l'API Gemini Enterprise Agent Platform. Consultez la liste des
  [régions disponibles pour l'IA générative sur Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=fr).
- Tous les modèles que vous avez créés dans Google AI Studio doivent être réentraînés dans Gemini Enterprise Agent Platform.

Si vous n'avez plus besoin d'utiliser votre clé API Gemini pour l'API Gemini Developer, suivez les bonnes pratiques de sécurité et supprimez-la.

Pour supprimer une clé API :

1. Ouvrez la
   [page Identifiants de l'API Google Cloud](https://console.cloud.google.com/apis/credentials?hl=fr).
2. Recherchez la clé API que vous souhaitez supprimer, puis cliquez sur l'icône **Actions**.
3. Sélectionnez **Supprimer la clé API**.
4. Dans la fenêtre **Supprimer l'identifiant**, sélectionnez **Supprimer**.

   Propager la suppression d'une clé API prend quelques minutes. Une fois la propagation terminée, tout trafic utilisant la clé API supprimée est rejeté.

## Étapes suivantes

- Consultez la
  [présentation de l'IA générative sur Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=fr)
  pour en savoir plus sur les solutions d'IA générative sur Gemini Enterprise Agent Platform.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
