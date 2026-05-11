---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=ar
fetched_at: 2026-05-11T12:30:33.743150+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التخزين المؤقت للسياق

في سير عمل الذكاء الاصطناعي النموذجي، قد يتم تمرير رموز الإدخال نفسها بشكل متكرر إلى أحد النماذج. توفّر Gemini API آليتَين مختلفتَين للتخزين المؤقت:

- التخزين المؤقت الضمني (مفعَّل تلقائيًا في Gemini 2.5 والنماذج الأحدث، ولا يضمن توفير التكاليف)
- التخزين المؤقت الصريح (يمكن تفعيله يدويًا في معظم النماذج، ويضمن توفير التكاليف)

يكون التخزين المؤقت الصريح مفيدًا في الحالات التي تريد فيها ضمان توفير التكاليف، ولكن مع بعض العمل الإضافي من جانب المطوّر.

## التخزين المؤقت الضمني

يكون التخزين المؤقت الضمني مفعَّلاً تلقائيًا لجميع نماذج Gemini 2.5 والنماذج الأحدث. ونحن نمرّر تلقائيًا وفورات التكاليف إذا كانت طلباتك تستخدم البيانات المخزّنة مؤقتًا. وليس عليك اتّخاذ أي إجراء لتفعيل هذه الميزة. يتم إدراج الحد الأدنى لعدد رموز الإدخال للتخزين المؤقت للسياق في الجدول التالي لكل نموذج:

| الطراز | الحد الأدنى لعدد الرموز |
| --- | --- |
| Gemini 3 Flash Preview | 1024 |
| Gemini 3 Pro Preview | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

لزيادة فرصة استخدام البيانات المخزّنة مؤقتًا ضمنيًا:

- حاوِل وضع المحتويات الكبيرة والشائعة في بداية الطلب
- حاوِل إرسال الطلبات التي تتضمّن بادئة مشابهة خلال فترة زمنية قصيرة

يمكنك الاطّلاع على عدد الرموز التي تم استخدامها من البيانات المخزّنة مؤقتًا في حقل `usage_metadata` في عنصر الاستجابة.

## التخزين المؤقت الصريح

باستخدام ميزة التخزين المؤقت الصريح في Gemini API، يمكنك تمرير بعض المحتوى إلى النموذج مرة واحدة، وتخزين رموز الإدخال مؤقتًا، ثم الإشارة إلى الرموز المخزّنة مؤقتًا للطلبات اللاحقة. عند استخدام كميات معيّنة، تكون تكلفة استخدام الرموز المخزّنة مؤقتًا أقل من تكلفة تمرير مجموعة الرموز نفسها بشكل متكرر.

عند تخزين مجموعة من الرموز مؤقتًا، يمكنك اختيار المدة التي تريد أن تظل فيها البيانات المخزّنة مؤقتًا قبل حذف الرموز تلقائيًا. تُعرف مدة التخزين المؤقت هذه باسم *مدة البقاء* (TTL). إذا لم يتم ضبط مدة البقاء، يتم ضبطها تلقائيًا على ساعة واحدة. تعتمد تكلفة التخزين المؤقت على حجم رمز الإدخال والمدة التي تريد أن تظل فيها الرموز.

يفترض هذا القسم أنّك ثبّت أحد حِزم Gemini SDK (أو ثبّت أداة curl)
وأنّك ضبطت مفتاح واجهة برمجة التطبيقات، كما هو موضّح في
[دليل البدء السريع](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar).

### إنشاء محتوى باستخدام ذاكرة تخزين مؤقت

### Python

يوضّح المثال التالي كيفية إنشاء محتوى باستخدام تعليمات نظام مخزّنة مؤقتًا وملف فيديو.

### الفيديوهات

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3-flash-preview'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### ملفات PDF

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3-flash-preview"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

يوضّح المثال التالي كيفية إنشاء محتوى باستخدام تعليمات نظام مخزّنة مؤقتًا وملف نصي.

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3-flash-preview";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### انتقال

يوضّح المثال التالي كيفية إنشاء محتوى باستخدام ذاكرة تخزين مؤقت.

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3-flash-preview"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

يوضّح المثال التالي كيفية إنشاء ذاكرة تخزين مؤقت ثم استخدامها لإنشاء محتوى.

### الفيديوهات

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3-flash-preview",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### ملفات PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3-flash-preview"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### سرد ذاكرات التخزين المؤقت

لا يمكن استرداد المحتوى المخزّن مؤقتًا أو عرضه، ولكن يمكنك استرداد
البيانات الوصفية لذاكرة التخزين المؤقت (`name`، `model`، `display_name`، `usage_metadata`،
`create_time`، `update_time`، و`expire_time`).

### Python

