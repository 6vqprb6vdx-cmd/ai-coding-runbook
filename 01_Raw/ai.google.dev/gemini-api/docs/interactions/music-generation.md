---
source_url: https://ai.google.dev/gemini-api/docs/interactions/music-generation?hl=pl
fetched_at: 2026-06-15T06:25:30.086110+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie muzyki za pomocą Lyrii 3

Lyria 3 to rodzina modeli generowania muzyki od Google, dostępna w ramach Gemini API. Za pomocą Lyrii 3 możesz generować wysokiej jakości dźwięk stereo o częstotliwości próbkowania 44,1 kHz na podstawie promptów tekstowych lub obrazów. Te modele zapewniają spójność strukturalną, w tym wokal, zsynchronizowany tekst i pełne aranżacje instrumentalne.

Rodzina Lyria 3 obejmuje 2 modele:

| Model | Identyfikator modelu | Urządzenia | Czas trwania | Wyniki |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | krótkie klipy, pętle, wersje przedpremierowe; | 30 sekund | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | pełne utwory z wersami, refrenami i przejściami; | Kilka minut (można kontrolować za pomocą prompta) | MP3 |

Oba modele można używać za pomocą nowego [interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl), który obsługuje dane wejściowe w różnych formatach (tekst i obrazy) i generuje **stereofoniczny dźwięk o wysokiej jakości (44,1 kHz)**.

## Generowanie klipu muzycznego

