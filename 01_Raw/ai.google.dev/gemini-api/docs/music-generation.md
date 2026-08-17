---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=fr
fetched_at: 2026-08-17T02:19:15.778216+00:00
title: "G\u00e9n\u00e9rer de la musique avec Lyria\u00a03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Générer de la musique avec Lyria 3

Lyria 3 est la famille de modèles de génération de musique de Google, disponible via l'API Gemini. Avec Lyria 3, vous pouvez générer un son stéréo de haute qualité à 44, 1 kHz à partir de requêtes textuelles ou d'images. Ces modèles offrent une cohérence structurelle, y compris des voix, des paroles synchronisées et des arrangements instrumentaux complets.

La famille Lyria 3 comprend deux modèles :

| Modèle | ID du modèle | Application idéale | Durée | Sortie |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Extraits courts, boucles, aperçus | 30 secondes | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Chansons complètes avec couplets, refrains et ponts | Quelques minutes (contrôlables à l'aide d'une requête) | MP3 |

Les deux modèles peuvent être utilisés avec la nouvelle
[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr), qui accepte les entrées multimodales (texte et images) et produit un son **stéréo haute fidélité à 44,1 kHz**
.

## Générer un clip musical

Le modèle Lyria 3 Clip génère toujours un extrait de **30 secondes**. Pour générer un extrait, appelez la méthode `interactions.create` avec un prompt textuel. La réponse inclut toujours les paroles et la structure de la chanson générées, ainsi que l'audio dans le schéma `steps`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Vous pouvez récupérer les données musicales générées à l'aide de la propriété `interaction.output_audio`, qui renvoie le dernier bloc audio généré. Vous pouvez également récupérer les paroles et la structure de la chanson à l'aide de la propriété `interaction.output_text`. Pour en savoir plus sur les propriétés pratiques, consultez la
[présentation des interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr#convenience-properties).

## Générer une chanson complète

Utilisez le modèle `lyria-3-pro-preview` pour générer des chansons complètes qui durent quelques minutes. Le modèle Pro comprend la structure musicale et peut créer des compositions avec des couplets, des refrains et des ponts distincts. Vous pouvez influencer la
durée en la spécifiant dans votre requête (par exemple, "créer une chanson de 2 minutes") ou en
utilisant [des horodatages](#timing) pour définir la structure.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Sélectionner un format de sortie

Par défaut, les modèles Lyria 3 génèrent de l'audio au format **MP3**. Pour Lyria 3 Pro, vous pouvez également demander la sortie au format **WAV** en définissant le `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Analyser la réponse

La réponse de Lyria 3 contient plusieurs blocs de contenu dans le schéma `steps`.
Les interactions renvoient une séquence d'étapes, où les étapes `model_output` contiennent le contenu généré.
Les blocs de contenu textuel contiennent les paroles générées ou une description JSON de la structure de la chanson.
Les blocs de contenu de type `audio` contiennent les données audio encodées en base64.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Paroles et musique entrelacées

Étant donné que la sortie de Lyria 3 est complexe (elle contient des étapes et des blocs distincts pour les paroles générées (texte) et la chanson elle-même (audio)), les propriétés pratiques offrent un raccourci rapide et recommandé.

Toutefois, si vous souhaitez un contrôle total et programmatique sur la chronologie brute des étapes renvoyées par le serveur (par exemple, en enregistrant des blocs de contenu individuels à mesure qu'ils sont reçus), vous pouvez itérer manuellement sur `steps` :

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## Générer de la musique à partir d'images

Lyria 3 accepte les entrées multimodales. Vous pouvez fournir jusqu'à **10 images** avec votre prompt textuel dans la liste `input`. Le modèle composera une musique inspirée du contenu visuel.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Fournir des paroles personnalisées

Vous pouvez écrire vos propres paroles et les inclure dans la requête. Utilisez des balises de section telles que `[Verse]`, `[Chorus]` et `[Bridge]` pour aider le modèle à comprendre la structure de la chanson :

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Contrôler le timing et la structure

Vous pouvez spécifier exactement ce qui se passe à des moments précis de la chanson à l'aide d'horodatages. Cela est utile pour contrôler le moment où les instruments entrent en jeu, le moment où les paroles sont prononcées et la progression de la chanson :

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Générer des pistes instrumentales

Pour la musique de fond, les bandes-son de jeux ou tout cas d'utilisation où les voix ne sont pas requises, vous pouvez demander au modèle de produire des pistes uniquement instrumentales :

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Générer de la musique dans différentes langues

Lyria 3 génère des paroles dans la langue de votre requête. Pour générer une chanson avec des paroles en français, rédigez votre requête en français. Le modèle adapte son style vocal et sa prononciation à la langue.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Intelligence du modèle

Lyria 3 analyse le processus de votre requête, où le modèle raisonne sur la structure musicale (intro, couplet, refrain, pont, etc.) en fonction de votre requête.
Cela se produit avant la génération de l'audio et garantit la cohérence structurelle et la musicalité.

## Guide sur les requêtes

Plus votre requête sera précise, meilleurs seront les résultats. Voici ce que vous pouvez inclure pour guider la génération :

- **Genre** : spécifiez un genre ou un mélange de genres (par exemple, « lo-fi hip hop »,
  « jazz fusion », « orchestre cinématographique »).
- **Instruments** : nommez des instruments spécifiques (par exemple, "piano Fender Rhodes",
  "guitare slide", "boîte à rythmes TR-808").
- **BPM** : définissez le tempo (par exemple, "120 BPM", "tempo lent autour de 70 BPM").
- **Tonalité/Gamme** : spécifiez une tonalité musicale (par exemple, "en sol majeur", "en ré mineur").
- **Ambiance et atmosphère** : utilisez des adjectifs descriptifs (par exemple, "nostalgique",
  "agressif", "éthéré", "rêveur").
- **Structure** : utilisez des balises telles que `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` ou des horodatages pour contrôler la progression de la chanson.
- **Durée** : le modèle Clip produit toujours des extraits de 30 secondes. Pour le modèle Pro, spécifiez la durée souhaitée dans votre requête (par exemple, "créer une chanson de 2 minutes") ou utilisez des horodatages pour contrôler la durée.

### Exemples de prompts

Voici quelques exemples de requêtes efficaces :

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Bonnes pratiques

- **Commencez par itérer avec Clip.** Utilisez le modèle `lyria-3-clip-preview` plus rapide pour tester les requêtes avant de vous engager dans une génération complète avec `lyria-3-pro-preview`.
- **Soyez précis.** Les requêtes vagues produisent des résultats génériques. Mentionnez les instruments, le BPM, la tonalité, l'ambiance et la structure pour obtenir le meilleur résultat.
- **Utilisez la même langue.** Rédigez votre requête dans la langue dans laquelle vous souhaitez que les paroles soient générées.
- **Utilisez des balises de section.** Les balises `[Verse]`, `[Chorus]` et `[Bridge]` donnent au modèle une structure claire à suivre.
- **Séparez les paroles des instructions.** Lorsque vous fournissez des paroles personnalisées, séparez-les clairement de vos instructions de direction musicale.

## Limites

- **Sécurité** : toutes les requêtes sont vérifiées par des filtres de sécurité. Les requêtes qui déclenchent les filtres seront bloquées. Cela inclut les requêtes qui demandent des voix d'artistes spécifiques ou la génération de paroles protégées par des droits d'auteur.
- **Filigranes** : tous les contenus audio générés incluent un
  [filigrane audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=fr) à des fins d'
  identification. Ce filigrane est imperceptible à l'oreille humaine et n'affecte pas l'expérience d'écoute.
- **Édition avec chat multitour** : la génération de musique est un processus à un seul tour.
  L'édition itérative ou l'affinage d'un extrait généré via plusieurs requêtes ne sont pas compatibles avec la version actuelle de Lyria 3.
- **Longueur** : le modèle Clip génère toujours des extraits de 30 secondes. Le modèle Pro génère des chansons qui durent quelques minutes. La durée exacte peut être influencée par votre requête.
- **Déterminisme** : les résultats peuvent varier d'un appel à l'autre, même avec la même requête.

## Étape suivante

- Consultez la [tarification](https://ai.google.dev/gemini-api/docs/pricing?hl=fr) des modèles Lyria 3.
- Essayez la génération de musique en streaming et en temps réel 
  avec Lyria RealTime.
- Générez des conversations à plusieurs locuteurs avec les
  [modèles TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).
- Découvrez comment générer des [images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) ou des [vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Découvrez comment Gemini peut [comprendre les fichiers audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr).
- Discutez en temps réel avec Gemini à l'aide de l'
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
