---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar
fetched_at: 2026-10-26T05:56:47.570110+00:00
title: "\u0641\u0647\u0645 \u0627\u0644\u0641\u064a\u062f\u064a\u0648 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# فهم الفيديو

> لمزيد من المعلومات حول إنشاء الفيديوهات، يمكنك الاطّلاع على دليل [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ar).

يمكن لنماذج Gemini معالجة الفيديوهات، ما يتيح العديد من حالات الاستخدام المتقدّمة للمطوّرين
التي كانت تتطلّب في السابق نماذج خاصة بمجالات معيّنة.
تشمل بعض قدرات Gemini المرئية ما يلي: وصف الفيديوهات وتقسيمها واستخراج المعلومات منها، والإجابة عن أسئلة حول محتوى الفيديو، والإشارة إلى طوابع زمنية محدّدة ضمن الفيديو.

يمكنك تقديم فيديوهات كمدخلات إلى Gemini بالطرق التالية:

| طريقة الإرسال | أقصى حجم | حالة الاستخدام المقترَحة |
| --- | --- | --- |
| [File API](#upload-video) | ‫20 غيغابايت (مدفوعة) / 2 غيغابايت (مجانية) | الملفات الكبيرة (100 ميغابايت أو أكثر) والفيديوهات الطويلة (10 دقائق أو أكثر) والملفات القابلة لإعادة الاستخدام |
| [التسجيل في Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar#registration) | ‫2 غيغابايت (لكل ملف، بدون حدود لمساحة التخزين) | الملفات الكبيرة (أكثر من 100 ميغابايت) والفيديوهات الطويلة (أكثر من 10 دقائق) والملفات الدائمة والقابلة لإعادة الاستخدام. |
| [البيانات المضمّنة](#inline-video) | < 100 ميغابايت | الملفات الصغيرة (أقل من 100 ميغابايت) والمدّة القصيرة (أقل من دقيقة واحدة) والمدخلات لمرة واحدة |
| [عناوين URL على YouTube](#youtube) | لا ينطبق | الفيديوهات العلنية على YouTube |

> **ملاحظة:** ننصح باستخدام [File API](#upload-video) في معظم حالات الاستخدام، خاصةً للملفات التي يزيد حجمها عن 100 ميغابايت أو عندما تريد إعادة استخدام الملف في طلبات متعددة.

للتعرّف على طرق أخرى لإدخال الملفات، مثل استخدام عناوين URL خارجية أو ملفات مخزّنة في Google Cloud، يُرجى الاطّلاع على دليل [طرق إدخال الملفات](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar).

### تحميل ملف فيديو

ينزّل الرمز التالي فيديو نموذجيًا، ويحمّله باستخدام [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar)، وينتظر إلى أن تتم معالجته، ثم يستخدم مرجع الملف الذي تم تحميله لتلخيص الفيديو.

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

لتحسين كفاءة الرموز المميّزة وأدائها، ننصحك باستخدام
[معالجة الفيديو المستندة إلى الذكاء الاصطناعي الوكيل](#agentic-video-understanding).

استخدِم دائمًا Files API عندما يكون إجمالي حجم الطلب (بما في ذلك الملف والطلب النصي
وتعليمات النظام وما إلى ذلك) أكبر من 20 ميغابايت، أو عندما تكون مدة الفيديو
طويلة، أو إذا كنت تنوي استخدام الفيديو نفسه في طلبات متعددة.
تقبل File API تنسيقات ملفات الفيديو مباشرةً.

لمزيد من المعلومات حول العمل باستخدام ملفات الوسائط، يُرجى الاطّلاع على [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar).

### تمرير بيانات الفيديو بشكل مضمّن

بدلاً من تحميل ملف فيديو باستخدام File API، يمكنك تمرير فيديوهات أصغر حجمًا مباشرةً في الطلب إلى `generateContent`. هذا مناسب لمقاطع الفيديو الأقصر التي يقل حجم الطلب الإجمالي فيها عن 20 ميغابايت.

في ما يلي مثال على تقديم بيانات فيديو مضمّنة:

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

### تمرير عناوين URL على YouTube

يمكنك تمرير عناوين URL على YouTube مباشرةً إلى Gemini API كجزء من طلبك على النحو التالي:

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

**القيود:**

- في المستوى المجاني، لا يمكنك تحميل أكثر من 8 ساعات من فيديوهات على YouTube يوميًا.
- في المستوى المدفوع، ما مِن حدّ أقصى لطول الفيديو.
- بالنسبة إلى النماذج الأقدم من Gemini 2.5، يمكنك تحميل فيديو واحد فقط لكل طلب. في Gemini 2.5 والإصدارات الأحدث، يمكنك تحميل 10 فيديوهات كحدّ أقصى لكل طلب.
- يمكنك تحميل فيديوهات علنية فقط (وليس فيديوهات خاصة أو غير مُدرَجة).

## فهم الفيديوهات باستخدام الذكاء الاصطناعي الوكيل

تستخدم إدخالات الفيديو تلقائيًا المعالجة الثابتة (استخراج اللقطات بمعدّل لقطة واحدة في الثانية) في جميع النماذج، بما في ذلك Gemini 4.
تتيح نماذج Gemini 4 Argon و3.8 Flash و3.6 Flash و3.5 Flash Lite أيضًا ميزة
**فهم الفيديو المستند إلى الوكيل**، وهي وضع اختياري يستكشف فيه النموذج المخطط الزمني للفيديو بشكل ديناميكي، ويفحص النصوص بشكل انتقائي، ويعدّل معدلات عرض اللقطات ودرجة الدقة بشكل تكيفي أثناء التشغيل استنادًا إلى الطلب.

| **الوضع** | **الوصف** | **الطُرز المتوافقة** |
| --- | --- | --- |
| **ثابت** (تلقائي) | يستخرج اللقطات بمعدّل ثابت (لقطة واحدة في الثانية) ويضعها في السياق في عملية واحدة. الإعداد التلقائي لجميع نماذج Gemini، بما في ذلك Gemini 4 | جميع نماذج Gemini |
| **Agentic** | يتنقّل النموذج ديناميكيًا في المخطط الزمني للفيديو، ويحمّل فقط المحتوى الذي يحتاجه استنادًا إلى الطلب. يوفّر كفاءة أعلى في استخدام الرموز المميّزة بنسبة تصل إلى% 88 وجودة أعلى بنسبة% 7 تقريبًا في المحتوى الطويل. | ‫Gemini 4 Argon و3.8‎ Flash و3.6‎ Flash و3.5‎ Flash Lite |

### اختيار وضع المعالجة

اختَر وضع المعالجة الذي يتطابق مع مدة الفيديو ونوع الطلب:

- **ثابتة (الإعداد التلقائي):** هي الأنسب للمقاطع القصيرة (أقل من 5 دقائق)، أو الملخّصات الشاملة للفيديو حيث يكون التسجيل بأكمله ذا صلة، أو طلبات البحث التي تتطلّب استجابة سريعة، أو الدقة على مستوى الإطار في المقطع بأكمله. في الفيديوهات القصيرة أو الطلبات العامة التي تتطلّب فحص معظم الفيديو، تتجنّب المعالجة الثابتة الرموز المميّزة الإضافية للتفكير (`thoughts_token_count`) وعمليات الذهاب والعودة لاستدعاء الأدوات (`tool_use_prompt_token_count`) التي يتطلّبها التنقّل في المخطط الزمني.
- **الوكيل:** يُعدّ هذا الوضع الأفضل للفيديوهات الطويلة (التي تزيد مدتها عن 5 إلى 10 دقائق)، أو لعمليات البحث عن معلومات دقيقة جدًا، أو لطلبات البحث التي تستهدف لحظات أو مواضيع معيّنة. يفحص النموذج النصوص أولاً ويحمّل فقط المقاطع المرئية ذات الصلة عند الطلب، ما يقلّل من استخدام الرموز المميّزة لإدخال الفيديو بنسبة تصل إلى% 88 بدون ملء قدرة الاستيعاب.

> **ملاحظة:** بالنسبة إلى الفيديوهات الطويلة أو الطلبات المعقّدة التي تستغرق فيها المعالجة المستندة إلى الوكلاء وقتًا أطول، استخدِم ميزة البث (`client.models.generate_content_stream`). يحافظ ذلك على نشاط الاتصال، ويعرض خطوات الاستدلال الوسيطة، ويتجنّب انتهاء مهلة الاتصال أو المصادقة.

### ضبط وضع المعالجة

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

> **ملاحظة:** للتأكّد من استخدام المعالجة المستندة إلى الوكلاء، افحص `response.candidates[0].content.parts`. يشير ظهور الجزأين `tool_call` و`tool_response` مع نوع الأداة `MEDIA_PROCESSING` إلى أنّ النموذج تنقّل في الفيديو بشكل ديناميكي.

> **ملاحظة:** على عكس الأدوات الأخرى من جهة الخادم (مثل "بحث Google" أو "سياق عناوين URL")، لا يتطلّب "الفيديو المستند إلى وكيل" ضبط `include_server_side_tool_invocations=True` في `ToolConfig` لعرض أو بث طلبات الأدوات والنتائج. يتم عرض الجزءَين `tool_call` و`tool_response`
> المستخدَمَين للتنقّل في الفيديو تلقائيًا عند ضبط `media_processing="AGENTIC"` على أي جزء من الإدخال.

### بنية الردّ

عند تفعيل المعالجة المستندة إلى الوكلاء، يتضمّن الردّ أجزاء إضافية تكشف عن تتبُّع التنقّل الداخلي:

- `tool_call` **أجزاء** (`tool_type: "MEDIA_PROCESSING"`): يتم إصدارها في كل مرة يطلب فيها النموذج مقطع فيديو أو نصًا صوتيًا.
- `tool_response` **الأجزاء** (`tool_type: "MEDIA_PROCESSING"`): نتيجة كل عملية تحميل.

ليس عليك معالجة هذه الأجزاء أو الردّ عليها يدويًا، بل يمكنك إعادة الردّ الكامل كسجلّ محادثة وستتم معالجتها تلقائيًا.

إذا تم ضبط `include_thoughts=True` في `ThinkingConfig`، ستظهر خطوات الاستدلال كأجزاء `thought: true` متداخلة مع أزواج طلب/ردّ الأداة. عند إيقاف الأفكار، يتم حذف نص الفكرة ولكن تظل أجزاء الأداة متوفّرة.

يعرض المثال التالي حمولة الاستجابة مع أجزاء متداخلة من طلبات الأدوات والاستجابات:

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

### الجمع بين أوضاع المعالجة في الفيديوهات

يمكنك ضبط أوضاع معالجة مختلفة لكل "جزء فيديو" في الطلب نفسه:

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

## استخدام ميزة "التخزين المؤقت للسياق" للفيديوهات الطويلة

بالنسبة إلى الفيديوهات التي تزيد مدتها عن 10 دقائق أو عندما تخطّط لإجراء طلبات متعددة على ملف الفيديو نفسه، استخدِم [التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar) لتقليل التكاليف وتحسين وقت الاستجابة. يتيح لك التخزين المؤقت للسياق معالجة الفيديو مرة واحدة وإعادة استخدام الرموز المميزة لطلبات البحث اللاحقة، ما يجعله مثاليًا لجلسات الدردشة أو التحليل المتكرر للمحتوى الطويل.

## الرجوع إلى الطوابع الزمنية في المحتوى

يمكنك طرح أسئلة حول نقاط زمنية محدّدة في الفيديو باستخدام طوابع زمنية بالتنسيق `MM:SS`.

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

## استخراج إحصاءات مفصّلة من الفيديو

توفّر نماذج Gemini إمكانات قوية لفهم محتوى الفيديو من خلال معالجة المعلومات من كل من **محتوى الصوت والمرئي**. يتيح لك ذلك استخراج مجموعة وافية من التفاصيل، بما في ذلك إنشاء أوصاف للأحداث التي تقع في فيديو والإجابة عن الأسئلة حول محتواه.

بالنسبة إلى الأوصاف المرئية، يأخذ النموذج عيّنات من الفيديو بمعدّل **لقطة واحدة في الثانية**. يعمل معدّل أخذ العيّنات التلقائي هذا بشكل جيد مع معظم المحتوى، ولكن تجدر الإشارة إلى أنّه قد لا يرصد تفاصيل في الفيديوهات التي تتضمّن حركة سريعة أو تغييرات سريعة في المشاهد.
بالنسبة إلى هذا المحتوى الذي يتضمّن حركة سريعة، ننصحك [بضبط عدد لقطات مخصّص في الثانية](#custom-frame-rate).

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

## تخصيص معالجة الفيديو

يمكنك تخصيص معالجة الفيديو في Gemini API من خلال ضبط فترات الاقتصاص
أو توفير عيّنات مخصّصة لعدد اللقطات في الثانية. لا تتوفّر خيارات التخصيص هذه إلا عند معالجة الفيديو في وضع "`"static"`".

### ضبط الفواصل الزمنية للقطع

يمكنك اقتصاص الفيديو من خلال تحديد `videoMetadata` مع وقتَي البدء والانتهاء.

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

### ضبط عدد لقطات مخصّص في الثانية

يمكنك ضبط عيّنات مخصّصة لعدد اللقطات في الثانية من خلال تمرير وسيطة `fps` إلى
`videoMetadata`.

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

يتم تلقائيًا أخذ عيّنة من الفيديو بمعدل لقطة واحدة في الثانية. قد تحتاج إلى ضبط عدد اللقطات في الثانية (أقل من 1) للفيديوهات الطويلة. وهذا مفيد بشكل خاص للفيديوهات الثابتة في الغالب (مثل المحاضرات). استخدِم عدد لقطات أعلى في الثانية للفيديوهات التي تتطلّب تحليلاً زمنيًا دقيقًا، مثل فهم الحركة السريعة أو تتبُّع الحركة العالية السرعة.

## تنسيقات الفيديو المتوافقة

يتيح Gemini أنواع MIME التالية لتنسيقات الفيديو:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## تفاصيل فنية حول الفيديوهات

- **النماذج والسياق المتوافقان**: يمكن لجميع نماذج Gemini معالجة بيانات الفيديو.
  - يمكن للنماذج التي تتضمّن قدرة استيعاب مليون رمز مميّز معالجة فيديوهات تصل مدتها إلى 3 ساعات تلقائيًا (بدرجة دقة منخفضة للوسائط)، أو فيديوهات تصل مدتها إلى ساعة واحدة بدرجة دقة عالية للوسائط.
- **طرق المعالجة**: تتوافق نماذج Gemini 4 Argon و3.8 Flash و3.6 Flash و3.5 Flash Lite والنماذج الأحدث مع طريقتَين لمعالجة الفيديوهات:
  - **ثابتة**: يتم استخراج اللقطات بمعدّل لقطة واحدة في الثانية ووضعها في السياق (الإعداد التلقائي لجميع النماذج). تتم معالجة الصوت بمعدل 1 كيلوبت في الثانية (قناة واحدة).
    تتم إضافة الطوابع الزمنية كل ثانية. هذا الخيار هو الأفضل للمقاطع القصيرة أو عندما يكون كل إطار مهمًا (مثل الفحص إطارًا تلو الآخر). يُرجى العِلم أنّ تسلسلات الحركة السريعة
    قد تفقد التفاصيل بسبب معدّل اللقطات في الثانية الذي يبلغ لقطة واحدة.
  - **التفاعلية**: يتنقّل النموذج ديناميكيًا في الفيديو، ويحمّل النص و/أو الإطارات و/أو الصوت عند الطلب. يستخدم هذا النموذج رموزًا مميّزة أقل بنسبة تصل إلى %88 للمحتوى الطويل، ولكن قد يؤدي التنقّل إلى زيادة الوقت المستغرَق للحصول على الرمز المميّز الأول وإجمالي استخدام الرموز المميّزة في المقاطع القصيرة (أقل من 5 دقائق) أو طلبات البحث الواسعة النطاق بسبب عمليات الاستدلال الداخلية والرحلات المتكررة إلى الأدوات.
    تتضمّن الردود `MEDIA_PROCESSING` أجزاء من طلبات الأدوات والردود عليها من أجل
    الحفاظ على سياق الاستدلال في جميع الجولات. هذا النموذج هو الأفضل للفيديوهات الطويلة والطلبات المستهدفة،
    لأنّه يقلّل من تكاليف الرموز المميّزة ويحسّن جودة الردود. متوافق مع Gemini 4 Argon و3.8 Flash و3.6 Flash و3.5 Flash Lite لمزيد من التفاصيل، يُرجى الاطّلاع على [فهم الفيديو المستند إلى الوكلاء](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar#agentic-video-understanding).
- **احتساب الرموز المميّزة (الوضع الثابت)**: يتم تقسيم كل ثانية من الفيديو إلى رموز مميّزة على النحو التالي:
  - اللقطات الفردية (يتم أخذ عينات بمعدل لقطة واحدة في الثانية):
    - إذا تم ضبط `media_resolution` على قيمة منخفضة، يتم تقسيم الإطارات إلى رموز مميزة بمعدل 66 رمزًا مميزًا لكل إطار.
    - بخلاف ذلك، يتم تقسيم اللقطات إلى رموز مميزة بمعدل 258 رمزًا مميزًا لكل لقطة.
  - الصوت: 32 رمزًا مميزًا في الثانية
  - يتم تضمين البيانات الوصفية أيضًا.
  - الإجمالي: حوالي 100 رمز مميز لكل ثانية من الفيديو بدقة الوسائط التلقائية (المنخفضة)، أو حوالي 300 رمز مميز لكل ثانية من الفيديو بدقة الوسائط العالية
- **احتساب الرموز المميزة (الوضع التلقائي)**: يختلف استخدام الرموز المميزة حسب مدى تعقيد المحتوى واستراتيجية التنقّل في النموذج. يتم احتساب الرموز المميزة الخاصة بالاستدلال على التنقّل التي يتم إنشاؤها أثناء استكشاف الفيديو ضمن **رموز مميّزة للتفكير** (`thoughts_token_count`)، بينما يتم احتساب الإطارات والصوت والنصوص التي يتم تحميلها عند الطلب ضمن رموز طلب الأداة (`tool_use_prompt_token_count`).
  تستخدم المعالجة المستندة إلى الوكيل عادةً عددًا أقل من الرموز المميزة الإجمالية بنسبة تصل إلى% 88 مقارنةً بالمعالجة الثابتة للمحتوى الطويل، لأنّ النموذج لا يحمّل سوى النص و/أو الإطارات و/أو الصوت الذي يحتاج إليه للإجابة عن الطلب (راجِع [دليل الرموز المميزة](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ar#video-token-usage)).
- **دقة الوسائط**: يتيح Gemini 3 التحكّم بدقة في معالجة الصور المتعددة الوسائط باستخدام المَعلمة `media_resolution`. تحدّد المَعلمة
  `media_resolution` **الحدّ الأقصى لعدد الرموز المميزة
  المخصّصة لكل صورة إدخال أو إطار فيديو.** تؤدي الدقة الأعلى إلى تحسين قدرة النموذج على قراءة النصوص الدقيقة أو تحديد التفاصيل الصغيرة، ولكنها تزيد من استخدام الرموز المميزة ووقت الاستجابة. المَعلمتان `media_resolution` و`media_processing` مستقلّتان، ويمكنك ضبطهما معًا في جزء الفيديو نفسه.

لمزيد من التفاصيل حول عمليات احتساب الرموز المميّزة، يُرجى الاطّلاع على دليل [الرموز المميّزة](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ar).

- **تنسيق الطابع الزمني**: عند الإشارة إلى لحظات معيّنة في فيديو ضمن
  طلبك، استخدِم التنسيق `MM:SS` (مثلاً، `01:15` للدلالة على دقيقة واحدة و15
  ثانية).
- **موضع الطلب**: في حال الجمع بين نص وفيديو واحد، ضَع الطلب النصي
  *بعد* جزء الفيديو في مصفوفة `contents`.
- **انتهاء المهلة للطلبات الطويلة**: بالنسبة إلى الفيديوهات التي تتطلّب وقت معالجة أطول أو تتضمّن الاستدلال المتعدّد الخطوات المعقّد، استخدِم البث (`client.models.generate_content_stream`). يمكن أن تتجاوز الطلبات المتزامنة غير المخصّصة للبث والتي تتم إعادة محاولتها في الخلفية في ظل الطلب المرتفع مدة صلاحية الاتصال أو رمز المصادقة المميز، ما قد يؤدي إلى ظهور أخطاء `401 Unauthorized` أو أخطاء انتهاء المهلة غير متوقّعة. يُبقي البث الاتصال نشطًا ويعرض الاستدلال الوسيط وتقدّم استدعاء الأداة.

## الخطوات التالية

- [دقة الوسائط](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ar): يمكنك التحكّم في دقة إطارات الفيديو لتحقيق التوازن بين الجودة واستخدام الرموز المميّزة.
- [الرموز المميّزة](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ar): تعرَّف على كيفية تقسيم محتوى الفيديو إلى رموز مميّزة
  في وضعَي المعالجة الثابتة والمعالجة المستندة إلى الوكلاء.
- [تعليمات النظام](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar#system-instructions):
  تتيح لك تعليمات النظام توجيه سلوك النموذج استنادًا إلى احتياجاتك وحالات الاستخدام المحدّدة.
- [‫Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar): مزيد من المعلومات حول تحميل الملفات وإدارتها لاستخدامها مع Gemini
- [استراتيجيات الطلبات المستندة إلى الملفات](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide): تتيح واجهة Gemini API إمكانية إنشاء الطلبات باستخدام بيانات النصوص والصور والصوت والفيديو، وهو ما يُعرف أيضًا باسم إنشاء الطلبات المتعددة الوسائط.
- [إرشادات الأمان](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ar): في بعض الأحيان، تقدّم نماذج الذكاء الاصطناعي التوليدي نتائج غير متوقعة، مثل النتائج غير الدقيقة أو المتحيزة أو المسيئة. تُعدّ المعالجة اللاحقة والتقييم البشري أساسيَّين للحدّ من خطر الأضرار الناجمة عن هذه النتائج.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
