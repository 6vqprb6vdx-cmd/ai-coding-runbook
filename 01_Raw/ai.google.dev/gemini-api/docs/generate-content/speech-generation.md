---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr
fetched_at: 2026-10-05T06:36:54.731095+00:00
title: "G\u00e9n\u00e9ration de synth\u00e8se vocale \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Génération de synthèse vocale

L'API Gemini peut transformer des entrées de texte en contenu audio à un ou plusieurs intervenants à l'aide des fonctionnalités de génération de synthèse vocale (TTS) de Gemini.
La génération de synthèse vocale est *[contrôlable](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#controllable)*. Vous pouvez combiner des métadonnées structurées (`speech_metadata`) et des balises vocales intégrées pour guider le *style*, l'*accent*, le *rythme* et le *ton* de l'audio.

[Essayer dans Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr)

La fonctionnalité TTS diffère de la génération vocale fournie par l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr), qui est conçue pour les entrées et sorties audio interactives, non structurées et multimodales. Alors que l'API Live excelle dans les contextes conversationnels dynamiques, la TTS via l'API Gemini est conçue pour les scénarios qui nécessitent une récitation exacte du texte avec un contrôle précis du style et du son, comme la génération de podcasts ou de livres audio.

Ce guide vous explique comment générer de l'audio à une ou plusieurs voix à partir de texte à l'aide de [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`).

## Avant de commencer

Assurez-vous d'utiliser un modèle Gemini TTS listé dans la section [Modèles compatibles](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#supported-models). Pour obtenir des résultats optimaux, consultez [Quand utiliser tel ou tel modèle](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#when-to-use-which-model) afin de sélectionner le modèle le mieux adapté à votre charge de travail.

Il peut être utile de [tester les modèles Gemini TTS dans AI Studio](https://aistudio.google.com/generate-speech?hl=fr) avant de commencer à créer.

## TTS à un seul locuteur

Pour convertir du texte en audio à un seul locuteur avec les modèles Gemini 3.8 TTS, transmettez la transcription verbatim dans `parts[].text`, joignez le style au niveau du tour dans `parts[].speech_metadata` et configurez votre voix dans `speechConfig.voiceConfig`. Vous pouvez transmettre un nom de voix prédéfini, un ID de bibliothèque vocale étendue, un ID de [conception vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr) personnalisée (`voice_...`) ou un ID de [réplication vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr) (`voice_...` ou `voicekey_...` sans état facultatif).

Cet exemple enregistre le fichier audio de sortie du modèle au format WAV :

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## TTS multilocuteur

Pour les dialogues à plusieurs locuteurs, configurez deux locuteurs dans `multiSpeakerVoiceConfig.speakerVoiceConfigs` à l'aide de `prebuiltVoiceConfig` et transmettez chaque tour de dialogue en tant que `part` distinct avec `speech_metadata` spécifiant à la fois `speaker` et `style` facultatif au niveau du tour :

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## Contrôler le style de parole avec des métadonnées et des tags

Gemini 3.8 TTS traite le champ `text` strictement comme une transcription mot à mot. Pour contrôler la diffusion sans que les indications scéniques soient lues à voix haute, séparez vos instructions par portée :

- **Diffusion soutenue au niveau du tour de parole (`speech_metadata.style`)** : indiquez les émotions, le style de diffusion, la prosodie, le rythme et le volume qui s'appliquent à l'ensemble d'un tour de parole dans `speech_metadata.style` (par exemple, `"style": "whispered urgently"`, `"style": "out of breath"` ou `"style": "warm and enthusiastic"`).
- **Événements ponctuels (balises intégrées)** : placez les brèves pauses ou les brèves émissions vocales non verbales directement dans la transcription à l'aide de crochets (par exemple, `"Wait... <short pause> did you hear that? <sigh>"` ou `"Excuse me <cough> as I was saying..."`).

Pour découvrir toutes les bonnes pratiques, consultez le [guide sur les requêtes](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#prompting-guide).

## Options vocales

Gemini 3.8 TTS permet de sélectionner ou de créer des voix de quatre manières :

1. **Voix Studio prédéfinies** : 30 voix sélectionnées sont listées dans le tableau suivant.
2. **Bibliothèque vocale étendue** : des centaines de voix supplémentaires dans différentes langues, avec différents accents et différents archétypes de personnages sont disponibles à l'aide de `client.voices.list()` (`GET /v1beta/voices`).
3. **[Conception de voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr)** : générez une personnalité vocale personnalisée à partir d'une description en langage naturel dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr) ou à l'aide de `POST /v1beta/voices` (`type="prompted"`, qui renvoie un ID `voice_...` persistant et un aperçu WAV `sample_audio` dans `CreateVoice` et `GetVoice`).
4. **[Réplication de la voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr)** : répliquez la voix d'un locuteur à partir d'un audio de référence et de consentement dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr) ou à l'aide de `POST /v1beta/voices` (`type="replicated"`, `store=True` persistant par défaut ou `store=False` sans état facultatif).

### Limites et TTL des voix personnalisées

| Type de voix | Mode de stockage | Quota / Limite | Rétention (TTL) |
| --- | --- | --- | --- |
| **Voix avec état** (`voice_...`, générées ou répliquées) | `store=True` | **200 voix par projet** (partagées entre les voix incitées et répliquées) | **1 an à compter de la dernière utilisation\*** |
| **Clés vocales sans état** (`voicekey_...`, répliquées) | `store=False` | Géré par le client | **7 jours** |

\* **Extension de la durée de vie** : la période de conservation d'un an est réinitialisée chaque fois que la voix est utilisée activement (soit pour synthétiser la parole, soit comme voix de base pour un remix). Les voix qui n'ont pas été utilisées pendant un an sont automatiquement supprimées.

### Voix prédéfinies

|  |  |  |
| --- | --- | --- |
| **Zephyr** : *Lumineux* | **Puck** : *Upbeat* | **Charon** : *informatif* |
| **Kore** : *Ferme* | **Fenrir** : *excitabilité* | **Leda** : *jeune* |
| **Orus** : *ferme* | **Aoede** : *Breezy* | **Callirrhoe** : *tranquille* |
| **Autonoe** : *Lumineux* | **Encelade** : *Souffle* | **Iapetus** : *Effacer* |
| **Umbriel** : *décontracté* | **Algieba** : *Lisse* | **Despina** : *Smooth* |
| **Erinome** : *Effacer* | **Algenib** : *Graveleux* | **Rasalgethi** : *Informations* |
| **Laomedeia** : *Upbeat* | **Achernar** : *Soft* | **Alnilam** -- *Firm* |
| **Schedar** : *pair* | **Gacrux** : *Contenu réservé aux adultes* | **Pulcherrima** -- *Forward* |
| **Achird** : *amical* | **Zubenelgenubi** : *décontracté* | **Vindemiatrix** : *Doux* |
| **Sadachbia** : *Lively* | **Sadaltager** : *connaissances* | **Sulafat** : *chaude* |

### Bibliothèque vocale étendue et filtrage

En plus des 30 voix de studio présentées dans le tableau précédent, la **bibliothèque vocale étendue** propose des centaines de voix supplémentaires dans différentes langues, avec des accents régionaux, des personnages et des domaines variés. Vous pouvez parcourir, filtrer et écouter l'intégralité de la bibliothèque de voix de manière interactive dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr), ou l'interroger de manière programmatique à l'aide de `client.voices.list()` (`GET /v1beta/voices`, en utilisant `google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` renvoie vos voix stockées personnalisées (de la plus récente à la plus ancienne), suivies des voix de catalogue prédéfinies correspondant à vos critères de filtrage. Lorsque plusieurs valeurs sont transmises pour un filtre de liste, les voix correspondant à **n'importe quelle** valeur de ce filtre sont renvoyées (`OR`), tandis que les paramètres de filtre distincts sont combinés avec `AND` :

| Paramètre | Type | Description |
| --- | --- | --- |
| `language_code` | `list[str]` | Balise(s) de langue BCP-47 (par exemple, `["en-US", "en-GB"]`). Correspondance exacte non sensible à la casse. |
| `region_code` | `list[str]` | Code(s) de région ISO 3166-1 alpha-2 ou UN M.49 (par exemple, `["US", "GB"]`). |
| `accent` | `list[str]` | Descripteur(s) d'accent régional (par exemple, `["American", "British"]`). |
| `gender` | `list[str]` | Genre perçu (`"female"`, `"male"` ou `"neutral"`). |
| `pitch` | `list[str]` | Classification de la hauteur vocale (`"low"`, `"medium"` ou `"high"`). |
| `persona` | `list[str]` | Personnalité vocale ou archétype de personnage (par exemple, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` dans REST) | `list[str]` | Domaine d'utilisation optimal (par exemple, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` en Python) | `list[str]` | Filtrer par source vocale : `"prebuilt"`, `"prompted"` ([Conception de voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr)) ou `"replicated"` ([Réplication de voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr)). |
| `search` | `str` | La recherche de sous-chaînes en texte libre correspond à la casse insensible par rapport à `display_name` et `description`. |
| `page_size` | `int` | Nombre maximal de voix renvoyées par page (`50` par défaut, `1000` maximum). |
| `page_token` | `str` | Jeton de `response.next_page_token` permettant d'extraire la page de résultats suivante. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Langues disponibles

