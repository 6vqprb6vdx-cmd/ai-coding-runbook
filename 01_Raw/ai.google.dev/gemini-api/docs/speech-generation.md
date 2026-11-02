---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar
fetched_at: 2026-11-02T07:01:45.060332+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0645\u062d\u062a\u0648\u0649 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 \"\u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u0646\u0635 \u0625\u0644\u0649 \u0643\u0644\u0627\u0645\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء محتوى باستخدام تكنولوجيا "تحويل النص إلى كلام"

يمكن لـ Gemini API تحويل النص المُدخَل إلى ملف صوتي لمتحدّث واحد أو عدة متحدّثين باستخدام إمكانات تحويل النص إلى كلام (TTS) في Gemini.
يمكن *[التحكّم](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#controllable)* في إنشاء ميزة "تحويل النص إلى كلام"، ما يعني أنّه يمكنك الجمع بين البيانات الوصفية المنظَّمة لردود المساعد (`speech_metadata`) وعلامات الصوت المضمّنة لتوجيه *أسلوب* الصوت و*لهجته* و*وتيرته* و*نبرته*.

تختلف ميزة &quot;تحويل النص إلى كلام&quot; عن ميزة إنشاء الكلام التي توفّرها [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar)، والمصمّمة للمدخلات والمخرجات التفاعلية وغير المنظَّمة والمتعددة الوسائط. في حين أنّ Live API تتفوّق في سياقات المحادثات الديناميكية، فإنّ ميزة "تحويل النص إلى كلام" من خلال Gemini API مصمّمة للسيناريوهات التي تتطلّب تلاوة النص بدقة مع التحكّم الدقيق في الأسلوب والصوت، مثل إنشاء بودكاست أو كتاب مسموع.

يوضّح لك هذا الدليل كيفية إنشاء ملفات صوتية لمتحدّث واحد أو لمتحدّثين متعدّدين من
النصوص باستخدام [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ar)
(`gemini-3.8-flash-tts`) و[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ar)
(`gemini-3.8-flash-lite-tts`).

## قبل البدء

تأكَّد من استخدام نموذج Gemini لتحويل النص إلى كلام مدرَج في قسم
[النماذج المتوافقة](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#supported-models)،
والترقية إلى أحدث إصدار من حزمة Google GenAI SDK (`google-genai >= 2.25.0` للغة Python
أو `@google/genai >= 2.24.0` للغة JavaScript/TypeScript) أو استخدام واجهة برمجة التطبيقات REST API.
للحصول على أفضل النتائج، راجِع
[حالات استخدام كل نموذج](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#when-to-use-which-model)
لاختيار أفضل نموذج لعبء العمل.

قد يكون من المفيد
[اختبار نماذج تحويل النص إلى كلام في Gemini في AI Studio](https://aistudio.google.com/generate-speech?hl=ar)
قبل البدء في الإنشاء.

## تحويل النص إلى كلام لمتحدّث واحد

لتحويل النص إلى صوت لمتحدّث واحد باستخدام نماذج تحويل النص إلى كلام في Gemini 3.8، يجب إدخال النص الحرفي في `input`، وإرفاق نمط على مستوى الدور باستخدام تعليق توضيحي `speech_metadata`، وضبط الصوت في `generation_config.speech_config`. يمكنك اختيار صوت من [خيارات الصوت](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#voices) المُعدّة مسبقًا، أو من "مكتبة الأصوات الموسّعة" (`GET /v1beta/voices`)، أو من معرّف [تصميم صوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar) مخصّص (`voice_...`)، أو من معرّف [تقليد الصوت](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ar) (`voice_...`، أو `voicekey_...` الاختياري بدون حالة).

يحفظ هذا المثال الناتج الصوتي التلقائي بتنسيق WAV ‏ (`audio/wav`) من النموذج مباشرةً في ملف:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

في حزمتَي تطوير البرامج (SDK) لكل من Python وJavaScript، يمكنك استرداد بيانات الصوت التي تم إنشاؤها باستخدام السمة المريحة `interaction.output_audio` التي تعرض آخر مجموعة صوتية تم إنشاؤها (في استجابات REST JSON الأولية، يتم تخزين الصوت بترميز base64 في `steps[].content[].data`). للحصول على تفاصيل حول السمات المريحة، يُرجى الاطّلاع على [نظرة عامة على التفاعلات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar#convenience-properties).

## تحويل النص إلى كلام لعدة متحدثين

بالنسبة إلى الحوارات التي يشارك فيها عدة متحدثين، يجب ضبط متحدثَين في `speech_config.speakers`
وتمرير كل دور كعنصر نصي منفصل مع تعليق توضيحي `speech_metadata`
يحدّد `speaker` و`style` الاختياري على مستوى الدور. يُرجى العِلم أنّ
`speech_config` يقبل مصفوفة (`[{"voice": "..."}]`) لإنشاء صوت
متحدّث واحد وكائن (`{"speakers": [...]}`) لإنشاء صوت عدة متحدّثين:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## التحكّم في أسلوب الكلام باستخدام البيانات الوصفية والعلامات

يتعامل نموذج تحويل النص إلى كلام Gemini 3.8 مع حقل `text` على أنّه نص حرفي فقط. للتحكّم في طريقة الإلقاء بدون قراءة التوجيهات المسرحية بصوت عالٍ، يمكنك تقسيم التعليمات حسب النطاق:

- **طريقة الإلقاء المستمرة على مستوى الدور (`speech_metadata.style`):** يمكنك تحديد المشاعر
  وطريقة الإلقاء والنبرة والسرعة ومستوى الصوت التي تنطبق على الدور بأكمله
  في الحقل `style` (على سبيل المثال، `"style": "whispered urgently"`
  أو `"style": "out of breath"` أو `"style": "warm and enthusiastic"`).
- **الأحداث في وقت محدّد (العلامات المضمّنة):** يمكنك وضع فواصل صوتية قصيرة غير كلامية أو فواصل مؤقتة مباشرةً داخل النص باستخدام الأقواس الزاوية (على سبيل المثال، `"Wait... <short pause> did you hear that? <sigh>"` أو `"Excuse me <cough> as I was saying..."`).

يمكنك الاطّلاع على [دليل كتابة الطلبات](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#prompting-guide)
لمعرفة أفضل الممارسات الشاملة.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Dr. Anya",
                    "style": "whispered urgently",
                }],
            },
            {
                "type": "text",
                "text": "<gasp> No way! <laugh> We've been searching for this species all season!",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Liam",
                    "style": "warm and enthusiastic",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Dr. Anya", "voice": "Kore"},
                {"speaker": "Liam", "voice": "Puck"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: 'Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Dr. Anya',
                  style: 'whispered urgently',
               }],
            },
            {
               type: 'text',
               text: "<gasp> No way! <laugh> We've been searching for this species all season!",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Liam',
                  style: 'warm and enthusiastic',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Dr. Anya', voice: 'Kore' },
               { speaker: 'Liam', voice: 'Puck' },
            ],
         },
      },
   });

   if (interaction.output_audio?.data) {
      const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
      fs.writeFileSync('out.wav', audioBuffer);
   }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Dr. Anya",
            "style": "whispered urgently"
          }]
        },
        {
          "type": "text",
          "text": "<gasp> No way! <laugh> We'\''ve been searching for this species all season!",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Liam",
            "style": "warm and enthusiastic"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "speakers": [
          { "speaker": "Dr. Anya", "voice": "Kore" },
          { "speaker": "Liam", "voice": "Puck" }
        ]
      }
    }
  }'
