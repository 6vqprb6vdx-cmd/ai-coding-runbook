---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=hi
fetched_at: 2026-09-21T06:00:06.312745+00:00
title: "\u0911\u0921\u093f\u092f\u094b \u0915\u094b \u091f\u0947\u0915\u094d\u0938\u094d\u091f \u092e\u0947\u0902 \u092c\u0926\u0932\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# ऑडियो को टेक्स्ट में बदलना

Gemini API, ऑडियो फ़ाइलों में मौजूद बोली को टेक्स्ट में बदलता है. इसके लिए, Gemini 3.5 Transcribe मॉडल (`gemini-3.5-transcribe`) का इस्तेमाल किया जाता है. Gemini की ऑडियो समझने की क्षमताओं के आधार पर, यह सटीक ट्रांसक्रिप्शन देता है. इसमें भाषा की पहचान अपने-आप होती है, बोलने वाले की पहचान होती है, शब्द-लेवल के टाइमस्टैंप होते हैं, और कस्टम शब्दावली के बारे में सुझाव मिलते हैं. इसमें [स्मार्ट ट्रांसक्रिप्शन](#transcription-modes) मोड भी मिलता है. इसमें शब्दों को सही तरीके से व्यवस्थित करने और फ़ॉर्मैट करने की सुविधा होती है.

किसी ऑडियो फ़ाइल को टेक्स्ट में बदलने के लिए, ऑडियो अपलोड करें और उसे `gemini-3.5-transcribe` को भेजें:

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

## खास जानकारी

Gemini 3.5 Transcribe को, बोली को लिखाई में बदलने के टास्क के लिए ऑप्टिमाइज़ किया गया है. यह अलग-अलग लहज़ों, बैकग्राउंड के शोर, और कई भाषाओं में की गई बातचीत को समझ सकता है.

मुख्य सुविधाओं में ये शामिल हैं:

- **अपने-आप बोली की पहचान करने की सुविधा (एएसआर):** यह [85 से ज़्यादा स्थानीय भाषाओं](#supported-languages) की पहचान अपने-आप करती है. यह सुविधा, मैन्युअल कॉन्फ़िगरेशन के बिना, एक वाक्य में और एक से ज़्यादा वाक्यों में कोड-स्विचिंग को मैनेज करती है.
- **कस्टम शब्दावली:** इसमें 1,000 वाक्यांशों को पास करके, डोमेन के हिसाब से शब्दों, छोटे नामों, और सही नामों को पहचानने की सुविधा को बेहतर बनाया जाता है.
- **स्पीकर डायराइज़ेशन:** यह सुविधा, एक से ज़्यादा लोगों की आवाज़ में अंतर करती है. साथ ही, बोले गए सेगमेंट को अलग-अलग लेबल असाइन करती है.
- **शब्द-लेवल के टाइमस्टैंप:** इससे, पहचाने गए हर शब्द के शुरू और खत्म होने के समय के सटीक ऑफ़सेट जनरेट होते हैं.
- **स्मार्ट ट्रांसक्रिप्शन:** यह सुविधा, बोलने में होने वाली रुकावटों, फ़िलर शब्दों, और दोहराव को हटा देती है. साथ ही, टेक्स्ट को व्यवस्थित फ़ॉर्मैट में बदल देती है.
- **फ़ॉर्मैट करना और सामान्य बनाना:** इसमें कैपिटल लेटर, विराम चिह्न, और टेक्स्ट को सामान्य बनाने की प्रोसेस शामिल है. जैसे, "2 करोड़ 60 लाख डॉलर" को "2.6 करोड़ डॉलर" में बदलना.

ऑडियो कॉन्टेंट के आधार पर तर्क देने या सवालों के जवाब पाने के लिए, [ऑडियो को समझना](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=hi) सुविधा का इस्तेमाल करें. टेक्स्ट-टू-स्पीच ऑडियो सिंथेसिस के लिए, [टेक्स्ट-टू-स्पीच](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi) का इस्तेमाल करें.

## भाषा का पता लगाना और सुझाव पाना

डिफ़ॉल्ट रूप से, मॉडल बोली जा रही भाषा का पता अपने-आप लगाता है. यह सुविधा, बोलने वालों के कोड-स्विच करने पर, भाषाओं के बीच डाइनैमिक तरीके से स्विच करती है.

अपने-आप पहचान होने की सुविधा का इस्तेमाल करने के लिए, `language_codes` को शामिल न करें या खाली सूची दें:

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

अगर आपको भाषा के बारे में पहले से पता है, तो ट्रांसक्रिप्शन की सटीकता को बेहतर बनाने के लिए, `language_codes` में BCP-47 भाषा कोड डालें. इसके लिए, [इस्तेमाल की जा सकने वाली भाषाएं](#supported-languages) देखें:

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

## कस्टम शब्दावली

स्पीच मॉडल को असामान्य शब्दों, तकनीकी शब्दों, ब्रैंड के नामों या व्यक्तिवाचक संज्ञाओं के बारे में बताया जा सकता है. `custom_vocabulary` ऐरे में ज़्यादा से ज़्यादा 1,000 शब्द डालें. आम तौर पर, सबसे अच्छे नतीजे 100 शब्दों तक मिलते हैं:

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

## स्पीकर डायराइज़ेशन

स्पीकर डायराइज़ेशन की सुविधा, रिकॉर्डिंग में मौजूद अलग-अलग आवाज़ों की पहचान करती है. साथ ही, हर सेगमेंट को स्पीकर आइडेंटिफ़ायर के साथ टैग करती है. जैसे, `spk_1` या `spk_2`. इसमें ज़्यादा से ज़्यादा आठ स्पीकर इस्तेमाल किए जा सकते हैं. हालांकि, तीन या उससे ज़्यादा स्पीकर के लिए एट्रिब्यूशन की सुविधा, अब भी एक्सपेरिमेंट के तौर पर उपलब्ध है.

`diarization` को `True` पर सेट करके, डायराइज़ेशन की सुविधा चालू करें:

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

## शब्दों के लेवल पर टाइमस्टैंप

शब्द-लेवल के टाइमस्टैंप से, ऑडियो स्ट्रीम में पहचाने गए हर शब्द के शुरू और खत्म होने के सटीक ऑफ़सेट मिलते हैं.

`word_timestamp` को `True` पर सेट करके, टाइमस्टैंप चालू करें:

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

स्पीकर लेबल और शब्द के टाइमस्टैंप, दोनों पाने के लिए, एक ही अनुरोध में `diarization` और `word_timestamp` को साथ में इस्तेमाल किया जा सकता है:

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

## ट्रांसक्रिप्शन मोड

Gemini 3.5 Transcribe, `mode` पैरामीटर के ज़रिए ट्रांसक्रिप्शन के दो मोड सपोर्ट करता है:

- **`VERBATIM` (डिफ़ॉल्ट)**: इसमें बोले गए हर शब्द का सटीक ट्रांसक्रिप्ट मिलता है. इसमें फ़िलर शब्दों ("अम्", "अह", "जैसे", "आपको पता है"), दोहराव, ठहराव, और गलत शुरुआत को शामिल किया जाता है. टाइमस्टैंप या स्पीकर डायराइज़ेशन का इस्तेमाल करते समय, इसकी ज़रूरत होती है.
- **`SMART` (स्मार्ट ट्रांसक्रिप्शन)**: यह सुविधा, ट्रांसक्रिप्ट को पढ़ने के लिए ऑप्टिमाइज़ करती है. इसके लिए, यह पोस्ट-प्रोसेसिंग की बेहतर तकनीक का इस्तेमाल करती है:
  - **अस्पष्टता हटाना**: बातचीत में फ़िलर शब्दों, स्टट्रिंग, और गलत शुरुआत को हटाता है.
  - **बोलते समय की गई गलतियों को ठीक करना**: यह सुविधा, बोलते समय की गई गलतियों को सीधे तौर पर ठीक करती है. उदाहरण के लिए, *"चलो मंगलवार को मिलते हैं, नहीं नहीं, बुधवार को दो बजे"* को *"चलो बुधवार को दो बजे मिलते हैं"* में बदल देती है.
  - **स्ट्रक्चर्ड फ़ॉर्मैटिंग अपने-आप होने की सुविधा**: यह सुविधा, बोले गए शब्दों को पैराग्राफ़, नंबर वाली सूचियों, बुलेट पॉइंट, फ़ॉर्मैट की गई तारीखों, मुद्राओं, और संख्याओं में अपने-आप व्यवस्थित करती है.
  - **व्याकरण से जुड़ी अशुद्धियों को ठीक करना**: इसमें विराम चिह्न, वाक्य के पहले अक्षर को कैपिटल लेटर में लिखना, और वाक्य को सही क्रम में लिखना शामिल है.

| ऑडियो कॉन्टेंट | `VERBATIM` आउटपुट | `SMART` (स्मार्ट ट्रांसक्रिप्शन) आउटपुट |
| --- | --- | --- |
| "अरे, तो मीटिंग के लिए, मुझे लगता है कि हमें, अह, ऐलिस को न्योता देना चाहिए और, नहीं, बॉब और कैरल को न्योता देना चाहिए." | "मीटिंग के लिए, हमें एलिस को न्योता देना चाहिए. नहीं, हमें बॉब और कैरल को न्योता देना चाहिए." | "मीटिंग के लिए, हमें बॉब और कैरल को न्योता भेजना चाहिए." |
| "पहले आइटम की समीक्षा करो, दूसरे आइटम के लिए बजट तय करो, तीसरे आइटम के लिए समयसीमा तय करो, और रीकैप भेजो" | "first item review budget second item finalize timeline third item send recap" | "1. बजट की समीक्षा करें 2. टाइमलाइन को फ़ाइनल करें 3. रीकैप भेजो" |

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

## ट्रांसक्रिप्शन आउटपुट को पार्स किया जा रहा है

पूरी ट्रांसक्रिप्ट का टेक्स्ट `response.text` में दिखता है.

`word_timestamp` या `diarization` चालू होने पर, एपीआई शब्दों के लेवल पर एनोटेशन और उम्मीदवार के हिस्सों से जुड़े स्पीकर लेबल भी दिखाता है.

यहां शब्दों के टाइमस्टैंप और स्पीकर के बोलने की बारी को निकालने और उन पर बार-बार काम करने का तरीका बताया गया है:

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

## इस्तेमाल की जा सकने वाली भाषाएं

Gemini 3.5 Transcribe के लिए, यहाँ दी गई भाषाएँ और BCP-47 भाषा कोड इस्तेमाल किए जा सकते हैं:

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अफ़्रीकान्स | `af-ZA` | जापानी | `ja-JP` |
| अमहैरिक | `am-ET` | जावानीज़ | `jv-ID` |
| अरबी (मिस्र) | `ar-EG` | Kabuverdianu | `kea-CV` |
| आर्मीनियन | `hy-AM` | कन्नड़ | `kn-IN` |
| असमिया | `as-IN` | कज़ाक | `kk-KZ` |
| अज़रबैजानी | `az-AZ` | कोरियन | `ko-KR` |
| बेलारूसी | `be-BY` | किर्गिज़ | `ky-KG` |
| बांग्ला (बांग्लादेश) | `bn-BD` | लातवियन | `lv-LV` |
| बांग्ला (भारत) | `bn-IN` | लिंगाला | `ln-CD` |
| बोस्नियन | `bs-BA` | लिथुएनियन | `lt-LT` |
| बल्गैरियन | `bg-BG` | मैसेडोनियन | `mk-MK` |
| बल्गेरियन (ऐरोमेनियन) | `rup-BG` | मलय | `ms-MY` |
| बर्मीज़ | `my-MM` | मलयालम | `ml-IN` |
| कैंटोनीज़ (ट्रेडिशनल) | `yue-Hant-HK` | मोल्टीज़ | `mt-MT` |
| कैटलैन | `ca-ES` | मैंडरिन चाइनीज़ (सिंप्लिफ़ाइड) | `cmn-Hans-CN` |
| सेबुआनो | `ceb` | मराठी | `mr-IN` |
| सेंट्रल खमेर | `km-KH` | मंगोलियन | `mn-MN` |
| क्रोएशियन | `hr-HR` | नेपाली | `ne-NP` |
| चेक | `cs-CZ` | नॉर्वीजन | `nb-NO` |
| डैनिश | `da-DK` | ओड़िया | `or-IN` |
| डच | `nl-NL` | पोलिश | `pl-PL` |
| अंग्रेज़ी (ग्रेट ब्रिटेन) | `en-GB` | पॉर्चुगीज़ (ब्राज़ील) | `pt-BR` |
| अंग्रेज़ी (भारत) | `en-IN` | पॉर्चगीज़ (पुर्तगाल) | `pt-PT` |
| अंग्रेज़ी (संयुक्त राज्य अमेरिका) | `en-US` | पंजाबी | `pa-IN` |
| एस्टोनियन | `et-EE` | पंजाबी (गुरमुखी लिपि) | `pa-Guru-IN` |
| फ़ारसी | `fa-IR` | रोमानियन | `ro-RO` |
| फ़िलिपीनी | `fil-PH` | रूसी | `ru-RU` |
| फ़िनिश | `fi-FI` | सर्बियन | `sr-RS` |
| फ़्रांसीसी | `fr-FR` | सिंधी (अरबी लिपि) | `sd-Arab-IN` |
| गैलिशियन | `gl-ES` | स्लोवाक | `sk-SK` |
| जॉर्जियन | `ka-GE` | स्लोवेनियन | `sl-SI` |
| जर्मन | `de-DE` | स्पैनिश (लैटिन अमेरिका) | `es-419` |
| ग्रीक | `el-GR` | स्पैनिश (संयुक्त राज्य अमेरिका) | `es-US` |
| गुजराती | `gu-IN` | स्वाहिली (केन्या) | `sw-KE` |
| हौसा | `ha-NG` | स्वीडिश | `sv-SE` |
| हिब्रू | `he-IL` | ताजिक | `tg-TJ` |
| हिन्दी | `hi-IN` | तेलुगु | `te-IN` |
| हंगेरियन | `hu-HU` | थाई | `th-TH` |
| आइसलैंडिक | `is-IS` | टर्किश | `tr-TR` |
| इंडियन इंग्लिश | `en-IN` | यूक्रेनियन | `uk-UA` |
| इंडोनेशियन | `id-ID` | उज़्बेक | `uz-UZ` |
| इटैलियन | `it-IT` | वियतनामीज़ | `vi-VN` |

## इस्तेमाल किए जा सकने वाले ऑडियो फ़ॉर्मैट

Gemini 3.5 Transcribe, इन ऑडियो फ़ॉर्मैट के MIME टाइप के साथ काम करता है:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

इस्तेमाल किए जा सकने वाले MIME टाइप और पैरामीटर स्कीमा की पूरी सूची देखने के लिए, [Interactions API का रेफ़रंस](https://ai.google.dev/api/interactions-api?hl=hi#Resource:Content) देखें.

## पैरामीटर का रेफ़रंस

`GenerateContentConfig` में मौजूद `audio_transcription_config` ऑब्जेक्ट में फ़ील्ड सेट करके, ट्रांसक्रिप्शन की सुविधा कॉन्फ़िगर करें:

| फ़ील्ड | टाइप | ब्यौरा |
| --- | --- | --- |
| `language_codes` | स्ट्रिंग का कलेक्शन | BCP-47 भाषा कोड (जैसे, `["en-US"]`). अगर इसे शामिल नहीं किया जाता है या यह खाली (`[]`) है, तो मॉडल अपने-आप भाषा का पता लगाता है और कोड-स्विचिंग को मैनेज करता है. |
| `custom_vocabulary` | स्ट्रिंग का कलेक्शन | ज़्यादा से ज़्यादा 1,000 कस्टम शब्द, संक्षिप्त नाम या व्यक्तिवाचक संज्ञाएं, ताकि बोली की पहचान करने की सुविधा को बेहतर बनाया जा सके. यह सुविधा, स्पीकर के हिसाब से ऑडियो को अलग-अलग हिस्सों में बांटने और शब्द-लेवल के टाइमस्टैंप के साथ काम नहीं करती. |
| `word_timestamp` | बूलियन | शब्द की शुरुआत और खत्म होने के ऑफ़सेट शामिल करने के लिए, इसे `True` पर सेट करें. अगर इसे शामिल नहीं किया जाता है या `False` पर सेट किया जाता है, तो शब्दों के टाइमस्टैंप नहीं दिखाए जाते. कस्टम शब्दावली के साथ काम नहीं करता. |
| `diarization` | बूलियन | अलग-अलग लोगों की आवाज़ की पहचान करने और उन्हें लेबल करने के लिए, इसे `True` पर सेट करें. कस्टम शब्दावली के साथ काम नहीं करता. |
| `mode` | स्ट्रिंग | बोली को लेख में बदलने का मोड. इस्तेमाल की जा सकने वाली वैल्यू: `"VERBATIM"` (डिफ़ॉल्ट) और `"SMART"`. यह टाइमस्टैंप और डायराइज़ेशन के साथ काम नहीं करता. |

## सबसे सही तरीके

- **साफ़ ऑडियो दें:** पक्का करें कि ऑडियो रिकॉर्डिंग में आवाज़ साफ़ सुनाई दे और उसमें कोई गड़बड़ी न हो.
- **ऑडियो की भाषा की जानकारी दें:** अगर आपको ऑडियो की भाषा के बारे में पहले से पता है, तो `language_codes` को सेट करें, ताकि ऑडियो को टेक्स्ट में ज़्यादा सटीक तरीके से बदला जा सके.
- **कस्टम शब्दावली को टारगेट करना:** `custom_vocabulary` में रोज़मर्रा के आम शब्दों के बजाय, सिर्फ़ अलग-अलग डोमेन टर्म, ब्रैंड के नाम या संज्ञाएं शामिल करें.
- **ज़्यादा बड़ी रिकॉर्डिंग के लिए, Files API का इस्तेमाल करें:** अगर फ़ाइल कुछ सेकंड से ज़्यादा लंबी है, तो `client.files.upload` का इस्तेमाल करके फ़ाइल अपलोड करें. इसके बाद, मॉडल के कॉन्टेंट में अपलोड की गई फ़ाइल को पास करें.

## सीमाएं

- **ऑडियो की अवधि:** स्टैंडर्ड यूनरी अनुरोधों में, एक घंटे तक की ऑडियो फ़ाइलें इस्तेमाल की जा सकती हैं. स्पीकर के हिसाब से लेबलिंग या शब्द-लेवल के टाइमस्टैंप जैसी सुविधाएं चालू होने पर, ऑडियो प्रोसेसिंग सिर्फ़ 30 मिनट तक की जा सकती है.
- **शब्द के लेवल पर टाइमस्टैंप:** शब्द के लेवल पर टाइमस्टैंप की सुविधा चालू करने से, ट्रांसक्रिप्शन की कुल सटीकता कम हो सकती है.
- **स्पीकर डायराइज़ेशन:** स्पीकर डायराइज़ेशन की सुविधा, आठ स्पीकर तक काम करती है. तीन या इससे ज़्यादा स्पीकर के लिए, स्पीकर एट्रिब्यूशन की सुविधा अभी एक्सपेरिमेंट के तौर पर उपलब्ध है.
- **कस्टम शब्दावली:** `custom_vocabulary` में ज़्यादा से ज़्यादा 1,000 शब्द जोड़े जा सकते हैं. हालांकि, आम तौर पर 100 शब्दों से ही सबसे अच्छे नतीजे मिलते हैं. `custom_vocabulary` को स्पीकर के हिसाब से लेबल करने या शब्द-लेवल के टाइमस्टैंप के साथ इस्तेमाल नहीं किया जा सकता. एपीआई, उन अनुरोधों को अस्वीकार कर देता है जिनमें `custom_vocabulary` के साथ इनमें से किसी भी सुविधा का इस्तेमाल किया गया हो.
- **मोड के साथ काम करने की सुविधा:** स्मार्ट ट्रांसक्रिप्शन (`mode: "SMART"`) को `word_timestamp` या `diarization` के साथ इस्तेमाल नहीं किया जा सकता.

## आगे क्या करना है

- लाइव एपीआई का इस्तेमाल करके, [बोली को लेख में बदलने की सुविधा से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=hi) की मदद से, रीयल-टाइम में ऑडियो स्ट्रीम करें.
- ऑडियो कॉन्टेंट का विश्लेषण करने, उसकी खास जानकारी पाने या उससे जुड़े सवाल पूछने के लिए, [ऑडियो को समझना](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=hi) सुविधा का इस्तेमाल करें.
- [लिखाई को बोली में बदलने की सुविधा](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi) का इस्तेमाल करके, टेक्स्ट से ऑडियो बनाने का तरीका जानें.
- मॉडल की कीमत और टोकन की सीमा जानने के लिए, [कीमत तय करने वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#gemini-3.5-transcribe) देखें.
- मीडिया फ़ाइलें अपलोड करने और उन्हें मैनेज करने के बारे में ज़्यादा जानने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) गाइड देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-08 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-08 (UTC) को अपडेट किया गया."],[],[]]
