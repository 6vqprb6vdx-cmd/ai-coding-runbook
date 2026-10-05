---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=it
fetched_at: 2026-10-05T06:32:56.934088+00:00
title: "Replica della voce \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Replica della voce

La replica vocale consente di replicare le caratteristiche vocali di un oratore da un breve campione audio utilizzando l'endpoint Voci dell'API Gemini (`POST /v1beta/voices`). Sia [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it) (`gemini-3.8-flash-tts`) sia [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it) (`gemini-3.8-flash-lite-tts`) supportano la replica vocale.

Il modo più rapido per replicare, verificare il consenso e fare l'audizione di una voce replicata è
con l'esperienza interattiva di **Replica della voce** in
[Google AI Studio](https://aistudio.google.com/generate-speech?hl=it). Puoi registrare
o caricare clip di riferimento e di consenso direttamente nel browser, visualizzare in anteprima la
voce e copiare l'`voice_...`ID risultante direttamente nel codice
dell'applicazione.

[Prova in Google AI Studio](https://aistudio.google.com/generate-speech?hl=it)

![Flusso di lavoro di replica vocale](https://ai.google.dev/static/gemini-api/docs/images/voice-replication-overview.svg?hl=it)

## Modalità di archiviazione stateful e stateless

La replica vocale supporta due modalità di archiviazione durante le chiamate `voices.create`
(`POST /v1beta/voices`), con l'archiviazione stateful attivata per impostazione predefinita:

- **Archiviazione con stato (`store=True`, predefinita consigliata)**: Google archivia il tuo profilo vocale verificato nel tuo progetto e restituisce un `voice_id` (`replicated_voice.id`, ad esempio `voice_abc123...`) leggero e persistente. Puoi passare questo `voice_id` tra le richieste e gestirlo con `voices.list()`, `voices.get()` e `voices.delete()`.
- **Chiavi stateless gestite dal client (`store=False`, facoltativo):** per i carichi di lavoro
  che richiedono la persistenza lato server zero dei profili vocali biometrici, imposta
  `store=False`. L'API restituisce un `voice_key` criptato e autonomo
  (`replicated_voice.key`, a partire da `voicekey_...`) che la tua applicazione
  memorizza localmente e trasmette direttamente nelle richieste di sintesi.

| Modalità di archiviazione | Identificatore | Limite di progetti | Conservazione (TTL) |
| --- | --- | --- | --- |
| **Voci stateful** (`store=True`) | `voice_...` | **200 voci per progetto** (condivise tra le voci richieste e replicate) | **1 anno** |
| **Chiavi vocali stateless** (`store=False`) | `voicekey_...` | Gestita dal cliente | **7 giorni** |

## Requisiti relativi all'audio e ai requisiti per il consenso

Ogni richiesta di replica di `CreateVoice` richiede due registrazioni audio di persone reali
dello **stesso oratore adulto** (consigliato WAV mono a 16 bit e 24 kHz):

1. **Audio di riferimento (`source_audio`)**: un clip di 10-30 secondi di voce pulita e naturale
   dell'oratore di cui vuoi replicare la voce.
2. **Audio di consenso (`consent_audio`):** una registrazione della stessa persona che recita chiaramente la dichiarazione di consenso obbligatoria in una delle [lingue supportate](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=it#consent-phrases-by-language) (ad esempio, in inglese):
   > *"Sono il proprietario di questa voce e acconsento all'utilizzo di questa voce da parte di Google per creare un modello vocale sintetico".*

## Crea una voce replicata (predefinita con stato)

Utilizza l'SDK Google GenAI (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) o l'API REST
con `store=True` per creare e salvare un profilo vocale replicato nel tuo progetto:

### Python

```
import base64
from google import genai

client = genai.Client()

with open("reference_speaker.wav", "rb") as f:
    source_b64 = base64.b64encode(f.read()).decode("utf-8")

with open("speaker_consent.wav", "rb") as f:
    consent_b64 = base64.b64encode(f.read()).decode("utf-8")

# Create a persistent replicated voice (store=True)
replicated_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "replicated",
        "display_name": "Custom Replicated Speaker",
        "replicated": {
            "source_audio": {
                "mime_type": "audio/wav",
                "data": source_b64,
            },
            "consent_audio": {
                "mime_type": "audio/wav",
                "data": consent_b64,
            },
        },
    },
)

print(f"Created voice ID: {replicated_voice.id}")
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const sourceB64 = fs.readFileSync("reference_speaker.wav").toString("base64");
const consentB64 = fs.readFileSync("speaker_consent.wav").toString("base64");

// Create a persistent replicated voice (store: true)
const replicatedVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "replicated",
    display_name: "Custom Replicated Speaker",
    replicated: {
      source_audio: {
        mime_type: "audio/wav",
        data: sourceB64,
      },
      consent_audio: {
        mime_type: "audio/wav",
        data: consentB64,
      },
    },
  },
});

console.log(`Created voice ID: ${replicatedVoice.id}`);
```

### REST

```
SOURCE_B64=$(base64 -w 0 reference_speaker.wav)
CONSENT_B64=$(base64 -w 0 speaker_consent.wav)

curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{
    \"store\": true,
    \"voice\": {
      \"model\": \"gemini-3.8-flash-tts\",
      \"type\": \"replicated\",
      \"display_name\": \"Custom Replicated Speaker\",
      \"replicated\": {
        \"source_audio\": {
          \"mime_type\": \"audio/wav\",
          \"data\": \"$SOURCE_B64\"
        },
        \"consent_audio\": {
          \"mime_type\": \"audio/wav\",
          \"data\": \"$CONSENT_B64\"
        }
      }
    }
  }"
```

## Sintetizzare il parlato con la tua voce replicata

Passa il valore `id` (`voice_...`) restituito in `voiceConfig.voice` quando chiami
`generateContent`:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Hello! This audio was synthesized using a replicated"
                " speaker voice."
            ),
            "speech_metadata": {"style": "warm and conversational"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": replicated_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("replicated_speech.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Hello! This audio was synthesized using a replicated speaker voice.",
      speechMetadata: { style: "warm and conversational" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: replicatedVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("replicated_speech.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Hello! This audio was synthesized using a replicated speaker voice.",
        "speech_metadata": {
          "style": "warm and conversational"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_REPLICATED_VOICE_ID"
        }
      }
    }
  }'
```

## Gestire le voci replicate archiviate

Se create con `store=True`, le voci replicate possono essere elencate, filtrate, ispezionate ed eliminate tramite l'API Voices (vedi [Libreria di voci estesa e filtri](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#voice-library) per tutti i parametri di filtro):

### Python

```
from google import genai

client = genai.Client()

# List stored replicated voices in your project
response = client.voices.list(type_=["replicated"])
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=replicated_voice.id)

# Delete a stored replicated voice
client.voices.delete(id=replicated_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored replicated voices in your project
const response = await ai.voices.list({ type: ["replicated"] });
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(replicatedVoice.id);

// Delete a stored replicated voice
await ai.voices.delete(replicatedVoice.id);
```

### REST

```
# List stored replicated voices in your project
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=replicated"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_REPLICATED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored replicated voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_REPLICATED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Opzione: chiavi vocali stateless gestite dal client (`store=False`)

Se la tua applicazione non richiede la persistenza lato server dei profili vocali, imposta
`store=False` quando crei la voce replicata. L'API restituisce un `voice_key` (`replicated_voice.key`, a partire da `voicekey_...`) criptato che memorizzi lato client e trasmetti direttamente in `voiceConfig.voice`:

### Python

```
import base64
from google import genai

client = genai.Client()

with open("reference_speaker.wav", "rb") as f:
    source_b64 = base64.b64encode(f.read()).decode("utf-8")

with open("speaker_consent.wav", "rb") as f:
    consent_b64 = base64.b64encode(f.read()).decode("utf-8")

# Create a stateless client-managed voice key (store=False)
replicated_voice = client.voices.create(
    store=False,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "replicated",
        "replicated": {
            "source_audio": {"mime_type": "audio/wav", "data": source_b64},
            "consent_audio": {"mime_type": "audio/wav", "data": consent_b64},
        },
    },
)

# Pass replicated_voice.key ("voicekey_...") directly in voice_config
response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Hello! This audio uses a stateless client-managed voice key.",
            "speech_metadata": {"style": "warm and conversational"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": replicated_voice.key}
        },
    },
)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const sourceB64 = fs.readFileSync("reference_speaker.wav").toString("base64");
const consentB64 = fs.readFileSync("speaker_consent.wav").toString("base64");

// Create a stateless client-managed voice key (store: false)
const replicatedVoice = await ai.voices.create({
  store: false,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "replicated",
    replicated: {
      source_audio: { mime_type: "audio/wav", data: sourceB64 },
      consent_audio: { mime_type: "audio/wav", data: consentB64 },
    },
  },
});

// Pass replicatedVoice.key ("voicekey_...") directly in voiceConfig
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Hello! This audio uses a stateless client-managed voice key.",
      speechMetadata: { style: "warm and conversational" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: replicatedVoice.key },
    },
  },
});
```

### REST

```
SOURCE_B64=$(base64 -w 0 reference_speaker.wav)
CONSENT_B64=$(base64 -w 0 speaker_consent.wav)

curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{
    \"store\": false,
    \"voice\": {
      \"model\": \"gemini-3.8-flash-tts\",
      \"type\": \"replicated\",
      \"replicated\": {
        \"source_audio\": {\"mime_type\": \"audio/wav\", \"data\": \"$SOURCE_B64\"},
        \"consent_audio\": {\"mime_type\": \"audio/wav\", \"data\": \"$CONSENT_B64\"}
      }
    }
  }"
```

## Frasi di consenso supportate per lingua

L'audio del consenso deve recitare chiaramente la dichiarazione esatta in una delle 30 impostazioni internazionali delle lingue supportate:

| Lingua | Impostazioni internazionali (`lang_id`) | Dichiarazione di consenso letterale |
| --- | --- | --- |
| **Arabo** | `ar-XA` | أنا مالك هذا الصوت وأوافق على أن تستخدم Google هذا الصوت لإنشاء نموذج صوتي اصطناعي. |
| **Bengalese** | `bn-IN` | আমি এই ভয়েসের মালিক এবং আমি একটি সিন্থেটিক ভয়েস মডেল তৈরি করতে এই ভয়েস ব্যবহার করে Google-এর সাথে সম্মতি দিচ্ছি। |
| **Cinese (semplificato)** | `zh-CN` | 我是此声音的拥有者并授权谷歌使用此声音创建语音合成模型 |
| **Olandese** | `nl-NL` | Ik ben de eigenaar van deze stem en ik geef Google toestemming om deze stem te gebruiken om een synthetisch stemmodel te maken. |
| **Italiano** | `en-US` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **English (UK)** | `en-GB` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **Inglese (India)** | `en-IN` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **Inglese (Australia)** | `en-AU` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **Francese (Francia)** | `fr-FR` | Je suis le propriétaire de cette voix et j'autorise Google à utiliser cette voix pour créer un modèle de voix synthétique. |
| **Francese (Canada)** | `fr-CA` | Je suis le propriétaire de cette voix et j'autorise Google à utiliser cette voix pour créer un modèle de voix synthétique. |
| **Tedesco** | `de-DE` | Ich bin der Eigentümer dieser Stimme und bin damit einverstanden, dass Google diese Stimme zur Erstellung eines synthetischen Stimmmodells verwendet. |
| **Gujarati** | `gu-IN` | હું આ વોઈસનો માલિક છું અને સિન્થેટિક વોઈસ મોડલ બનાવવા માટે આ વોઈસનો ઉપયોગ કરીને google ને હું સંમતિ આપું છું |
| **Hindi** | `hi-IN` | मैं इस आवाज का मालिक हूं और मैं सिंथेटिक आवाज मॉडल बनाने के लिए Google को इस आवाज का उपयोग करने की सहमति देता हूं |
| **Indonesiano** | `id-ID` | Saya pemilik suara ini dan saya menyetujui Google menggunakan suara ini untuk membuat model suara sintetis. |
| **Italiano** | `it-IT` | Sono il proprietario di questa voce e acconsento che Google la utilizzi per creare un modello di voce sintetica. |
| **Giapponese** | `ja-JP` | 私はこの音声の所有者であり、Googleがこの音声を使用して音声合成モデルを作成することを承認します。 |
| **Kannada** | `kn-IN` | ನಾನು ಈ ಧ್ವನಿಯ ಮಾಲಿಕ ಮತ್ತು ಸಂಶ್ಲೇಷಿತ ಧ್ವನಿ ಮಾದರಿಯನ್ನು ರಚಿಸಲು ಈ ಧ್ವನಿಯನ್ನು ಬಳಸಿಕೊಂಡುಗೂಗಲ್ ಗೆ ನಾನು ಸಮ್ಮತಿಸುತ್ತೇನೆ. |
| **Coreano** | `ko-KR` | 나는 이 음성의 소유자이며 구글이 이 음성을 사용하여 음성 합성 모델을 생성할 것을 허용합니다. |
| **Malayalam** | `ml-IN` | ഈ ശബ്ദത്തിന്റെ ഉടമ ഞാനാണ്, ഒരു സിന്തറ്റിക് വോയ്സ് മോഡൽ സൃഷ്ടിക്കാൻ ഈ ശബ്ദം ഉപയോഗിക്കുന്നതിന് ഞാൻ Google-ന് സമ്മതം നൽകുന്നു. |
| **Marathi** | `mr-IN` | मी या आवाजाचा मालक आहे आणि सिंथेटिक व्हॉइस मॉडेल तयार करण्यासाठी हा आवाज वापरण्यासाठी मी Google ला संमती देतो |
| **Polacco** | `pl-PL` | Jestem właścicielem tego głosu i wyrażam zgodę na wykorzystanie go przez Google w celu utworzenia syntetycznego modelu głosu. |
| **Portoghese (Brasile)** | `pt-BR` | Eu sou o proprietário desta voz e autorizo o Google a usá-la para criar um modelo de voz sintética. |
| **Russo** | `ru-RU` | Я являюсь владельцем этого голоса и даю согласие Google на использование этого голоса для создания модели синтетического голоса. |
| **Spagnolo (Spagna)** | `es-ES` | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética. |
| **Spanish (US)** | `es-US` | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética. |
| **Tamil** | `ta-IN` | நான் இந்த குரலின் உரிமையாளர் மற்றும் செயற்கை குரல் மாதிரியை உருவாக்க இந்த குரலை பயன்படுத்த குகல்க்கு நான் ஒப்புக்கொள்கிறேன். |
| **Telugu** | `te-IN` | నేను ఈ వాయిస్ యజమానిని మరియు సింతటిక్ వాయిస్ మోడల్ ని రూపొందించడానికి ఈ వాయిస్ ని ఉపయోగించడానికి googleకి నేను సమ్మతిస్తున్నాను. |
| **Thai** | `th-TH` | ฉันเป็นเจ้าของเสียงนี้ และฉันยินยอมให้ Google ใช้เสียงนี้เพื่อสร้างแบบจำลองเสียงสังเคราะห์ |
| **Turco** | `tr-TR` | Bu sesin sahibi benim ve Google'ın bu sesi kullanarak sentetik bir ses modeli oluşturmasına izin veriyorum. |
| **Vietnamita** | `vi-VN` | Tôi là chủ sở hữu giọng nói này và tôi đồng ý cho Google sử dụng giọng nói này để tạo mô hình giọng nói tổng hợp. |

## Best practice per la registrazione dell'audio di riferimento

- **Registra in un ambiente silenzioso**:riduci al minimo l'eco della stanza, il rumore di fondo,
  la musica e le voci sovrapposte.
- **Corrispondenza delle condizioni di registrazione**:registra sia `source_audio` che
  `consent_audio` sullo stesso microfono nella stessa impostazione acustica in modo che il
  controllo della verifica dell'oratore vada a buon fine in modo affidabile.
- **Converti in WAV mono a 24 kHz**:per ottenere risultati ottimali, ricampiona l'audio di input in
  WAV PCM mono a 24 kHz e 16 bit prima della codifica.

## Passaggi successivi

- Scopri come creare persona personalizzate a partire da descrizioni testuali in
  [Progettazione vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it).
- Scopri lo stile a livello di turno, i tag in linea e il dialogo con più relatori nella
  [guida Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-24 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-24 UTC."],[],[]]