```

## إنشاء الكلام من خلال البث

يمكنك بث الصوت الذي تم إنشاؤه أثناء تركيبه من خلال ضبط
`stream: true`. على عكس الطلبات الأحادية (التي تعرض ملف WAV كاملاً مع عنوان RIFF)، **تعرض طلبات البث تلقائيًا أجزاء PCM خطية (`audio/l16`، 24 كيلوهرتز، أحادية) غير موقعة ذات 16 بت بدون عنوان**، بحيث يمكن تشغيل أجزاء الصوت أو دمجها بشكل مستمر بدون عناوين الحاويات.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## تنسيقات إخراج الصوت

تستخدم نماذج تحويل النص إلى كلام في Gemini 3.8 تنسيقات صوتية تلقائية مختلفة حسب ما إذا كان الطلب أحاديًا أو بثًا:

- **الطلبات الأحادية (`stream=False`):** تعرض ملفات صوتية كاملة بتنسيق **WAV (`audio/wav`)** مع عنوان RIFF عادي (24 كيلوهرتز، أحادي، 16 بت، PCM بتنسيق little-endian). يمكنك حفظ وحدات بايت الصوت التي تم فك ترميزها مباشرةً في ملف `.wav` بدون
  إضافة عنوان WAV يدويًا.
- **طلبات البث (`stream=True`):** يتم عرض أجزاء **PCM خطية أولية بدون عنوان (`audio/l16`)** (24 كيلوهرتز، أحادي، 16 بت، PCM بتنسيق little-endian) بشكل تلقائي حتى يمكن بث الأجزاء أو دمجها بشكل مستمر بدون عناوين حاويات في كل جزء.

لطلب ترميز صوتي أو معدّل بيانات مختلف في الملف الصوتي، اضبط `mime_type` و`sample_rate` الاختياري داخل `response_format`:

| التنسيق | قيمة `mime_type` | الوصف |
| --- | --- | --- |
| **WAV** *(unary default)* | `"audio/wav"` | ملف WAV غير مضغوط برأس RIFF (تنسيق PCM أحادي القناة، 16 بت، بنظام ترتيب بايتات صغير، وبتردد تلقائي يبلغ 24 كيلوهرتز). الإعداد التلقائي للطلبات الأحادية |
| **Raw PCM (L16)** *(الإعداد التلقائي للبث)* | `"audio/l16"` | صوت PCM خطي غير مضغوط وبدون عنوان، 16 بت، موقَّع، بنظام little-endian (24 كيلوهرتز، أحادي). الإعداد التلقائي لطلبات البث |
| **Mu-law** | `"audio/mulaw"` | صوت بترميز G.711 mu-law ‏8 بت (يُستخدم عادةً في أنظمة الاتصالات الهاتفية/الاستجابة الصوتية التفاعلية في أمريكا الشمالية واليابان). |
| **A-law** | `"audio/alaw"` | صوت بترميز G.711 A-law ‏8 بت (شائع الاستخدام في أنظمة الاتصالات الهاتفية الأوروبية والدولية). |

يمكنك أيضًا تحديد `sample_rate` بالهرتز (على سبيل المثال، `24000` أو `16000` أو
`8000`).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## خيارات الصوت

تتيح ميزة "تحويل النص إلى كلام" في Gemini 3.8 أربع طرق لاختيار الأصوات أو إنشائها:

1. **أصوات الاستوديو المُعدّة مسبقًا:** 30 صوتًا منظّمًا مدرجًا في الجدول التالي.
2. **مكتبة أصوات موسّعة:** مئات الأصوات الإضافية بلغات ولهجات وأنماط شخصيات مختلفة يمكن الوصول إليها باستخدام `client.voices.list()` (`GET /v1beta/voices`).
3. **[تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar):** يمكنك إنشاء شخصية صوتية مخصّصة من وصف بلغة طبيعية في [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ar) أو باستخدام `POST /v1beta/voices` (`type="prompted"`، الذي يعرض معرّف `voice_...` ثابتًا ومعاينة `sample_audio` WAV في `CreateVoice` و`GetVoice`).
4. **[تقليد الصوت](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ar):** يمكنك تقليد صوت المتحدّث من خلال عيّنة صوتية مرجعية وموافقة في [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ar) أو باستخدام `POST /v1beta/voices` (`type="replicated"`، أو `store=True` الثابتة تلقائيًا أو `store=False` الاختيارية غير المحدّدة الحالة).

### الحدود القصوى للصوت المخصَّص ومدة الصلاحية

| نوع الصوت | وضع التخزين | الحصة / الحدّ | الاحتفاظ بالبيانات (مدة البقاء) |
| --- | --- | --- | --- |
| **الأصوات التي تتأثر بالسياق** (`voice_...`، سواء كانت مستندة إلى طلبات أو مكرَّرة) | `store=True` | **‫200 صوت لكل مشروع** (مشترَكة بين الأصوات المستندة إلى نموذج والأصوات المكرّرة) | **عام واحد من آخر استخدام\*** |
| **مفاتيح الصوت عديمة الحالة** (`voicekey_...`، مكرّرة) | `store=False` | تتم إدارتها من قِبل العميل | **‫7 أيام** |

\* **تمديد فترة الاحتفاظ بالبيانات:** تتم إعادة ضبط فترة الاحتفاظ بالبيانات التي تبلغ عامًا واحدًا في كل مرة يتم فيها استخدام الصوت بشكل نشط (إما من خلال تحويل النص إلى كلام باستخدام الصوت أو استخدامه كصوت أساسي لإعادة المزج). يتم تلقائيًا حذف الأصوات التي لا يتم استخدامها لمدة عام واحد.

### الأصوات المُعدّة مسبقًا

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** -- *مفيدة* |
| **Kore** -- *Firm* | **Fenrir** -- *متحمّس* | ‫**Leda** -- *شبابي* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe**: *مريح* |
| **Autonoe** -- *مشرق* | **Enceladus** -- *Breathy* | **إيابيتوس** -- *واضح* |
| **Umbriel**: *سهل التعامل* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **إرينوم** -- *شفاف* | **Algenib** -- *أجش* | **Rasalgethi** -- *مفيدة* |
| **Laomedeia** -- *مرح* | **Achernar** -- *ناعم* | **Alnilam** -- *الشركة* |
| **Schedar** -- *Even* | **Gacrux**: *ناضج* | **Pulcherrima** -- *واثق* |
| **Achird**: *ودود* | **Zubenelgenubi** -- *غير متكلف* | **Vindemiatrix** -- *لطيف* |
| **سعد الأخبية** -- *مفعم بالحيوية* | **Sadaltager** -- *مستخدم مطّلع* | **Sulafat** -- *دافئ* |

### مكتبة أصوات موسّعة وفلترة

بالإضافة إلى أصوات الاستوديو المميّزة الثلاثين الواردة في الجدول السابق، توفّر **مكتبة الأصوات الموسّعة** مئات الأصوات الإضافية بلغات ولهجات إقليمية وشخصيات ومجالات مختلفة. يمكنك تصفّح &quot;مكتبة الأصوات&quot; بالكامل وفلترتها
وتجربتها بشكل تفاعلي في
[Google AI Studio](https://aistudio.google.com/generate-speech?hl=ar)، أو الاستعلام عنها
برمجيًا باستخدام `client.voices.list()` (`GET /v1beta/voices`، باستخدام
`google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

