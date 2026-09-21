---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=de
fetched_at: 2026-09-21T05:52:33.624775+00:00
title: "Sprachausgabe \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Sprachausgabe

Mit der Gemini API kann Texteingabe mithilfe der Gemini-Funktionen zur Text-to-Speech-Generierung (TTS) in Audio für einen einzelnen oder mehrere Sprecher umgewandelt werden.
Die TTS-Generierung (Text-to-Speech) ist *[steuerbar](#controllable)*. Das bedeutet, dass Sie mit natürlicher Sprache Interaktionen strukturieren und *Stil*, *Akzent*, *Tempo* und *Ton* der Audioausgabe festlegen können.

[In Google AI Studio ausprobieren](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=de)

Die TTS-Funktion unterscheidet sich von der Sprachgenerierung über die [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de), die für interaktive, unstrukturierte Audio- sowie multimodale Ein- und Ausgaben konzipiert ist. Während die Live API sich durch dynamische Gesprächskontexte auszeichnet, ist TTS über die Gemini API für Szenarien konzipiert, in denen eine genaue Textwiedergabe mit detaillierter Steuerung von Stil und Klang erforderlich ist, z. B. bei der Erstellung von Podcasts oder Hörbüchern.

In dieser Anleitung erfahren Sie, wie Sie Audio mit einem oder mehreren Sprechern aus Text generieren.

## Hinweis

Achten Sie darauf, dass Sie eine Gemini-Modellvariante mit Gemini-TTS-Funktionen (Text-to-Speech) verwenden, wie im Abschnitt [Unterstützte Modelle](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#supported-models) aufgeführt. Für optimale Ergebnisse sollten Sie überlegen, welches Modell am besten zu Ihrem spezifischen Anwendungsfall passt.

Es kann hilfreich sein, die [Gemini TTS-Modelle in AI Studio zu testen](https://aistudio.google.com/generate-speech?hl=de), bevor Sie mit der Entwicklung beginnen.

## TTS für einen einzelnen Sprecher

Wenn Sie Text in Audioinhalte mit einem einzelnen Sprecher umwandeln möchten, legen Sie die Antwortmodalität auf „audio“ fest und übergeben Sie ein `SpeechConfig`-Objekt mit `VoiceConfig`.
Sie müssen einen Namen für die Stimme aus den vordefinierten [Ausgabestimmen](#voices) auswählen.

In diesem Beispiel wird die Audioausgabe des Modells in einer WAV-Datei gespeichert:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
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
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## TTS mit mehreren Sprechern

Für Audio mit mehreren Sprechern benötigen Sie ein `MultiSpeakerVoiceConfig`-Objekt, in dem jeder Sprecher (bis zu 2) als `SpeakerVoiceConfig` konfiguriert ist.
Sie müssen jede `speaker` mit denselben Namen definieren, die im [Prompt](#controllable) verwendet werden:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
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

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
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
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## Sprachstil mit Prompts steuern

Sie können Stil, Ton, Akzent und Tempo sowohl für TTS mit einem als auch mit mehreren Sprechern mit Prompts in natürlicher Sprache oder [Audio-Tags](#transcript-tags) steuern.
Bei einem Prompt mit nur einem Sprecher können Sie beispielsweise Folgendes sagen:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

Geben Sie in einem Prompt mit mehreren Sprechern den Namen und das entsprechende Transkript für jeden Sprecher an. Sie können auch für jeden Lautsprecher einzeln Anweisungen geben:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Verwenden Sie eine [Stimmoption](#voices), die dem Stil oder der Emotion entspricht, die Sie vermitteln möchten, um diese noch stärker zu betonen. Im vorherigen Prompt könnte beispielsweise die gehauchte Stimme von *Enceladus* die Wörter „müde“ und „gelangweilt“ betonen, während der fröhliche Ton von *Puck* die Wörter „aufgeregt“ und „glücklich“ ergänzen könnte.

## Prompt zum Konvertieren in Audio generieren

Die TTS-Modelle geben nur Audio aus. Sie können jedoch [andere Modelle](https://ai.google.dev/gemini-api/docs/models?hl=de) verwenden, um zuerst ein Transkript zu erstellen, das Sie dann dem TTS-Modell zum Vorlesen übergeben.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3.6-flash",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3.6-flash",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## Stimmoptionen

TTS-Modelle unterstützen die folgenden 30 Sprachoptionen im Feld `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *Hell* | **Puck** – *Upbeat* | **Charon** – *Informativ* |
| **Kore** – *Fest* | **Fenrir** – *Leicht erregbar* | **Leda** – *Jugendlich* |
| **Orus** – *Firm* | **Aoede** – *Breezy* | **Callirrhoe** – *Gelassen* |
| **Autonoe** – *Hell* | **Enceladus** – *Breathy* | **Iapetus** – *Clear* |
| **Umbriel** – *Unkompliziert* | **Algieba** – *Glatt* | **Despina** – *Smooth* |
| **Erinome** – *Wolkenlos* | **Algenib** – *Gravelly* | **Rasalgethi** – *Informativ* |
| **Laomedeia** – *Upbeat* | **Achernar** – *Weich* | **Alnilam** – *Firm* |
| **Schedar** – *Gerade* | **Gacrux** – *Nicht jugendfrei* | **Pulcherrima** – *Vorwärts* |
| **Achird** – *Freundlich* | **Zubenelgenubi** – *Casual* | **Vindemiatrix** – *Sanft* |
| **Sadachbia** – *Lively* | **Sadaltager** – *Sachkundig* | **Sulafat** – *Warm* |

Alle Sprachoptionen finden Sie in [AI Studio](https://aistudio.google.com/generate-speech?hl=de).

## Unterstützte Sprachen

Die TTS-Modelle erkennen die Eingabesprache automatisch. Folgende Sprachen werden unterstützt:

| Sprache | BCP-47-Code | Sprache | BCP-47-Code |
| --- | --- | --- | --- |
| Arabisch | ar | Filipino | fil |
| Bengalisch | bn | Finnisch | fi |
| Niederländisch | nl | Galizisch | gl |
| Englisch | de | Georgisch | ka |
| Französisch | fr | Griechisch | el |
| Deutsch | de | Gujarati | gu |
| Hindi | hi | Haitianisch | ht |
| Indonesisch | id | Hebräisch | er |
| Italienisch | it | Ungarisch | hu |
| Japanisch | ja | Isländisch | ist |
| Koreanisch | ko | Javanisch | jv |
| Marathi | mr | Kannada | kn |
| Polnisch | pl | Konkani | kok |
| Portugiesisch | pt | Lao | lo |
| Rumänisch | ro | Latin | la |
| Russisch | ru | Lettisch | lv |
| Spanisch | es | Litauisch | lt |
| Tamil | ta | Luxemburgisch | lb |
| Telugu | te | Mazedonisch | mk |
| Thailändisch | th | Maithili | mai |
| Türkisch | tr | Malagasy | mg |
| Ukrainisch | uk | Malaiisch | ms |
| Vietnamesisch | vi | Malayalam | ml |
| Afrikaans | af | Mongolisch | mn |
| Albanisch | sq | Nepalesisch | ne |
| Amharisch | am | Norwegisch (Bokmål) | nb |
| Armenisch | hy | Norwegisch, Nynorsk | nn |
| Aserbaidschanisch | az | Oriya | oder |
| Baskisch | eu | Paschtu | ps |
| Belarussisch | be | Persisch | fa |
| Bulgarisch | bg | Punjabi | pa |
| Burmesisch | my | Serbisch | sr |
| Katalanisch | ca | Sindhi | sd |
| Cebuano | ceb | Singhalesisch | si |
| Chinesisch (Mandarin) | cmn | Slowakisch | sk |
| Kroatisch | Std. | Slowenisch | sl |
| Tschechisch | cs | Swahili | sw |
| Dänisch | da | Schwedisch | sv |
| Estnisch | et | Urdu | ur |

## Unterstützte Modelle

| Modell | Einzelner Sprecher | Mehrere Sprecher |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=de) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=de) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=de) | ✔️ | ✔️ |

## Anleitung zu Prompts

Das Modell **Gemini Native Audio Generation Text-to-Speech (TTS)** unterscheidet sich von herkömmlichen TTS-Modellen dadurch, dass es ein Large Language Model verwendet, das ***nicht nur weiß, was gesagt werden soll, sondern auch, wie es gesagt werden soll***.

Das Modell interpretiert ein Transkript und bestimmt, wie Ihre Worte übermittelt werden sollen. Einfache Transkripte ohne zusätzliche Prompts klingen natürlich. Gemini TTS bietet aber auch Tools, mit denen Sie die Ausgabe steuern können.

Dieser Leitfaden soll Ihnen grundlegende Orientierungshilfe und Ideen für die Entwicklung von Audioinhalten bieten. Wir beginnen mit **Tags** für die schnelle Inline-Steuerung und sehen uns dann erweiterte **Prompting-Strukturen** für die vollständige Leistungssteuerung an.

### Audio-Tags

Tags sind Inline-Modifikatoren wie `[whispers]` oder `[laughs]`, mit denen Sie die Auslieferung detailliert steuern können. Damit können Sie den Ton, das Tempo und die emotionale Stimmung einer Zeile oder eines Abschnitts des Transkripts ändern. Sie können damit auch Zwischenrufe und einige andere nicht verbale Geräusche wie `[cough]`, `[sighs]` oder `[gasp]` hinzufügen.

Es gibt keine vollständige Liste der Tags, die funktionieren und nicht funktionieren. Wir empfehlen, mit verschiedenen Emotionen und Ausdrücken zu experimentieren, um zu sehen, wie sich die Ausgabe ändert.

Wenn Ihr Transkript nicht auf Englisch ist, empfehlen wir, trotzdem englische Audio-Tags zu verwenden, um optimale Ergebnisse zu erzielen.

**Kreative Audiotags**

Um zu zeigen, welche Art von Variabilität mit Audio-Tags möglich ist, finden Sie hier eine Reihe von Beispielen, die alle dasselbe aussagen, aber je nach verwendeten Tags unterschiedlich formuliert sind.

Sie können die Betonung der Wiedergabe ändern, indem Sie am Anfang einer Zeile Tags hinzufügen, um den Sprecher aufgeregt, gelangweilt oder widerwillig klingen zu lassen:

- `[excitedly]` Hallo, ich bin ein neues Text-zu-Sprache-Modell und kann Dinge auf viele verschiedene Arten sagen. Was kann ich für Sie tun?
- `[bored]` Hallo, ich bin ein neues Modell für die Sprachausgabe…
- `[reluctantly]` Hallo, ich bin ein neues Modell für die Sprachausgabe…

Tags können auch verwendet werden, um das Tempo der Wiedergabe zu ändern oder um das Tempo mit der Betonung zu kombinieren:

- `[very fast]` Hallo, ich bin ein neues Modell für die Sprachausgabe…
- `[very slow]` Hallo, ich bin ein neues Modell für die Sprachausgabe…
- `[sarcastically, one painfully slow word at a time]` Hallo, ich bin ein neues Modell für die Sprachsynthese…

Außerdem hast du die Möglichkeit, bestimmte Abschnitte zu flüstern und andere zu schreien.

- `[whispers]` Hallo, ich bin ein neues Sprachausgabemodell, `[shouting]`, und ich kann Dinge auf viele verschiedene Arten sagen. `[whispers]` Was kann ich für Sie tun?

Sie können auch mit jeder beliebigen kreativen Idee experimentieren:

- `[like a cartoon dog]` Hallo, ich bin ein neues Modell für die Sprachausgabe…
- `[like dracula]` Hallo, ich bin ein neues Modell für die Sprachausgabe…

Häufig verwendete Tags sind:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Mit Tags können Sie die Bereitstellung Ihres Transkripts schnell und einfach steuern. Für noch mehr Kontrolle können Sie sie mit einem Kontext-Prompt kombinieren, um den allgemeinen Ton und die Stimmung der Performance festzulegen.

### Erweiterte Prompts

Sie können sich einen erweiterten Prompt als Systemanweisung für das Modell vorstellen. So können Sie dem Modell mehr Kontext und Kontrolle über die Leistung geben.

Ein robuster Prompt enthält idealerweise die folgenden Elemente, die zusammen eine gute Leistung ermöglichen:

- **Audioprofil**: Hier wird eine Persona für die Stimme erstellt, die eine Charakteridentität, einen Archetyp und andere Merkmale wie Alter, Hintergrund usw. definiert.
- **Szene**: Legt die Bühne fest. Beschreibt sowohl die physische Umgebung als auch die Atmosphäre.
- **Hinweise des Regisseurs**: Hier finden Sie Leistungsanleitungen, in denen Sie aufschlüsseln können, welche Anweisungen für Ihr virtuelles Talent wichtig sind. Beispiele sind Stil, Atmung, Tempo, Artikulation und Akzent.
- **Beispielkontext**: Bietet dem Modell einen kontextbezogenen Ausgangspunkt, sodass Ihr virtueller Schauspieler auf natürliche Weise in die von Ihnen eingerichtete Szene eintritt.
- **Transkript**: Der Text, der vom Modell gesprochen wird. Für eine optimale Leistung sollten das Thema des Transkripts und der Schreibstil mit den Anweisungen übereinstimmen, die Sie geben.
- **Audio-Tags**: Modifikatoren, die Sie in ein Transkript einfügen können, um die Wiedergabe eines bestimmten Textabschnitts zu ändern, z. B. `[whispers]` oder `[shouting]`.

Beispiel für einen vollständigen Prompt:

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
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### Detaillierte Prompt-Strategien

Sehen wir uns die einzelnen Elemente des Prompts genauer an.

#### Audioprofil

Beschreiben Sie kurz die Persona des Charakters.

- **Name:** Wenn Sie Ihrem Charakter einen Namen geben, kann das Modell die Leistung besser anpassen. Beziehen Sie sich beim Festlegen der Szene und des Kontexts auf den Charakter.
- **Rolle**: Die grundlegende Identität und der Archetyp der Figur, die in der Szene dargestellt wird, z. B. Radiomoderator, Podcaster, Nachrichtenreporter usw.

Beispiele:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Szene

Legen Sie den Kontext für die Szene fest, einschließlich Ort, Stimmung und Umgebungsdetails, die den Ton und die Atmosphäre bestimmen. Beschreibe, was um die Figur herum passiert und wie sich das auf sie auswirkt. Die Szene bietet den Umgebungs-Kontext für die gesamte Interaktion und lenkt die schauspielerische Leistung auf subtile, organische Weise.

Beispiele:

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

#### Anmerkungen des Regisseurs

Dieser wichtige Abschnitt enthält spezifische Leistungsrichtlinien. Sie können alle anderen Elemente überspringen, wir empfehlen jedoch, dieses Element einzufügen.

Definieren Sie nur, was für die Leistung wichtig ist, und achten Sie darauf, nicht zu viele Angaben zu machen. Zu viele strenge Regeln schränken die Kreativität der Modelle ein und können zu einer schlechteren Leistung führen. Achte auf ein ausgewogenes Verhältnis zwischen der Rollen- und Szenenbeschreibung und den spezifischen Leistungsregeln.

Die häufigsten Anweisungen sind **Stil, Tempo und Akzent**. Das Modell ist jedoch nicht auf diese beschränkt und erfordert sie auch nicht. Sie können benutzerdefinierte Anweisungen hinzufügen, um zusätzliche Details zu berücksichtigen, die für Ihre Leistung wichtig sind. Dabei können Sie so viele oder so wenige Details angeben, wie nötig.

Beispiel:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Stil:**

Legt den Ton und Stil der generierten Sprache fest. Geben Sie beispielsweise „fröhlich“, „energisch“, „entspannt“ oder „gelangweilt“ an, um die Leistung zu beeinflussen. Sei beschreibend und gib so viele Details wie nötig an: *„Ansteckende Begeisterung. Der Zuhörer soll das Gefühl haben, Teil eines riesigen, aufregenden Community-Events zu sein.“* ist besser als einfach nur *„energetisch und enthusiastisch“* zu sagen.

Sie können auch Begriffe aus der Voiceover-Branche wie „vocal smile“ ausprobieren. Sie können beliebig viele Stilmerkmale kombinieren.

Beispiele:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Mehr Tiefe

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Komplex

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Akzent:**

Beschreiben Sie den gewünschten Akzent. Je genauer Ihre Angaben sind, desto besser sind die Ergebnisse. Verwenden Sie beispielsweise „*Akzent des britischen Englisch, wie er in Croydon, England, gesprochen wird*“ anstelle von „*Britischer Akzent*“.

Beispiele:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**Budgetabstufung**:

Gesamtes Pacing und Pacing-Variationen im gesamten Beitrag.

Beispiele:

Einfach

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Mehr Tiefe

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Komplex

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Transkript und Audio-Tags

Das Transkript enthält genau die Wörter, die das Modell sprechen wird. Ein Audio-Tag ist ein Wort in eckigen Klammern, das angibt, wie etwas gesagt werden soll, eine Änderung des Tons oder eine Zwischenbemerkung.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Jetzt ausprobieren**

Probieren Sie einige dieser Beispiele selbst in [AI Studio](https://aistudio.google.com/generate-speech?hl=de) aus, testen Sie unsere [TTS-App](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=de) und lassen Sie Gemini die Regie übernehmen. Hier sind einige Tipps für gute Gesangsleistungen:

- Achten Sie darauf, dass der gesamte Prompt kohärent ist. Das Skript und die Regie gehen Hand in Hand, um eine gute Leistung zu erzielen.
- Sie müssen nicht alles beschreiben. Manchmal hilft es, dem Modell Raum zu lassen, die Lücken zu füllen, um die Natürlichkeit zu erhöhen. (Just like a talented actor)
- Wenn du einmal nicht weiterkommst, kannst du dir von Gemini helfen lassen, dein Skript oder deine Performance zu erstellen.

## Sprachgenerierung per Streaming

Sie können die generierte Audioausgabe streamen, während sie vom Modell generiert wird. Dies ist nützlich, um die wahrgenommene Latenz zu verringern.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response_stream = client.models.generate_content_stream(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

for chunk in response_stream:
   try:
      data = chunk.candidates[0].content.parts[0].inline_data.data
      # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
      # Process the audio chunk (e.g., play it or write to a file)
   except (IndexError, AttributeError):
      pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        }
    }'
```

## Beschränkungen

- TTS-Modelle können nur Texteingaben empfangen und Audioausgaben generieren.
- Eine TTS-Sitzung hat ein [Kontextfenster](https://ai.google.dev/gemini-api/docs/long-context?hl=de)-Limit von 32.000 Tokens.
- Im Abschnitt [Sprachen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#languages) finden Sie Informationen zur Sprachunterstützung.
- TTS unterstützt kein Streaming für Modelle, die älter als Version 3.1 sind (Streaming wird für `gemini-3.1-flash-tts-preview` und neuere Versionen unterstützt).

Bei der Verwendung des Gemini 3.1 Flash TTS-Vorschaumodells für die Sprachgenerierung gelten die folgenden Einschränkungen:

- **Stimme stimmt nicht mit den Prompt-Anweisungen überein**:Die Ausgabe des Modells stimmt möglicherweise nicht immer genau mit dem ausgewählten Sprecher überein, sodass sich das Audio anders anhört als erwartet. Um zu vermeiden, dass der Ton nicht zum Sprecher passt (z. B. wenn eine tiefe Männerstimme versucht, wie ein junges Mädchen zu sprechen), sollten Sie darauf achten, dass der geschriebene Ton und Kontext Ihres Prompts natürlich zum Profil des ausgewählten Sprechers passen.
- **Qualität längerer Ausgaben**:Die Sprachqualität und ‑konsistenz können bei generierten Ausgaben, die länger als einige Minuten sind, nachlassen. Wir empfehlen, Ihre Transkripte in kleinere Abschnitte aufzuteilen.
- **Gelegentliche Rückgabe von Text-Tokens**:Das Modell gibt gelegentlich Text-Tokens anstelle von Audio-Tokens zurück, was dazu führt, dass der Server die Anfrage mit einem `500`-Fehler ablehnt. Da dies nur zufällig und bei einem sehr geringen Prozentsatz der Anfragen auftritt, sollten Sie in Ihrer Anwendung eine automatische Wiederholungslogik implementieren, um diese Fälle zu behandeln.
- **Falsche Ablehnungen durch den Prompt-Klassifikator**:Bei vagen Prompts wird der Sprachsynthese-Klassifikator möglicherweise nicht ausgelöst, was zu einer abgelehnten Anfrage (`PROHIBITED_CONTENT`) führt oder dazu, dass das Modell Ihre Stilanweisungen und Regieanweisungen vorliest. Validieren Sie Ihre Prompts, indem Sie eine klare Präambel hinzufügen, in der das Modell angewiesen wird, Sprache zu synthetisieren, und explizit angeben, wo das eigentliche gesprochene Transkript beginnt.

## Nächste Schritte

- [Cookbook zur Audioerstellung](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=de)
- Die [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) von Gemini bietet interaktive Optionen zur Audiogenerierung, die Sie mit anderen Modalitäten kombinieren können.
- Informationen zur Arbeit mit *Audioeingaben* finden Sie im Leitfaden [Verständnis von Audioinhalten](https://ai.google.dev/gemini-api/docs/audio?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
