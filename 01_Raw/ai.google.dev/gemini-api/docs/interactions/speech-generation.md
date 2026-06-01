---
source_url: https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=fr
fetched_at: 2026-06-01T19:43:33.970102+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Génération de synthèse vocale

L'API Gemini peut transformer une entrée de texte en contenu audio à une ou plusieurs voix à l'aide des fonctionnalités de génération de synthèse vocale (TTS) de Gemini.
La génération de synthèse vocale (TTS) est *[contrôlable](#controllable)*, ce qui signifie que vous pouvez utiliser le langage naturel pour structurer les interactions et guider le *style*, l'*accent*, le *rythme* et le *ton* de l'audio.

La fonctionnalité TTS diffère de la génération vocale fournie par l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr), qui est conçue pour les entrées et sorties audio interactives, non structurées et multimodales. Alors que l'API Live excelle dans les contextes conversationnels dynamiques, la synthèse vocale via l'API Gemini est conçue pour les scénarios qui nécessitent une récitation exacte du texte avec un contrôle précis du style et du son, comme la génération de podcasts ou de livres audio.

Ce guide explique comment générer de l'audio à un ou plusieurs locuteurs à partir de texte.

## Avant de commencer

Assurez-vous d'utiliser une variante du modèle Gemini 2.5 avec les fonctionnalités de synthèse vocale Gemini, comme indiqué dans la section [Modèles compatibles](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=fr#supported-models). Pour obtenir des résultats optimaux, réfléchissez au modèle qui correspond le mieux à votre cas d'utilisation spécifique.

Vous trouverez peut-être utile de [tester les modèles Gemini 2.5 TTS dans AI Studio].

## Synthèse vocale à un seul locuteur

