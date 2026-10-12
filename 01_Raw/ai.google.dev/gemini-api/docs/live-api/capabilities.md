---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=it
fetched_at: 2026-10-12T06:57:29.979966+00:00
title: "Guida alle funzionalit\u00e0 dell'API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida alle funzionalità dell'API Live

Si tratta di una guida completa che illustra le funzionalità e le configurazioni
disponibili con l'API Live.
Consulta la pagina [Inizia a utilizzare l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=it) per una panoramica e un codice campione per i casi d'uso comuni.

## Prima di iniziare

- **Acquisisci familiarità con i concetti di base**:se non l'hai ancora fatto,
  leggi prima la pagina [Inizia a utilizzare l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=it) .
  Verranno illustrati i principi fondamentali dell'API Live, il suo funzionamento e i diversi [approcci di implementazione](https://ai.google.dev/gemini-api/docs/live?hl=it#implementation-approach).
- **Prova l'API Live in AI Studio**:potrebbe esserti utile provare l'API Live in [Google AI Studio](https://aistudio.google.com/app/live?hl=it) prima di iniziare a creare. Per utilizzare l'API Live in Google AI Studio, seleziona **Stream**.

## Confronto modelli

La seguente tabella riepiloga le principali differenze tra i modelli
[Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=it),
[Gemini 3.8 Live con Ragionamento esteso](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=it) e
[Gemini 3.1 Flash Live (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=it):

| Funzionalità | Gemini 3.8 Live | Gemini 3.8 Live Extended Thinking | Gemini 3.1 Flash Live (anteprima) |
| --- | --- | --- | --- |
| **Consigliati per** | Opzione predefinita per la maggior parte delle esperienze con agenti vocali a bassa latenza. | Consigliato quando è necessario un ragionamento di base più approfondito. | Modello di anteprima legacy. Ti consigliamo di eseguire l'aggiornamento a [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=it). |
| **[Pensiero](#native-audio-output-thinking)** | Supportato (ragionamento intercalato). `thinkingLevel` non è supportato (ometti dalla configurazione). | Supportato. Ragionamento in background configurabile (`thinkingLevel`: `low`, `medium`, `high`; `minimal` non è supportato). | Utilizza `thinkingLevel` per controllare la profondità del pensiero con impostazioni come `minimal`, `low`, `medium` e `high`. Il valore predefinito è `minimal` per l'ottimizzazione della latenza più bassa. Consulta [Pensare in termini di API Live](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=it). |
| **[Ricezione della risposta](https://ai.google.dev/api/live?hl=it#bidigeneratecontentservercontent)** | Un singolo evento server può contenere più parti di contenuti contemporaneamente. | Un singolo evento server può contenere più parti di contenuti contemporaneamente. Quando il ragionamento asincrono è attivo, `turnComplete: true` non indica una sessione inattiva; utilizza `interaction_status` (`IN_PROGRESS` rispetto a `IDLE`). | Un singolo evento server può contenere più parti di contenuti contemporaneamente (ad esempio, `inlineData` e trascrizione). Assicurati che il codice elabori tutte le parti di ogni evento per evitare di perdere contenuti. |
| **[Contenuti del cliente](#incremental-updates)** | `send_client_content` è supportato durante l'intero ciclo di vita della sessione con ruoli espliciti (`user` o `model`). `turn_complete=true` interrompe in modo incondizionato la generazione. | `send_client_content` è supportato durante l'intero ciclo di vita della sessione con ruoli espliciti (`user` o `model`). `turn_complete=true` interrompe in modo incondizionato la generazione. | `send_client_content` è supportato durante l'intero ciclo di vita della sessione con ruoli espliciti (`user` o `model`). `turn_complete=true` interrompe in modo incondizionato la generazione. |
| **[Chiamata di funzione asincrona](https://ai.google.dev/gemini-api/docs/live-tools?hl=it#async-function-calling)** (`behavior: NON_BLOCKING`) | Supportato (impostazione predefinita). Imposta `behavior: NON_BLOCKING` o utilizza la modalità di blocco compatibile con le versioni precedenti con `behavior: BLOCKING`. La pianificazione delle funzioni (`SILENT`, `WHEN_IDLE`, `INTERRUPTED`) è supportata. | Supportato (solo asincrono). È supportata solo l'esecuzione di `NON_BLOCKING`. La modalità di blocco e la pianificazione delle funzioni non sono supportate. | Non supportato. La chiamata di funzione è solo sequenziale. Il modello non inizierà a rispondere finché non avrai inviato la risposta dello strumento. |

Per eseguire la migrazione a Gemini 3.8 Live, consulta la
[guida alla migrazione](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=it#migrating).
Per saperne di più su Thinking, consulta la
[guida a Thinking](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=it) e la
[guida all'upgrade](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=it#upgrading).

## Creazione di una connessione

Il seguente esempio mostra come creare una connessione con una chiave API:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.8-live"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Modalità di interazione

Le sezioni seguenti forniscono esempi e contesto di supporto per le diverse modalità di input e output disponibili nell'API Live.

### Invio di audio

L'audio deve essere inviato come dati PCM non elaborati (audio PCM non elaborato a 16 bit, 16 kHz, little-endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### Formati audio

I dati audio nell'API Live sono sempre PCM non elaborati, little-endian,
a 16 bit. L'uscita audio utilizza sempre una frequenza di campionamento di 24 kHz. L'audio di input
è nativamente a 16 kHz, ma l'API Live esegue il ricampionamento se necessario,
quindi è possibile inviare qualsiasi frequenza di campionamento. Per indicare la frequenza di campionamento dell'audio di input, imposta
il tipo MIME di ogni [blob](https://ai.google.dev/api/caching?hl=it#Blob) contenente audio su un valore
come `audio/pcm;rate=16000`.

### Ricezione dell'audio

Le risposte audio del modello vengono ricevute come blocchi di dati.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### Invio dell'SMS in corso…

Il testo può essere inviato utilizzando `send_realtime_input` (Python) o `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### Invio del video

I fotogrammi video vengono inviati come singole immagini (ad es.JPEG o PNG) a una frequenza fotogrammi specifica (max. 1 fotogramma al secondo).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### Aggiornamenti incrementali dei contenuti

Utilizza gli aggiornamenti incrementali per inviare l'input di testo, stabilire il contesto della sessione o
ripristinarlo. Per i contesti brevi, puoi inviare interazioni
passo passo per rappresentare la sequenza esatta di eventi:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

Per contesti più lunghi, è consigliabile fornire un riepilogo di un singolo messaggio per liberare
la finestra contestuale per le interazioni successive. Consulta la sezione [Ripresa delle sessioni](https://ai.google.dev/gemini-api/docs/live-session?hl=it#session-resumption) per un altro metodo di caricamento del contesto della sessione.

### Trascrizioni audio

Oltre alla risposta del modello, puoi anche ricevere le trascrizioni dell'uscita audio e dell'input audio.

Per attivare la trascrizione dell'uscita audio del modello, invia
`output_audio_transcription` nella configurazione di configurazione. La lingua della trascrizione viene
dedotta dalla risposta del modello.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Per attivare la trascrizione dell'input audio del modello, invia
`input_audio_transcription` nella configurazione di configurazione.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### Cambiare voce e lingua

I modelli di [output audio nativo](#native-audio-output) supportano una qualsiasi delle voci
disponibili per i nostri modelli di [Text-to-Speech (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#voices). Puoi ascoltare tutte le voci in [AI Studio](https://aistudio.google.com/app/live?hl=it).

Per specificare una voce, imposta il nome della voce all'interno dell'oggetto `speechConfig` come parte
della configurazione della sessione:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

L'API Live supporta [più lingue](#supported-languages).
I modelli di [output audio nativo](#native-audio-output) scelgono automaticamente
la lingua appropriata e non supportano l'impostazione esplicita del codice
della lingua.

## Funzionalità audio native

I nostri modelli più recenti sono dotati di
[output audio nativo](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=it),
che offre una sintesi vocale naturale e realistica e prestazioni multilingue migliorate.

### Ragionamento

I modelli Gemini 3.8 Live Extended Thinking e Gemini 3.1 utilizzano `thinkingLevel` per
controllare la profondità del ragionamento. Per `gemini-3.8-live`, `thinkingLevel` non è supportato
e deve essere omesso nella configurazione. Gemini 3.8 Live Extended Thinking supporta `low`,
`medium` e `high` (`minimal` non è supportato). I modelli Gemini 3.1 supportano
`minimal`, `low`, `medium` e `high`. Per maggiori dettagli, vedi
[Thinking in the Live API](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=it).

### Python

```
model = "gemini-3.8-live-extended-thinking"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.8-live-extended-thinking';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

Inoltre, puoi attivare i riepiloghi dei pensieri impostando `includeThoughts` su
`true` nella configurazione. Per maggiori informazioni, consulta la sezione [Riepiloghi dei pensieri](https://ai.google.dev/gemini-api/docs/thinking?hl=it#summaries):

### Python

```
model = "gemini-3.8-live-extended-thinking"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.8-live-extended-thinking';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### Dialogo empatico

Questa funzionalità consente a Gemini di adattare il suo stile di risposta al tono e all'espressione dell'input.

Per utilizzare il dialogo empatico, imposta la versione dell'API su `v1beta` e imposta
`enable_affective_dialog` su `true`nel messaggio di configurazione:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### Audio proattivo

Quando questa funzionalità è attiva, Gemini può decidere in modo proattivo di non rispondere
se i contenuti non sono pertinenti.

Per utilizzarlo, imposta la versione dell'API su `v1beta` e configura il campo `proactivity`
nel messaggio di configurazione e imposta `proactive_audio` su `true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## Traduzione in tempo reale

L'API Live supporta la traduzione in tempo reale e a bassa latenza delle conversazioni. Questa funzionalità ti consente di creare applicazioni di traduzione vocale in tempo reale.

Per ulteriori informazioni ed esempi, consulta la [guida alla traduzione live](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=it).

## Rilevamento di attività vocale (VAD)

Il rilevamento di attività vocale (VAD) consente al modello di riconoscere quando una persona sta
parlando. Ciò è essenziale per creare conversazioni naturali, in quanto consente a un utente di interrompere il modello in qualsiasi momento.

Quando VAD rileva un'interruzione, la generazione in corso viene annullata e
ignorata. Nella cronologia della sessione vengono conservate solo le informazioni già inviate al cliente. Il server invia quindi un messaggio [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentservercontent) per segnalare l'interruzione.

Il server Gemini scarta quindi tutte le chiamate di funzione in attesa e invia un messaggio
`BidiGenerateContentServerContent` con gli ID delle chiamate annullate.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### VAD automatico

Per impostazione predefinita, il modello esegue automaticamente il rilevamento dell'attività vocale su
un flusso di input audio continuo. VAD può essere configurato con il
campo [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=it#RealtimeInputConfig.AutomaticActivityDetection)
della [configurazione di configurazione](https://ai.google.dev/api/live?hl=it#BidiGenerateContentSetup).

Quando il flusso audio viene messo in pausa per più di un secondo (ad esempio,
perché l'utente ha disattivato il microfono), deve essere inviato un evento
[`audioStreamEnd`](https://ai.google.dev/api/live?hl=it#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end)
per svuotare l'audio memorizzato nella cache. Il client può riprendere a inviare
dati audio in qualsiasi momento.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Con `send_realtime_input`, l'API risponderà automaticamente all'audio in base
al rilevamento dell'attività vocale. Mentre `send_client_content` aggiunge i messaggi al contesto del modello in
ordine, `send_realtime_input` è ottimizzato per la reattività a scapito
dell'ordine deterministico.

### Configurazione automatica del VAD

Per un maggiore controllo sull'attività VAD, puoi configurare i seguenti parametri. Per ulteriori informazioni, consulta il [riferimento API](https://ai.google.dev/api/live?hl=it#automaticactivitydetection).

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### VAD ibrido

La VAD ibrida combina i vantaggi della VAD automatica (rilevamento robusto dell'inizio del discorso) e della VAD manuale (finalizzazione della risposta a bassa latenza).

In questa configurazione:

1. **Il VAD automatico rimane attivo** sul server. Il server rileva automaticamente
   l'inizio del discorso dell'utente, utilizzando il padding del prefisso per evitare di tagliare
   l'inizio delle espressioni.
2. Il client utilizza un **VAD lato client** per rilevare quando l'utente smette
   di parlare.
3. Quando il VAD lato client rileva la fine del discorso, invia un segnale [`audio_stream_end`](https://ai.google.dev/api/live?hl=it#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) al server.
4. Il server considera il segnale `audio_stream_end` come un prompt di finalizzazione immediata, bypassando il ritardo predefinito di rilevamento del silenzio lato server e restituendo la trascrizione e la risposta del modello con una latenza minima.
5. Se il VAD lato client non viene attivato, il VAD lato server funge da
   fallback per rilevare la fine del discorso.

Tieni presente che, se la soglia VAD lato client è impostata in modo troppo aggressivo, potrebbe causare
interruzioni del parlato. Tuttavia, questo approccio previene i problemi di troncamento iniziale che potrebbero verificarsi con il VAD manuale.

### Python

```
# Set up with automatic VAD enabled (default)
config = {
    "response_modalities": ["AUDIO"],
}

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio data normally
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects the end of speech, send:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Set up with automatic VAD enabled (default)
const config = {
  responseModalities: [Modality.AUDIO],
};

// Send audio data normally
session.sendRealtimeInput({
  audio: {
    data: base64Audio,
    mimeType: "audio/pcm;rate=16000"
  }
});

// When client-side VAD detects the end of speech, send:
session.sendRealtimeInput({ audioStreamEnd: true });
```

### Disattivare il rilevamento automatico dell'attività vocale

In alternativa, il VAD automatico può essere disattivato impostando
`realtimeInputConfig.automaticActivityDetection.disabled` su `true` nel messaggio
di configurazione. In questa configurazione, il client è responsabile del rilevamento della voce dell'utente e dell'invio dei messaggi [`activityStart`](https://ai.google.dev/api/live?hl=it#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) e [`activityEnd`](https://ai.google.dev/api/live?hl=it#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) al momento opportuno. Un `audioStreamEnd` non viene inviato
in questa configurazione. Qualsiasi interruzione dello stream viene invece contrassegnata da
un messaggio `activityEnd`.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### Comprendere i parametri VAD e il loro impatto sulla qualità

Quando si utilizza il VAD automatico, due parametri chiave controllano il modo in cui l'audio viene
segmentato in turni di conversazione prima di essere inviato al modello:

- **`prefixPaddingMs`**: la quantità di audio da includere *prima* che venga rilevato il parlato. Questo "look-back" assicura che il modello acquisisca l'inizio completo
  del parlato, inclusa la prima sillaba che potrebbe iniziare prima
  dell'attivazione del VAD. Un valore di `0` potrebbe causare il troncamento dell'inizio delle parole.
- **`silenceDurationMs`**: per quanto tempo il server attende il silenzio
  prima di terminare un turno di conversazione. Determina la tolleranza del sistema
  alle pause naturali a metà frase (ad es. per pensare, respirare o
  per i limiti delle clausole).

#### Impatto di `silenceDurationMs` sulla qualità audio

Il valore `silenceDurationMs` influisce direttamente sulle dimensioni e sulla completezza
dei segmenti audio che il modello riceve per l'elaborazione:

- **Consigliato (500 ms - 800 ms)**: offre un buon equilibrio. Il modello
  riceve blocchi audio completi e ricchi di contesto, mantenendo la latenza
  ragionevole. Il valore predefinito interno del server è di circa 800 ms.
- **Troppo basso (ad es. 100-200 ms)**: il sistema termina i turni di parola durante le pause naturali, suddividendo una singola espressione in più piccoli frammenti audio. Il modello riceve questi frammenti singolarmente, perdendo
  il contesto tra i frammenti e con conseguente qualità inferiore della trascrizione e della risposta.
- **Troppo alto (ad es. 2000 ms o più):** il sistema attende a lungo dopo che l'utente smette di parlare, aumentando la latenza percepita prima che il modello risponda.

#### Best practice per la VAD manuale (lato client)

Quando disattivi il rilevamento automatico dell'attività vocale e gestisci i segnali `activityStart`/`activityEnd`
dal tuo rilevamento vocale lato client, tieni presente che
i meccanismi di buffering audio integrati del server vengono bypassati. Ciò significa che:

1. **Nessun buffer pre-speech:** il server non antepone più l'audio all'inizio del discorso rilevato. Il tuo cliente deve includere un contesto audio sufficiente prima di inviare `activityStart`.
2. **Nessuna tolleranza al silenzio**:il server agisce immediatamente sul segnale
   `activityEnd` senza ulteriori attese. Se la VAD lato client
   utilizza una soglia di fine del discorso aggressiva (ad es. 200 ms di silenzio),
   il discorso potrebbe essere interrotto a metà frase durante le pause naturali.

Per preservare la qualità audio con il VAD manuale, utilizza una soglia di silenzio di fine discorso di almeno **500 ms** nel rilevatore di attività vocale del client.
Le soglie inferiori a questo valore spesso causano un audio frammentato che peggiora
la qualità della trascrizione e della risposta del modello.

## Conteggio dei token

Puoi trovare il numero totale di token utilizzati nel campo
[usageMetadata](https://ai.google.dev/api/live?hl=it#usagemetadata) del messaggio del server restituito.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## Risoluzione dei contenuti multimediali

Puoi specificare la risoluzione dei contenuti multimediali di input impostando il campo
`mediaResolution` nell'ambito della configurazione della sessione:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

Puoi configurare `mediaResolution` per le sessioni multimodali che includono
input audio, video o immagine. Mentre `mediaResolution` regola l'allocazione dei token
per frame per gli input visivi, i flussi audio vengono tokenizzati a una
velocità fissa al secondo in tutte le impostazioni di risoluzione. Per saperne di più,
consulta la guida alla [risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it).

## Limitazioni

Tieni presenti le seguenti limitazioni dell'API Live
quando pianifichi il tuo progetto.

### Modalità di risposta

I modelli audio nativi supportano solo la modalità di risposta `AUDIO. Se hai bisogno della
risposta del modello come testo, utilizza la funzionalità
[Trascrizione audio dell'output](#audio-transcription).

### Autenticazione client

L'API Live fornisce solo l'autenticazione server-server
per impostazione predefinita. Se implementi l'applicazione Live API
utilizzando un [approccio client-server](https://ai.google.dev/gemini-api/docs/live?hl=it#implementation-approach), devi utilizzare
[token effimeri](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=it) per ridurre i rischi per la sicurezza.

### Durata della sessione

Le sessioni solo audio sono limitate a 15 minuti,
mentre le sessioni audio e video sono limitate a 2 minuti.
Tuttavia, puoi configurare diverse [tecniche di gestione delle sessioni](https://ai.google.dev/gemini-api/docs/live-session?hl=it) per estensioni illimitate della durata della sessione.

### Finestra contestuale

Una sessione ha un limite della finestra contestuale di:

- 128.000 token per i modelli con [output audio nativo](#native-audio-output)
- 32.000 token per altri modelli dell'API Live

## Lingue supportate

L'API Live supporta le seguenti 99 lingue.

| Lingua | Codice BCP-47 | Lingua | Codice BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af` | Lettone | `lv` |
| Akan | `ak` | Lituano | `lt` |
| Albanese | `sq` | Macedone | `mk` |
| Amarico | `am` | Malese | `ms` |
| Arabo | `ar` | Malayalam | `ml` |
| Armeno | `hy` | Maltese | `mt` |
| Assamese | `as` | Maori | `mi` |
| Azero | `az` | Marathi | `mr` |
| Basco | `eu` | Mongolo | `mn` |
| Bielorusso | `be` | Nepalese | `ne` |
| Bengalese | `bn` | Norvegese | `no`, `nb` |
| Bosniaco | `bs` | Odia | `or` |
| Bulgaro | `bg` | Oromo | `om` |
| Birmano | `my` | Pashto | `ps` |
| Catalano | `ca` | Persiano | `fa` |
| Cebuano | `ceb` | Polacco | `pl` |
| Cinese (semplificato) | `zh-Hans` | Portoghese (Brasile) | `pt-BR` |
| Cinese (tradizionale) | `zh-Hant` | Portoghese (Portogallo) | `pt-PT` |
| Croato | `hr` | Punjabi | `pa` |
| Ceco | `cs` | Quechua | `qu` |
| Danese | `da` | Rumeno | `ro` |
| Olandese | `nl` | Romancio | `rm` |
| Inglese | `en` | Russo | `ru` |
| Estone | `et` | Serbo | `sr` |
| Faroese | `fo` | Sindhi | `sd` |
| Filippino | `fil` | Singalese | `si` |
| Finlandese | `fi` | Slovacco | `sk` |
| Francese | `fr` | Sloveno | `sl` |
| Galiziano | `gl` | Somalo | `so` |
| Georgiano | `ka` | Sotho del sud | `st` |
| Tedesco | `de` | Spagnolo | `es` |
| Greek | `el` | Swahili | `sw` |
| Gujarati | `gu` | Svedese | `sv` |
| Hausa | `ha` | Tagico | `tg` |
| Ebraico | `he` | Tamil | `ta` |
| Hindi | `hi` | Telugu | `te` |
| Ungherese | `hu` | Thailandese | `th` |
| Islandese | `is` | Tswana | `tn` |
| Indonesiano | `id` | Turco | `tr` |
| Irlandese | `ga` | Turkmeno | `tk` |
| Italiano | `it` | Ucraino | `uk` |
| Giapponese | `ja` | Urdu | `ur` |
| Kannada | `kn` | Uzbeco | `uz` |
| Kazako | `kk` | Vietnamita | `vi` |
| Khmer | `km` | Gallese | `cy` |
| Kinyarwanda | `rw` | Frisone occidentale | `fy` |
| Coreano | `ko` | Wolof | `wo` |
| Curdo | `ku` | Yoruba | `yo` |
| Kirgizo | `ky` | Zulu | `zu` |
| Lao | `lo` |  |  |

## Passaggi successivi

- Leggi le guide [Utilizzo degli strumenti](https://ai.google.dev/gemini-api/docs/live-tools?hl=it) e [Gestione delle sessioni](https://ai.google.dev/gemini-api/docs/live-session?hl=it) per informazioni essenziali sull'utilizzo efficace dell'API Live.
- Prova l'API live in [Google AI Studio](https://aistudio.google.com/app/live?hl=it).
- Per saperne di più sui modelli dell'API Live, consulta le pagine dei modelli
  [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=it) e
  [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=it).
- Prova altri esempi nel [cookbook dell'API Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=it),
  nel [cookbook degli strumenti dell'API Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=it)
  e nello [script di primo utilizzo dell'API Live](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-19 UTC."],[],[]]
