---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=it
fetched_at: 2026-08-24T02:32:36.756385+00:00
title: "Generare musica con Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Generare musica con Lyria 3

Lyria 3 è la famiglia di modelli di generazione di musica di Google, disponibile tramite l'API Gemini. Con Lyria 3, puoi generare audio stereo di alta qualità a 44, 1 kHz da prompt di testo o da immagini. Questi modelli offrono coerenza strutturale, incluse voci, testi sincronizzati e arrangiamenti strumentali completi.

La famiglia Lyria 3 include due modelli:

| Modello | ID modello | Ideale per | Durata | Output |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clip corti, loop, anteprime | 30 secondi | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Brani completi con strofe, ritornelli, ponti | Un paio di minuti (controllabile tramite prompt) | MP3 |

Entrambi i modelli possono essere utilizzati con la nuova
[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it), supportano input multimodali
input (testo e immagini) e producono **audio stereo ad alta fedeltà a 44,1 kHz**
.

## Generare un clip musicale

Il modello Lyria 3 Clip genera sempre un clip di **30 secondi**. Per generare un clip, chiama il metodo `interactions.create` con un prompt testuale. La risposta include sempre i testi e la struttura del brano generati insieme all'audio nello schema `steps`.

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

Puoi recuperare i dati musicali generati utilizzando la proprietà `interaction.output_audio`, che restituisce l'ultimo blocco audio generato. Puoi anche recuperare i testi e la struttura del brano utilizzando la proprietà `interaction.output_text`. Per maggiori dettagli sulle proprietà di convenienza, consulta la
[panoramica di Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it#convenience-properties).

## Generare un brano completo

Utilizza il modello `lyria-3-pro-preview` per generare brani completi della durata di un paio di minuti. Il modello Pro comprende la struttura musicale e può creare composizioni con strofe, ritornelli e ponti distinti. Puoi influenzare la
durata specificandola nel prompt (ad es. "crea un brano di 2 minuti") o
utilizzando [i timestamp](#timing) per definire la struttura.

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

## Selezionare il formato di output

Per impostazione predefinita, i modelli Lyria 3 generano audio in formato **MP3**. Per Lyria 3 Pro, puoi anche richiedere l'output in formato **WAV** impostando `response_format`.

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

## Analizzare la risposta

La risposta di Lyria 3 contiene più blocchi di contenuti nello schema `steps`.
Le interazioni restituiscono una sequenza di passaggi, in cui i passaggi `model_output` contengono i contenuti generati.
I blocchi di contenuti di testo contengono i testi generati o una descrizione JSON della struttura del brano.
I blocchi di contenuti con tipo `audio` contengono i dati audio codificati in Base64.

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

#### Testi e musica intercalati

Poiché l'output di Lyria 3 è complesso e contiene passaggi e blocchi separati per i testi generati (testo) e il brano stesso (audio), le proprietà di convenienza offrono una scorciatoia rapida e consigliata.

Tuttavia, se vuoi un controllo programmatico completo sulla sequenza temporale non elaborata dei passaggi restituiti dal server (ad esempio la registrazione dei singoli blocchi di contenuti man mano che vengono ricevuti), puoi eseguire manualmente l'iterazione su `steps`:

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

## Generare musica da immagini

Lyria 3 supporta input multimodali: puoi fornire fino a **10 immagini** insieme al prompt testuale nell'elenco `input` e il modello comporrà musica ispirata ai contenuti visivi.

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

## Fornire testi personalizzati

Puoi scrivere i tuoi testi e includerli nel prompt. Utilizza tag di sezione come `[Verse]`, `[Chorus]` e `[Bridge]` per aiutare il modello a comprendere la struttura del brano:

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

## Controllare la tempistica e la struttura

Puoi specificare esattamente cosa succede in momenti specifici del brano utilizzando i timestamp. Questa funzionalità è utile per controllare quando entrano gli strumenti, quando vengono forniti i testi e come procede il brano:

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

## Generare tracce strumentali

Per la musica di sottofondo, le colonne sonore dei giochi o qualsiasi caso d'uso in cui non sono richieste le voci, puoi chiedere al modello di produrre tracce solo strumentali:

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

## Generare musica in lingue diverse

Lyria 3 genera i testi nella lingua del prompt. Per generare un brano con testi in francese, scrivi il prompt in francese. Il modello adatta lo stile vocale e la pronuncia in base alla lingua.

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

## Intelligenza del modello

Lyria 3 analizza il processo del prompt in cui il modello ragiona sulla struttura musicale (introduzione, strofa, ritornello, ponte e così via) in base al prompt.
Questa operazione viene eseguita prima della generazione dell'audio e garantisce la coerenza strutturale e la musicalità.

## Guida ai prompt

Più specifico è il prompt, migliori saranno i risultati. Ecco cosa puoi includere per guidare la generazione:

- **Genere**: specifica un genere o una combinazione di generi (ad es. "lo-fi hip hop",
  "jazz fusion", "orchestrale cinematografico").
- **Strumenti**: indica strumenti specifici (ad es. "pianoforte Fender Rhodes",
  "chitarra slide", "drum machine TR-808").
- **BPM**: imposta il tempo (ad es. "120 BPM", "tempo lento intorno a 70 BPM").
- **Tonalità/scala**: specifica una tonalità musicale (ad es. "in sol maggiore", "re minore").
- **Stato d'animo e atmosfera**: utilizza aggettivi descrittivi (ad es. "nostalgico",
  "aggressivo", "etereo", "sognante").
- **Struttura**: utilizza tag come `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` o timestamp per controllare la progressione del brano.
- **Durata**: il modello Clip produce sempre clip di 30 secondi. Per il modello Pro, specifica la durata prevista nel prompt (ad es. "crea un brano di 2 minuti") o utilizza i timestamp per controllare la durata.

### Prompt di esempio

Ecco alcuni esempi di prompt efficaci:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Best practice

- **Esegui prima l'iterazione con Clip.** Utilizza il modello `lyria-3-clip-preview` più veloce per sperimentare con i prompt prima di eseguire una generazione completa con `lyria-3-pro-preview`.
- **Usa un testo specifico.** I prompt vaghi producono risultati generici. Per ottenere il miglior output, indica strumenti, BPM, tonalità, stato d'animo e struttura.
- **Usa la lingua corretta.** Scrivi il prompt nella lingua in cui vuoi che siano i testi.
- **Utilizza i tag di sezione.** I tag `[Verse]`, `[Chorus]` e `[Bridge]` forniscono al modello una struttura chiara da seguire.
- **Separa i testi dalle istruzioni.** Quando fornisci testi personalizzati, separali chiaramente dalle istruzioni sulla direzione musicale.

## Limitazioni

- **Sicurezza**: tutti i prompt vengono controllati dai filtri di sicurezza. I prompt che attivano i filtri verranno bloccati. Sono inclusi i prompt che richiedono voci di artisti specifici o la generazione di testi protetti da copyright.
- **Filigrana**: tutto l'audio generato include una
  [filigrana audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=it) per
  l'identificazione. Questa filigrana è impercettibile all'orecchio umano e non influisce sull'esperienza di ascolto.
- **Modifica multi-turno**: la generazione di musica è un processo a turno singolo.
  La modifica iterativa o il perfezionamento di un clip generato tramite più prompt non è supportato nella versione attuale di Lyria 3.
- **Lunghezza**: il modello Clip genera sempre clip di 30 secondi. Il modello Pro genera brani della durata di un paio di minuti; la durata esatta può essere influenzata dal prompt.
- **Determinismo**: i risultati possono variare tra le chiamate, anche con lo stesso prompt.

## Passaggi successivi

- Controlla i [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it) dei modelli Lyria 3.
- Prova la generazione di musica in streaming [in tempo reale](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=it)
  con Lyria RealTime.
- Genera conversazioni con più relatori con i
  [modelli TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it).
- Scopri come generare [immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) o [video](https://ai.google.dev/gemini-api/docs/video?hl=it).
- Scopri come Gemini può [comprendere i file audio](https://ai.google.dev/gemini-api/docs/audio?hl=it).
- Avvia una conversazione in tempo reale con Gemini utilizzando l'
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