Les modèles TTS détectent automatiquement la langue d'entrée.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) est compatible avec **plus de 130 langues**, et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`) est compatible avec **plus de 100 langues** :

| Langue | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Aceh (écriture arabe) | ✔️ | ✔️ |
| Afrikaans | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amharique | ✔️ | ✔️ |
| Arménien | ✔️ | ✔️ |
| Assamais | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Balinais | ✔️ | ✔️ |
| Bengali | ✔️ | ✔️ |
| Banjar (écriture arabe) | ✔️ | — |
| Banjar (alphabet latin) | ✔️ | ✔️ |
| Bachkir | ✔️ | — |
| Basque | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| Bemba | ✔️ | — |
| Bhodjpouri | ✔️ | ✔️ |
| Bosniaque | ✔️ | ✔️ |
| Bouguis | ✔️ | ✔️ |
| Bulgare | ✔️ | ✔️ |
| Birman | ✔️ | — |
| Cantonais | ✔️ | ✔️ |
| Catalan | ✔️ | ✔️ |
| Cebuano | ✔️ | ✔️ |
| Sorani | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| Chinois (script Hans) | ✔️ | ✔️ |
| Chinois (script Hant) | ✔️ | ✔️ |
| Tatar de Crimée | ✔️ | — |
| Croate | ✔️ | ✔️ |
| Tchèque | ✔️ | ✔️ |
| Danois | ✔️ | ✔️ |
| Néerlandais | ✔️ | ✔️ |
| Dioula | ✔️ | — |
| Dzongkha | ✔️ | — |
| Arabe (Égypte) | ✔️ | ✔️ |
| Anglais | ✔️ | ✔️ |
| Estonien | ✔️ | ✔️ |
| Tagalog | ✔️ | ✔️ |
| Finnois | ✔️ | — |
| Français | ✔️ | ✔️ |
| Galicien | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Géorgien | ✔️ | ✔️ |
| Allemand | ✔️ | ✔️ |
| Grec | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Gujarati | ✔️ | ✔️ |
| Créole haïtien | ✔️ | ✔️ |
| Mongol khalkha | ✔️ | ✔️ |
| Haoussa | ✔️ | ✔️ |
| Hébreu | ✔️ | ✔️ |
| Hindi | ✔️ | ✔️ |
| Hongrois | ✔️ | ✔️ |
| Islandais | ✔️ | ✔️ |
| Igbo | ✔️ | — |
| Ilocano | ✔️ | ✔️ |
| Indonésien | ✔️ | ✔️ |
| Persan iranien | ✔️ | ✔️ |
| Italien | ✔️ | ✔️ |
| Japonais | ✔️ | ✔️ |
| Javanais | ✔️ | ✔️ |
| Kabyle | ✔️ | — |
| Kamba | ✔️ | ✔️ |
| Kannada | ✔️ | ✔️ |
| Cachemiri (écriture arabe) | ✔️ | ✔️ |
| Cachemiri (Devanagari) | ✔️ | ✔️ |
| Kazakh | ✔️ | ✔️ |
| Khmer | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Kinyarwanda | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Coréen | ✔️ | ✔️ |
| Kirghiz | ✔️ | ✔️ |
| Laotien | ✔️ | ✔️ |
| Latgalien | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Lituanien | ✔️ | — |
| Luxembourgeois | ✔️ | — |
| Macédonien | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili | ✔️ | ✔️ |
| Malayalam | ✔️ | ✔️ |
| Maltais | ✔️ | ✔️ |
| Manipuri | ✔️ | ✔️ |
| Marathi | ✔️ | ✔️ |
| Minangkabau (écriture arabe) | ✔️ | ✔️ |
| Minangkabau (alphabet latin) | ✔️ | — |
| Mizo | ✔️ | ✔️ |
| Népalais (langue individuelle) | ✔️ | ✔️ |
| Peul du Nigeria | ✔️ | ✔️ |
| Azerbaïdjanais du Nord | ✔️ | ✔️ |
| Sotho du Nord | ✔️ | ✔️ |
| Ouzbek du Nord | ✔️ | ✔️ |
| Norvégien bokmål | ✔️ | ✔️ |
| Nynorsk (norvégien) | ✔️ | ✔️ |
| Chichewa | ✔️ | ✔️ |
| Occitan | ✔️ | — |
| Odia (langue individuelle) | ✔️ | ✔️ |
| Pangasinan | ✔️ | — |
| Perse (Afghanistan) | ✔️ | ✔️ |
| Polish | ✔️ | ✔️ |
| Portugais | ✔️ | ✔️ |
| Panjabi | ✔️ | ✔️ |
| Roumain | ✔️ | ✔️ |
| Russe | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Serbe | ✔️ | ✔️ |
| Sindhî | ✔️ | — |
| Cingalais | ✔️ | ✔️ |
| Slovaque | ✔️ | ✔️ |
| Slovène | ✔️ | — |
| Somali | ✔️ | — |
| Azéri | ✔️ | ✔️ |
| Pachto du Sud | ✔️ | ✔️ |
| Sotho du Sud | ✔️ | — |
| Espagnol | ✔️ | ✔️ |
| Arabe standard (écriture arabe) | ✔️ | ✔️ |
| Arabe standard (alphabet latin) | ✔️ | ✔️ |
| Letton standard | ✔️ | ✔️ |
| Malais standard | ✔️ | ✔️ |
| Swahili (langue individuelle) | ✔️ | — |
| Swati | ✔️ | — |
| Suédois | ✔️ | — |
| Tadjik | ✔️ | — |
| Tamoul | ✔️ | ✔️ |
| Telugu | ✔️ | ✔️ |
| Thaï | ✔️ | — |
| Tigrinya | ✔️ | — |
| Tosque albanais | ✔️ | — |
| Turkish | ✔️ | ✔️ |
| Ouïghour | ✔️ | — |
| Vietnamien | ✔️ | ✔️ |

