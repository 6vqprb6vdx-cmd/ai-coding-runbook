---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=fr
fetched_at: 2026-06-01T19:37:08.122491+00:00
title: "G\u00e9n\u00e9rer des images \u00e0 l'aide d'Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Générer des images à l'aide d'Imagen

Imagen est le modèle de génération d'images haute fidélité de Google. Il est capable de générer des images réalistes et de haute qualité à partir de requêtes textuelles. Toutes les images générées incluent un filigrane SynthID. Pour en savoir plus sur les variantes de modèle Imagen disponibles, consultez la section [Versions de modèle](#model-versions).

## Générer des images à l'aide des modèles Imagen

Cet exemple montre comment générer des images avec un [modèle Imagen](https://deepmind.google/technologies/imagen/?hl=fr) :

### Python

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  generated_image.image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateImages({
    model: 'imagen-4.0-generate-001',
    prompt: 'Robot holding a red skateboard',
    config: {
      numberOfImages: 4,
    },
  });

  let idx = 1;
  for (const generatedImage of response.generatedImages) {
    let imgBytes = generatedImage.image.imageBytes;
    const buffer = Buffer.from(imgBytes, "base64");
    fs.writeFileSync(`imagen-${idx}.png`, buffer);
    idx++;
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  config := &genai.GenerateImagesConfig{
      NumberOfImages: 4,
  }

  response, _ := client.Models.GenerateImages(
      ctx,
      "imagen-4.0-generate-001",
      "Robot holding a red skateboard",
      config,
  )

  for n, image := range response.GeneratedImages {
      fname := fmt.Sprintf("imagen-%d.png", n)
          _ = os.WriteFile(fname, image.Image.ImageBytes, 0644)
  }
}
```

### REST

```
curl -X POST \
    "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "instances": [
          {
            "prompt": "Robot holding a red skateboard"
          }
        ],
        "parameters": {
          "sampleCount": 4
        }
      }'
