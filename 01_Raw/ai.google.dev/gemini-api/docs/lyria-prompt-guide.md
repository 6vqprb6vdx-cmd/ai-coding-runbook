---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=fr
fetched_at: 2026-11-02T07:04:54.376142+00:00
title: "Guide sur les prompts Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Guide sur les prompts Lyria

L'API Gemini propose deux façons de générer de la musique avec Lyria :

- **Lyria 3.5 et Lyria 3 Clip** : génération non en streaming de clips de 30 secondes ou de morceaux complets avec paroles et voix. Consultez [Générer de la musique avec Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr).
- **Lyria RealTime** : streaming musical interactif en temps réel et pilotage en direct sur WebSockets. Consultez [Génération de musique en temps réel avec Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=fr).

Les deux modèles répondent aux requêtes textuelles descriptives, à la terminologie musicale et aux instructions structurelles. Ce guide explique comment rédiger des requêtes efficaces pour la génération par lot et le pilotage en temps réel.

## Principes de base des requêtes

Votre requête peut être une courte expression :

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

Ou une description structurée et détaillée :

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

Les requêtes courtes et détaillées génèrent de bons résultats. Utilisez les stratégies suivantes pour orienter le modèle vers le son exact que vous souhaitez obtenir.

## Genre et style

Commencez votre requête par le genre principal. Vous pouvez combiner des genres pour créer des hybrides uniques :

- Mélange de metal et de hip-hop
- Death metal combiné à des voix d'opéra
- Musique de chambre classique avec des éléments de drone électronique sombres
- Musique électronique moderne pour danser (EDM) mélangée à de l'Europop

Vous pouvez également spécifier une époque musicale ou une variante régionale :

- Boom-bap hip-hop du début des années 90
- Pop yé-yé française des années 1960
- Post-punk et new wave des années 1980
- R&B mainstream des années 2000
- Techno minimaliste berlinoise ou hyphy de la baie de San Francisco

### Mots clés de genre

Utilisez ces termes de genre reconnus dans vos requêtes pour Lyria 3.5 et Lyria RealTime :

- **Dance et électro** : `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **Hip-hop et R&B** : `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **Rock et musique alternative** : `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **Jazz, soul et funk** : `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **Folk et traditionnelle** : `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **Classique et acoustique** : `Baroque, Orchestral Score, Piano Ballad`

## Instruments et textures

Lyria sélectionne automatiquement l'instrumentation appropriée pour le genre demandé. Si vous souhaitez des instruments spécifiques ou des combinaisons inhabituelles, déclarez-les explicitement :

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

Décrivez le son et l'interaction des instruments pour définir l'ambiance et la texture :

- Une ligne de basse 303 déformée qui traverse des hi-hats nets et serrés
- Pads de synthé analogiques chaleureux et gonflés sous une guitare acoustique intimiste et sèche
- Mur de son composé de plusieurs couches de guitare fuzz, avec des voix lointaines et réverbérées

### Mots clés d'instrument

- **Claviers et synthétiseurs** : `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Basse et batterie** : `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **Guitares et cordes** : `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Vent et cuivres** : `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **Percussions** : `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## Structure et timing des titres

Pour Lyria 3.5, définissez la progression du morceau à l'aide de tags ou de flèches :

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- Commence par une introduction au piano calme, puis passe à un couplet énergique, marque une pause avec un moment de silence, puis explose dans le refrain.

Vous pouvez diriger les transitions et la dynamique de l'énergie :

- Faites monter la tension dans le pré-refrain, puis passez au silence avant un refrain explosif.
- Crescendo progressif tout au long du morceau, avec l'ajout d'un instrument par section
- Un arrêt soudain après le pont, suivi d'un refrain a cappella

Vous pouvez également demander des repères temporels spécifiques :

- Créer un temps fort à 12 secondes
- L'échantillon vocal se répète toutes les quatre mesures
- Le refrain commence à 22 secondes.

## Paroles et voix

Lyria 3.5 génère des pistes vocales avec paroles par défaut. Vous pouvez fournir vos propres paroles, demander au modèle de les générer ou demander une version instrumentale.

### Utiliser vos propres paroles

Incluez vos paroles directement dans la requête sous un en-tête `Lyrics:`. Ajoutez un tag à chaque section pour guider la diction :

```
Lyrics:

[Intro]
Ooooh, yeah

[Verse 1]
Early morning rain on the window pane
City lights wash away the pain
Walking down this empty street again

[Chorus]
We keep moving on (moving on)
Until the morning light
Everything will be alright
```