تعرض الدالة `ListVoices` الأصوات المخصّصة المخزّنة (مرتّبة من الأحدث إلى الأقدم) تليها الأصوات المُعدّة مسبقًا في الكتالوج والتي تطابق معايير الفلتر. عند تمرير قيم متعددة لفلتر قائمة، يتم عرض الأصوات التي تطابق **أي** قيمة في هذا الفلتر (`OR`)، بينما يتم دمج معلَمات الفلتر المختلفة مع `AND`:

| المَعلمة | النوع | الوصف |
| --- | --- | --- |
| `language_code` | `list[str]` | علامات لغة BCP-47 (على سبيل المثال، `["en-US", "en-GB"]`). مطابقة تامة غير حساسة لحالة الأحرف. |
| `region_code` | `list[str]` | رموز المناطق بتنسيق ISO 3166-1 alpha-2 أو UN M.49 (مثلاً، `["US", "GB"]`) |
| `accent` | `list[str]` | أوصاف اللهجات الإقليمية (على سبيل المثال، `["American", "British"]`) |
| `gender` | `list[str]` | المظهر الخارجي للجنس (`"female"` أو `"male"` أو `"neutral"`) |
| `pitch` | `list[str]` | تصنيف طبقة الصوت (`"low"` أو `"medium"` أو `"high"`) |
| `persona` | `list[str]` | الشخصية الصوتية أو نموذج الشخصية (على سبيل المثال، `["Warm, Friendly"]` و`["Narrator"]`) |
| `contexts` (`context` في REST) | `list[str]` | نطاق الاستخدام الأمثل (على سبيل المثال، `["Audiobook", "Conversational", "News"]`) |
| ‫`type` (‫`type_` في Python) | `list[str]` | الفلترة حسب مصدر الصوت: `"prebuilt"` أو `"prompted"` ([تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar)) أو `"replicated"` ([تقليد الصوت](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ar)). |
| `search` | `str` | بحث عن سلسلة فرعية في نص حرّ يتطابق مع كل من `display_name` و`description` بدون حساسية لحالة الأحرف |
| `page_size` | `int` | الحد الأقصى لعدد الأصوات التي يتم عرضها في كل صفحة (القيمة التلقائية هي `50`، والحد الأقصى هو `1000`). |
| `page_token` | `str` | الرمز المميّز من `response.next_page_token` لجلب الصفحة التالية من النتائج |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## اللغات المتاحة

