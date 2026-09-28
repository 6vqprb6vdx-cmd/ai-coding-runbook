---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=zh-CN
fetched_at: 2026-09-28T06:08:52.113988+00:00
title: "\u97f3\u9891\u8f6c\u5199 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 音频转写

Gemini API 使用 Gemini 3.5 Transcribe 模型 (`gemini-3.5-transcribe`) 将音频文件中的语音转换为文本。凭借 Gemini 的音频理解能力，该 API 可提供准确的转写内容，并支持自动语言识别、说话人日志记录、字级时间戳和自定义词汇提示。它还提供[智能转写](#transcription-modes)模式，可移除口语中的不流畅之处并进行智能格式设置。

如需转写音频文件，请上传音频并将其传递给 `gemini-3.5-transcribe`：

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

## 概览

Gemini 3.5 Transcribe 针对语音转文字任务进行了优化。它可以处理各种口音、背景噪声和多语言对话。

主要功能包括：

- **自动语音识别 (ASR)**：自动检测 [85 多种语言区域设置](#supported-languages)。无需手动配置即可处理句内和句间语码转换。
- **自定义词汇**：通过传递最多 1,000 个短语，使识别偏向于特定领域的术语、缩写和专有名词。
- **说话人日志**：区分多个说话人，并将说话片段归因于不同的标签。
- **字词级时间戳**：为每个识别出的字词生成精确的开始和结束时间偏移值。
- **智能转写**：清理口误、填充词、重复内容，并应用结构化格式。
- **格式设置和归一化**：应用大小写、标点和逆文本归一化，例如将“2600 万美元”转换为“2600 万美元”。

如需对音频内容进行一般性音频推理或问答，请使用[音频理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=zh-cn)。如需进行文字转语音音频合成，请使用 [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-cn)。

## 语言检测和提示

默认情况下，模型会自动检测口语。当说话者进行语码转换时，它会在语言之间动态切换。

如需使用自动检测，请省略 `language_codes` 或提供一个空列表：

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

如果您提前知道语言，请在 `language_codes` 中指定 BCP-47 语言代码，以提高转写准确率（请参阅[支持的语言](#supported-languages)）：

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

## 自定义词汇

您可以引导语音模型识别不常见的字词、技术术语、品牌名称或专有名词。在 `custom_vocabulary` 数组中提供最多 1,000 个字词（通常最多提供 100 个字词可获得最佳效果）：

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

## 讲话人区分

讲话人区分功能可识别录音中的不同语音，并为每个片段添加讲话人标识符（例如 `spk_1` 或 `spk_2`）。最多支持 8 位发言者（3 位或更多发言者的归因功能处于实验阶段）。

通过将 `diarization` 设置为 `True` 来启用区分讲话人功能：

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

## 字词级时间戳

字词级时间戳可为音频串流中识别出的每个字词提供确切的开始和结束偏移值。

通过将 `word_timestamp` 设置为 `True` 来启用时间戳：

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

您可以在单个请求中同时使用 `diarization` 和 `word_timestamp`，以同时接收讲话人标签和字词时间戳：

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

## 转写模式

Gemini 3.5 Transcribe 通过 `mode` 参数支持两种转写模式：

- **`VERBATIM`（默认）**：返回所有语音内容的逐字逐句的转写，保留原始的填充词（“嗯”“呃”“像”“你知道”）、重复内容、停顿和错误开头。使用时间戳或说话人日记时，需要此参数。
- **`SMART`（智能转写）**：通过应用智能后处理来优化转写内容，以便于阅读：
  - **去除口语障碍**：去除对话中的填充词、口吃和误启动。
  - **内嵌自我修正**：直接解决语音修正问题（例如，*“我们周二见面吧，不，周三下午两点”*会变成*“我们周三下午两点见面吧”*）。
  - **自动结构化格式**：自动将语音中的想法整理成段落、编号列表、项目符号、格式化日期、货币和数字。
  - **语法清理**：应用自然的标点符号、句子大小写和流畅度。

| 朗读音频 | `VERBATIM` 输出 | `SMART`（智能转写）输出 |
| --- | --- | --- |
| “嗯，关于会议，我觉得我们应该邀请 Alice，等等，不，是 Bob 和 Carol。” | “嗯，对于会议，我认为我们应该邀请 Alice，等等，是 Bob 和 Carol。” | “我认为我们应该邀请 Bob 和 Carol 参加这次会议。” |
| “First item review budget second item finalize timeline third item send recap” | “first item review budget second item finalize timeline third item send recap” | “1. 查看预算 2. 确定时间轴 3. 发送总结” |

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

## 解析转写输出

完整的转写文本会返回到 `response.text` 中。

启用 `word_timestamp` 或 `diarization` 后，API 还会返回附加到候选部分的详细字级注释和发言人标签。

以下代码展示了如何提取字词时间戳和发言轮次并对其进行迭代：

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

## 支持的语言

Gemini 3.5 Transcribe 支持以下语言和 BCP-47 语言代码：

| 语言 | BCP-47 代码 | 语言 | BCP-47 代码 |
| --- | --- | --- | --- |
| 南非荷兰语 | `af-ZA` | 日语 | `ja-JP` |
| 阿姆哈拉语 | `am-ET` | 爪哇语 | `jv-ID` |
| 阿拉伯语（埃及） | `ar-EG` | Kabuverdianu | `kea-CV` |
| 亚美尼亚语 | `hy-AM` | 卡纳达语 | `kn-IN` |
| 阿萨姆语 | `as-IN` | 哈萨克语 | `kk-KZ` |
| 阿塞拜疆语 | `az-AZ` | 韩语 | `ko-KR` |
| 白俄罗斯语 | `be-BY` | 吉尔吉斯语 | `ky-KG` |
| 孟加拉语（孟加拉） | `bn-BD` | 拉脱维亚语 | `lv-LV` |
| 孟加拉语（印度） | `bn-IN` | 林加拉语 | `ln-CD` |
| 波斯尼亚语 | `bs-BA` | 立陶宛语 | `lt-LT` |
| 保加利亚语 | `bg-BG` | 马其顿语 | `mk-MK` |
| 保加利亚语（阿罗马尼亚语） | `rup-BG` | 马来语 | `ms-MY` |
| 缅甸语 | `my-MM` | 马拉雅拉姆语 | `ml-IN` |
| 粤语（繁体） | `yue-Hant-HK` | 马耳他语 | `mt-MT` |
| 加泰罗尼亚语 | `ca-ES` | 普通话（简体） | `cmn-Hans-CN` |
| 宿务语 | `ceb` | 马拉地语 | `mr-IN` |
| 中部高棉语 | `km-KH` | 蒙古语 | `mn-MN` |
| 克罗地亚语 | `hr-HR` | 尼泊尔语 | `ne-NP` |
| 捷克语 | `cs-CZ` | 挪威语 | `nb-NO` |
| 丹麦语 | `da-DK` | 奥里亚语 | `or-IN` |
| 荷兰语 | `nl-NL` | 波兰语 | `pl-PL` |
| 英语（英国） | `en-GB` | 葡萄牙语（巴西） | `pt-BR` |
| 英语（印度） | `en-IN` | 葡萄牙语（葡萄牙） | `pt-PT` |
| 英语（美国） | `en-US` | 旁遮普语 | `pa-IN` |
| 爱沙尼亚语 | `et-EE` | 旁遮普语（果鲁穆奇文） | `pa-Guru-IN` |
| 波斯语 | `fa-IR` | 罗马尼亚语 | `ro-RO` |
| 菲律宾语 | `fil-PH` | 俄语 | `ru-RU` |
| 芬兰语 | `fi-FI` | 塞尔维亚语 | `sr-RS` |
| 法语 | `fr-FR` | 信德语（阿拉伯文字） | `sd-Arab-IN` |
| 加利西亚语 | `gl-ES` | 斯洛伐克语 | `sk-SK` |
| 格鲁吉亚语 | `ka-GE` | 斯洛文尼亚语 | `sl-SI` |
| 德语 | `de-DE` | 西班牙语（拉丁美洲） | `es-419` |
| 希腊语 | `el-GR` | 西班牙语（美国） | `es-US` |
| 古吉拉特语 | `gu-IN` | 斯瓦希里语（肯尼亚） | `sw-KE` |
| 豪萨语 | `ha-NG` | 瑞典语 | `sv-SE` |
| 希伯来语 | `he-IL` | 塔吉克语 | `tg-TJ` |
| 印地语 | `hi-IN` | 泰卢固语 | `te-IN` |
| 匈牙利语 | `hu-HU` | 泰语 | `th-TH` |
| 冰岛语 | `is-IS` | 土耳其语 | `tr-TR` |
| 印度式英语 | `en-IN` | 乌克兰语 | `uk-UA` |
| 印度尼西亚语 | `id-ID` | 乌兹别克语 | `uz-UZ` |
| 意大利语 | `it-IT` | 越南语 | `vi-VN` |

## 参数参考

通过设置 `GenerateContentConfig` 中 `audio_transcription_config` 对象内的字段来配置转写：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `language_codes` | 字符串数组 | BCP-47 语言代码（例如 `["en-US"]`）。如果省略或为空 (`[]`)，模型会自动检测语言并处理代码切换。 |
| `custom_vocabulary` | 字符串数组 | 最多可添加 1,000 个自定义术语、缩写或专有名词，以使语音识别偏向于这些词汇。 |
| `word_timestamp` | 布尔值 | 设置为 `True` 可包含字词开始和结束偏移值。如果省略或为 `False`，则不返回字词时间戳。 |
| `diarization` | 布尔值 | 设置为 `True` 可识别不同的说话人并为其添加标签。 |
| `mode` | 字符串 | 转写模式。支持的值：`"VERBATIM"`（默认）和 `"SMART"`。与时间戳和区分词不兼容。 |

## 最佳做法

- **提供清晰的音频**：确保音频录制具有清晰的人声分离度，并避免严重剪辑。
- **在已知音频语言的情况下提供语言提示**：如果您提前知道音频语言，请指定 `language_codes` 以尽可能提高准确性。
- **以自定义词汇为目标**：在 `custom_vocabulary` 中仅包含独特的领域术语、品牌名称或专有名词，而不是常见的日常用语。
- **针对大型录制内容使用 Files API**：对于时长超过几秒的文件，请使用 `client.files.upload` 上传文件，并将返回的文件传递给模型内容。

## 限制

- **音频时长**：标准一元请求支持时长不超过 1 小时的音频文件。启用讲话人区分或字词级时间戳等功能时，音频处理时长上限为 30 分钟。
- **字词级时间戳**：启用字词级时间戳可能会降低整体转写准确度。
- **讲话人区分**：讲话人区分功能最多支持 8 位讲话人。针对 3 个或更多发言者的发言者归因功能目前处于实验阶段。
- **自定义词汇**：您可以在 `custom_vocabulary` 中提供最多 1,000 个字词，但通常最多 100 个字词就能获得最佳效果。
- **模式兼容性**：智能转写 (`mode: "SMART"`) 不能与 `word_timestamp` 或 `diarization` 结合使用。

## 后续步骤

- 使用 Live API 通过[实时转写指南](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=zh-cn)实时传输音频。
- 探索[音频理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=zh-cn)功能，分析、总结或查询音频内容。
- 了解如何使用 [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-cn) 将文字合成为音频。
- 如需了解模型价格和令牌限制，请参阅[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-3.5-transcribe)。
- 如需详细了解如何上传和管理媒体文件，请参阅 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-10。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-10。"],[],[]]