## Modèles compatibles

| Modèle | Locuteur unique | Plusieurs locuteurs | Conception de la voix | Réplication vocale |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Preview Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=fr) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=fr) | ✔️ | ✔️ | — | — |

### Quand utiliser quel modèle

Les deux modèles TTS Gemini 3.8 partagent exactement le même schéma d'API et le même format d'invite, ce qui vous permet de passer de l'un à l'autre en modifiant un seul paramètre :

- **Utilisez [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr)
  (`gemini-3.8-flash-tts`)** lorsque la fidélité acoustique maximale, le jeu nuancé
  et le contrôle expressif sont prioritaires. Il est idéal pour les travaux créatifs de qualité studio, les dialogues complexes à plusieurs locuteurs, les tags vocaux lourds, les prononciations difficiles, les dialectes régionaux ou minoritaires, et les narrations longues nécessitant une stabilité vocale et de ton de pièce à toute épreuve.
- **Utilisez [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr)
  (`gemini-3.8-flash-lite-tts`)** comme solution de remplacement rapide et économique pour `gemini-3.1-flash-tts-preview`. Il est optimisé pour la production en masse à grand volume, les cascades d'agents vocaux conversationnels, les fonctionnalités de lecture à voix haute, la réplication vocale fiable et la parole quotidienne à un seul locuteur dans les principales langues.