```

![Image générée par IA d&#39;un robot tenant un skateboard rouge](https://ai.google.dev/static/gemini-api/docs/images/robot-skateboard.png?hl=fr)

Image générée par IA d'un robot tenant un skateboard rouge

### Configuration d'Imagen

Pour le moment, Imagen n'accepte que les requêtes en anglais et les paramètres suivants :

- `numberOfImages` : nombre d'images à générer, entre 1 et 4 (inclus).
  La valeur par défaut est 4.
- `imageSize` : taille de l'image générée. Cette fonctionnalité n'est compatible qu'avec les modèles Standard et Ultra. Les valeurs acceptées sont `1K` et `2K`.
  La valeur par défaut est `1K`.
- `aspectRatio` : modifie le format de l'image générée. Les valeurs acceptées sont `"1:1"`, `"3:4"`, `"4:3"`, `"9:16"` et `"16:9"`. La valeur par défaut est `"1:1"`.
- `personGeneration` : autorise le modèle à générer des images de personnes. Les valeurs suivantes sont acceptées :

  - `"dont_allow"` : bloquer la génération d'images de personnes.
  - `"allow_adult"` : générer des images d'adultes, mais pas d'enfants. Ce paramètre est la valeur par défaut
  - `"allow_all"` : génère des images incluant des adultes et des enfants.

## Guide sur les requêtes Imagen

Cette section du guide Imagen vous montre comment la modification d'une requête texte vers image peut produire différents résultats, ainsi que des exemples d'images que vous pouvez créer.

### Principes de base concernant l'écriture de requêtes

Une bonne requête est descriptive et claire, et utilise des mots clés et des modificateurs pertinents. Commencez par réfléchir à l'**objet**, au **contexte** et au **style**.

![Requête avec l&#39;objet, le contexte et le style mis en avant](https://ai.google.dev/static/gemini-api/docs/images/imagen/style-subject-context.png?hl=fr)

Texte de l'image : Un *croquis* (**style**) d'un *appartement moderne* (**objet**) entouré de *gratte-ciel* (**contexte et arrière-plan**).

1. **Objet :** La première chose à laquelle réfléchir pour une requête est l'*objet* : c'est-à-dire l'objet, la personne, l'animal ou le paysage dont vous souhaitez obtenir une image.
2. **Contexte et arrière-plan :** L'*arrière-plan ou le contexte* dans lequel le sujet sera placé est tout aussi important. Essayez de placer votre sujet dans différents arrière-plans. Par exemple, un studio sur fond blanc, en extérieur ou en intérieur.
3. **Style :** Pour finir, ajoutez le style d'image souhaité. Les *styles* peuvent être généraux (peinture, photographie, croquis) ou très spécifiques (pastel, fusain, 3D isométrique). Vous pouvez également combiner des styles.

Après avoir rédigé une première version de votre requête, affinez-la en ajoutant des détails jusqu'à obtenir l'image souhaitée. L'itération est importante.
Commencez par établir votre idée principale, puis affinez-la et développez-la jusqu'à ce que l'image générée corresponde à votre vision.

|  |  |  |
| --- | --- | --- |
| exemple d&#39;image photoréaliste 1   Requête : Un parc au printemps au bord d'un lac | exemple d&#39;image photoréaliste 2   Requête : un parc au printemps au bord d'un lac, **le soleil se couche sur le lac, heure dorée** | exemple d&#39;image photoréaliste 3   Requête : Un parc au printemps à côté d'un lac, ***le soleil se couche sur le lac, heure dorée, fleurs sauvages rouges*** |

Les modèles Imagen peuvent transformer vos idées en images détaillées, que vos requêtes soient courtes ou longues et détaillées. Affinez votre vision en ajoutant des détails à vos requêtes jusqu'à obtenir le résultat parfait.

|  |  |
| --- | --- |
| Les requêtes courtes vous permettent de générer rapidement une image.  Exemple de requête courte Imagen 4   Requête : photo en gros plan d'une femme d'une vingtaine d'années, photographie de rue, film, tons chauds orange atténués | Les requêtes plus longues vous permettent d'ajouter des détails spécifiques et de créer votre image.  Exemple de requête longue Imagen 4   Requête : photo captivante d'une femme d'une vingtaine d'années dans le style de la photographie de rue. L'image doit ressembler à une capture d'écran d'un film avec des tons chauds orange atténués. |

Conseils supplémentaires pour rédiger des requêtes Imagen :

- **Utilisez un langage descriptif** : employez des adjectifs et des adverbes détaillés pour donner une image claire à Imagen.
- **Fournissez du contexte** : si nécessaire, incluez des informations générales pour aider l'IA à comprendre.
- **Faites référence à des artistes ou à des styles spécifiques** : si vous avez une esthétique particulière en tête, il peut être utile de faire référence à des artistes ou à des mouvements artistiques spécifiques.
- **Utilisez des outils de prompt engineering** : envisagez d'explorer les outils ou ressources de prompt engineering pour vous aider à affiner vos prompts et à obtenir des résultats optimaux.
- **Améliorer les détails du visage dans vos photos personnelles et de groupe** : spécifiez les détails du visage comme point focal de la photo (par exemple, utilisez le mot "portrait" dans la requête).

### Générer du texte dans des images

Les modèles Imagen peuvent ajouter du texte dans les images, ce qui ouvre de nouvelles possibilités de génération d'images créatives. Suivez les conseils ci-dessous pour exploiter pleinement cette fonctionnalité :

- **Itérez en toute confiance** : vous devrez peut-être régénérer des images jusqu'à obtenir le résultat souhaité. L'intégration de texte d'Imagen est encore en cours de développement. Parfois, plusieurs tentatives sont nécessaires pour obtenir les meilleurs résultats.
- **Soyez bref** : limitez le texte à 25 caractères maximum pour une génération optimale.
- **Plusieurs expressions** : testez deux ou trois expressions distinctes pour fournir des informations supplémentaires. Évitez de dépasser trois expressions pour des compositions plus claires.

  ![Exemple de génération de texte Imagen 4](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_generate-text.png?hl=fr)

  Requête : une affiche avec le texte "Summerland" en gras comme titre, et en dessous le slogan "L'été n'a jamais été aussi agréable"
- **Emplacement du texte** : bien qu'Imagen puisse tenter de positionner le texte comme indiqué, attendez-vous à des variations occasionnelles. Cette fonctionnalité est en constante amélioration.
- **Style de police "Inspirer"** : spécifiez un style de police général pour influencer subtilement les choix d'Imagen. Ne vous attendez pas à une réplication précise des polices, mais plutôt à des interprétations créatives.
- **Taille de la police** : spécifiez une taille de police ou une indication générale de la taille (par exemple, *petite*, *moyenne*, *grande*) pour influencer la génération de la taille de la police.

### Paramétrage des prompts

Pour mieux contrôler les résultats, il peut être utile de paramétrer les entrées dans Imagen. Par exemple, supposons que vous souhaitiez que vos clients puissent générer des logos pour leur entreprise et que vous souhaitiez vous assurer que les logos sont toujours générés sur un fond de couleur unie. Vous souhaitez également limiter les options que le client peut sélectionner dans un menu.

Dans cet exemple, vous pouvez créer une requête paramétrée semblable à celle-ci :

```
A {logo_style} logo for a {company_area} company on a solid color background. Include the text {company_name}.
```

Dans votre interface utilisateur personnalisée, le client peut saisir les paramètres à l'aide d'un menu. La valeur choisie est alors insérée dans la requête qu'Imagen reçoit.

Exemple :

1. Invite : `A minimalist logo for a health care company on a solid color background. Include the text Journey.`

   ![Exemple de paramétrisation de requête Imagen 4](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_healthcare.png?hl=fr)
2. Invite : `A modern logo for a software company on a solid color background. Include the text Silo.`

   ![Exemple de paramétrisation de requête Imagen 4 : exemple 2](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_software.png?hl=fr)
3. Invite : `A traditional logo for a baking company on a solid color background. Include the text Seed.`

   ![Exemple de paramétrisation de requête Imagen 4 : 3](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_baking.png?hl=fr)

### Techniques d'écriture de requête avancées

Utilisez les exemples suivants pour créer des requêtes plus spécifiques basées sur des attributs tels que les descripteurs de photo, les formes et les matériaux, les courants artistiques historiques et les modificateurs de qualité d'image.

#### Photographie

- La requête inclut : *"Une photo de…"*

Pour utiliser ce style, commencez par utiliser des mots clés qui indiquent clairement à Imagen que vous souhaitez obtenir une photographie. Start your prompts with
*"A photo of. . ."*. Par exemple :

|  |  |  |
| --- | --- | --- |
| exemple d&#39;image photoréaliste 1   Requête : **Une photo de** grains de café dans une cuisine sur une surface en bois | exemple d&#39;image photoréaliste 2   Requête: **Une photo** d'une barre de chocolat sur un plan de travail | exemple d&#39;image photoréaliste 3   Requête : **Une photo de** bâtiment moderne avec de l'eau en arrière-plan |

Source de l'image : chaque image a été générée à l'aide de la requête textuelle correspondante avec le modèle Imagen 4.

##### Modificateurs de photo

Dans les exemples ci-dessous, vous pouvez voir plusieurs modificateurs et paramètres spécifiques à la photographie. Vous pouvez combiner plusieurs modificateurs pour un contrôle plus précis.

1. **Proximité de l'appareil** : *gros plan, plan large*

   |  |  |
   | --- | --- |
   | exemple d&#39;image de gros plan   Requête : Une photo **en gros plan** de grains de café | exemple d&#39;image de plan large   Requête : Une photo **en plan large** d'un petit sac de  grains de café dans une cuisine en désordre |
2. **Position de l'appareil** : *vue aérienne, vue de dessous*

   |  |  |
   | --- | --- |
   | exemple de photo en vue aérienne   Requête : **photo aérienne** d'une ville urbaine avec des gratte-ciel | exemple d&#39;image en vue de dessous   Requête : Photo d'une canopée de forêt avec un ciel bleu en **vue de dessous** |
3. **Éclairage** : *naturel, spectaculaire, chaud, froid*

   |  |  |
   | --- | --- |
   | exemple d&#39;image avec éclairage naturel   Requête : photo en studio d'un fauteuil moderne, **éclairage naturel** | exemple d&#39;image avec éclairage spectaculaire   Requête : photo en studio d'un fauteuil moderne, **éclairage spectaculaire** |
4. **Paramètres de l'appareil** : *flou de mouvement, flou artistique, bokeh, portrait*

   |  |  |
   | --- | --- |
   | exemple d&#39;image avec flou de mouvement   Requête : photo d'une ville avec des gratte-ciel à l'intérieur d'une voiture avec **floutage du mouvement** | exemple d&#39;image avec flou artistique   Requête : photo avec **flou artistique** d'un pont dans une ville urbaine de nuit |
5. **Types d'objectifs** : *35 mm, 50 mm, fisheye, grand angle, macro*

   |  |  |
   | --- | --- |
   | exemple d&#39;image avec objectif macro   Requête : photo de feuille, **objectif macro** | exemple d&#39;image avec objectif fisheye   Requête : photographie de rue, New York, **objectif fisheye** |
6. **Types de pellicule** : *noir et blanc, polaroid*

   |  |  |
   | --- | --- |
   | exemple d&#39;image de photo polaroid   Requête : un **portrait polaroid** d'un chien portant des lunettes de soleil | exemple d&#39;image de photo en noir et blanc   Requête : **photo en noir et blanc** d'un chien portant des lunettes de soleil |

Source de l'image : chaque image a été générée à l'aide de la requête textuelle correspondante avec le modèle Imagen 4.

### Illustration et art

- La requête inclut : *"Une painting de…"*, *"Une sketch de…"*

Les styles artistiques vont des styles monochromes tels que les esquisses au crayon à l'art numérique hyperréaliste. Par exemple, les images suivantes utilisent la même requête avec différents styles :

*"Une [art style or creation technique] d'une berline électrique angulaire avec des gratte-ciel en arrière-plan"*

|  |  |  |
| --- | --- | --- |
| exemples d&#39;images artistiques   Requête : Un **dessin technique au crayon** d'une berline… | exemples d&#39;images artistiques   Requête : Un **dessin au fusain** d'une berline… | exemples d&#39;images artistiques   Requête : Un **dessin au crayon de couleur** d'une berline… |

|  |  |  |
| --- | --- | --- |
| exemples d&#39;images artistiques   Requête : Une **peinture au pastel** d'une berline… | exemples d&#39;images artistiques   Requête : Un **rendu numérique** d'une berline… | exemples d&#39;images artistiques   Requête : Une **affiche art déco** d'une berline… |

Source de l'image : chaque image a été générée à l'aide de la requête textuelle correspondante avec le modèle Imagen 2.

##### Formes et matériaux

- La requête inclut : *"…fait en…"*, *"…en forme de…"*

L'un des points forts de cette technologie est que vous pouvez créer des images qui seraient autrement difficiles voire impossibles à obtenir. Par exemple, vous pouvez recréer le logo de votre entreprise dans différents matériaux et textures.

|  |  |  |
| --- | --- | --- |
| image d&#39;exemple de formes et matériaux 1   Requête : un sac de sport **fait en** fromage | image d&#39;exemple de formes et matériaux 2   Requête : tubes néons **en forme** d'oiseau | image d&#39;exemple de formes et matériaux 3   Requête : un fauteuil **fait en papier**, photo en studio, style origami |

Source de l'image : chaque image a été générée à l'aide de la requête textuelle correspondante avec le modèle Imagen 4.

#### Références artistiques historiques

- La requête inclut : *"…dans le style de…"*

Certains styles sont devenus iconiques au fil des années. Voici quelques idées de styles artistiques ou de peinture que vous pouvez essayer.

*"génère une image dans le style de [art period or movement]
 : une ferme éolienne"*

|  |  |  |
| --- | --- | --- |
| *Exemple d&#39;image de style impressionniste   Requête : génère une image **dans le style d'un tableau impressionniste**   : une ferme éolienne* | *Exemple d&#39;image de style renaissance   Requête : génère une image **dans le style d'un tableau de la Renaissance**   : une ferme éolienne* | *Exemple d&#39;image de style pop-art   Requête : génère une image **dans le style pop art**   : une ferme éolienne* |

Source de l'image : chaque image a été générée à l'aide de la requête textuelle correspondante avec le modèle Imagen 4.

#### Modificateurs de qualité d'image

Certains mots clés peuvent indiquer au modèle que vous recherchez un élément de haute qualité. Voici quelques exemples de modificateurs de qualité :

- **Modificateurs généraux** : *de haute qualité, agréable, stylisé*
- **Photos** : *4K, HDR, photo studio*
- **Art, iIlustration** : *professionnel, détaillé*

Voici quelques exemples de requêtes utilisées avec et sans modificateurs de qualité.

|  |  |
| --- | --- |
| exemple d&#39;image de maïs sans modificateurs   Requête (aucun modificateur de qualité) : photo d'un pied de maïs | exemple d&#39;image de maïs avec modificateurs   Requête (avec modificateurs de qualité) : **image 4K HDR**   d'un pied de maïs **prise par un   photographe professionnel** |

Source de l'image : chaque image a été générée à l'aide de la requête textuelle correspondante avec le modèle Imagen 4.

#### Formats

La génération d'images Imagen vous permet de définir cinq formats d'image distincts.

1. **Carré** (1:1, par défaut) : photo carrée standard. Les utilisations courantes de ce format incluent les publications sur les réseaux sociaux.
2. **Plein écran** (4:3) : ce format est couramment utilisé dans les médias ou les films.
   Il correspond également aux dimensions de la plupart des anciens téléviseurs (non panoramiques) et des appareils photo de format moyen. Il capture une plus grande partie de la scène horizontalement (comparé au format 1:1), ce qui en fait le format préféré pour la photographie.

   |  |  |
   | --- | --- |
   | Exemple de format   Requête : gros plan des doigts d'un Musicien qui jouent du piano, film en noir et blanc, rétro (format 4:3) | Exemple de format   Requête : Photo professionnelle en studio de frites pour un restaurant haut de gamme, dans le style d'un magazine de cuisine (format 4:3) |
3. **Portrait plein écran** (3:4) : il s'agit du format plein écran ayant une rotation de 90 degrés. Cela permet de capturer une plus grande partie de la scène verticalement par rapport au format 1:1.

   |  |  |
   | --- | --- |
   | Exemple de format   Requête : une femme faisant une randonnée, près de ses bottes, le reflet dans une flaque de grandes montagnes en arrière-plan, dans le style d'une publicité, angles spectaculaires (format 3:4) | Exemple de format   Requête : plan en vue aérienne d'une rivière s'écoulant dans une montagne mystique (format 3:4) |
4. **Écran large** (16:9) : ce format a remplacé le format 4:3 et est désormais le format le plus courant pour les téléviseurs, les écrans d'ordinateur et les écrans de téléphones mobiles (paysage).
   Utilisez ce format lorsque vous souhaitez inclure plus d'arrière-plan (par exemple, des paysages).

   ![Exemple de format](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_16-9_man.png?hl=fr)

   Requête : un homme portant des vêtements blancs, assis sur la plage, en gros plan, un éclairage de l'heure dorée (format 16:9)
5. **Portrait** (9:16) : il s'agit d'un format grand écran, mais pivoté. Il s'agit d'un format relativement nouveau qui est rendu populaire par les applications vidéo courtes (par exemple, les Shorts YouTube). Utilisez ce format pour les éléments élevés ayant une orientation verticale marquée, tels que les bâtiments, les arbres, les cascades ou d'autres éléments similaires.

   ![Exemple de format](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_9-16_skyscraper.png?hl=fr)

   Requête : rendu numérique d'un gratte-ciel massif, moderne, grand et épique avec un magnifique coucher de soleil en arrière-plan (format 9:16)

#### Images photoréalistes

Différentes versions du modèle de génération d'images peuvent offrir une combinaison de sorties artistiques et photoréalistes. Utilisez les mots suivants dans vos requêtes pour générer un résultat plus réaliste en fonction du sujet que vous souhaitez générer.

| Cas d'utilisation | Type d'objectif | Longueurs focales | Informations supplémentaires |
| --- | --- | --- | --- |
| Personnes (Portraits) | Primaire, zoom | 24-35 mm | Pellicule noir et blanc, Film noir, Profondeur de champ, Bichromie (mentionnez les noms de deux couleurs) |
| Aliment, insectes, plantes (objets, nature morte) | Macro | 60-105 mm | Niveau de détail élevé, mise au point précise, éclairage contrôlé |
| Sport, faune (mouvement) | Téléobjectif | 100-400 mm | Vitesse d'obturation rapide, Action ou suivi des mouvements |
| Astronomique, paysage (grand angle) | Grand angle | 10-24 mm | Durées d'exposition longues, mise au point nette, longue exposition, eau ou nuages fluides |

##### Portraits

| Cas d'utilisation | Type d'objectif | Longueurs focales | Informations supplémentaires |
| --- | --- | --- | --- |
| Personnes (Portraits) | Primaire, zoom | 24-35 mm | Pellicule noir et blanc, Film noir, Profondeur de champ, Bichromie (mentionnez les noms de deux couleurs) |

Avec plusieurs mots clés du tableau, Imagen peut générer les portraits suivants :

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de portrait photographique | exemple de portrait photographique | exemple de portrait photographique | exemple de portrait photographique |

Requête : *Femme, portrait en 35 mm, bichromie bleu et gris*  
Modèle : `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de portrait photographique | exemple de portrait photographique | exemple de portrait photographique | exemple de portrait photographique |