تتعرّف نماذج تحويل النص إلى كلام على لغة الإدخال تلقائيًا.
يتيح [نموذج تحويل النص إلى كلام Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ar)
(`gemini-3.8-flash-tts`) **أكثر من 130 لغة**،
بينما يتيح [نموذج تحويل النص إلى كلام Gemini 3.8 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ar)
(`gemini-3.8-flash-lite-tts`) **أكثر من 100 لغة**:

| اللغة | Gemini 3.8 Flash TTS | نموذج تحويل النص إلى كلام Gemini 3.8 Flash-Lite |
| --- | --- | --- |
| الأتشيهية (بالأبجدية العربية) | ✔️ | ✔️ |
| الأفريقانية | ✔️ | ✔️ |
| الأكانية | ✔️ | ✔️ |
| الأمهرية | ✔️ | ✔️ |
| الأرمينية | ✔️ | ✔️ |
| الأسامية | ✔️ | ✔️ |
| الأوادية | ✔️ | ✔️ |
| باليني | ✔️ | ✔️ |
| البنغالية | ✔️ | ✔️ |
| البنجرية (بالأحرف العربية) | ✔️ | — |
| البنجرية (نص لاتيني) | ✔️ | ✔️ |
| الباشكيرية | ✔️ | — |
| الباسكية | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| البيمبا | ✔️ | — |
| البهوجبورية | ✔️ | ✔️ |
| البوسنية | ✔️ | ✔️ |
| بوغينيز | ✔️ | ✔️ |
| البلغارية | ✔️ | ✔️ |
| البورمية | ✔️ | — |
| الكَنْتونية | ✔️ | ✔️ |
| الكتالانية | ✔️ | ✔️ |
| السيبيوانية | ✔️ | ✔️ |
| الكردية الوسطى | ✔️ | ✔️ |
| التشاتيسغارهية | ✔️ | ✔️ |
| الصينية (نص هانز) | ✔️ | ✔️ |
| الصينية (نص هانت) | ✔️ | ✔️ |
| التتارية القرمية | ✔️ | — |
| الكرواتية | ✔️ | ✔️ |
| التشيكية | ✔️ | ✔️ |
| الدانماركية | ✔️ | ✔️ |
| الهولندية | ✔️ | ✔️ |
| الدايلا | ✔️ | — |
| الدزونغا | ✔️ | — |
| العربية المصرية | ✔️ | ✔️ |
| الإنجليزية | ✔️ | ✔️ |
| الإستونية | ✔️ | ✔️ |
| الفلبينية | ✔️ | ✔️ |
| الفنلندية | ✔️ | — |
| الفرنسية | ✔️ | ✔️ |
| الغليشيانية | ✔️ | ✔️ |
| الجاندا | ✔️ | ✔️ |
| الجورجية | ✔️ | ✔️ |
| الألمانية | ✔️ | ✔️ |
| اليونانية | ✔️ | ✔️ |
| الغوارانية | ✔️ | — |
| الغوجاراتية | ✔️ | ✔️ |
| الكريولية الهايتية | ✔️ | ✔️ |
| المنغولية (هالها) | ✔️ | ✔️ |
| الهوسا | ✔️ | ✔️ |
| العبرية | ✔️ | ✔️ |
| الهندية | ✔️ | ✔️ |
| الهنغارية | ✔️ | ✔️ |
| الأيسلندية | ✔️ | ✔️ |
| الإيجبو | ✔️ | — |
| الايلوكو | ✔️ | ✔️ |
| الإندونيسية | ✔️ | ✔️ |
| الفارسية الإيرانية | ✔️ | ✔️ |
| الإيطالية | ✔️ | ✔️ |
| اليابانية | ✔️ | ✔️ |
| الجاوية | ✔️ | ✔️ |
| القبائلية | ✔️ | — |
| الكامبا | ✔️ | ✔️ |
| الكانادا | ✔️ | ✔️ |
| الكشميرية (بالأحرف العربية) | ✔️ | ✔️ |
| الكشميرية (نص ديفا) | ✔️ | ✔️ |
| الكازاخستانية | ✔️ | ✔️ |
| الخميرية | ✔️ | ✔️ |
| الكيكويو | ✔️ | ✔️ |
| الكينيارواندا | ✔️ | ✔️ |
| كونغو | ✔️ | ✔️ |
| الكورية | ✔️ | ✔️ |
| القيرغيزية | ✔️ | ✔️ |
| لاو | ✔️ | ✔️ |
| اللاتغالية | ✔️ | — |
| اللينجالا | ✔️ | ✔️ |
| الليتوانية | ✔️ | — |
| اللكسمبورغية | ✔️ | — |
| المقدونية | ✔️ | ✔️ |
| ماجادهي | ✔️ | ✔️ |
| المايثيلية | ✔️ | ✔️ |
| المالايالامية | ✔️ | ✔️ |
| المالطية | ✔️ | ✔️ |
| المانيبورية | ✔️ | ✔️ |
| المراثية | ✔️ | ✔️ |
| المينانجكاباو (بالأحرف العربية) | ✔️ | ✔️ |
| المينانجكاباو (نص لاتيني) | ✔️ | — |
| ميزو | ✔️ | ✔️ |
| النيبالية (لغة فردية) | ✔️ | ✔️ |
| الفولانية النيجيرية | ✔️ | ✔️ |
| الأذربيجانية الشمالية | ✔️ | ✔️ |
| السوتو الشمالية | ✔️ | ✔️ |
| الأوزبكية الشمالية | ✔️ | ✔️ |
| البوكمالية النرويجية | ✔️ | ✔️ |
| النرويجية الجديدة | ✔️ | ✔️ |
| النيانجا | ✔️ | ✔️ |
| الأوكسيتانية | ✔️ | — |
| الأوديا (لغة فردية) | ✔️ | ✔️ |
| البانغاسينية | ✔️ | — |
| الفارسية (أفغانستان) | ✔️ | ✔️ |
| البولندية | ✔️ | ✔️ |
| البرتغالية | ✔️ | ✔️ |
| البنجابية | ✔️ | ✔️ |
| الرومانية | ✔️ | ✔️ |
| الروسية | ✔️ | ✔️ |
| السنتالية | ✔️ | ✔️ |
| الصربية | ✔️ | ✔️ |
| السندية | ✔️ | — |
| السنهالية | ✔️ | ✔️ |
| السلوفاكية | ✔️ | ✔️ |
| السلوفينية | ✔️ | — |
| الصومالية | ✔️ | — |
| الأذربيجانية الجنوبية | ✔️ | ✔️ |
| البشتوية الجنوبية | ✔️ | ✔️ |
| السوتو الجنوبية | ✔️ | — |
| الإسبانية | ✔️ | ✔️ |
| العربية الفصحى (الكتابة العربية) | ✔️ | ✔️ |
| العربية الفصحى (نص لاتيني) | ✔️ | ✔️ |
| اللاتفية العادية | ✔️ | ✔️ |
| الملايوية المعيارية | ✔️ | ✔️ |
| السواحيلية (لغة فردية) | ✔️ | — |
| السواتي | ✔️ | — |
| السويدية | ✔️ | — |
| الطاجيكية | ✔️ | — |
| التاميلية | ✔️ | ✔️ |
| التيلوغوية | ✔️ | ✔️ |
| التايلاندية | ✔️ | — |
| التيجرينيا | ✔️ | — |
| الألبانية التوسكية | ✔️ | — |
| التركية | ✔️ | ✔️ |
| الأويغورية | ✔️ | — |
| الفيتنامية | ✔️ | ✔️ |

