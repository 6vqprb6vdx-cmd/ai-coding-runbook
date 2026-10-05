---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=de
fetched_at: 2026-10-05T06:37:19.772323+00:00
title: "Audiotranskript \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Audiotranskript

Die Gemini API wandelt Sprache in Audiodateien mit dem Gemini 3.5 Transcribe-Modell (`gemini-3.5-transcribe`) in Text um. Basierend auf den Audio-Analysefunktionen von Gemini bietet sie eine genaue Transkription mit automatischer Spracherkennung, Sprecherzuordnung, Zeitstempeln auf Wortebene und benutzerdefinierten Vokabelhinweisen. Außerdem gibt es einen [intelligenten Transkriptionsmodus](#transcription-modes), in dem Füllwörter entfernt und die Formatierung optimiert wird.

Wenn Sie eine Audiodatei transkribieren möchten, laden Sie die Audiodatei hoch und übergeben Sie sie an `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## Übersicht

Gemini 3.5 Transcribe ist für Speech-to-Text-Aufgaben optimiert. Sie kommt mit verschiedenen Akzenten, Hintergrundgeräuschen und mehrsprachigen Unterhaltungen zurecht.

Zu den wichtigsten Funktionen gehören:

- **Automatische Spracherkennung (ASR)**: Erkennt automatisch Sprachen in [über 85 Regionen](#supported-languages). Es werden Code-Switching innerhalb und zwischen Sätzen ohne manuelle Konfiguration unterstützt.
- **Benutzerdefiniertes Vokabular**:Die Erkennung wird auf domainspezifische Begriffe, Akronyme und Eigennamen ausgerichtet, indem bis zu 1.000 Wortgruppen übergeben werden.
- **Sprecherzuordnung**:Unterscheidet zwischen mehreren Sprechern und weist gesprochene Segmente bestimmten Labels zu.
- **Zeitstempel auf Wortebene**:Generiert genaue Start- und Endzeit-Offsets für jedes erkannte Wort.
- **Intelligente Transkription**:Sprachfehler, Füllwörter und Wiederholungen werden entfernt und eine strukturierte Formatierung wird angewendet.
- **Formatierung und Normalisierung**:Hier werden Großschreibung, Zeichensetzung und inverse Textnormalisierung angewendet, z. B. wird „twenty six million dollars“ in „$26M“ umgewandelt.

Wenn Sie Audioinhalte allgemein analysieren oder Fragen zu Audioinhalten beantworten lassen möchten, verwenden Sie [Audio-Analyse](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=de). Für die Audiosynthese mit Text-to-Speech verwenden Sie [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=de).

## Spracherkennung und Hinweise

Standardmäßig wird die gesprochene Sprache automatisch erkannt. Die Sprache wird dynamisch gewechselt, wenn die Sprecher die Sprache wechseln.

Wenn Sie die automatische Erkennung verwenden möchten, lassen Sie `language_codes` weg oder geben Sie eine leere Liste an:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

Wenn Sie die Sprache im Voraus kennen, geben Sie BCP-47-Sprachcodes in `language_codes` an, um die Genauigkeit der Transkription zu verbessern (siehe [Unterstützte Sprachen](#supported-languages)):

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## Benutzerdefiniertes Vokabular

Sie können das Sprachmodell auf ungewöhnliche Wörter, Fachjargon, Markennamen oder Eigennamen ausrichten. Geben Sie bis zu 1.000 Begriffe im `custom_vocabulary`-Array an. Die besten Ergebnisse werden in der Regel mit bis zu 100 Begriffen erzielt:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Sprecherbestimmung

Bei der Sprecherbestimmung werden verschiedene Stimmen in der Aufnahme identifiziert und jedes Segment wird mit einer Sprecher-ID wie `spk_1` oder `spk_2` getaggt. Es werden bis zu acht Sprecher unterstützt. Die Zuordnung für drei oder mehr Sprecher ist experimentell.

Aktivieren Sie die Sprecherbestimmung, indem Sie `diarization` auf `True` setzen:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## Zeitstempel auf Wortebene

Zeitstempel auf Wortebene liefern genaue Start- und End-Offsets für jedes erkannte Wort im Audio-Stream.

Aktivieren Sie Zeitstempel, indem Sie `word_timestamp` auf `True` setzen:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

Sie können `diarization` und `word_timestamp` in einer einzigen Anfrage kombinieren, um sowohl Sprecherlabels als auch Wortzeitstempel zu erhalten:

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true
    }
  }
}
```

## Transkriptionsmodi

Gemini 3.5 Transcribe unterstützt zwei Transkriptionsmodi über den Parameter `mode`:

- **`VERBATIM` (Standard)**: Gibt ein exaktes Wort-für-Wort-Transkript von allem Gesprochenen zurück, wobei Füllwörter („um“, „äh“, „wie“, „du weißt schon“), Wiederholungen, Pausen und Fehlstarts beibehalten werden. Erforderlich, wenn Zeitstempel oder die Sprecherzuordnung verwendet werden.
- **`SMART` (Smart Transcription)**: Das Transkript wird durch intelligente Nachbearbeitung für die Anzeige optimiert:
  - **Entfernen von Füllwörtern**: Füllwörter, Stottern und Fehlstarts werden entfernt.
  - **Inline-Korrekturen**: Gesprochene Korrekturen werden direkt berücksichtigt. Aus *„Lass uns am Dienstag treffen, nein, am Mittwoch um 14:00 Uhr“* wird beispielsweise *„Lass uns am Mittwoch um 14:00 Uhr treffen“*.
  - **Automatische strukturierte Formatierung**: Gesprochene Gedanken werden automatisch in Absätze, nummerierte Listen, Stichpunkte, formatierte Datumsangaben, Währungen und Zahlen strukturiert.
  - **Grammatische Bereinigung**: Wendet natürliche Satzzeichen, Groß- und Kleinschreibung und einen natürlichen Fluss an.

| Gesprochene Audioinhalte | `VERBATIM`-Ausgabe | `SMART`-Ausgabe (Smart Transcription) |
| --- | --- | --- |
| „Ähm, also für die Besprechung sollten wir, äh, Alice einladen und, nein, Bob und Carol.“ | „Für die Besprechung sollten wir Alice und nein, Bob und Carol einladen.“ | „Ich denke, wir sollten Bob und Carol zu dem Meeting einladen.“ |
| „First item review budget second item finalize timeline third item send recap“ (Erstens Budget für ersten Artikel prüfen, zweitens Zeitachse für zweiten Artikel fertigstellen, drittens Zusammenfassung senden) | „first item review budget second item finalize timeline third item send recap“ (erstes Element: Budget prüfen; zweites Element: Zeitachse fertigstellen; drittes Element: Zusammenfassung senden) | "1. Prüfen Sie das Budget 2. Zeitachse fertigstellen 3. Zusammenfassung senden“ |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## Transkriptionsausgabe parsen

Der vollständige Transkripttext wird in `response.text` zurückgegeben.

Wenn `word_timestamp` oder `diarization` aktiviert ist, gibt die API auch detaillierte Anmerkungen auf Wortebene und Sprecherlabels zurück, die den Kandidatenteilen zugeordnet sind.

So extrahieren und durchlaufen Sie Wortzeitstempel und Sprecherwechsel:

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

## Unterstützte Sprachen

Die folgenden Sprachen und BCP-47-Sprachcodes werden für Gemini 3.5 Transcribe unterstützt:

| Sprache | BCP-47-Code | Sprache | BCP-47-Code |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japanisch | `ja-JP` |
| Amharisch | `am-ET` | Javanisch | `jv-ID` |
| Arabisch (Ägypten) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armenisch | `hy-AM` | Kannada | `kn-IN` |
| Assamesisch | `as-IN` | Kasachisch | `kk-KZ` |
| Aserbaidschanisch | `az-AZ` | Koreanisch | `ko-KR` |
| Belarussisch | `be-BY` | Kirgisisch | `ky-KG` |
| Bengalisch (Bangladesch) | `bn-BD` | Lettisch | `lv-LV` |
| Bengalisch (Indien) | `bn-IN` | Lingala | `ln-CD` |
| Bosnisch | `bs-BA` | Litauisch | `lt-LT` |
| Bulgarisch | `bg-BG` | Mazedonisch | `mk-MK` |
| Bulgarisch (Aromanisch) | `rup-BG` | Malaiisch | `ms-MY` |
| Burmesisch | `my-MM` | Malayalam | `ml-IN` |
| Kantonesisch (traditionell) | `yue-Hant-HK` | Maltesisch | `mt-MT` |
| Katalanisch | `ca-ES` | Chinesisch (Mandarin, vereinfacht) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Standard-Khmer | `km-KH` | Mongolisch | `mn-MN` |
| Kroatisch | `hr-HR` | Nepalesisch | `ne-NP` |
| Tschechien | `cs-CZ` | Norwegisch | `nb-NO` |
| Dänisch | `da-DK` | Oriya | `or-IN` |
| Niederländisch | `nl-NL` | Polnisch | `pl-PL` |
| Englisch (Vereinigtes Königreich) | `en-GB` | Portugiesisch (Brasilien) | `pt-BR` |
| Englisch (Indien) | `en-IN` | Portugiesisch (Portugal) | `pt-PT` |
| Englisch (USA) | `en-US` | Punjabi | `pa-IN` |
| Estnisch | `et-EE` | Panjabi (Gurmukhi-Schrift) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Rumänisch | `ro-RO` |
| Filipino | `fil-PH` | Russisch | `ru-RU` |
| Finnisch | `fi-FI` | Serbisch | `sr-RS` |
| Französisch | `fr-FR` | Sindhi (arabische Schrift) | `sd-Arab-IN` |
| Galizisch | `gl-ES` | Slowakisch | `sk-SK` |
| Georgisch | `ka-GE` | Slowenisch | `sl-SI` |
| Deutsch | `de-DE` | Spanisch (Lateinamerika) | `es-419` |
| Griechisch | `el-GR` | Spanisch (USA) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenia) | `sw-KE` |
| Hausa | `ha-NG` | Schwedisch | `sv-SE` |
| Hebräisch | `he-IL` | Tadschikisch | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Ungarisch | `hu-HU` | Thailändisch | `th-TH` |
| Isländisch | `is-IS` | Türkisch | `tr-TR` |
| Indisches Englisch | `en-IN` | Ukrainisch | `uk-UA` |
| Indonesisch | `id-ID` | Usbekisch | `uz-UZ` |
| Italienisch | `it-IT` | Vietnamesisch | `vi-VN` |

