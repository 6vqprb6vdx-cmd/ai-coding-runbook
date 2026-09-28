---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=fr
fetched_at: 2026-09-28T06:19:15.902451+00:00
title: "Transcription en direct avec l'API Gemini\u00a0Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Transcription en direct avec l'API Gemini Live

L'API Gemini Live permet la transcription instantanée de la parole en texte à faible latence à l'aide du modèle [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=fr). En vous connectant à l'API Live via des WebSockets ou en utilisant le SDK Google Gen AI, vous pouvez diffuser en continu des entrées audio et recevoir des transcriptions textuelles incrémentielles en temps réel au fur et à mesure que la parole est prononcée.

[Essayer la transcription en direct dans Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=fr)
[Ouvrir le cookbook Colabcode](https://github.com/google-gemini/cookbook)
[Utiliser les compétences de l'agent de programmationterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr#gemini-live-api-dev)

En tirant parti de l'API Gemini Live, les plates-formes de développement telles que [Agora](https://docs.agora.io/en/ai/models/asr/gemini), [Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration), [LiveKit](https://docs.livekit.io/agents/models/stt/gemini/), [Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google), [Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) et [Vision Agents](https://visionagents.ai/integrations/stt/gemini) permettent aux développeurs de créer et de déployer facilement des interfaces vocales hautes performances. Ces plates-formes gèrent en coulisses une infrastructure complexe de streaming multimédia en temps réel, ce qui permet aux développeurs de se concentrer entièrement sur la conception de l'expérience utilisateur.

## Agent réel ou transcription en direct

Bien que les deux utilisent la connexion de streaming bidirectionnel de l'API Live, la transcription instantanée fonctionne comme un pipeline de reconnaissance vocale dédié à faible latence plutôt que comme un agent conversationnel.

| Fonctionnalité | Agent en direct | Transcription en direct |
| --- | --- | --- |
| **Rôle principal** | Assistant conversationnel qui écoute, réfléchit et répond. | Pipeline de reconnaissance vocale en temps réel qui transcrit l'audio entrant. |
| **Modalité de réponse** | Texte et audio parlés (`response_modalities=["AUDIO"]`). | Transcriptions de texte en streaming (`response_modalities=["TEXT"]`) |
| **Style d'interaction** | Dialogue au tour par tour avec détection des pauses et des interruptions. | Traitement continu du flux à mesure que l'orateur parle. |
| **Fonctionnalités disponibles** | Appel de fonction, recherche Google, instructions système. | Pondération du langage (`custom_vocabulary`), détection de la langue, VAD manuelle et hybride, transcription intelligente. |
| **Flux d'entrée** | Multimodal : audio, vidéo, images, texte. | Entrée audio (PCM 16 bits brut). |

## Premiers pas

Les exemples suivants montrent comment ouvrir une session de streaming bidirectionnel avec `gemini-3.5-transcribe-live` et recevoir des transcriptions en temps réel.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## Transcriptions provisoires et définitives

Lorsque des flux audio sont transmis à l'API Live, le serveur émet deux champs de transcription complémentaires dans `server_content` :

- **`interim_input_transcription`** : hypothèses partielles spéculatives à faible latence mises à jour pendant que l'orateur parle. Ces mises à jour partielles sont rapides et ne prennent que quelques instants. Utilisez `interim_input_transcription` pour afficher des sous-titres ou des aperçus de sous-titres responsifs dans l'UI en direct.
- **`input_transcription`** : transcription finalisée émise lorsque l'orateur fait une pause, que le tour est terminé ou que la parole est finalisée. Une fois émis, ce texte représente la transcription faisant autorité du modèle pour ce segment de parole. En mode transcription intelligente, cela inclut la réponse nettoyée et mise en forme.

L'exemple suivant montre comment afficher les résultats partiels intermédiaires du flux et valider les transcriptions finales :

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## Envoi de l'audio

Diffusez des blocs audio sur la connexion active en tant qu'audio PCM 16 bits brut.

- **Format audio** : PCM 16 bits brut à 16 kHz (mono, little-endian).
- **Taille des blocs** : envoyez l'audio par blocs de 100 ms (de 1 024 à 2 048 frames).
- **Type MIME** : `audio/pcm;rate=16000` (ou la fréquence d'échantillonnage correspondante).

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## Fonctionnalités de transcription

### Détection automatique de la langue

Par défaut, si vous omettez `language_codes` ou définissez `language_codes=[]`, l'identification automatique de la langue est activée. Le modèle détecte de manière dynamique la langue parlée dans les énoncés, y compris les conversations multilingues et le changement de code.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Indicateur de langue spécifique

Fournissez des codes de langue BCP-47 explicites (par exemple, `["es-ES"]` pour l'espagnol ou `["fr-FR"]` pour le français) afin de favoriser la reconnaissance de langues spécifiques (voir [Langues acceptées](#supported-languages)).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Pondération du vocabulaire personnalisé

Fournissez une liste de 1 000 expressions, noms propres, noms de marques ou termes techniques maximum dans `custom_vocabulary` pour orienter la reconnaissance vocale vers une terminologie spécifique (les meilleurs résultats sont généralement obtenus avec un maximum de 100 termes).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Transcription intelligente

Configurez la mise en forme de la transcription à l'aide du paramètre `mode` dans `input_audio_transcription` :

- **`VERBATIM` (par défaut)** : produit une transcription littérale exacte de tout ce qui est dit, en conservant les mots de remplissage bruts ("euh", "hum", "genre"), les répétitions et les faux départs.
- **`SMART` (Transcription intelligente)** : nettoie et structure la transcription pour la rendre plus lisible :

  - **Suppression des hésitations** : supprime les mots de remplissage, les bégaiements et les faux départs.
  - **Autocorrection en ligne** : corrige naturellement les erreurs de prononciation.
  - **Mise en forme structurée** : met automatiquement en forme les listes, les puces, les nombres, les dates et les sauts de paragraphe.
  - **Grammaire et casse** : applique une mise en forme naturelle des majuscules et de la ponctuation.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## Stratégies de détection de l'activité vocale (VAD)

### Détection automatique de l'activité vocale (par défaut)

Par défaut, la détection automatique de l'activité vocale côté serveur détecte quand un locuteur commence et arrête de parler.

### VAD hybride

La [détection d'activité vocale hybride](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=fr#hybrid-vad) combine la détection automatique du début de la parole côté serveur et la détection de la fin de la parole côté client pour finaliser les tours de parole sans latence :

1. **La détection automatique de l'activité vocale côté serveur reste activée** pour détecter précisément le début des paroles avec un remplissage audio de préfixe, ce qui évite la troncature du premier mot.
2. **La VAD côté client détecte le silence** : lorsqu'une VAD locale sur l'appareil détecte que l'orateur a cessé de parler, le client envoie immédiatement un signal `audio_stream_end`.
3. **Finalisation rapide** : le serveur traite `audio_stream_end` comme une invite de finalisation immédiate du tour de parole, en ignorant le délai d'attente de silence par défaut côté serveur et en renvoyant la transcription finalisée avec une latence minimale.
4. **Solution de secours** : si la VAD côté client ne se déclenche pas, la VAD côté serveur sert de solution de secours automatique.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### VAD manuelle (appuyer pour parler)

Pour les interfaces de talkie-walkie ou les boutons "appuyer pour parler", désactivez complètement la VAD automatique et contrôlez explicitement les limites des tours de parole à l'aide de `activity_start` et `activity_end` :

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## Jetons éphémères dans les applications clientes

Pour les applications client-serveur (comme les applications mobiles ou Web qui diffusent du contenu directement depuis un micro), utilisez des [jetons éphémères](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=fr) pour éviter d'exposer votre clé API dans le code client.

Créez un jeton éphémère contraint sur votre serveur avant d'initier la connexion client :

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## Langues disponibles

Les langues et codes de langue BCP-47 suivants sont compatibles avec Gemini 3.5 Transcribe Live :

| Langue | Code BCP-47 | Langue | Code BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japonais | `ja-JP` |
| Amharique | `am-ET` | Javanais | `jv-ID` |
| Arabe (Égypte) | `ar-EG` | Kabuverdianu | `kea-CV` |
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

## Référence de paramètre

Configurez la transcription instantanée à l'aide des champs de `input_audio_transcription` et `realtime_input_config` :

| Paramètre | Type | Description |
| --- | --- | --- |
| `language_codes` | Tableau de chaînes | Codes de langue BCP-47 (par exemple, `["en-US"]`). S'ils sont omis ou vides (`[]`), le modèle détecte automatiquement la langue et gère la parole multilingue. |
| `custom_vocabulary` | Tableau de chaînes | Jusqu'à 1 000 termes, acronymes, noms de marques ou noms propres personnalisés pour orienter la reconnaissance vocale. |
| `mode` | Chaîne | Mode Transcription : `"VERBATIM"` (par défaut) ou `"SMART"` (Transcription intelligente). Lorsqu'il est défini sur `"SMART"`, le modèle supprime les mots de remplissage, met en forme les listes et corrige les hésitations. |
| `automatic_activity_detection.disabled` | Booléen | Définissez sur `true` pour désactiver la détection automatique de l'activité vocale et envoyer manuellement les signaux `activityStart` et `activityEnd`. |

### Champs de réponse du serveur

| Champ | Description |
| --- | --- |
| `server_content.interim_input_transcription` | Hypothèse de transcription partielle provisoire à faible latence émise en continu pendant que l'utilisateur parle. |
| `server_content.input_transcription` | Transcription d'entrée définitive et faisant autorité, émise à la fin d'un tour de parole. |

## Limites

- **Durée de la session** : les sessions de transcription instantanée permettent la diffusion en continu pendant 10 minutes maximum.
- **Identification du locuteur** : l'identification du locuteur n'est pas disponible dans les sessions de streaming en direct. Pour la segmentation des locuteurs, utilisez le point de terminaison [Transcription audio](https://ai.google.dev/gemini-api/docs/transcribe?hl=fr#speaker-diarization) non en streaming.
- **Codes temporels au niveau du mot** : les codes temporels au niveau du mot ne sont pas compatibles avec l'API Live. L'API Live émet des codes temporels au niveau de l'énoncé (`interim_input_transcription` et `input_transcription`).
- **Vocabulaire personnalisé** : vous pouvez fournir jusqu'à 1 000 termes dans `custom_vocabulary`, mais les meilleurs résultats sont généralement obtenus avec un maximum de 100 termes.
- **Compatibilité des modes** : la transcription intelligente (`"mode": "SMART"`) supprime les mots de remplissage et met en forme le texte en fonction de l'intention, mais ne peut pas être combinée aux annotations de mots.

## Étape suivante

- Consultez la [documentation Gemini Transcribe](https://ai.google.dev/gemini-api/docs/transcribe?hl=fr) pour les fichiers audio non diffusés en streaming.
- Consultez la [présentation de l'API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr) pour les agents vocaux conversationnels.
- Consultez le [guide de la traduction instantanée](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=fr) pour la traduction vocale en temps réel.
- Consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-3.5-transcribe-live) pour connaître les tarifs de l'API Live Stream.
- Consultez le [guide des fonctionnalités de l'API Live](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/10 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/10 (UTC)."],[],[]]