## النماذج المتوافقة

| الطراز | متحدّث واحد | متحدّثون متعددون | تصميم الصوت | تقليد الصوت |
| --- | --- | --- | --- | --- |
| [‫Gemini 3.8 Flash لتحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ar) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [‫Gemini 3.8 Flash-Lite لتحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ar) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [النسخة الحصرية من Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ar) | ✔️ | ✔️ | — | — |
| [‫Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=ar) | ✔️ | ✔️ | — | — |

### حالات استخدام كل نموذج

يستخدم كلا نموذجَي تحويل النص إلى كلام في Gemini 3.8 مخطط واجهة برمجة التطبيقات (API) وتنسيق الطلبات نفسهما،
ما يتيح لك التبديل بينهما من خلال تغيير مَعلمة واحدة:

- **استخدام [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ar)
  (`gemini-3.8-flash-tts`)** عندما تكون الأولوية القصوى هي الدقة الصوتية العالية والأداء الدقيق
  والتحكّم التعبيري. وهو مثالي للأعمال الإبداعية على مستوى الاستوديو، والحوارات المعقّدة التي يشارك فيها عدة متحدثين، والعلامات الصوتية المكثفة، والنطق الصعب، واللهجات الإقليمية أو لهجات الأقليات، والسرد الطويل الذي يتطلب صوتًا قويًا وثباتًا في نبرة الغرفة.