Requête : *Femme, portrait en 35 mm, film noir*  
Modèle : `imagen-4.0-generate-001`

##### Objets

| Cas d'utilisation | Type d'objectif | Longueurs focales | Informations supplémentaires |
| --- | --- | --- | --- |
| Aliment, insectes, plantes (objets, nature morte) | Macro | 60-105 mm | Niveau de détail élevé, mise au point précise, éclairage contrôlé |

Avec plusieurs mots clés du tableau, Imagen peut générer les images d'objets suivantes :

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de photographie d&#39;objet | exemple de photographie d&#39;objet | exemple de photographie d&#39;objet | exemple de photographie d&#39;objet |

Requête : *feuille de maranta, objectif macro, 60 mm*  
Modèle : `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de photographie d&#39;objet | exemple de photographie d&#39;objet | exemple de photographie d&#39;objet | exemple de photographie d&#39;objet |

Requête : *Assiette de pâtes, Objectif macro de 100 mm*  
Modèle : `imagen-4.0-generate-001`

##### Mouvement

| Cas d'utilisation | Type d'objectif | Longueurs focales | Informations supplémentaires |
| --- | --- | --- | --- |
| Sport, faune (mouvement) | Téléobjectif | 100-400 mm | Vitesse d'obturation rapide, Action ou suivi des mouvements |

Avec plusieurs mots clés du tableau, Imagen peut générer les images de mouvement suivantes :

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de photographie de mouvement | exemple de photographie de mouvement | exemple de photographie de mouvement | exemple de photographie de mouvement |

Requête : *Un "touchdown" victorieux, vitesse d'obturation rapide, suivi des mouvements*  
Modèle : `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de photographie de mouvement | exemple de photographie de mouvement | exemple de photographie de mouvement | exemple de photographie de mouvement |