Utilisez des parenthèses pour les chœurs, les échos ou les ad-libs, comme dans `(moving on)`.

### Diriger les paroles générées

Lorsque vous demandez à Lyria 3.5 d'écrire des paroles, décrivez la narration, l'émotion ou les expressions clés :

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

Pour les genres électroniques et dance, demandez des accroches vocales courtes et répétitives :

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### Profils des chanteurs et des prestations vocales

Spécifiez le genre, la tessiture et le timbre pour obtenir un rendu précis :

- **Soprano** : timbre clair et cristallin, avec une voix agile et puissante. Son clair capable de produire des textures aériennes et soufflées.
- **Alto féminin** : registre grave riche, chaleureux et rauque. Timbre enfumé avec une voix de poitrine émouvante et résonnante.
- **Ténor** : voix claire, perçante et énergique Timbre juvénile avec une grande puissance de belting qui se démarque dans les mix denses.
- **Baryton masculin** : voix de poitrine profonde et veloutée, avec un ton chaleureux, apaisant et mélodieux.
- **Rockeur usé** : timbre rauque et granuleux rappelant le rock alternatif des années 1990. Intensité émotionnelle brute avec des notes aiguës tendues.

### Effets vocaux non lyriques

Vous pouvez également demander des dialogues parlés, des effets de voix et des effets de sampling :

- Une voix de speaker radio vintage présente la chanson avant que le rythme ne commence.
- Une voix parlée murmure juste avant le drop, suivie de synthés énergiques
- Boucles d'échantillons vocaux hachés et transposés servant d'élément rythmique instrumental

## Paramètres musicaux

Affinez votre requête avec des propriétés musicales standards :

- **Tempo (BPM)** : définissez directement le tempo (par exemple, `120 BPM`, `slow tempo around 72 BPM` ou `fast 160 BPM`).
- **Tonalité et gamme** : spécifiez la tonalité et la gamme de base (par exemple, `in G major`, `in D minor`, `in C pentatonic`).
- **Ambiance et atmosphère** : utilisez des adjectifs descriptifs émotionnels :
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Écrire des requêtes pour Lyria RealTime

Lyria RealTime utilise des **prompts pondérés** plutôt qu'une seule chaîne de prompt monolithique. Cela vous permet de mélanger dynamiquement plusieurs influences musicales et de diriger la musique en continu via une connexion WebSocket.

### Structure de prompt pondérée

Chaque requête pondérée se compose d'une expression textuelle descriptive et d'une pondération à virgule flottante :

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### Stratégies de pilotage en temps réel

- **Mélanger les genres** : mélangez des styles distincts en attribuant des pondérations équilibrées :
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **Transitions dynamiques** : pour que la musique change en douceur, ajustez les pondérations des requêtes au fil du temps :
  1. Commencez par `chill jazz piano (weight: 1.0)`.
  2. Ajoutez progressivement `electronic breakbeat (weight: 0.3)`.
  3. Augmentez `electronic breakbeat` à `0.8` tout en diminuant `chill jazz piano` à `0.3`.
- **Superposer des éléments** : séparez les tags d'instruments et les tags d'humeur pour pouvoir les ajuster indépendamment :
  - Requête 1 : `bossa nova guitar (weight: 0.9)`
  - Requête 2 : `warm acoustic bass (weight: 0.7)`
  - Requête 3 : `subtle vinyl crackle (weight: 0.3)`

## Exemples de prompts

### Exemples Lyria 3.5

- **Lo-Fi Study Beat** :
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **Hymne pop** :
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cyberpunk cinématique** :
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Ensemble de paramètres Lyria RealTime

```
# Initial high-energy groove
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="techno groove", weight=1.0),
        types.WeightedPrompt(text="acid 303 bass", weight=0.8),
    ]
)

# Transition to a melodic breakdown
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="ambient synth pads", weight=1.0),
        types.WeightedPrompt(text="subtle reverberant piano", weight=0.7),
        types.WeightedPrompt(text="techno groove", weight=0.2),
    ]
)
```

## Étape suivante

- [Générez de la musique avec Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr) : générez des titres complets et des extraits de 30 secondes à l'aide de l'API Interactions.
- [Génération de musique en temps réel avec Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=fr) : créez des applications de streaming musical interactives en temps réel sur WebSockets.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/18 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/18 (UTC)."],[],[]]