Model Lyria 3 Clip zawsze generuje **30-sekundowy** klip. Aby wygenerować klip, wywołaj metodę `interactions.create` z promptem tekstowym. Odpowiedź zawsze zawiera wygenerowane słowa i strukturę utworu wraz z dźwiękiem w schemacie `steps`.

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
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Wygenerowane dane muzyczne możesz pobrać za pomocą właściwości `interaction.output_audio`, która zwraca ostatni wygenerowany blok audio. Możesz też pobrać tekst i strukturę utworu za pomocą właściwości `interaction.output_text`. Szczegółowe informacje o właściwościach ułatwiających korzystanie z usługi znajdziesz w artykule [Omówienie interakcji](https://ai.google.dev/gemini-api/docs/interactions?hl=pl#convenience-properties).

## Generowanie pełnych utworów

Użyj modelu `lyria-3-pro-preview`, aby wygenerować pełne utwory trwające kilka minut. Model Pro rozumie strukturę muzyczną i może tworzyć kompozycje z wyraźnymi zwrotkami, refrenami i przejściami. Możesz wpłynąć na czas trwania utworu, podając go w prompcie (np. „utwórz 2-minutową piosenkę”) lub używając [sygnatur czasowych](#timing) do zdefiniowania struktury.

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
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Wybierz format wyjściowy

Domyślnie modele Lyria 3 generują dźwięk w formacie **MP3**. W przypadku Lyria 3 Pro możesz też poprosić o wygenerowanie danych wyjściowych w formacie **WAV**, ustawiając `response_format`.

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Analizowanie odpowiedzi

Odpowiedź z Lyrii 3 zawiera wiele bloków treści w schemacie `steps`.
Interakcje zwracają sekwencję kroków, w której kroki `model_output` zawierają wygenerowane treści.
Bloki treści tekstowych zawierają wygenerowany tekst lub opis struktury utworu w formacie JSON.
Bloki treści typu `audio` zawierają dane audio zakodowane w formacie base64.

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

#### Tekst i muzyka przeplatają się

Dane wyjściowe z Lyrii 3 są złożone – zawierają oddzielne etapy i bloki wygenerowanego tekstu i samego utworu (audio). Właściwości ułatwiające obsługę stanowią szybki i zalecany skrót.

Jeśli jednak chcesz mieć pełną kontrolę programową nad surową osią czasu kroków zwracanych przez serwer (np. rejestrować poszczególne bloki treści w miarę ich otrzymywania), możesz ręcznie iterować po `steps`:

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

## Generowanie muzyki na podstawie obrazów

Lyria 3 obsługuje dane wejściowe multimodalne – możesz przesłać maksymalnie **10 obrazów**
wraz z promptem tekstowym na `input` liście, a model skomponuje muzykę
inspirowaną treściami wizualnymi.

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
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Podaj własny tekst

Możesz napisać własny tekst i uwzględnić go w prompcie. Używaj tagów sekcji, takich jak `[Verse]`, `[Chorus]` i `[Bridge]`, aby pomóc modelowi zrozumieć strukturę utworu:

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Kontrolowanie czasu i struktury

Za pomocą sygnatur czasowych możesz określić, co ma się dziać w konkretnych momentach utworu. Jest to przydatne do kontrolowania, kiedy wchodzą instrumenty, kiedy pojawiają się słowa i jak rozwija się utwór:

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Generowanie utworów instrumentalnych

W przypadku muzyki w tle, ścieżek dźwiękowych do gier lub innych zastosowań, w których nie są wymagane wokale, możesz poprosić model o wygenerowanie utworów instrumentalnych:

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Generowanie muzyki w różnych językach

Lyria 3 generuje tekst w języku prompta. Aby wygenerować utwór z tekstem w języku francuskim, napisz prompt w tym języku. Model dostosowuje styl głosu i wymowę do języka.

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Inteligencja modelu

Lyria 3 analizuje proces promptowania, w którym model wnioskuje na podstawie prompta o strukturze muzycznej (intro, zwrotka, refren, bridge itp.).
Dzieje się to przed wygenerowaniem dźwięku i zapewnia spójność strukturalną oraz muzykalność.

## Przewodnik po promptach

Im bardziej szczegółowy prompt, tym lepsze wyniki. Oto co możesz uwzględnić, aby ułatwić generowanie:

- **Gatunek:** określ gatunek lub mieszankę gatunków (np. „lo-fi hip hop”, „jazz fusion”, „cinematic orchestral”).
- **Instrumenty:** podaj konkretne instrumenty (np. „fortepian Fender Rhodes”, „gitara slide”, „automat perkusyjny TR-808”).
- **BPM:** ustaw tempo (np. „120 BPM”, „wolne tempo około 70 BPM”).
- **Tonacja:** podaj tonację (np. „w tonacji G-dur”, „d-moll”).
- **Nastrój i atmosfera:** używaj przymiotników opisowych (np. „nostalgiczny”, „agresywny”, „etericzny”, „marzycielski”).
- **Struktura:** używaj tagów takich jak `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]` lub sygnatur czasowych, aby kontrolować postęp utworu.
- **Czas trwania:** model Clip zawsze tworzy 30-sekundowe klipy. W przypadku modelu Pro określ zamierzoną długość w promcie (np. „utwórz 2-minutową piosenkę”) lub użyj sygnatur czasowych, aby kontrolować czas trwania.

### Przykładowe prompty

Oto kilka przykładów skutecznych promptów:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Sprawdzone metody

- **Najpierw iteruj za pomocą funkcji Clip.** Używaj szybszego modelu `lyria-3-clip-preview`, aby eksperymentować z promptami, zanim zdecydujesz się na wygenerowanie pełnej wersji za pomocą modelu `lyria-3-pro-preview`.
- **Unikaj ogólników.** Niejasne prompty dają ogólne wyniki. Aby uzyskać najlepszy wynik, podaj instrumenty, tempo, tonację, nastrój i strukturę.
- **Dopasuj język.** Wpisz prompt w języku, w którym chcesz uzyskać tekst utworu.
- **Używaj tagów sekcji.** Tagi `[Verse]`, `[Chorus]` i `[Bridge]` nadają modelowi wyraźną strukturę, której może się trzymać.
- **Oddziel teksty piosenek od instrukcji.** Podając niestandardowy tekst, wyraźnie oddziel go od instrukcji dotyczących kierunku muzycznego.

## Ograniczenia

- **Bezpieczeństwo:** wszystkie prompty są sprawdzane przez filtry bezpieczeństwa. Prompty, które aktywują filtry, zostaną zablokowane. Obejmuje to prompty, które wymagają użycia głosu konkretnego wykonawcy lub wygenerowania tekstów piosenek chronionych prawem autorskim.
- **Dodawanie znaków wodnych:** wszystkie wygenerowane pliki audio zawierają [znak wodny audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=pl), który umożliwia identyfikację. Ten znak wodny jest niesłyszalny dla ludzkiego ucha i nie wpływa na jakość odsłuchu.
- **Edytowanie wieloetapowe:** generowanie muzyki to proces jednoetapowy.
  Iteracyjne edytowanie lub ulepszanie wygenerowanego klipu za pomocą wielu promptów nie jest obsługiwane w obecnej wersji Lyrii 3.
- **Długość:** model Clip zawsze generuje 30-sekundowe klipy. Model Pro generuje utwory trwające kilka minut. Na dokładny czas trwania może wpływać prompt.
- **Determinacja:** wyniki mogą się różnić w zależności od połączenia, nawet w przypadku tego samego prompta.

## Co dalej?

- Sprawdź [ceny](https://ai.google.dev/gemini-api/docs/interactions/pricing?hl=pl) modeli Lyria 3.
- Wypróbuj [generowanie muzyki w czasie rzeczywistym](https://ai.google.dev/gemini-api/docs/interactions/realtime-music-generation?hl=pl) za pomocą Lyrii RealTime.
- generować rozmowy z udziałem wielu osób za pomocą [modeli TTS](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=pl),
- Dowiedz się, jak generować [obrazy](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=pl) i [filmy](https://ai.google.dev/gemini-api/docs/interactions/video?hl=pl).
- Dowiedz się, jak Gemini może [rozumieć pliki audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pl),
- Prowadź rozmowy z Gemini w czasie rzeczywistym za pomocą [interfejsu Live API](https://ai.google.dev/gemini-api/docs/interactions/live?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