Requête : *Cerf courant dans la forêt, vitesse d'obturation rapide, suivi des mouvements*  
Modèle : `imagen-4.0-generate-001`

##### Grand angle

| Cas d'utilisation | Type d'objectif | Longueurs focales | Informations supplémentaires |
| --- | --- | --- | --- |
| Astronomique, paysage (grand angle) | Grand angle | 10-24 mm | Durées d'exposition longues, mise au point nette, longue exposition, eau ou nuages fluides |

Avec plusieurs mots clés du tableau, Imagen peut générer les images grand angle suivantes :

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de photographie grand angle | exemple de photographie grand angle | exemple de photographie grand angle | exemple de photographie grand angle |

Requête : *Une chaîne de montagnes très large, paysage grand angle de 10 mm*  
Modèle : `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| exemple de photographie grand angle | exemple de photographie grand angle | exemple de photographie grand angle | exemple de photographie grand angle |

Requête : *une photo de la lune, astrophotographie, grand angle de 10 mm*  
Modèle : `imagen-4.0-generate-001`

## Versions de modèle

### Imagen 4

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `imagen-4.0-generate-001`  `imagen-4.0-ultra-generate-001`  `imagen-4.0-fast-generate-001` |
| Types de données acceptés pour save | **Entrée**  Texte  **Résultat**  Images |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  480 jetons (texte)  **Images de sortie**  1 à 4 (Ultra/Standard/Rapide) |
| calendar\_monthDernière mise à jour | Juin 2025 |

### Imagen 3

Le modèle Imagen 3 a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/13 (UTC)."],[],[]]
