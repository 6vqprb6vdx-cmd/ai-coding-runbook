---
source_url: https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ar
fetched_at: 2026-06-08T14:59:10.811929+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الفيديوهات

> للتعرّف على كيفية إنشاء الفيديوهات، يُرجى الاطّلاع على دليل [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar).

يمكن لنماذج Gemini معالجة الفيديوهات، ما يتيح العديد من حالات الاستخدام المتقدّمة للمطوّرين التي كانت تتطلّب في السابق نماذج خاصة بالمجال.
تشمل بعض إمكانات Gemini في مجال الرؤية ما يلي: وصف الفيديوهات وتقسيمها واستخراج المعلومات منها، والإجابة عن الأسئلة حول محتوى الفيديو، والإشارة إلى طوابع زمنية محدّدة داخل الفيديو.

يمكنكم تقديم الفيديوهات كبيانات إدخال إلى Gemini بالطرق التالية:

| طريقة الإرسال | أقصى حجم | حالة الاستخدام المقترَحة |
| --- | --- | --- |
| [‫File API](#upload-video) | 20 غيغابايت (مدفوعة) / 2 غيغابايت (مجانية) | الملفات الكبيرة (أكثر من 100 ميغابايت)، والفيديوهات الطويلة (أكثر من 10 دقائق)، والملفات القابلة لإعادة الاستخدام |
| [تسجيل Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar#registration) | 2 غيغابايت (لكل ملف، بدون حدود للتخزين) | الملفات الكبيرة (أكثر من 100 ميغابايت)، والفيديوهات الطويلة (أكثر من 10 دقائق)، والملفات الثابتة القابلة لإعادة الاستخدام |
| [البيانات المضمّنة](#inline-video) | أقل من 100 ميغابايت | الملفات الصغيرة (أقل من 100 ميغابايت)، والفيديوهات القصيرة (أقل من دقيقة واحدة)، والبيانات التي يتم إدخالها مرة واحدة |
| [عناوين URL لفيديوهات YouTube](#youtube) | لا ينطبق | فيديوهات YouTube العلنية |

> **ملاحظة:** ننصح باستخدام [File API](#upload-video) في معظم حالات الاستخدام، خاصةً للملفات الأكبر من 100 ميغابايت أو عندما تريدون إعادة استخدام الملف في طلبات متعددة.

للتعرّف على طرق إدخال الملفات الأخرى، مثل استخدام عناوين URL خارجية أو ملفات
مخزّنة في Google Cloud، يُرجى الاطّلاع على دليل
[طرق إدخال الملفات](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=ar).

### تحميل ملف فيديو

يُنزِّل الرمز البرمجي التالي فيديو نموذجيًا ويحمّله باستخدام [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ar)، وينتظر معالجته، ثم يستخدم مرجع الملف الذي تم تحميله لتلخيص الفيديو.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  // Wait for the file to be processed.
  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### راحة

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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

يجب دائمًا استخدام Files API عندما يكون إجمالي حجم الطلب (بما في ذلك الملف والمطلوب النصي وتعليمات النظام وما إلى ذلك) أكبر من 20 ميغابايت، أو إذا كانت مدة الفيديو كبيرة، أو إذا كنتم تنوون استخدام الفيديو نفسه في طلبات متعددة.
تقبل File API تنسيقات ملفات الفيديو مباشرةً.

لمزيد من المعلومات عن استخدام ملفات الوسائط، يُرجى الاطّلاع على
[Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ar).

### تمرير بيانات الفيديو مضمّنة

بدلاً من تحميل ملف فيديو باستخدام File API، يمكنكم تمرير فيديوهات أصغر حجمًا مباشرةً في الطلب. هذا مناسب للفيديوهات القصيرة التي يقل إجمالي حجم الطلب فيها عن 20 ميغابايت.

في ما يلي مثال على تقديم بيانات فيديو مضمّنة:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### راحة

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### تمرير عناوين URL لفيديوهات YouTube

يمكنكم تمرير عناوين URL لفيديوهات YouTube مباشرةً إلى Gemini API كجزء من طلبكم على النحو التالي:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**القيود:**

- في المستوى المجاني، لا يمكنكم تحميل أكثر من 8 ساعات من فيديوهات YouTube في اليوم.
- في المستوى المدفوع، لا يوجد حدّ أقصى استنادًا إلى مدة الفيديو.
- بالنسبة إلى النماذج التي تسبق Gemini 2.5، لا يمكنكم تحميل سوى فيديو واحد لكل طلب. بالنسبة إلى Gemini 2.5 والنماذج الأحدث، يمكنكم تحميل 10 فيديوهات بحدّ أقصى لكل طلب.
- لا يمكنكم تحميل سوى الفيديوهات العلنية (وليس الفيديوهات الخاصة أو غير المُدرَجة).

## الإشارة إلى الطوابع الزمنية في المحتوى

يمكنكم طرح أسئلة حول نقاط زمنية محدّدة داخل الفيديو باستخدام طوابع زمنية بالتنسيق `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### راحة

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## استخراج إحصاءات مفصّلة من الفيديو

توفّر نماذج Gemini إمكانات قوية لفهم محتوى الفيديو من خلال معالجة المعلومات من كلٍّ من **المقطع الصوتي والمرئي**. يتيح لكم ذلك استخراج مجموعة كبيرة من التفاصيل، بما في ذلك إنشاء أوصاف لما يحدث في الفيديو والإجابة عن الأسئلة حول محتواه.

بالنسبة إلى الأوصاف المرئية، يأخذ النموذج عيّنات من الفيديو بمعدّل **إطار واحد في الثانية** (FPS). يعمل معدّل أخذ العيّنات التلقائي هذا بشكل جيد لمعظم المحتوى، ولكن يُرجى العِلم أنّه قد لا يرصد التفاصيل في الفيديوهات التي تتضمّن حركة سريعة أو تغييرات سريعة في المشهد.
بالنسبة إلى هذا المحتوى الذي يتضمّن حركة عالية، ننصحكم بـ [ضبط عدد اللقطات في الثانية المخصّص](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### راحة

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## تنسيقات الفيديو المتوافقة

تتوافق Gemini مع أنواع MIME لتنسيقات الفيديو التالية:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## التفاصيل الفنية حول الفيديوهات

- **النماذج والسياق المتوافقة**: يمكن لجميع نماذج Gemini معالجة بيانات الفيديو.
  - يمكن للنماذج التي تتضمّن قدرة استيعاب بسعة مليون رمز مميّز معالجة فيديوهات تصل مدتها إلى ساعة واحدة بدقة الوسائط التلقائية أو 3 ساعات بدقة الوسائط المنخفضة.
- **معالجة File API**: عند استخدام File API، يتم تخزين الفيديوهات بمعدّل إطار واحد في الثانية (FPS) وتتم معالجة الصوت بمعدّل 1 كيلوبت في الثانية (قناة واحدة).
  تتم إضافة الطوابع الزمنية كل ثانية.
  - قد تتغيّر هذه المعدّلات في المستقبل لتحسين الاستنتاج.
- **احتساب الرموز المميّزة**: يتم تقسيم كل ثانية من الفيديو إلى رموز مميّزة على النحو التالي:
  - الإطارات الفردية (التي يتم أخذ عيّنات منها بمعدّل إطار واحد في الثانية):
    - إذا تم ضبط `media_resolution` على منخفضة، يتم تقسيم الإطارات إلى رموز مميّزة بمعدّل 66 رمزًا مميّزًا لكل إطار.
    - وإلّا، يتم تقسيم الإطارات إلى رموز مميّزة بمعدّل 258 رمزًا مميّزًا لكل إطار.
  - الصوت: 32 رمزًا مميّزًا في الثانية
  - يتم أيضًا تضمين البيانات الوصفية.
  - الإجمالي: حوالي 300 رمز مميّز في الثانية من الفيديو بدقة الوسائط التلقائية، أو 100 رمز مميّز في الثانية من الفيديو بدقة الوسائط المنخفضة
- **دقة الوسائط**: يقدّم Gemini 3 تحكّمًا دقيقًا في معالجة الرؤية المتعدّدة الوسائط
  باستخدام المعلَمة `media_resolution`. تحدّد المعلَمة `media_resolution` **الحد الأقصى لعدد الرموز المميّزة المخصّصة لكل صورة إدخال أو إطار فيديو.**
  تؤدي الدقة الأعلى إلى تحسين قدرة النموذج على قراءة النصوص الدقيقة أو تحديد التفاصيل الصغيرة، ولكنها تزيد من استخدام الرموز المميّزة ووقت الاستجابة.

  لحساب الرموز المميّزة، يُرجى الاطّلاع على دليل [الرموز المميّزة](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ar).
- **تنسيق الطابع الزمني**: عند الإشارة إلى لحظات محدّدة في فيديو ضمن طلبكم، استخدِموا التنسيق `MM:SS` (مثلاً، `01:15` للدقيقة و15 ثانية).
- **أفضل الممارسات**:

  - استخدِموا فيديو واحدًا فقط لكل طلب للحصول على أفضل النتائج.
  - إذا كنتم تجمعون بين نص وفيديو واحد، ضعوا المطلوب النصي *بعد* جزء الفيديو في مصفوفة `input`.
  - يُرجى العِلم أنّ تسلسلات الأحداث السريعة قد تفقد التفاصيل بسبب معدّل أخذ العيّنات الذي يبلغ إطارًا واحدًا في الثانية. ننصحكم بإبطاء هذه المقاطع إذا لزم الأمر.

## الخطوات التالية

يوضّح هذا الدليل كيفية تحميل ملفات الفيديو وإنشاء نصوص من بيانات إدخال الفيديو. لمزيد من المعلومات، يُرجى الاطّلاع على المَراجع التالية:

- [تعليمات النظام](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar#system-instructions):
  تتيح لكم تعليمات النظام توجيه سلوك النموذج استنادًا إلى
  احتياجاتكم وحالات استخدامكم المحدّدة.
- [واجهة برمجة تطبيقات الملفات](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ar): مزيد من المعلومات عن تحميل الملفات وإدارتها لاستخدامها مع Gemini.
- [استراتيجيات إنشاء الطلبات بالملفات](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ar#prompt-guide): تتيح Gemini API إنشاء الطلبات باستخدام بيانات النص والصورة والصوت والفيديو، ويُعرف ذلك أيضًا باسم إنشاء الطلبات المتعددة الوسائط.
- [إرشادات الأمان](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ar): في بعض الأحيان، تُنتج نماذج الذكاء الاصطناعي التوليدي
  نتائج غير متوقّعة، مثل النتائج غير الدقيقة
  أو المتحيّزة أو المسيئة. تُعدّ المعالجة اللاحقة والتقييم من قِبل فريق ضروريَين للحدّ من خطر الضرر الناتج عن هذه النتائج.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-09 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-09 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