- **استخدام [نموذج تحويل النص إلى كلام Gemini 3.8 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ar)
  (`gemini-3.8-flash-lite-tts`)** كبديل سريع وفعّال من حيث التكلفة لـ `gemini-3.1-flash-tts-preview`: تم تحسينه لإنتاج كميات كبيرة من المحتوى الصوتي، وإنشاء سلاسل من الوكلاء الصوتيين الحواريين، وتوفير ميزات القراءة بصوت عالٍ، وتقليد الصوت بشكل موثوق، وتحويل النص إلى كلام بصوت متحدث واحد يوميًا باللغات الرئيسية.

### دليل نقل البيانات

في حال نقل البيانات من `gemini-3.1-flash-tts-preview` أو إصدارات أقدم من نماذج تحويل النص إلى كلام في Gemini إلى Gemini 3.8:

1. **نقل التعليمات على مستوى الدور إلى `speech_metadata`:** يتعامل نموذج تحويل النص إلى كلام Gemini 3.8 مع النص المُدخَل على أنّه نص حرفي. يجب نقل تعليمات التسليم المستمر (`style`، مثل `"whispering"` أو `"out of breath"` أو `"speaking slowly"`) وتصنيفات المتحدّثين (`speaker`) إلى تعليقات توضيحية منظَّمة من النوع `speech_metadata` بدلاً من تضمين تعليمات المسرح في نص النص.
2. **استخدام علامات الأقواس الزاوية المضمّنة للأحداث الصوتية في وقت محدّد فقط:** يجب إبقاء
   الأصوات غير اللفظية والوقفات اللحظية مضمّنة في النص باستخدام
   الأقواس الزاوية (مثل `<laugh>` أو `<sigh>` أو `<cough>` أو `<breath>` أو
   `<short pause>`). يجب تجنُّب علامات المؤثرات الصوتية (مثل التصفيق أو الارتطام)
   ووضع أساليب الإلقاء في `speech_metadata.style`.
3. **تحديد `speaker` في كل دور في الطلبات التي تتضمّن عدة متحدثين:** يجب أن يتضمّن كل دور في الطلب الذي يتضمّن عدة متحدثين `speaker` بشكل صريح داخل `speech_metadata` يتطابق مع أحد المتحدثين الذين تم ضبطهم.
4. **تصميم الشخصيات مسبقًا باستخدام ميزة "تصميم الصوت":** يمكنك استبدال الفقرات المتعددة
   `"Audio Profile"` أو `"Director's Notes"` بمقاطع صوتية مخصّصة تم إنشاؤها
   في [تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar)، ثم استخدام معرّف `voice_...`
   في طلبات تحويل النص إلى كلام مع سلاسل `style` فارغة أو بسيطة.
