---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=fr
fetched_at: 2026-09-07T05:43:18.039973+00:00
title: "Transcription audio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Transcription audio

L'API Gemini convertit la parole contenue dans les fichiers audio en texte à l'aide du modèle Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Grâce aux capacités de compréhension audio de Gemini, elle fournit une transcription précise avec identification automatique de la langue, attribution des locuteurs, codes temporels au niveau des mots et suggestions de vocabulaire personnalisé. Il propose également un mode de [transcription intelligente](#transcription-modes) qui supprime les hésitations et met en forme le texte de manière intelligente.

Pour transcrire un fichier audio, importez-le et transmettez-le à `gemini-3.5-transcribe` :

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## Présentation

Gemini 3.5 Transcribe est optimisé pour les tâches de reconnaissance vocale. Il gère les différents accents, les bruits de fond et les conversations multilingues.

Voici les principales fonctionnalités de cette solution :

- **Reconnaissance vocale automatique (ASR)** : détecte automatiquement les langues dans [plus de 85 paramètres régionaux](#supported-languages). Gère le code-switching intra-phrase et inter-phrase sans configuration manuelle.
- **Vocabulaire personnalisé** : oriente la reconnaissance vers les termes, acronymes et noms propres spécifiques à un domaine en transmettant jusqu'à 1 000 expressions.
- **Diarisation des locuteurs** : permet de distinguer plusieurs locuteurs et d'attribuer les segments parlés à des identifiants distincts.
- **Codes temporels au niveau du mot** : génèrent des décalages temporels de début et de fin précis pour chaque mot reconnu.
- **Transcription intelligente** : supprime les hésitations, les mots de remplissage et les répétitions, et applique une mise en forme structurée.
- **Mise en forme et normalisation** : applique la mise en majuscules, la ponctuation et la normalisation inverse du texte (par exemple, en convertissant "vingt-six millions de dollars" en "26 M$").

Pour le raisonnement audio général ou les systèmes de questions-réponses sur le contenu audio, utilisez [Compréhension audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr). Pour la synthèse audio de texte en voix, utilisez [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).

## Détection de la langue et suggestions

Par défaut, le modèle détecte automatiquement la langue parlée. Il passe d'une langue à l'autre de manière dynamique lorsque les locuteurs alternent les langues.

Pour utiliser la détection automatique, omettez `language_codes` ou fournissez une liste vide :

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

Si vous connaissez la langue à l'avance, spécifiez les codes de langue BCP-47 dans `language_codes` pour améliorer la précision de la transcription (voir [Langues acceptées](#supported-languages)) :

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## Vocabulaire personnalisé

Vous pouvez orienter le modèle vocal vers des mots inhabituels, du jargon technique, des noms de marques ou des noms propres. Fournissez jusqu'à 1 000 termes dans le tableau `custom_vocabulary` (les meilleurs résultats sont généralement obtenus avec un maximum de 100 termes) :

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Identification du locuteur

L'identification des locuteurs permet d'identifier les différentes voix dans l'enregistrement et d'attribuer un identifiant à chaque segment, comme `spk_1` ou `spk_2`. Jusqu'à huit locuteurs sont pris en charge (l'attribution pour trois locuteurs ou plus est expérimentale).

Activez l'identification des locuteurs en configurant `diarization_mode` dans `mode` :

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## Codes temporels au niveau du mot

Les codes temporels au niveau du mot fournissent des décalages de début et de fin exacts pour chaque mot reconnu dans le flux audio.

Activez les codes temporels en configurant `timestamp_granularities` dans `mode` :

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

Vous pouvez combiner `diarization_mode` et `timestamp_granularities` dans `mode` pour recevoir à la fois les identifiants des intervenants et les horodatages au niveau du mot :

### Python

```
generation_config = {
    "transcription_config": {
        "custom_vocabulary": ["Gemini"],
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    custom_vocabulary: ["Gemini"],
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "custom_vocabulary": ["Gemini"],
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## Modes de transcription

Gemini 3.5 Transcribe est compatible avec deux modes de transcription via le paramètre `mode` :

- **`verbatim` (par défaut)** : renvoie une transcription exacte mot pour mot de tout ce qui a été dit, en conservant les mots de remplissage bruts ("euh", "enfin", "genre", "tu vois"), les répétitions, les pauses et les faux départs. Les codes temporels et l'identification du locuteur sont configurés dans ce mode (`{"type": "verbatim", ...}`).
- **`smart` (Transcription intelligente)** : optimise la transcription pour la lecture en appliquant un post-traitement intelligent :
  - **Suppression des hésitations** : élimine les mots de remplissage, les bégaiements et les faux départs.
  - **Corrections spontanées** : les corrections orales sont résolues directement (par exemple, *"Rendez-vous mardi, non, mercredi à 14h"* devient *"Rendez-vous mercredi à 14h"*).
  - **Mise en forme structurée automatique** : structure automatiquement les pensées exprimées en paragraphes, listes numérotées, listes à puces, dates, devises et nombres mis en forme.
  - **Nettoyage grammatical** : applique une ponctuation, une mise en forme des phrases et un flux naturels.

| Audio parlé | Résultat de la fonction `verbatim` | Résultat de la fonction `smart` (transcription intelligente) |
| --- | --- | --- |
| "Euh, pour la réunion, je pense qu'on devrait inviter Alice et, non, Bob et Carol." | "Euh, pour la réunion, je pense qu'on devrait inviter Alice, non, Bob et Carol." | "Pour la réunion, je pense que nous devrions inviter Bob et Carol." |
| "First item review budget second item finalize timeline third item send recap" (Examine le budget en premier, finalise le calendrier en deuxième, envoie le récapitulatif en troisième) | "examine le premier élément, vérifie le budget du deuxième élément, finalise le calendrier du troisième élément, envoie le récapitulatif" | "1. Vérifiez le budget. 2. Finalisez la timeline 3. Envoyer le récapitulatif" |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## Analyser la transcription

Le texte complet de la transcription est renvoyé dans `interaction.output_text`.

Lorsque `timestamp_granularities` ou `diarization_mode` est activé, l'API renvoie également des annotations détaillées au niveau des mots, associées au contenu de l'interaction.

Voici comment extraire et parcourir les codes temporels des mots et les tours de parole :

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### JavaScript

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.450s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.850s"
            }
          ]
        }
      ]
    }
  ]
}
```

## Langues disponibles

Les langues et les codes de langue BCP-47 suivants sont compatibles avec Gemini 3.5 Transcribe :

| Langue | Code BCP-47 | Langue | Code BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japonais | `ja-JP` |
| Amharique | `am-ET` | Javanais | `jv-ID` |
| Arabe (Égypte) | `ar-EG` | Créole capverdien | `kea-CV` |
| Arménien | `hy-AM` | Kannada | `kn-IN` |
| Assamais | `as-IN` | Kazakh | `kk-KZ` |
| Azéri | `az-AZ` | Coréen | `ko-KR` |
| Biélorusse | `be-BY` | Kirghiz | `ky-KG` |
| Bengali (Bangladesh) | `bn-BD` | Letton | `lv-LV` |
| Bengali (Inde) | `bn-IN` | Lingala | `ln-CD` |
| Bosniaque | `bs-BA` | Lituanien | `lt-LT` |
| Bulgare | `bg-BG` | Macédonien | `mk-MK` |
| Bulgare (aroumain) | `rup-BG` | Malaisien | `ms-MY` |
| Birman | `my-MM` | Malayalam | `ml-IN` |
| Cantonais (traditionnel) | `yue-Hant-HK` | Maltais | `mt-MT` |
| Catalan | `ca-ES` | Chinois mandarin (simplifié) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Khmer central | `km-KH` | Mongol | `mn-MN` |
| Croate | `hr-HR` | Népalais | `ne-NP` |
| Tchèque | `cs-CZ` | Norvégien | `nb-NO` |
| Danois | `da-DK` | Oriya | `or-IN` |
| Néerlandais | `nl-NL` | Polonais | `pl-PL` |
| Anglais (Grande-Bretagne) | `en-GB` | Portugais (Brésil) | `pt-BR` |
| Anglais (Inde) | `en-IN` | Portugais (Portugal) | `pt-PT` |
| Anglais (États-Unis) | `en-US` | Panjabi | `pa-IN` |
| Estonien | `et-EE` | Panjabi (écriture gurmukhī) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Roumain | `ro-RO` |
| Tagalog | `fil-PH` | Russe | `ru-RU` |
| Finnois | `fi-FI` | Serbe | `sr-RS` |
| Français | `fr-FR` | Sindhi (écriture arabe) | `sd-Arab-IN` |
| Galicien | `gl-ES` | Slovaque | `sk-SK` |
| Géorgien | `ka-GE` | Slovène | `sl-SI` |
| Allemand | `de-DE` | Espagnol (Amérique latine) | `es-419` |
| Grec | `el-GR` | Espagnol (États-Unis) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Haoussa | `ha-NG` | Suédois | `sv-SE` |
| Hébreu | `he-IL` | Tadjik | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Hongrois | `hu-HU` | Thaï | `th-TH` |
| Islandais | `is-IS` | Turc | `tr-TR` |
| Anglais (Inde) | `en-IN` | Ukrainien | `uk-UA` |
| Indonésien | `id-ID` | Ouzbek | `uz-UZ` |
| Italien | `it-IT` | Vietnamien | `vi-VN` |

## Formats audio acceptés

Gemini 3.5 Transcribe est compatible avec les types MIME de format audio suivants :

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF – `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 – `audio/l16`
- Opus – `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Pour obtenir la liste complète des types MIME et des schémas de paramètres acceptés, consultez la [documentation de référence de l'API Interactions](https://ai.google.dev/api/interactions-api?hl=fr#Resource:Content).

## Référence de paramètre

Configurez la transcription en définissant les champs de l'objet `transcription_config` dans `generation_config` :

| Champ | Type | Description |
| --- | --- | --- |
| `language_codes` | Tableau de chaînes | Codes de langue BCP-47 (par exemple, `["en-US"]`). S'ils sont omis ou vides (`[]`), le modèle détecte automatiquement la langue et gère le changement de code. |
| `custom_vocabulary` | Tableau de chaînes | Jusqu'à 1 000 termes, acronymes ou noms propres personnalisés pour orienter la reconnaissance vocale. |
| `mode` | Objet ou chaîne | Configuration du mode de transcription. Accepte `"smart"` ou un objet en mode verbatim (`{"type": "verbatim", ...}`). La transcription verbatim est définie par défaut. |
| `mode.type` | Chaîne | *(Mode verbatim uniquement)* Identifiant du mode. Toujours défini sur `"verbatim"`. |
| `mode.timestamp_granularities` | Tableau de chaînes | *(Mode verbatim uniquement)* : précision des codes temporels à renvoyer. Transmettez `["word"]` pour activer les décalages de début et de fin des mots. |
| `mode.diarization_mode` | Chaîne | *(Mode verbatim uniquement)* : mode de diarisation. Transmettez `"speaker"` pour identifier les différents intervenants et leur attribuer un libellé. |

## Bonnes pratiques

- **Fournissez un son clair** : assurez-vous que les enregistrements audio ont une séparation vocale claire et évitez les découpages importants.
- **Fournissez des indications de langue si vous les connaissez** : si vous connaissez la langue de l'audio à l'avance, spécifiez `language_codes` pour maximiser la précision.
- **Ciblez un vocabulaire personnalisé** : n'incluez que des termes de domaine distincts, des noms de marques ou des noms propres dans `custom_vocabulary`, plutôt que des mots courants.
- **Utilisez l'API Files pour les enregistrements volumineux** : pour les fichiers de plus de quelques secondes, importez-les à l'aide de `client.files.upload` et transmettez l'URI de fichier renvoyé au modèle.

## Limites

- **Durée de l'audio** : les requêtes unitaires standards sont compatibles avec les fichiers audio d'une durée maximale d'une heure. Le traitement audio est limité à 30 minutes lorsque des fonctionnalités telles que la segmentation des locuteurs ou les codes temporels au niveau des mots sont activées.
- **Codes temporels au niveau du mot** : l'activation des codes temporels au niveau du mot peut dégrader la précision globale de la transcription.
- **Identification du locuteur** : l'identification du locuteur est compatible avec un maximum de huit locuteurs. L'attribution des locuteurs pour trois locuteurs ou plus est une fonctionnalité expérimentale.
- **Vocabulaire personnalisé** : vous pouvez fournir jusqu'à 1 000 termes dans `custom_vocabulary`, mais les meilleurs résultats sont généralement obtenus avec un maximum de 100 termes.
- **Compatibilité des modes** : la transcription intelligente (`"smart"`) ne peut pas être combinée avec `timestamp_granularities` ni `diarization_mode`.

## Étape suivante

- Diffusez de l'audio en temps réel avec le [guide de transcription en direct](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=fr) à l'aide de l'API Live.
- Explorez la [compréhension audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr) pour analyser, résumer ou interroger des contenus audio.
- Découvrez comment synthétiser des contenus audio à partir de texte à l'aide de [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).
- Consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-3.5-transcribe) pour connaître les tarifs des modèles et les limites de jetons.
- Consultez le guide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) pour savoir comment importer et gérer des fichiers multimédias.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/08/28 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/08/28 (UTC)."],[],[]]
