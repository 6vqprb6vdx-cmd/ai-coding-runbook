---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-TW
fetched_at: 2026-09-21T05:45:37.334180+00:00
title: "\u5f71\u7247\u89e3\u8b80 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# 影片解讀

> 如要瞭解如何生成影片，請參閱 [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=zh-tw) 指南。

Gemini 模型可以處理影片，因此開發人員能實現許多前所未有的用途，這在過去需要使用特定領域的模型。Gemini 的部分影像功能包括：描述、區隔及擷取影片資訊、回答影片內容相關問題，以及參照影片中的特定時間戳記。

你可以透過下列方式將影片提供給 Gemini：

| 輸入法 | 大小上限 | 建議用途 |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (付費) / 2 GB (免費) | 大型檔案 (100 MB 以上)、長影片 (10 分鐘以上)、可重複使用的檔案。 |
| [Cloud Storage 註冊](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-tw#registration) | 2 GB (每個檔案，無儲存空間限制) | 大型檔案 (100 MB 以上)、長影片 (10 分鐘以上)、可重複使用的檔案。 |
| [內嵌資料](#inline-video) | < 100MB | 小型檔案 (小於 100 MB)、短時間 (小於 1 分鐘)、一次性輸入。 |
| [YouTube 網址](#youtube) | 不適用 | 公開的 YouTube 影片。 |

> **注意：**建議在大多數情況下使用 [File API](#upload-video)，尤其是檔案大小超過 100 MB，或是您想在多個要求中重複使用檔案時。

如要瞭解其他檔案輸入方法，例如使用外部網址或儲存在 Google Cloud 中的檔案，請參閱[檔案輸入方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-tw)指南。

### 上傳影片檔案

下列程式碼會下載影片樣本、使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) 上傳影片、等待處理完成，然後使用上傳的檔案參照來總結影片內容。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

如要提升詞元使用效率和效能，建議使用[代理功能影片處理](#agentic-video-understanding)。

如果要求總大小 (包括檔案、文字提示詞、系統指令等) 超過 20 MB、影片長度較長，或您打算在多個提示詞中使用相同影片，請一律使用 Files API。File API 可直接接受影片檔案格式。

如要進一步瞭解如何處理媒體檔案，請參閱 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw)。

### 內嵌傳遞影片資料

您可以直接在 `generateContent` 的要求中傳遞較小的影片，不必使用 File API 上傳影片檔案。這適合總要求大小小於 20 MB 的短片。

以下是提供內嵌影片資料的範例：

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### 傳送 YouTube 網址

你可以直接將 YouTube 網址傳送至 Gemini API，做為要求的一部分，如下所示：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**限制：**

- 免費方案每天最多只能上傳 8 小時的 YouTube 影片。
- 付費方案則沒有影片長度限制。
- 如果是 Gemini 2.5 之前的模型，每次要求只能上傳 1 部影片。如果是 Gemini 2.5 以上版本，每個要求最多可上傳 10 部影片。
- 你只能上傳公開影片，無法上傳私人或不公開影片。

## 代理式影片解讀

影片輸入內容預設會使用靜態處理方式 (以每秒 1 個影格的速度擷取影格)。Gemini 3.8 Flash、3.7 Flash、3.6 Flash 和 3.5 Flash Lite 模型也支援**代理式影片理解**，模型會動態探索影片時間軸，選擇性檢查轉錄稿，並根據提示即時調整影格速率和解析度。

| **眾數** | **說明** | **支援的機型** |
| --- | --- | --- |
| **靜態** (預設) | 以固定速率 (1 FPS) 擷取影格，並在單一階段中將影格放入內容。適合短片。 | 所有 Gemini 模型 |
| **代理功能** | 模型會根據提示動態瀏覽影片時間軸，只載入所需的內容。在長篇內容方面，權杖效率最多可提升 88%，品質則可提升約 7%。 | Gemini 3.8 Flash、3.7 Flash、3.6 Flash、3.5 Flash Lite |

### 選擇處理模式

一般而言，建議先從**代理**模式開始，特別是在提升回覆品質或權杖效率時。

- **代理：**長篇影片或針對特定時刻的查詢。模型會動態瀏覽時間軸，找出與脈絡相關的資訊，不必填滿脈絡視窗。
- **靜態：**對短片 (5 分鐘以內) 執行延遲時間敏感型查詢，或需要整個短片達到影格層級精確度的情況。

> **注意：**如果是長影片或複雜提示，代理程式處理時間較長，請使用串流 (`client.models.generate_content_stream`)。這樣可維持連線、顯示中間推論步驟，並避免連線或驗證逾時。

### 設定處理模式

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **注意：**如要確認是否使用代理程式處理，請檢查 `response.candidates[0].content.parts`。如果 `tool_call` 和 `tool_response` 部分存在 `MEDIA_PROCESSING` 工具類型，表示模型動態瀏覽了影片。

> **注意：**與其他伺服器端工具 (例如 Google 搜尋或網址內容) 不同，代理程式影片不需要在 `ToolConfig` 中設定 `include_server_side_tool_invocations=True`，即可傳回或串流工具呼叫和結果。當 `media_processing="AGENTIC"` 設為任何輸入部分時，系統會自動傳回影片導覽的 `tool_call` 和 `tool_response` 部分。

### 回覆結構

啟用代理程式處理功能後，回應會包含額外部分，顯示內部導覽追蹤記錄：

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`)：模型每次要求影片片段或音訊轉錄稿時發出。
- `tool_response` **部分** (`tool_type: "MEDIA_PROCESSING"`)：每個載入作業的結果。

您不必手動處理或回覆這些部分：將完整的回覆傳回做為對話記錄，系統就會自動處理。

如果 `include_thoughts=True` 設定在 `ThinkingConfig` 中，推論步驟會顯示為 `thought: true` 部分，並與工具呼叫/回應配對交錯。停用想法後，系統會省略想法文字，但仍會顯示工具部分。

以下範例顯示回應酬載，其中穿插工具呼叫和回應部分：

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### 在不同影片之間混合使用處理模式

您可以在同一個要求中，為每個影片部分設定不同的處理模式：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## 在長片中使用脈絡快取功能

如果影片長度超過 10 分鐘，或打算對同一個影片檔案提出多項要求，請使用[內容快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)功能，以降低成本並縮短延遲時間。脈絡快取功能可讓您處理一次影片，並在後續查詢中重複使用權杖，非常適合用於對話工作階段或重複分析長篇內容。

## 參考內容中的時間戳記

你可以使用 `MM:SS` 格式的時間戳記，詢問影片中特定時間點的問題。

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## 從影片擷取詳細洞察資料

Gemini 模型可處理**音訊和影像**串流中的資訊，深入瞭解影片內容。這項功能可讓你擷取豐富的詳細資料，包括生成影片內容的說明，以及回答相關問題。

如果是視覺描述，模型會以 **每秒 1 個影格** (FPS) 的速率對影片取樣。這個預設取樣率適用於大多數內容，但請注意，如果影片的動作快速或場景快速變化，可能就會遺漏細節。對於這類高動態內容，建議[設定自訂畫面更新率](#custom-frame-rate)。

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## 自訂影片處理方式

您可以設定剪輯間隔或提供自訂影格速率取樣，在 Gemini API 中自訂影片處理作業。只有在 `"static"` 模式下處理影片時，才能使用這些自訂選項。

### 設定剪輯間隔

您可以指定 `videoMetadata`，並提供開始和結束偏移量，藉此剪輯影片。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### 設定自訂影格率

您可以將 `fps` 引數傳遞至 `videoMetadata`，藉此設定自訂影格率取樣。

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

系統預設會從影片中取樣每秒 1 個影格。如果是長片，建議將 FPS 設為低於 1。這項功能特別適合大部分靜態的影片 (例如講座)。如果影片需要細微的時間分析，例如瞭解快速動作或追蹤高速移動的物體，請使用較高的每秒影格數。

## 支援的影片格式

Gemini 支援下列影片格式 MIME 類型：

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 影片技術詳細資料

- **支援的模型和脈絡**：所有 Gemini 模型都能處理影片資料。
  - 如果模型具有 100 萬個詞元脈絡窗口，預設可處理長達 3 小時的影片 (媒體解析度較低)，或長達 1 小時的影片 (媒體解析度較高)。
- **處理模式**：Gemini 3.8 Flash、3.7 Flash、3.6 Flash、3.5 Flash Lite 和後續模型支援兩種影片處理模式：
  - **靜態**：以每秒 1 個影格的速度擷取影格，並放入脈絡 (所有模型的預設值)。音訊處理速度為 1 Kbps (單一聲道)。系統每秒都會新增時間戳記。適合短片或需要逐格檢查的影片。請注意，由於取樣率為 1 FPS，快速動作序列可能會遺失細節。
  - **代理**：模型會動態瀏覽影片，並視需要載入轉錄稿和/或影格和/或音訊。這項功能可為長篇內容節省高達 88% 的詞元，但由於生成作業開始前需要進行內部推論和工具往返，短片 (少於 5 分鐘) 的首次詞元時間 (TTFT) 可能會稍微增加。回覆內容包括 `MEDIA_PROCESSING` 工具呼叫和回覆部分，可保留各輪對話的推理脈絡。最適合長篇影片，可降低權杖費用並提升回覆品質。支援 Gemini 3.8 Flash、3.7 Flash、3.6 Flash 和 3.5 Flash Lite。詳情請參閱「[代理式影片解讀](#agentic-video-understanding)」。
- **符記計算 (靜態模式)**：每秒影片會依下列方式轉換為符記：
  - 個別影格 (以 1 FPS 取樣)：
    - 如果將 `media_resolution` 設為「低」，每個影格會產生 66 個權杖。
    - 否則，每個影格會以 258 個權杖進行權杖化。
  - 音訊：每秒 32 個權杖。
  - 也包含中繼資料。
  - 總計：預設 (低) 媒體解析度下，每秒影片約 100 個權杖；高媒體解析度下，每秒影片約 300 個權杖。
- **權杖計算 (代理模式)**：權杖用量取決於內容複雜度和模型的導覽策略。影片探索期間產生的導覽推理權杖會計為**思考權杖** (`thoughts_token_count`)，而根據需求載入的影格、音訊和轉錄稿則會計為工具提示權杖 (`tool_use_prompt_token_count`)。由於模型只會載入回答提示所需的轉錄稿和/或影格和/或音訊，因此與靜態處理相比，代理式處理通常可減少最多 88% 的權杖總數 (請參閱[權杖指南](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=zh-tw#video-token-usage))。
- **媒體解析度**：Gemini 3 導入了精細控制項，可透過 `media_resolution` 參數精準控制多模態視覺處理程序。`media_resolution` 參數會決定每個輸入圖片或影片影格分配的**詞元數量上限**。解析度越高，模型就越能辨識細小文字或細節，但也會增加權杖用量和延遲時間。`media_resolution` 和 `media_processing` 參數彼此獨立，因此您可以在同一個影片 Part 中設定這兩個參數。

如要進一步瞭解如何計算權杖，請參閱[權杖](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=zh-tw)指南。

- **時間戳記格式**：在提示中提及影片的特定時間點時，請使用 `MM:SS` 格式 (例如 `01:15` 代表 1 分 15 秒)。
- **文字提示詞位置**：如果結合文字和單一影片，請將文字提示詞放在 `contents` 陣列的影片部分*之後*。
- **長時間要求逾時**：如果影片需要較長的處理時間或複雜的多步驟推論，請使用串流 (`client.models.generate_content_stream`)。如果同步非串流要求在需求量高時發生後端重試，可能會超過連線或驗證權杖有效時間範圍，進而顯示非預期的 `401 Unauthorized` 或逾時錯誤。串流會保持連線狀態，並顯示中間推論和工具呼叫進度。

## 後續步驟

- [媒體解析度](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-tw)：控制影片影格的解析度，以兼顧畫質和權杖用量。
- [權杖](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=zh-tw)：瞭解如何在靜態和代理處理模式中，將影片內容權杖化。
- [系統指令](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=zh-tw#system-instructions)：
  系統指令可根據特定需求和用途，引導模型行為。
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw)：進一步瞭解如何上傳及管理檔案，以供 Gemini 使用。
- [檔案提示策略](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw#prompt-guide)：Gemini API 支援使用文字、圖片、音訊和影片資料提示，也稱為多模態提示。
- [安全指引](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-tw)：有時生成式 AI 模型會產生出乎意料的輸出內容，例如不準確、有偏見或令人反感的內容。後續處理和人工評估是不可或缺的步驟，有助於降低這類輸出內容造成危害的風險。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-18 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-18 (世界標準時間)。"],[],[]]