5. **مراعاة مخرجات WAV التلقائية (`audio/wav`) في الطلبات الأحادية:** على عكس
   `gemini-3.1-flash-tts-preview` ونماذج تحويل النص إلى كلام السابقة (التي كانت تعرض
   ملفات PCM الأولية بدون رأس `audio/l16` تلقائيًا)، يعرض نموذج تحويل النص إلى كلام في Gemini 3.8 ملفات WAV الصوتية
   (`audio/wav`) مع رأس RIFF عادي تلقائيًا للطلبات الأحادية.
   - إذا كان الرمز البرمجي الخاص بك يغلّف سابقًا وحدات بايت PCM الأولية في عنوان WAV (على سبيل المثال، باستخدام وحدة `wave` في Python أو `ffmpeg`)، عليك إزالة غلاف العنوان اليدوي وكتابة وحدات البايت التي تم عرضها مباشرةً في ملف `.wav`.
   - إذا كان مسار التعلّم يتطلّب صوت PCM أو mu-law أو A-law خام بدون عنوان،
     اضبط `response_format.mime_type` صراحةً على `"audio/l16"` أو `"audio/mulaw"` أو
     `"audio/alaw"` (على سبيل المثال، `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}`
     في Interactions API أو `AUDIO_L16` في `generateContent`). يُرجى الاطّلاع على
     [تنسيقات إخراج الصوت](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#audio-output-formats).

## الدليل الإرشادي لكتابة الطلبات

تتعامل نماذج تحويل النص إلى كلام في Gemini 3.8 مع النص المُدخَل على أنّه **نص حرفي**.
على عكس النماذج السابقة التي كانت تتضمّن توجيهات الأداء في نص عادي،
يفصل Gemini 3.8 TTS بين التوجيهات المستمرة على مستوى الدور (`speech_metadata`)
والإشارات الصوتية المضمّنة في وقت محدّد.

### حقل النمط مقابل العلامات المضمّنة

قسِّم تعليمات الأداء حسب النطاق:

- **أسلوب الإلقاء على مستوى الجملة (`speech_metadata.style`):** يمكنك وضع سمات الإلقاء المستمر، مثل المشاعر أو العروض أو الوتيرة العامة أو أسلوب الإلقاء (مثل `"whispering"` أو `"out of breath"` أو `"muttering"` أو `"sarcastic"`)، في حقل `style` ضمن `speech_metadata`. لإنشاء شخصية وأداء ثابتَين في جميع الردود، صمِّم الشخصية مسبقًا في [تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar) واستخدِم `style` فقط لإجراء تعديلات اختيارية على مستوى الردود.
- **الأحداث في وقت محدّد (العلامات المضمّنة):** ضع علامات مضمّنة داخل النص باستخدام الأقواس الزاوية (`<cough>`، `<breath>`، `<sigh>`، `<short pause>`) للإشارة إلى الأصوات اللحظية غير الكلامية، مثل الضحك أو التنفس أو التوقفات. استخدم الأقواس الزاوية (`<...>`) للحصول على أعلى جودة صوت، والتزم بالأصوات البشرية بدلاً من المؤثرات الصوتية غير الصوتية.

| النطاق | أماكن وضع الجهاز | أمثلة |
| --- | --- | --- |
| **على مستوى الدور** (يستمر طوال الدور) | `speech_metadata.style` | `"angry tone"`، و`"speaking rapidly"`، و`"out of breath"`، و`"whispers"`، و`"sarcastic"` |
| **نقطة زمنية** (تحدث عند كلمة معيّنة) | مضمّنة في `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### السرعة والوقفات

يمكنك التحكّم في الإيقاع والصمت على ثلاثة مستويات من الدقة:

- **علامات الترقيم وعلامات الحذف:** استخدِم الفواصل والشرطات (`--`) وعلامات الحذف (`...`)
  لإظهار التردّد في المحادثة بشكل طبيعي.
- **علامات التوقّف المضمّنة:** يمكنك إدراج `<short pause>` أو `<long pause>` في نقاط محدّدة في النص حيث يجب أن يتوقّف المتحدّث مؤقتًا:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **سرعة الكلام على مستوى الدور:** يمكنك ضبط `"style": "speaking rapidly"` أو
  `"style": "speaking slowly"` في `speech_metadata` للتحكّم في سرعة الكلام
  على مستوى الدور بأكمله.

### اللحن والنبرة

استخدِم **`speech_metadata.style`** للتحكّم في العروض والنبرة والتغيير في نبرة الصوت في كل دور (على سبيل المثال، `"style": "high pitch, cheerful and excited inflection"` أو `"style": "monotone and flat"`). إذا تغيّرت المشاعر أو العروض في منتصف الحوار، قسِّم النص إلى أدوار منفصلة مع قيم `style` مختلفة لكل دور.

### تسليط الضوء

استخدِم الأحرف الكبيرة في كلمات معيّنة في النص، بالإضافة إلى علامات الترقيم والعلامات الصوتية
المضمّنة، للتركيز على الكلمات الرئيسية بشكل طبيعي:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### الأصوات غير اللفظية وغير الكلامية

يجب وضع الأصوات البشرية غير الكلامية في السطر باستخدام الأقواس الزاوية (`<...>`) في
النقطة المحددة التي يجب أن يحدث فيها الصوت. تشمل العلامات الصوتية المقترَحة ما يلي:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### الردود القصيرة وتداخل الكلام

في الحوارات التي تضم عدة متحدثين، يمكنك تضمين تفاعلات المستمعين بين علامات الخط العمودي (`|reaction|`) ضمن دور المتحدث لإنشاء قنوات خلفية طبيعية أو تداخل في الكلام بدون الحاجة إلى إنشاء دور منفصل لكل تفاعل.

- **التبادلات القصيرة في القنوات الخلفية:** يمكنك إضافة ردود فعل المستمعين القصيرة (`|oh hmm|`،
  `|oh really?|`، `|absolutely|`) داخل دور المتحدث النشط:
  - **الدور 1 (المتحدّث أ):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **الدور 2 (المتحدّث ب):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **الدور 3 (المتحدّث أ):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **الكلام المتداخل والمتشابك:** يمكنك استخدام عدة مقاطع شرطة رأسية لمحاكاة الكلام المتزامن أو المتشابك بين متحدثَين (يعمل بشكل أفضل مع `gemini-3.8-flash-tts`):
  - **العد التنازلي/الكورس المتزامن:** `"Let's surprise him on three |ok| ready?"` متبوعًا بـ `"one. two. three. |happy| happy |birthday| birthday!"`
  - **تداخل كامل بين المتحدّثين:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### الاتساق في جميع الأجيال وما يجب تجنبه

اتّبِع الإرشادات التالية للحفاظ على ثبات الهوية الصوتية في جميع الردود:

- **تصميم الشخصيات مسبقًا في تصميم الصوت بدلاً من استخدام مجموعات الأنماط الطويلة:**
  إنّ الفقرات الطويلة في `"Audio Profile"` والنقاط المتعددة في `"Director's Notes"`
  المنقولة من النماذج السابقة هي السبب الأكثر شيوعًا لانحراف الصوت.
  يمكنك استخدام حدسك الإبداعي نفسه في [تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar) لإنشاء شخصية مخصّصة في "`voice_...`"، ثم استخدام معرّف الصوت هذا في طلبات تحويل النص إلى كلام.
- **الاعتماد على المرجع الصوتي لضمان الثبات (تجاهُل التعليمات الوصفية):**
  يتم تدريب نماذج تحويل النص إلى كلام في Gemini 3.8 على التركيز على المرجع الصوتي أولاً.
  لا تُدرِج تعليمات تطلب من النموذج الحفاظ على ثبات الصوت (مثل `"do not switch speaker identity"` أو `"maintain identical timbre"`)، لأنّ النص الإضافي في الطلب يزيد من الانحراف. تجنَّب تعليمات الأسلوب غير الضرورية واسمح للنموذج بالتغيير بشكل طبيعي حول النقطة الثابتة التي يوفّرها المرجع الصوتي.
- **لا تحاول تغيير سمات المتحدّث الثابتة في `style`:** تجنَّب إدراج
  العمر أو الجنس أو الأسماء أو التغييرات الدائمة في اللهجة في `speech_metadata.style`.
  بدلاً من ذلك، اختَر صوتًا إقليميًا من "مكتبة الأصوات الموسّعة" أو أنشِئ صوتًا
  باستخدام [تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar).

### سير العمل المقترَح

1. **إنشاء الشخصية مرة واحدة:** يمكنك إنشاء شخصيتك في
   [تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar) أو اختيار صوت إقليمي من
   "مكتبة الأصوات الموسّعة" يتطابق مع لغتك المستهدفة وشخصيتك.
2. **كتابة نصوص محادثات طبيعية تتضمّن عيوبًا في الكلام:** للحصول على أقصى قدر من الطبيعية، اكتب `text` كنص محادثة حقيقي، بما في ذلك عيوب الكلام الطبيعية والتردد في المحادثات (على سبيل المثال، `"Oh uh yeah I think... hm, so that's interesting"`).
3. **اختبار ميزة "تحويل النص إلى كلام" العادية أولاً:** يمكنك تركيب النص باستخدام حقل `style` فارغ أولاً، فمعظم الطلبات لا تحتاج إلى تعليمات `style` على الإطلاق.
4. **إضافة طلبات `style` قصيرة للتعديلات فقط:** أضِف سلسلة `style` موجزة
   (مثل `"casual, friendly"` أو `"muttering, then reassuring"`) فقط
   للجولات التي تتطلّب تعديلاً معيّنًا في طريقة الإلقاء، وأعِد استخدام هذه السلسلة القصيرة
   نفسها في الجولات التي تريد فيها الحصول على أداء أساسي متّسق.

### الحوارات المتعددة الجولات والوكلاء الصوتيون

عند إنشاء وكلاء صوتيين حواريين في الوقت الفعلي أو تطبيقات متعددة الأدوار:

- أجرِ **مكالمة واحدة لتحويل النص إلى كلام في كل دور** عند وصول أجزاء نص النموذج اللغوي الكبير.
- يجب السماح لـ `voice` الذي تم ضبطه (مُعدّ مسبقًا أو مصمّم `voice_...` أو مكرّر
  `voice_...` / `voicekey_...`) بحمل هوية المتحدّث عبر الأدوار، وعدم
  إعادة إرسال شخصية طويلة في كل دور.
- اترك حقل `style` لكل دور فارغًا، أو أرسِل سلسلة ثابتة قصيرة واحدة
  (مثل `"casual, friendly"`) للمحادثة بأكملها.
- قسِّم ردود الوكيل الطويلة إلى جولات أقصر بدلاً من استخدام طلبات أسلوب أقوى.

## القيود

- تقبل نماذج تحويل النص إلى كلام الإدخالات النصية فقط وتنشئ مخرجات صوتية فقط.
- تتيح ميزة إنشاء أصوات متعددة في طلب واحد (`speech_config.speakers`) استخدام ما يصل إلى صوتَين من الأصوات المُعدّة مسبقًا. لدمج الأصوات المصمّمة بشكل مخصّص
  (`voice_...`) أو الأصوات المكرّرة (`voice_...` / `voicekey_...`) في
  حوار متعدّد الشخصيات، يجب تركيب صوت كل متحدث على حدة.
  بما أنّ الطلبات الأحادية تعرض `audio/wav` مع عنوان RIFF بحجم 44 بايت تلقائيًا، اطلب PCM الأولي (`{"type": "audio", "mime_type": "audio/l16"}`) أو أزِل عنوان WAV من كل دور قبل دمج إطارات الصوت PCM بتردد 24 كيلوهرتز.
- **الحدود القصوى لمساحة تخزين الصوت المخصّص ومدة صلاحيته:**
  - **الأصوات التي تحتفظ بالبيانات (`store=True`، سواء كانت مستندة إلى طلب أو مكرّرة):** الحد الأقصى هو
    **200 صوت لكل مشروع** مع **مدة بقاء (TTL) تبلغ سنة واحدة**.
  - **مفاتيح الصوت عديمة الحالة (`store=False` و`voicekey_...`):** **مدة البقاء (TTL) هي 7 أيام**
- يُرجى مراجعة قسم [اللغات المتاحة](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#languages) لمعرفة اللغات التي تغطيها الميزة.

## الخطوات التالية

- يمكنك إنشاء شخصيات صوتية مخصّصة من اللغة الطبيعية باستخدام ميزة
  [تصميم الصوت](https://ai.google.dev/gemini-api/docs/voice-design?hl=ar).
- تقليد صوت متحدث حالي في
  [تقليد الصوت](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ar)
- يمكنك مقارنة مواصفات النموذج في صفحتَي
  [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ar) و[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ar).
- استكشِف الصوت التفاعلي الثنائي الاتجاه باستخدام
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