Pour convertir du texte en audio à une seule voix, définissez la modalité de réponse sur "audio" et transmettez un objet `speech_config` avec un nom de voix.
Vous devrez choisir un nom de voix parmi les [voix de sortie](#voices) prédéfinies.

Cet exemple enregistre le contenu audio généré par le modèle dans un fichier WAV :

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

Vous pouvez récupérer les données audio générées à l'aide de la propriété `interaction.output_audio`, qui renvoie le dernier bloc audio généré. Pour en savoir plus sur les propriétés pratiques, consultez [Présentation des interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr#convenience-properties).

## Synthèse vocale multilocuteur

Pour l'audio multi-locuteurs, vous aurez besoin d'un objet `multi_speaker_voice_config` avec chaque locuteur (jusqu'à deux) configuré en tant que `speaker_voice_config`.
Vous devez définir chaque `speaker` avec les mêmes noms que ceux utilisés dans le [prompt](#controllable) :

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_modalities=["audio"],
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_modalities": ["audio"],
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## Contrôler le style de parole avec des requêtes

Vous pouvez contrôler le style, le ton, l'accent et le rythme à l'aide de requêtes en langage naturel pour la synthèse vocale à une ou plusieurs voix.
Par exemple, dans une requête à un seul locuteur, vous pouvez dire :

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

Dans une requête à plusieurs locuteurs, fournissez au modèle le nom de chaque locuteur et la transcription correspondante. Vous pouvez également fournir des conseils pour chaque enceinte individuellement :

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

Essayez d'utiliser une [option vocale](#voices) qui correspond au style ou à l'émotion que vous souhaitez transmettre, pour l'accentuer encore plus. Dans la requête précédente, par exemple, le ton haletant d'*Encelade* peut mettre l'accent sur les mots"fatigué " et"ennuyé", tandis que le ton enjoué de *Puck* peut compléter les mots "enthousiaste" et "heureux".

## Générer un prompt pour convertir un texte en audio

Les modèles TTS ne génèrent que de l'audio, mais vous pouvez utiliser [d'autres modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr) pour générer d'abord une transcription, puis la transmettre au modèle TTS pour qu'il la lise à voix haute.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.5-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_modalities=["audio"],
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.5-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_modalities: ['audio'],
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

## Options vocales

Les modèles TTS sont compatibles avec les 30 options vocales suivantes dans le champ `voice_name` :

|  |  |  |
| --- | --- | --- |
| **Zephyr** : *Lumineux* | **Puck** : *Upbeat* | **Charon** : *Contenu informatif* |
| **Kore** : *Ferme* | **Fenrir** : *excitabilité* | **Leda** : *Jeune* |
| **Orus** : *cabinet d'avocats* | **Aoede** : *Breezy* | **Callirrhoe** : *tranquille* |
| **Autonoe** : *Lumineux* | **Enceladus** : *Souffle* | **Iapetus** : *Effacer* |
| **Umbriel** : *décontracté* | **Algieba** : *Smooth* | **Despina** : *Lisse* |
| **Erinome** : *dégagé* | **Algenib** : *Graveleux* | **Rasalgethi** : *informatif* |
| **Laomedeia** : *Upbeat* | **Achernar** : *Soft* | **Alnilam** : *Ferme* |
| **Schedar** : *Even* | **Gacrux** : *Contenu réservé aux adultes* | **Pulcherrima** : *franche* |
| **Achird** : *amical* | **Zubenelgenubi** : *Décontracté* | **Vindemiatrix** : *Doux* |
| **Sadachbia** : *Lively* | **Sadaltager** : *connaissances* | **Sulafat** : *chaude* |

Vous pouvez écouter toutes les options vocales dans

## Langues disponibles

Les modèles TTS détectent automatiquement la langue d'entrée. Voici les langues disponibles :

| Langue | Code BCP-47 | Langue | Code BCP-47 |
| --- | --- | --- | --- |
| Arabe | ar | Tagalog | fil |
| Bengali | bn | Finnois | fi |
| Néerlandais | nl | Galicien | gl |
| Anglais | en | Géorgien | ka |
| Français | fr | Grec | el |
| Allemand | de | Gujarati | gu |
| Hindi | hi | Créole haïtien | ht |
| Indonésien | id | Hébreu | il |
| Italien | it | Hongrois | hu |
| Japonais | ja | Islandais | est |
| Coréen | ko | Javanais | jv |
| Marathi | mr | Kannada | kn |
| Polonais | pl | Konkani | kok |
| Portugais | pt | Laotien | lo |
| Roumain | ro | Latino | la |
| Russe | ru | Letton | lv |
| Espagnol | es | Lituanien | lt |
| Tamoul | ta | Luxembourgeois | lb |
| Télougou | te | Macédonien | mk |
| Thaï | th | Maithili | mai |
| Turc | tr | Malgache | mg |
| Ukrainien | uk | Malaisien | ms |
| Vietnamien | vi | Malayalam | ml |
| Afrikaans | af | Mongol | mn |
| Albanais | sq | Népalais | ne |
| Amharique | am | Norvégien (bokmål) | nb |
| Arménien | hy | Norvégien, Nynorsk | nn |
| Azéri | az | Odia | ou |
| Basque | eu | Pachtô | ps |
| Biélorusse | be | Persan | fa |
| Bulgare | bg | Panjabi | pa |
| Birman | my | Serbe | sr |
| Catalan | ca | Sindhî | sd |
| Cebuano | ceb | Cingalais | si |
| Chinois (mandarin) | cmn | Slovaque | sk |
| Croate | h | Slovène | sl |
| Tchèque | cs | Swahili | sw |
| Danois | da | Suédois | sv |
| Estonien | et | Urdu | ur |

## Modèles compatibles

| Modèle | Locuteur unique | Multihaut-parleur |
| --- | --- | --- |
| [Aperçu de la synthèse vocale Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=fr) | ✔️ | ✔️ |
| [TTS Gemini 2.5 Flash (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=fr) | ✔️ | ✔️ |
| [TTS Gemini 2.5 Pro (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=fr) | ✔️ | ✔️ |

## Guide sur les requêtes

Le modèle **Gemini Native Audio Generation Text-to-Speech (TTS)** se distingue des modèles TTS classiques en utilisant un grand modèle de langage qui sait ***non seulement quoi dire, mais aussi comment le dire***.

Vous pouvez considérer une requête avancée comme une instruction système que le modèle doit suivre. Il s'agit d'un moyen de donner plus de contexte au modèle et de contrôler ses performances.

Pour débloquer cette fonctionnalité, les utilisateurs peuvent se considérer comme des réalisateurs qui mettent en scène un talent vocal virtuel. Pour créer une requête, nous vous recommandons de tenir compte des éléments suivants : un **profil audio** qui définit l'identité et l'archétype du personnage, une **description de la scène** qui établit l'environnement physique et l'ambiance émotionnelle, et des **notes du réalisateur** qui offrent des conseils plus précis sur le style, l'accent et le rythme.

En fournissant des instructions nuancées, comme un accent régional précis, des caractéristiques paralinguistiques spécifiques (par exemple, un souffle) ou un rythme, les utilisateurs peuvent tirer parti de la conscience du contexte du modèle pour générer des performances audio très dynamiques, naturelles et expressives. Pour des performances optimales, nous vous recommandons d'aligner les **transcriptions** et les consignes de mise en scène, *afin que "qui le dit"* corresponde à *"ce qui est dit"* et à *"comment c'est dit"*.

L'objectif de ce guide est de vous fournir des instructions de base et de vous donner des idées pour développer des expériences audio à l'aide de la génération audio Gemini TTS. Nous avons hâte de découvrir vos créations !

### Tags audio

Les balises sont des modificateurs intégrés tels que `[whispers]` ou `[laughs]` qui vous permettent de contrôler précisément la diffusion. Vous pouvez les utiliser pour modifier le ton, le rythme et l'ambiance émotionnelle d'une ligne ou d'une section de la transcription. Vous pouvez également les utiliser pour ajouter des interjections et quelques autres sons non verbaux à la performance, comme `[cough]`, `[sighs]` ou `[gasp]`.

Il n'existe pas de liste exhaustive des tags qui fonctionnent ou non. Nous vous recommandons de tester différentes émotions et expressions pour voir comment le résultat change.

Si votre transcription n'est pas en anglais, nous vous recommandons d'utiliser quand même des balises audio en anglais pour obtenir de meilleurs résultats.

**Soyez créatif avec les tags audio**

Pour vous montrer le type de variabilité que vous pouvez obtenir avec les tags audio, voici un ensemble d'exemples qui disent tous la même chose, mais dont la diffusion change en fonction des tags utilisés.

Vous pouvez modifier l'intonation de la voix en ajoutant des tags au début d'une ligne pour que le locuteur soit enthousiaste, ennuyé ou réticent :

- `[excitedly]` Bonjour, je suis un nouveau modèle de synthèse vocale et je peux dire les choses de différentes manières. Que puis-je faire pour vous ?
- `[bored]` Bonjour, je suis un nouveau modèle de synthèse vocale…
- `[reluctantly]` Bonjour, je suis un nouveau modèle de synthèse vocale…

Les balises peuvent également être utilisées pour modifier le rythme de la diffusion ou pour combiner le rythme et l'emphase :

- `[very fast]` Bonjour, je suis un nouveau modèle de synthèse vocale…
- `[very slow]` Bonjour, je suis un nouveau modèle de synthèse vocale…
- `[sarcastically, one painfully slow word at a time]` Bonjour, je suis un nouveau modèle de synthèse vocale…

Vous pouvez également contrôler précisément certaines sections, ce qui signifie que vous pouvez chuchoter une partie et crier une autre.

- `[whispers]` Bonjour, je suis un nouveau modèle de synthèse vocale, `[shouting]` et je peux dire les choses de différentes manières. `[whispers]` Que puis-je faire pour vous ?

Vous pouvez également tester n'importe quelle idée créative :

- `[like a cartoon dog]` Bonjour, je suis un nouveau modèle de synthèse vocale…
- `[like dracula]` Bonjour, je suis un nouveau modèle de synthèse vocale…

Voici quelques-uns des tags communément utilisés :

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Les balises vous permettent de contrôler rapidement la diffusion de votre transcription. Pour encore plus de contrôle, vous pouvez les combiner avec une invite de contexte afin de définir le ton et l'ambiance générale de la performance.

### Structure des requêtes

Une requête robuste inclut idéalement les éléments suivants qui, ensemble, permettent d'obtenir d'excellentes performances :

- **Profil audio** : établit une personnalité pour la voix, en définissant une identité, un archétype et toute autre caractéristique comme l'âge, l'origine, etc.
- **Scène** : plante le décor. Décrit à la fois l'environnement physique et l'ambiance.
- **Notes du réalisateur** : conseils sur les performances qui vous permettent de déterminer les instructions importantes que votre talent virtuel doit prendre en compte. Par exemple, le style, la respiration, le rythme, l'articulation et l'accent.
- **Exemple de contexte** : fournit au modèle un point de départ contextuel, de sorte que votre acteur virtuel entre naturellement dans la scène que vous avez configurée.
- **Transcription** : texte que le modèle va lire à voix haute. Pour des performances optimales, n'oubliez pas que le thème et le style d'écriture de la transcription doivent correspondre aux instructions que vous donnez.
- **Balises audio** : modificateurs que vous pouvez insérer dans une transcription pour modifier la façon dont cette partie du texte est lue (par exemple, `[whispers]` ou `[shouting]`).

Exemple de requête complète :

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### Stratégies de requête détaillées

Décomposons chaque élément de la requête :

#### Profil audio

Décrivez brièvement le personnage.

- **Nom**. Donner un nom à votre personnage permet d'ancrer le modèle et de renforcer les performances. Faites référence au personnage par son nom lorsque vous définissez la scène et le contexte.
- **Rôle**. Identité et archétype principaux du personnage dans la scène (par exemple, DJ radio, podcasteur, journaliste, etc.).

Exemples :

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Scene

Définissez le contexte de la scène, y compris le lieu, l'ambiance et les détails environnementaux qui établissent le ton et l'atmosphère. Décris ce qui se passe autour du personnage et comment cela l'affecte. La scène fournit le contexte environnemental pour l'ensemble de l'interaction et guide le jeu d'acteur de manière subtile et naturelle.

Exemples :

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### Notes du réalisateur

Cette section essentielle inclut des conseils spécifiques sur les performances. Vous pouvez ignorer tous les autres éléments, mais nous vous recommandons d'inclure celui-ci.

Définissez uniquement ce qui est important pour les performances, en veillant à ne pas trop spécifier. Si vous définissez trop de règles strictes, vous limiterez la créativité des modèles et risquez d'obtenir des performances moins bonnes. Équilibrez la description du rôle et de la scène avec les règles de performance spécifiques.

Les instructions les plus courantes sont **Style, Rythme et Accent**, mais le modèle n'est pas limité à celles-ci et ne les exige pas. N'hésitez pas à inclure des instructions personnalisées pour couvrir tous les détails supplémentaires importants pour vos performances, et à fournir autant ou aussi peu de détails que nécessaire.

Exemple :

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Style :**

Définit le ton et le style de la voix générée. Indiquez des adjectifs comme "joyeux", "énergique", "détendu", "ennuyé", etc. pour guider la performance. Soyez descriptif et fournissez autant de détails que nécessaire : *"Enthousiasme contagieux. L'auditeur doit avoir l'impression de faire partie d'un événement communautaire passionnant et de grande envergure."* est plus efficace que *"énergique et enthousiaste".*

Vous pouvez même essayer des termes populaires dans le secteur de la voix off, comme "sourire vocal". Vous pouvez superposer autant de caractéristiques de style que vous le souhaitez.

Exemples :

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Plus de profondeur

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Complexe

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Accent :**

Décrivez l'accent sélectionné. Plus vous serez précis, meilleurs seront les résultats. Par exemple, utilisez *accent anglais britannique tel qu'il est parlé à Croydon, en Angleterre* au lieu de *accent britannique*.

Exemples :

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**Rythme**

Rythme global et variations de rythme tout au long de la pièce.

Exemples :

Simple

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Plus de profondeur

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Complexe

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**Essayer**

Essayez vous-même certains de ces exemples dans l'[application TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=fr) et laissez Gemini vous mettre dans le fauteuil du réalisateur. Voici quelques conseils pour obtenir des performances vocales de qualité :

- N'oubliez pas de veiller à la cohérence de l'ensemble du prompt : le script et la mise en scène vont de pair pour créer une performance de qualité.
- Ne vous sentez pas obligé de tout décrire. Parfois, laisser au modèle la possibilité de combler les lacunes contribue à la fluidité. (Tout comme un acteur talentueux)
- Si vous êtes bloqué, demandez à Gemini de vous aider à rédiger votre script ou à préparer votre prestation.

## Limites

- Les modèles TTS ne peuvent recevoir que des entrées de texte et générer des sorties audio.
- Une session TTS a une limite de [fenêtre de contexte](https://ai.google.dev/gemini-api/docs/long-context?hl=fr) de 32 000 jetons.
- Consultez la section [Langues](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=fr#languages) pour connaître les langues disponibles.
- La synthèse vocale n'est pas compatible avec le streaming.

Les contraintes suivantes s'appliquent spécifiquement lorsque vous utilisez le modèle Gemini 3.1 Flash TTS Preview pour générer de la parole :

- **Incohérence de la voix avec les instructions du prompt** : la sortie du modèle ne correspond pas toujours strictement à la voix sélectionnée, ce qui peut entraîner un son différent de celui attendu. Pour éviter les tons discordants (par exemple, une voix masculine grave qui tente de parler comme une jeune fille), assurez-vous que le ton et le contexte de votre requête écrite correspondent naturellement au profil du locuteur sélectionné.
- **Qualité des sorties plus longues** : la qualité et la cohérence de la voix peuvent commencer à se dégrader pour les sorties générées de plus de quelques minutes. Nous vous recommandons de diviser vos transcriptions en plus petits passages.
- **Retour occasionnel de jetons de texte** : le modèle renvoie parfois des jetons de texte au lieu de jetons audio, ce qui entraîne l'échec de la requête par le serveur avec une erreur `500`. Comme cela se produit de manière aléatoire dans un très faible pourcentage de requêtes, vous devez implémenter une logique de nouvelle tentative automatisée dans votre application pour les gérer.
- **Rejets incorrects du classificateur de requêtes** : il est possible que les requêtes vagues ne déclenchent pas le classificateur de synthèse vocale, ce qui entraîne un rejet de la requête (`PROHIBITED_CONTENT`) ou amène le modèle à lire à voix haute vos instructions de style et vos notes de mise en scène. Validez vos invites en ajoutant un préambule clair indiquant au modèle de synthétiser la parole, et en indiquant explicitement où commence la transcription réelle.

## Étape suivante

- L'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr) de Gemini propose des options de génération audio interactives que vous pouvez entrelacer avec d'autres modalités.
- Pour savoir comment utiliser les *entrées* audio, consultez le guide [Compréhension audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/28 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/28 (UTC)."],[],[]]