لسرد البيانات الوصفية لجميع ذاكرات التخزين المؤقت التي تم تحميلها، استخدِم `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

لاسترداد البيانات الوصفية لعنصر ذاكرة تخزين مؤقت واحد، استخدِم `get` إذا كنت تعرف اسمه:

```
client.caches.get(name=name)
```

### JavaScript

لسرد البيانات الوصفية لجميع ذاكرات التخزين المؤقت التي تم تحميلها، استخدِم `GoogleGenAI.caches.list()`:

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### انتقال

يسرد المثال التالي جميع ذاكرات التخزين المؤقت.

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

يسرد المثال التالي ذاكرات التخزين المؤقت باستخدام حجم صفحة يبلغ 2.

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### تعديل ذاكرة تخزين مؤقت

يمكنك ضبط `ttl` أو `expire_time` جديدَين لذاكرة تخزين مؤقت. لا يمكن تغيير أي شيء آخر في ذاكرة التخزين المؤقت.

### Python

يوضّح المثال التالي كيفية تعديل `ttl` لذاكرة تخزين مؤقت باستخدام `client.caches.update()`.

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

لضبط وقت انتهاء الصلاحية، سيتم قبول كائن `datetime` أو سلسلة بتنسيق datetime بتنسيق ISO (`dt.isoformat()`، مثل
`2025-01-27T16:02:36.473528+00:00`). يجب أن يتضمّن الوقت منطقة زمنية
(`datetime.utcnow()` لا يرفق منطقة زمنية،
`datetime.now(datetime.timezone.utc)` يرفق منطقة زمنية).

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

يوضّح المثال التالي كيفية تعديل `ttl` لذاكرة تخزين مؤقت باستخدام `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### انتقال

يوضّح المثال التالي كيفية تعديل `TTL` لذاكرة تخزين مؤقت.

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

يوضّح المثال التالي كيفية تعديل `ttl` لذاكرة تخزين مؤقت.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### حذف ذاكرة تخزين مؤقت

توفّر خدمة التخزين المؤقت عملية حذف لإزالة المحتوى يدويًا من ذاكرة التخزين المؤقت. يوضّح المثال التالي كيفية حذف ذاكرة تخزين مؤقت:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### انتقال

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### التخزين المؤقت الصريح باستخدام مكتبة OpenAI

إذا كنت تستخدم مكتبة [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar)، يمكنك تفعيل
التخزين المؤقت الصريح باستخدام السمة `cached_content` في
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=ar#extra-body).

## حالات استخدام التخزين المؤقت الصريح

يكون التخزين المؤقت للسياق مناسبًا بشكل خاص للسيناريوهات التي تتم فيها الإشارة بشكل متكرر إلى سياق أولي كبير من خلال طلبات أقصر. ننصحك باستخدام التخزين المؤقت للسياق في حالات الاستخدام التالية:

- روبوتات الدردشة التي تتضمّن تعليمات نظام [شاملة](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ar)
- التحليل المتكرر لملفات الفيديو الطويلة
- الطلبات المتكررة التي يتم إرسالها إلى مجموعات كبيرة من المستندات
- التحليل المتكرر لمستودع الرموز أو إصلاح الأخطاء

### كيفية تقليل التكاليف باستخدام التخزين المؤقت الصريح

التخزين المؤقت للسياق هو ميزة مدفوعة مصمّمة لتقليل التكلفة. تستند الفوترة إلى العوامل التالية:

1. **عدد رموز ذاكرة التخزين المؤقت:** عدد رموز الإدخال المخزّنة مؤقتًا، والتي يتم تحصيل رسومها بسعر مخفّض عند تضمينها في الطلبات اللاحقة
2. **مدة التخزين:** المدة التي يتم فيها تخزين الرموز مؤقتًا (مدة البقاء)، ويتم تحصيل الرسوم استنادًا إلى مدة البقاء لعدد الرموز المخزّنة مؤقتًا ما مِن حدود دنيا أو قصوى لـ "مدة البقاء".
3. **عوامل أخرى:** يتم تطبيق رسوم أخرى، مثل رموز الإدخال ورموز الإخراج غير المخزّنة مؤقتًا.

للاطّلاع على تفاصيل التسعير الحديثة، يُرجى الرجوع إلى صفحة [تسعير
Gemini API](https://ai.google.dev/pricing?hl=ar). للتعرّف على كيفية احتساب الرموز، يُرجى الاطّلاع على دليل [الرموز](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

### اعتبارات أخرى

يجب مراعاة الاعتبارات التالية عند استخدام التخزين المؤقت للسياق:

- يختلف *الحد الأدنى* لعدد رموز الإدخال للتخزين المؤقت للسياق حسب النموذج. ويكون *الحد الأقصى* هو نفسه الحد الأقصى للنموذج المحدّد. (لمزيد من المعلومات حول احتساب الرموز،
  يُرجى الاطّلاع على [دليل الرموز](https://ai.google.dev/gemini-api/docs/tokens?hl=ar)).
- لا يميّز النموذج بين الرموز المخزّنة مؤقتًا ورموز الإدخال العادية. المحتوى المخزّن مؤقتًا هو بادئة للطلب.
- ما مِن حدود خاصة للأسعار أو الاستخدام في ما يتعلق بالتخزين المؤقت للسياق، ويتم تطبيق الحدود القصوى القياسية للطلبات على `GenerateContent`، وتشمل الحدود القصوى للرموز الرموز المخزّنة مؤقتًا.
- يتم عرض عدد الرموز المخزّنة مؤقتًا في `usage_metadata` من عمليات الإنشاء والاسترداد والسرد في خدمة ذاكرة التخزين المؤقت، وأيضًا في `GenerateContent` عند استخدام ذاكرة التخزين المؤقت.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