## Unterstützte Audioformate

Gemini 3.5 Transcribe unterstützt die folgenden MIME-Typen für Audioformate:

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

Eine vollständige Liste der unterstützten MIME-Typen und Parameterschemas finden Sie in der [Interactions API-Referenz](https://ai.google.dev/api/interactions-api?hl=de#Resource:Content).

## Parameterverweis

Konfigurieren Sie die Transkription, indem Sie Felder im `audio_transcription_config`-Objekt in `GenerateContentConfig` festlegen:

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `language_codes` | String-Array | BCP-47-Sprachcodes (z.B. `["en-US"]`). Wenn dieser Parameter weggelassen oder leer ist (`[]`), erkennt das Modell die Sprache automatisch und verarbeitet Sprachwechsel. |
| `custom_vocabulary` | String-Array | Bis zu 1.000 benutzerdefinierte Begriffe, Akronyme oder Eigennamen, um die Spracherkennung zu optimieren. Nicht kompatibel mit Sprecherbestimmung und Zeitstempeln auf Wortebene. |
| `word_timestamp` | Boolesch | Auf `True` festgelegt, um Wortanfangs- und ‑endoffsets einzuschließen. Wenn weggelassen oder `False`, werden keine Wort-Zeitstempel zurückgegeben. Nicht mit benutzerdefiniertem Vokabular kompatibel. |
| `diarization` | Boolesch | Auf `True` setzen, um verschiedene Sprecher zu identifizieren und zu kennzeichnen. Nicht mit benutzerdefiniertem Vokabular kompatibel. |
| `mode` | String | Transkriptionsmodus Unterstützte Werte: `"VERBATIM"` (Standard) und `"SMART"`. Nicht kompatibel mit Zeitstempeln und Sprecherbestimmung. |

## Best Practices

- **Saubere Audioinhalte bereitstellen**:Achten Sie darauf, dass die Sprachaufnahmen klar getrennt sind und es nicht zu starkem Clipping kommt.
- **Sprachhinweise angeben, wenn bekannt**:Wenn Sie die Sprache des Audios im Voraus kennen, geben Sie `language_codes` an, um die Genauigkeit zu maximieren.
- **Benutzerdefiniertes Vokabular für das Zielvorhaben**:Verwenden Sie in `custom_vocabulary` nur eindeutige Fachbegriffe, Markennamen oder Eigennamen und keine gängigen Alltagswörter.
- **Files API für große Aufzeichnungen verwenden**:Bei Dateien, die länger als einige Sekunden sind, laden Sie die Datei mit `client.files.upload` hoch und übergeben Sie die zurückgegebene Datei an den Modellinhalt.

## Beschränkungen

- **Audiodauer**:Standardmäßige unäre Anfragen unterstützen Audiodateien mit einer Länge von bis zu einer Stunde. Die Audioverarbeitung ist auf 30 Minuten begrenzt, wenn Funktionen wie die Sprecherbestimmung oder Zeitstempel auf Wortebene aktiviert sind.
- **Zeitstempel auf Wortebene**:Wenn Sie Zeitstempel auf Wortebene aktivieren, kann sich die allgemeine Transkriptionsgenauigkeit verschlechtern.
- **Sprecherbestimmung**:Die Sprecherbestimmung unterstützt bis zu 8 Sprecher. Die Sprecherzuordnung für mindestens drei Sprecher ist noch in der Testphase.
- **Benutzerdefiniertes Vokabular**:Sie können bis zu 1.000 Begriffe in `custom_vocabulary` angeben. Die besten Ergebnisse werden jedoch in der Regel mit bis zu 100 Begriffen erzielt. `custom_vocabulary` kann nicht mit der Sprecherzuordnung oder Zeitstempeln auf Wortebene kombiniert werden. Die API lehnt Anfragen ab, in denen `custom_vocabulary` zusammen mit einer der beiden Funktionen angegeben wird.
- **Moduskompatibilität**:Die intelligente Transkription (`mode: "SMART"`) kann nicht mit `word_timestamp` oder `diarization` kombiniert werden.

## Nächste Schritte

- Mit der Live API können Sie Audio in Echtzeit streamen. Eine Anleitung dazu finden Sie im [Leitfaden zur Live-Transkription](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=de).
- Mit [Audio understanding](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=de) können Sie Audioinhalte analysieren, zusammenfassen oder abfragen.
- Hier erfahren Sie, wie Sie mit [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=de) Audioinhalte aus Text synthetisieren.
- Informationen zu Modellpreisen und Tokenlimits finden Sie auf der [Seite „Preise“](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.5-transcribe).
- Weitere Informationen zum Hochladen und Verwalten von Media-Dateien finden Sie im [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de)-Leitfaden.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-08 (UTC)."],[],[]]