### Guide de migration

Lorsque vous passez des modèles d'aperçu précédents (`gemini-3.1-flash-tts-preview` ou `gemini-2.5-pro-preview-tts`) à Gemini 3.8 TTS (`gemini-3.8-flash-tts` ou `gemini-3.8-flash-lite-tts`), examinez ces cinq principaux changements :

1. **Séparer le style de la transcription** : déplacez les instructions de jeu, de ton, de prosodie et de rythme (comme `"whispering"`, `"out of breath"` ou `"speaking slowly"`) du texte brut vers `speech_metadata.style`.
   Conservez `text` strictement comme transcription mot à mot, en ajoutant des tags vocaux intégrés.
2. **Concevez des personas en amont avec la conception vocale** : remplacez les blocs `"Audio Profile"` ou `"Director's Notes"` de plusieurs paragraphes par une voix personnalisée créée dans [Conception vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr), puis transmettez cet ID `voice_...` dans vos requêtes TTS avec des chaînes `style` minimales ou vides.
3. **Utilisez des tours de dialogue structurés** : pour les dialogues à plusieurs locuteurs, transmettez un `part` par tour de locuteur avec `speech_metadata.speaker` au lieu d'intégrer des préfixes `Speaker: ...` dans un seul bloc de texte.
4. **Utilisez des crochets pour les tags vocaux intégrés** : utilisez des crochets (`<laugh>`, `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) pour les vocalisations et les pauses humaines ponctuelles. Évitez les tags d'effets sonores non vocaux (comme les applaudissements ou les bruits sourds).
5. **Tenir compte de la sortie WAV (`AUDIO_WAV`) par défaut pour les requêtes unitaires** : contrairement à `gemini-3.1-flash-tts-preview` (qui renvoyait par défaut un `AUDIO_L16` PCM brut sans en-tête), les modèles Gemini 3.8 TTS renvoient un fichier audio **WAV (`AUDIO_WAV`)** complet avec un en-tête RIFF (PCM 16 bits, mono, 24 kHz) pour les requêtes unitaires :
   - Si votre code encapsulait auparavant des octets PCM bruts dans un en-tête WAV (par exemple, à l'aide du module `wave` de Python ou du package `wav` de Node), supprimez l'encapsuleur d'en-tête manuel et écrivez les octets audio décodés directement dans un fichier `.wav`.
   - Si votre pipeline existant nécessite un fichier audio PCM brut sans en-tête, mu-law ou A-law, définissez explicitement `response_format.audio.mime_type` sur `"AUDIO_L16"`, `"AUDIO_MULAW"` ou `"AUDIO_ALAW"` (par exemple, `{"response_format": {"audio": {"mime_type": "AUDIO_L16"}}}` dans `generateContent`, ou `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` dans l'API Interactions). Consultez [Formats de sortie audio](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#audio-output-formats).

## Guide sur les requêtes

Les modèles Gemini 3.8 TTS traitent le texte saisi strictement comme une **transcription mot pour mot**.
Contrairement aux modèles d'aperçu précédents où les indications scéniques étaient intégrées en texte brut, Gemini 3.8 TTS sépare les indications de niveau tour soutenues (`speech_metadata`) des tags vocaux intégrés ponctuels.

### Champ "Style" et balises intégrées

Répartissez vos instructions de performances par portée :

- **Niveau de tour de parole (`speech_metadata.style`)** : placez les attributs de diffusion soutenue (comme l'émotion, la prosodie, le rythme général ou le style de diffusion, comme `"whispering"`, `"out of breath"`, `"muttering"` ou `"sarcastic"`) dans le champ `style` de `speech_metadata`. Pour créer un personnage et une performance stables au fil des tours, concevez le personnage à l'avance dans la section [Conception de la voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr) et utilisez `style` uniquement pour les ajustements facultatifs au niveau du tour.
- **Événements ponctuels (tags intégrés)** : insérez les brèves vocalises, respirations ou pauses non verbales dans la transcription à l'aide de crochets (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Utilisez des crochets (`<...>`) pour obtenir la meilleure qualité audio possible et limitez-vous aux vocalises humaines plutôt qu'aux effets sonores non vocaux.

| Champ d'application | Où placer | Exemples |
| --- | --- | --- |
| **Au niveau du tour** (soutenu tout au long du tour) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **À un moment précis** (se produit à un mot spécifique) | En ligne dans `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Rythme et pauses

Vous pouvez contrôler le rythme et le silence à trois niveaux de précision :

- **Ponctuation et points de suspension** : utilisez des virgules, des tirets (`--`) et des points de suspension (`...`) pour simuler des hésitations naturelles.
- **Balises de pause intégrées** : insérez `<short pause>` ou `<long pause>` aux endroits exacts du script où l'orateur doit faire une pause :
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Rythme au niveau du tour** : définissez `"style": "speaking rapidly"` ou `"style": "speaking slowly"` dans `speech_metadata` pour contrôler le débit vocal pour l'ensemble du tour.

### Prosodie et ton

Utilisez **`speech_metadata.style`** pour contrôler la prosodie, la hauteur et l'inflexion de la voix tout au long d'un tour de parole (par exemple, `"style": "high pitch, cheerful and excited inflection"` ou `"style": "monotone and flat"`). Si l'émotion ou la prosodie changent au milieu du dialogue, divisez le script en tours de parole distincts avec des valeurs `style` différentes pour chacun d'eux.

### Mise en valeur

Mettez en majuscules certains mots de la transcription, en les combinant avec de la ponctuation et des balises vocales intégrées, pour mettre l'accent sur les mots clés :

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Exclamations et sons autres que la parole

Placez les vocalisations humaines non verbales sur la même ligne que le texte, en utilisant des chevrons (`<...>`) à l'endroit exact où le son doit se produire. Voici quelques exemples de tags vocaux recommandés :

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>`/`<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>`/`<laughter>` | `<moan>` | `<pant>` | `<pff>`/`<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>`/`<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>`/`<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Canaux secondaires et chevauchement des voix

Dans un dialogue à plusieurs locuteurs, entourez les réactions de l'auditeur de barres verticales (`|reaction|`) à l'intérieur du tour de parole d'un locuteur pour créer des retours naturels ou un chevauchement de la parole sans créer un tour de parole distinct par réaction.

- **Échanges brefs en canal arrière** : insérez de brèves réactions de l'auditeur (`|oh hmm|`, `|oh really?|`, `|absolutely|`) dans le tour de parole de l'interlocuteur actif :
  - **Tour 1 (Locuteur A)** : `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Tour 2 (Locuteur B)** : `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Tour 3 (Intervenant A) :** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Chevauchement et entrelacement de la parole** : utilisez plusieurs segments de barre verticale pour simuler la parole simultanée ou entrelacée entre deux locuteurs (fonctionne mieux avec `gemini-3.8-flash-tts`) :
  - **Compte à rebours/refrain simultanés** : `"Let's surprise him on three |ok| ready?"` suivi de `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Chevauchement complet des intervenants** : `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Cohérence entre les générations et ce qu'il faut éviter

Suivez ces consignes pour que l'identité vocale reste stable tout au long de la conversation :

- **Concevez des personas en amont dans la conception vocale au lieu de longs blocs de style** : les longs paragraphes `"Audio Profile"` et les listes à puces multiples `"Director's Notes"` hérités des modèles précédents sont la cause la plus fréquente de dérive vocale.
  Utilisez cette même intuition créative dès le début de la [conception vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr) pour générer une personnalité `voice_...` personnalisée persistante, puis transmettez cet ID vocal à vos appels TTS.
- **S'appuyer sur la référence vocale pour la stabilité (omettre les méta-instructions)** :
  Les modèles Gemini 3.8 TTS sont entraînés pour s'ancrer d'abord sur la référence audio.
  N'incluez pas d'instructions demandant au modèle de maintenir la voix stable (comme `"do not switch speaker identity"` ou `"maintain identical timbre"`). Un texte de requête supplémentaire augmente la dérive. Supprimez les instructions de style inutiles et laissez le modèle varier naturellement autour du point stable fourni par la référence vocale.
- **N'essayez pas de modifier les caractéristiques immuables du locuteur dans `style`** : évitez d'indiquer l'âge, le genre, les noms ou les changements d'accent permanents dans `speech_metadata.style`.
  Choisissez plutôt une voix régionale dans la bibliothèque vocale étendue ou créez-en une avec [Conception de voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr).

### Workflow recommandé

1. **Créez le personnage une seule fois** : créez votre personnage dans [Conception de voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr) ou sélectionnez une voix régionale dans la bibliothèque vocale étendue qui correspond à votre langue cible et à votre persona.
2. **Rédigez des transcriptions naturelles avec des hésitations** : pour un naturel maximal, rédigez le `text` comme une véritable transcription orale, y compris les hésitations et les disfluences naturelles (par exemple, `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Testez d'abord la synthèse vocale simple** : synthétisez votre transcription avec un champ `style` vide. La plupart des requêtes n'ont pas besoin d'instruction `style`.
4. **N'ajoutez des requêtes `style` courtes que pour les ajustements** : n'ajoutez une chaîne `style` concise (telle que `"casual, friendly"` ou `"muttering, then reassuring"`) que pour les tours qui nécessitent un ajustement de diffusion spécifique, et réutilisez cette chaîne courte exacte pour les tours lorsque vous souhaitez une base de référence cohérente.

### Agents vocaux et de dialogue multitours

Lorsque vous créez des agents vocaux conversationnels en temps réel ou des applications multitours :

- Effectuez **un appel TTS par tour** à mesure que les blocs de texte LLM arrivent.
- Laissez le `voice` configuré (`voice_...` prédéfini, conçu ou répliqué `voice_...` / `voicekey_...`) transmettre l'identité de l'interlocuteur à chaque tour de parole. N'envoyez jamais de persona de personnage long à chaque tour de parole.
- Laissez le champ `style` par tour vide ou envoyez une courte chaîne constante (comme `"casual, friendly"`) pour l'ensemble de la conversation.
- Divisez les longues réponses des agents en tours plus courts au lieu d'utiliser des consignes de style plus fortes.

## Génération de voix en flux continu

Vous pouvez diffuser l'audio généré au fur et à mesure de sa synthèse par le modèle. Contrairement aux requêtes unaires (qui renvoient un fichier WAV complet avec un en-tête RIFF), **les requêtes de streaming renvoient par défaut des blocs PCM (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, mono) bruts de 16 bits signés little-endian sans en-tête**. Les blocs audio peuvent ainsi être lus ou concaténés en continu sans en-tête de conteneur :

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## Formats de sortie audio

Les modèles Gemini 3.8 TTS utilisent différents formats audio par défaut selon que la requête est unaire ou en flux :

- **Requêtes unaires (`models.generate_content`)** : renvoient un fichier audio **WAV (`AUDIO_WAV`)** complet avec un en-tête RIFF (PCM 16 bits little-endian signé, mono, 24 kHz). Vous pouvez écrire les octets audio décodés directement dans un fichier `.wav` sans ajouter manuellement de conteneur WAV.
- **Requêtes de streaming (`models.generate_content_stream` / `streamGenerateContent`)** : renvoient par défaut des blocs **PCM linéaire brut sans en-tête (`AUDIO_L16`)** (PCM 24 kHz, mono, 16 bits signé little-endian) afin que les blocs puissent être diffusés en streaming ou concaténés en continu sans en-tête de conteneur sur chaque bloc.

Vous pouvez remplacer l'encodage et la fréquence d'échantillonnage de l'audio de sortie à l'aide de `generationConfig.responseFormat.audio` :

| Valeur `mimeType` | Format | Description |
| --- | --- | --- |
| `"AUDIO_WAV"` *(valeur par défaut unaire)* | WAV (`audio/wav`) | Fichier WAV complet avec un en-tête RIFF (24 kHz, mono, PCM 16 bits). |
| `"AUDIO_L16"` *(par défaut pour le streaming)* | PCM linéaire (`audio/l16`) | PCM linéaire little-endian signé 16 bits brut sans en-tête. Idéal pour le streaming, les pipelines audio personnalisés ou la concaténation d'extraits multirépenses. |
| `"AUDIO_MULAW"` | Loi μ (`audio/basic` / `audio/mulaw`) | Audio compressé G.711 μ-law. Fréquemment utilisé dans la téléphonie nord-américaine et japonaise (8 kHz). |
| `"AUDIO_ALAW"` | A-law (`audio/alaw`) | Audio compressé G.711 A-law. Fréquence couramment utilisée dans la téléphonie européenne et internationale (8 kHz). |

Vous pouvez également spécifier `sampleRate` (par exemple, `24000`, `16000` ou `8000` Hz ; la valeur par défaut est `24000` Hz).

L'exemple suivant demande un PCM 16 bits brut sans en-tête (`AUDIO_L16`) à 24 kHz :

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "response_format": {
            "audio": {
                "mime_type": "AUDIO_L16",
                "sample_rate": 24000,
            }
        },
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.pcm", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         responseFormat: {
            audio: {
               mimeType: 'AUDIO_L16',
               sampleRate: 24000,
            },
         },
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## Limites

- Les modèles TTS acceptent les entrées textuelles uniquement et génèrent des sorties audio uniquement.
- La génération multilocuteur en une seule requête (`multiSpeakerVoiceConfig`) est compatible avec un maximum de deux locuteurs utilisant des voix prédéfinies. Pour combiner des voix personnalisées (`voice_...`) ou répliquées (`voice_...` / `voicekey_...`) dans un dialogue à plusieurs personnages, synthétisez le tour de parole de chaque locuteur individuellement.
  Étant donné que les requêtes unaires renvoient `audio/wav` avec un en-tête RIFF de 44 octets par défaut, demandez le PCM brut (`AUDIO_L16`) ou supprimez l'en-tête WAV de chaque tour avant de concaténer les trames audio PCM de 24 kHz.
- **Limites de stockage et TTL pour les voix personnalisées :**
  - **Voix avec état (`store=True`, incitées ou répliquées)** : maximum de **200 voix par projet** avec une **valeur TTL (Time To Live) d'un an**.
  - **Clés vocales sans état (`store=False`, `voicekey_...`)** : **TTL de 7 jours** (time-to-live).
- Consultez la section [Langues acceptées](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#languages) pour connaître les langues disponibles.

## Étape suivante

- Créez des personas vocaux personnalisés à partir du langage naturel avec la [conception vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr).
- Répliquez la voix d'un locuteur existant dans la [réplication de voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr).
- Comparez les spécifications des modèles sur les pages [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr).
- Découvrez l'audio bidirectionnel interactif avec l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/02 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/02 (UTC)."],[],[]]
