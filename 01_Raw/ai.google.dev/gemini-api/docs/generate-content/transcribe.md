---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=zh-TW
fetched_at: 2026-09-07T05:42:36.612774+00:00
title: "\u97f3\u8a0a\u8f49\u9304 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 音訊轉錄

Gemini API 會使用 Gemini 3.5 Transcribe 模型 (`gemini-3.5-transcribe`)，將音訊檔案中的語音轉換為文字。根據 Gemini 的音訊理解能力，這項 API 可提供準確的轉錄內容，並自動辨識語言、區分說話者、提供字詞層級的時間戳記，以及自訂詞彙提示。此外，這項功能還提供[智慧轉錄](#transcription-modes)模式，可移除贅詞並智慧格式化。

如要轉錄音訊檔案，請上傳音訊並傳遞至 `gemini-3.5-transcribe`：

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

## 總覽

Gemini 3.5 Transcribe 專為語音轉文字工作而生，可處理各種口音、背景噪音和多語言對話。

主要功能如下所示：

- **自動語音辨識 (ASR)：**自動偵測 [85 種以上的語言](#supported-languages)。處理句子內和句子間的程式碼切換，無須手動設定。
- **自訂詞彙：**傳遞最多 1,000 個詞組，讓辨識結果偏向特定領域的詞彙、縮寫和專有名詞。
- **講者區分：**區分多位講者，並為說話片段加上不同標籤。
- **字詞層級時間戳記：**為每個辨識出的字詞產生精確的開始和結束時間偏移。
- **智慧轉錄：**清除贅字、重複內容和語病，並套用結構化格式。
- **格式和正規化：**套用大小寫、標點符號和反向文字正規化，例如將「二十六 million dollars」轉換為「$26M」。

如要對音訊內容進行一般音訊推理或問答，請使用[音訊理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=zh-tw)。如要合成文字轉語音音訊，請使用 [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-tw)。

## 語言偵測和提示

根據預設，模型會自動偵測說話者使用的語言。當講者切換語言時，這項功能會動態切換語言。

如要使用自動偵測功能，請省略 `language_codes` 或提供空白清單：

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

如果預先知道語言，請在 `language_codes` 中指定 BCP-47 語言代碼，以提高語音轉錄準確率 (請參閱「[支援的語言](#supported-languages)」)：

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

## 自訂詞彙

你可以引導語音模型辨識不常見的字詞、專業術語、品牌名稱或專有名詞。在 `custom_vocabulary` 陣列中提供最多 1,000 個字詞 (通常最多 100 個字詞就能獲得最佳結果)：

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

## 說話者分段標記

說話者分段標記功能會識別錄音中不同的聲音，並為每個片段加上說話者 ID，例如 `spk_1` 或 `spk_2`。最多支援 8 個音箱 (3 個以上音箱的歸因功能為實驗功能)。

將 `diarization` 設為 `True`，即可啟用分段標記：

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

## 字詞層級時間戳記

字詞層級時間戳記會提供音訊串流中每個辨識字詞的確切開始和結束偏移。

將 `word_timestamp` 設為 `True`，即可啟用時間戳記：

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

您可以在單一要求中合併 `diarization` 和 `word_timestamp`，同時取得發言者標籤和字詞時間戳記：

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
        custom_vocabulary=["Gemini"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
    customVocabulary: ["Gemini"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true,
      "customVocabulary": ["Gemini"]
    }
  }
}
```

## 轉錄模式

Gemini 3.5 Transcribe 支援兩種轉錄模式，可透過 `mode` 參數設定：

- **`VERBATIM` (預設)：**逐字轉錄所有說出的內容，保留原始的填充詞 (例如「嗯」、「呃」、「像」、「你知道」)、重複內容、停頓和錯誤開頭。使用時間戳記或說話者區分功能時，必須提供這項資訊。
- **`SMART` (智慧轉錄)**：透過智慧後續處理，讓轉錄稿更易於閱讀：
  - **移除贅詞**：移除對話中的贅詞、口吃和錯誤開場白。
  - **即時修正**：直接解決口語修正內容 (例如「我們星期二碰面，不對，星期三下午兩點」會變成「我們星期三下午兩點碰面」)。
  - **自動結構化格式**：自動將口述內容結構化為段落、編號清單、項目符號、格式化日期、貨幣和數字。
  - **文法清理**：套用自然的標點符號、句子大小寫和流暢度。

| 語音音訊 | `VERBATIM` 輸出 | `SMART` (智慧轉錄) 輸出內容 |
| --- | --- | --- |
| 「嗯，所以我覺得我們應該邀請愛麗絲參加會議，等等，不是，是小明和卡羅。」 | 「嗯，所以我覺得我們應該邀請愛麗絲參加會議，等等，是鮑伯和卡羅。」 | 「我覺得應該邀請 Bob 和 Carol 參加會議。」 |
| 「First item review budget second item finalize timeline third item send recap」(先審查預算，再確定時間表，最後傳送摘要) | 「first item review budget second item finalize timeline third item send recap」(第一個項目審查預算，第二個項目確定時間軸，第三個項目傳送摘要) | 「1. 查看預算 2. 完成時間軸 3. 傳送摘要」 |

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

## 剖析轉錄輸出內容

完整轉錄稿文字會以 `response.text` 形式傳回。

啟用 `word_timestamp` 或 `diarization` 時，API 也會傳回附加至候選部分的詳細字詞層級註解和發言者標籤。

以下說明如何擷取及疊代字詞時間戳記和說話者輪流說話的片段：

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

## 支援的語言

Gemini 3.5 Transcribe 支援下列語言和 BCP-47 語言代碼：

| 語言 | BCP-47 代碼 | 語言 | BCP-47 代碼 |
| --- | --- | --- | --- |
| 南非荷蘭文 | `af-ZA` | 日文 | `ja-JP` |
| 阿姆哈拉文 | `am-ET` | 爪哇語 | `jv-ID` |
| 阿拉伯文 (埃及) | `ar-EG` | Kabuverdianu | `kea-CV` |
| 亞美尼亞文 | `hy-AM` | 卡納達文 | `kn-IN` |
| 阿薩姆文 | `as-IN` | 哈薩克文 | `kk-KZ` |
| 亞塞拜然文 | `az-AZ` | 韓文 | `ko-KR` |
| 白俄羅斯語 | `be-BY` | 吉爾吉斯文 | `ky-KG` |
| 孟加拉文 (孟加拉) | `bn-BD` | 拉脫維亞文 | `lv-LV` |
| 孟加拉文 (印度) | `bn-IN` | 林格拉文 | `ln-CD` |
| 波士尼亞文 | `bs-BA` | 立陶宛文 | `lt-LT` |
| 保加利亞文 | `bg-BG` | 馬其頓文 | `mk-MK` |
| 保加利亞文 (阿羅馬尼亞文) | `rup-BG` | 馬來文 | `ms-MY` |
| 緬甸文 | `my-MM` | 馬拉雅拉姆文 | `ml-IN` |
| 粵語 (繁體) | `yue-Hant-HK` | 馬爾他文 | `mt-MT` |
| 加泰隆尼亞文 | `ca-ES` | 中文 (簡體) | `cmn-Hans-CN` |
| 宿霧文 | `ceb` | 馬拉地文 | `mr-IN` |
| 中部高棉文 | `km-KH` | 蒙古文 | `mn-MN` |
| 克羅埃西亞文 | `hr-HR` | 尼泊爾文 | `ne-NP` |
| 捷克文 | `cs-CZ` | 挪威文 | `nb-NO` |
| 丹麥文 | `da-DK` | 奧里雅文 | `or-IN` |
| 荷蘭文 | `nl-NL` | 波蘭文 | `pl-PL` |
| 英文 (英國) | `en-GB` | 葡萄牙文 (巴西) | `pt-BR` |
| 英文 (印度) | `en-IN` | 葡萄牙文 (葡萄牙) | `pt-PT` |
| 英文 (美國) | `en-US` | 旁遮普文 | `pa-IN` |
| 愛沙尼亞文 | `et-EE` | 旁遮普文 (古爾穆基字母) | `pa-Guru-IN` |
| 波斯文 | `fa-IR` | 羅馬尼亞文 | `ro-RO` |
| 菲律賓文 | `fil-PH` | 俄文 | `ru-RU` |
| 芬蘭文 | `fi-FI` | 塞爾維亞文 | `sr-RS` |
| 法文 | `fr-FR` | 信德文 (阿拉伯字母) | `sd-Arab-IN` |
| 加里西亞文 | `gl-ES` | 斯洛伐克文 | `sk-SK` |
| 喬治亞文 | `ka-GE` | 斯洛維尼亞文 | `sl-SI` |
| 德文 | `de-DE` | 西班牙文 (拉丁美洲) | `es-419` |
| 希臘文 | `el-GR` | 西班牙文 (美國) | `es-US` |
| 古吉拉特文 | `gu-IN` | 斯瓦希里文 (肯亞) | `sw-KE` |
| 豪薩文 | `ha-NG` | 瑞典文 | `sv-SE` |
| 希伯來文 | `he-IL` | 塔吉克文 | `tg-TJ` |
| 北印度文 | `hi-IN` | 泰盧固文 | `te-IN` |
| 匈牙利文 | `hu-HU` | 泰文 | `th-TH` |
| 冰島文 | `is-IS` | 土耳其文 | `tr-TR` |
| 印度英語 | `en-IN` | 烏克蘭文 | `uk-UA` |
| 印尼文 | `id-ID` | 烏茲別克文 | `uz-UZ` |
| 義大利文 | `it-IT` | 越南文 | `vi-VN` |

## 支援的音訊格式

Gemini 3.5 Transcribe 支援下列音訊格式 MIME 類型：

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

如需支援的 MIME 類型和參數結構定義完整清單，請參閱 [Interactions API 參考資料](https://ai.google.dev/api/interactions-api?hl=zh-tw#Resource:Content)。

## 參數參照

在 `GenerateContentConfig` 中設定 `audio_transcription_config` 物件內的欄位，即可設定轉錄功能：

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `language_codes` | 字串陣列 | BCP-47 語言代碼 (例如 `["en-US"]`)。如果省略或空白 (`[]`)，模型會自動偵測語言並處理代碼切換。 |
| `custom_vocabulary` | 字串陣列 | 最多 1,000 個自訂字詞、縮寫或專有名詞，可調整語音辨識結果。 |
| `word_timestamp` | 布林值 | 設為 `True` 可納入字詞的開始和結束偏移量。如果省略或設為 `False`，就不會傳回字詞時間戳記。 |
| `diarization` | 布林值 | 設為 `True` 可識別不同的說話者並加上標籤。 |
| `mode` | 字串 | 轉錄模式。支援的值：`"VERBATIM"` (預設值) 和 `"SMART"`。不支援時間戳記和分段標記。 |

## 最佳做法

- **提供清晰的音訊：**確保錄音的語音分離度良好，並避免嚴重剪輯。
- **已知語言時提供語言提示：**如果預先知道音訊語言，請指定 `language_codes`，盡可能提高準確度。
- **目標自訂詞彙：**請只在 `custom_vocabulary` 中加入不重複的網域字詞、品牌名稱或專有名詞，而非常見的日常用語。
- **使用 Files API 處理大型錄音檔：**如要上傳長度超過幾秒的檔案，請使用 `client.files.upload`，並將傳回的檔案傳遞至模型內容。

## 限制

- **音訊長度：**標準一元要求支援最長 1 小時的音訊檔案。啟用說話者分段標記或個別字詞時間戳記等功能時，音訊處理時間上限為 30 分鐘。
- **字詞層級時間戳記：**啟用字詞層級時間戳記可能會降低整體轉錄準確率。
- **說話者分段標記：**說話者分段標記最多可支援 8 位說話者。3 個以上音箱的說話者辨識功能目前為實驗功能。
- **自訂詞彙：**您最多可以在 `custom_vocabulary` 中提供 1,000 個字詞，但通常最多 100 個字詞就能獲得最佳結果。
- **模式相容性：**智慧轉錄 (`mode: "SMART"`) 無法與 `word_timestamp` 或 `diarization` 合併使用。

## 後續步驟

- 使用 Live API 透過[即時轉錄指南](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=zh-tw)串流即時音訊。
- 探索「音訊理解」，分析、摘要或查詢音訊內容。
- 瞭解如何使用 [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-tw) 從文字合成音訊。
- 如需模型定價和權杖限制，請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-3.5-transcribe)。
- 如要瞭解如何上傳及管理媒體檔案，請參閱「[Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw)」指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-08-28 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-08-28 (世界標準時間)。"],[],[]]
