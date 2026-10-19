---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa
fetched_at: 2026-10-19T05:34:34.440150+00:00
title: "\u062a\u0648\u0644\u06cc\u062f \u0646\u0648\u0634\u062a\u0627\u0631 \u0628\u0647 \u06af\u0641\u062a\u0627\u0631 (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# تولید نوشتار به گفتار (TTS)

«میانای برنامه‌سازی کاربردی Gemini» می‌تواند ورودی نوشتاری را بااستفاده از قابلیت‌های تولید نوشتار به گفتار (TTS) Gemini به صدای تک‌گوینده یا چندگوینده تبدیل کند.
تولید نوشتار به گفتار
*[قابل‌کنترل](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#controllable)* است، یعنی می‌توانید
فراداده‌های ساختاریافته نوبت (`speech_metadata`) و برچسب‌های صوتی درون‌خطی را ترکیب کنید
تا *سبک*، *لهجه*، *سرعت*، و *لحن* صدا را هدایت کنید.

قابلیت «تبدیل نوشتار به گفتار» با تولید گفتار ارائه‌شده ازطریق
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=fa) متفاوت است، که برای ورودی‌ها و خروجی‌های چندحالته،
تعاملی، و بدون ساختار طراحی شده است. درحالی‌که Live API در بافت‌های مکالمه‌ای پویا برتری دارد،
«تبدیل نوشتار به گفتار» ازطریق Gemini API برای سناریوهایی طراحی شده است که نیاز به خواندن دقیق نوشتار با کنترل دقیق بر سبک و صدا دارند، مانند تولید پادکست یا کتاب صوتی.

این راهنما به شما نشان می‌دهد که چگونه بااستفاده از [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fa)
(`gemini-3.8-flash-tts`) و
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fa)
(`gemini-3.8-flash-lite-tts`) از نوشتار، صدای تک‌گوینده و چندگوینده تولید کنید.

## قبل‌از شروع

مطمئن شوید که از مدل Gemini TTS فهرست‌شده در بخش
[مدل‌های پشتیبانی‌شده](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#supported-models) استفاده می‌کنید،
و به جدیدترین Google GenAI SDK (`google-genai >= 2.25.0` برای Python
یا `@google/genai >= 2.24.0` برای JavaScript/TypeScript) ارتقا دهید یا از REST API استفاده کنید.
برای نتایج بهینه،
[زمان استفاده از هر مدل](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#when-to-use-which-model)
را مرور کنید تا بهترین مدل را برای حجم کاری خود انتخاب کنید.

شاید برایتان مفید باشد که
[مدل‌های Gemini TTS را در AI Studio آزمایش کنید](https://aistudio.google.com/generate-speech?hl=fa)
قبل‌از اینکه ساختن را شروع کنید.

## نوشتار به گفتار تک‌گوینده

برای تبدیل نوشتار به صدای تک‌گوینده با مدل‌های Gemini 3.8 TTS،
ترانویسی کلمه‌به‌کلمه را در `input` ارسال کنید، سبک سطح نوبت را بااستفاده از
حاشیه‌نویسی `speech_metadata` پیوست کنید، و صدایتان را در
`generation_config.speech_config` پیکربندی کنید. می‌توانید صدایی را از
[گزینه‌های صدا](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#voices) پیش‌ساخته، «کتابخانه صدای گسترده» (`GET /v1beta/voices`)، شناسه
[طراحی صدای](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa) سفارشی (`voice_...`)، یا شناسه
[تکثیر صدا](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fa) (`voice_...`، یا
`voicekey_...` اختیاری بدون حالت) انتخاب کنید.

این مثال صدای خروجی WAV پیش‌فرض (`audio/wav`) را از مدل مستقیماً در فایلی ذخیره می‌کند:

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

### استراحت

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

در کیت‌های توسعه نرم‌افزار Python و JavaScript، می‌توانید داده‌های صوتی تولیدشده را بااستفاده از
دارایی راحتی `interaction.output_audio` بازیابی کنید، که آخرین بلوک صوتی تولیدشده را برمی‌گرداند (در پاسخ‌های خام REST JSON، صدای کدبندی‌شده با base64 در `steps[].content[].data` ذخیره می‌شود). برای جزئیات بیشتر درباره دارایی‌های راحتی،
[نمای کلی تعاملات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fa#convenience-properties) را ببینید.

## نوشتار به گفتار چندبلندگویی

برای دیالوگ چند بلندگو، دو بلندگو را در `speech_config.speakers`
پیکربندی کنید و هر نوبت را به‌عنوان یک عنصر نوشتاری جداگانه با یک حاشیه `speech_metadata`
که `speaker` و `style` اختیاری در سطح نوبت را مشخص می‌کند بگذرانید. توجه داشته باشید که
`speech_config` برای تولید تک‌بلندگو یک آرایه (`[{"voice": "..."}]`)
و برای تولید چندبلندگو یک شیء (`{"speakers": [...]}`) می‌پذیرد:

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

### استراحت

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
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## کنترل سبک گفتار با فراداده و برچسب‌ها

‫Gemini 3.8 TTS فیلد `text` را دقیقاً به‌عنوان ترانویسی کلمه‌به‌کلمه درنظر می‌گیرد. برای
کنترل کردن ارائه بدون اینکه دستورالعمل‌های صحنه بلند خوانده شود، دستورالعمل‌هایتان را
براساس دامنه تقسیم کنید:

- **ارائه پایدار در سطح نوبت (`speech_metadata.style`):** احساسات،
  سبک ارائه، عروض، سرعت، و میزان صدایی را که در کل نوبت اعمال می‌شود
  در فیلد `style` قرار دهید (برای مثال، `"style": "whispered urgently"`،
  `"style": "out of breath"`، یا `"style": "warm and enthusiastic"`).
- **رویدادهای نقطه‌ای (برچسب‌های درون‌خطی):** وقفه‌ها یا فوران‌های صوتی غیرگفتاری لحظه‌ای را بااستفاده از پرانتزهای زاویه‌دار (مثلاً `"Wait... <short pause> did you hear that? <sigh>"` یا `"Excuse me <cough> as I was saying..."`) مستقیماً در ترانویسی قرار دهید.

برای آشنایی با روال‌های مطلوب جامع، [راهنمای پیام‌واره‌نویسی](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#prompting-guide) را ببینید.

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

### استراحت

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

## تولید گفتار جاری‌سازی

می‌توانید صدای تولیدشده را همان‌طور که درحال ترکیب شدن است با تنظیم
`stream: true` جاری‌سازی کنید. برخلاف درخواست‌های تک‌مقداری (که فایل WAV کامل با سرصفحه RIFF برمی‌گردانند)، **درخواست‌های جاری‌سازی به‌طور پیش‌فرض تکه‌های PCM خطی لیتل اندین علامت‌دار ۱۶ بیتی خام بدون سرصفحه (`audio/l16`،‏ ۲۴ کیلوهرتز، مونو) برمی‌گردانند** تا تکه‌های صوتی بتوانند به‌طور پیوسته بدون سرصفحه محفظه پخش یا به‌هم متصل شوند.

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

### استراحت

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

## قالب‌های خروجی صوتی

مدل‌های Gemini 3.8 TTS از قالب‌های صوتی پیش‌فرض متفاوتی استفاده می‌کنند، بسته به اینکه
درخواست تک‌موردی یا جاری‌سازی باشد:

- **درخواست‌های یک‌تایی (`stream=False`):** صدای کامل **WAV (`audio/wav`)**
  را با سرصفحه استاندارد RIFF (۲۴ کیلوهرتز، تک‌کاناله، ۱۶ بیت علامت‌دار کوچک‌سر
  PCM) برمی‌گرداند. می‌توانید بایت‌های صوتی رمزگشایی‌شده را مستقیماً در فایل `.wav` ذخیره کنید بدون اینکه
  سرصفحه WAV را به‌صورت دستی به آن اضافه کنید.
- **درخواست‌های جاری‌سازی (`stream=True`):** به‌طور پیش‌فرض، بخش‌های **PCM خطی خام بدون سرصفحه (`audio/l16`)** (۲۴ کیلوهرتز، مونو، PCM با ترتیب بایت کوچک علامت‌دار ۱۶ بیتی) را برمی‌گرداند تا بخش‌ها بتوانند به‌طور مداوم بدون سرصفحه محفظه در هر بخش جاری‌سازی یا به‌هم متصل شوند.

برای درخواست کدبندی صوتی یا نرخ نمونه متفاوت، `mime_type` و
اختیاری `sample_rate` را در `response_format` پیکربندی کنید:

| قالب | به‌ارزش `mime_type` | شرح |
| --- | --- | --- |
| **WAV** *(unary default)* | `"audio/wav"` | فایل WAV فشرده‌نشده با سرایند RIFF (‫PCM با ترتیب بایت کوچک ۱۶ بیتی علامت‌دار، تک‌کاناله، پیش‌فرض ۲۴ کیلوهرتز). پیش‌فرض برای درخواست‌های یک‌تایی. |
| **Raw PCM (L16)** *(پیش‌فرض جاری‌سازی)* | `"audio/l16"` | صدای PCM خطی 16 بیتی بدون سرصفحه و فشرده‌نشده (24 کیلوهرتز، مونو). پیش‌فرض برای درخواست‌های جاری‌سازی. |
| **Mu-law** | `"audio/mulaw"` | صدای کدبندی‌شده ۸ بیتی G.711 mu-law (معمولاً در سیستم‌های تلفنی/IVR در آمریکای شمالی و ژاپن استفاده می‌شود). |
| **A-law** | `"audio/alaw"` | صدای کدگذاری‌شده ۸ بیتی G.711 A-law (که معمولاً در سیستم‌های تلفنی اروپایی و بین‌المللی استفاده می‌شود). |

همچنین می‌توانید `sample_rate` را به هرتز مشخص کنید (برای مثال، `24000`، `16000`، یا
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

### استراحت

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

## گزینه‌های گفتاری

‫Gemini 3.8 TTS از چهار روش برای انتخاب یا ایجاد صدا پشتیبانی می‌کند:

1. **صداهای استودیویی ازپیش ساخته‌شده:** ۳۰ صدای گلچین‌شده که در جدول زیر فهرست شده‌اند.
2. **کتابخانه صوتی گسترده:** صدها صدای اضافی در زبان‌ها،
   لهجه‌ها، و کهن‌الگوهای شخصیتی مختلف که بااستفاده از `client.voices.list()`
   (`GET /v1beta/voices`) دردسترس است.
3. **[طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa):** تولید یک شخصیت صوتی سفارشی از شرح زبان طبیعی در [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fa) یا بااستفاده از `POST /v1beta/voices` (`type="prompted"`، که یک شناسه `voice_...` پایدار و یک پیش‌نمایش WAV `sample_audio` در `CreateVoice` و `GetVoice` برمی‌گرداند).
4. **[همانندسازی صدا](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fa):** صدای گوینده را از صدای مرجع و رضایت در [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fa) یا بااستفاده از `POST /v1beta/voices` (`type="replicated"`، `store=True` پایدار به‌طور پیش‌فرض یا `store=False` بدون حالت اختیاری) همانندسازی کنید.

### محدودیت‌های صدای سفارشی و TTL

| تایپ گفتاری | حالت فضای ذخیره‌سازی | سهمیه / محدودیت | نگهداری (TTL) |
| --- | --- | --- | --- |
| **صداهای حالت‌دار** (`voice_...`، درخواست‌شده یا تکثیرشده) | `store=True` | **‫۲۰۰ صدا برای هر پروژه** (بین صداهای پیام‌واره‌ای و صداهای بازآفرینی‌شده هم‌رسانی می‌شود) | **۱ سال از آخرین استفاده\*** |
| **کلیدهای صوتی بی‌وضعیت** (`voicekey_...`، تکرارشده) | `store=False` | تحت‌مدیریت کارخواه | **‫۷ روز** |

\* **تمدید TTL:** هر بار که از صدا به‌طور فعال استفاده می‌شود (چه با ترکیب گفتار با صدا یا استفاده از آن به‌عنوان صدای پایه برای بازآمیزی)، پنجره نگهداری ۱ ساله بازنشانی می‌شود. صداهایی که به‌مدت ۱ سال فعالیتی نداشته باشند به‌طور خودکار حذف می‌شوند.

### صداهای پیش‌ساخته

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *روشن* | **Puck** -- *شاد* | **Charon** -- *اطلاعاتی* |
| **Kore** -- *Firm* | **Fenrir** -- *Excitable* | **Leda** -- *جوان* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *آسان‌گیر* |
| **Autonoe** -- *روشن* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear (صاف)* |
| **Umbriel** -- *آسان‌گیر* | **Algieba** -- *ملایم* | **Despina** -- *نرم* |
| **Erinome** -- *Clear* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *آموزنده* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *ملایم* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Mature* | **Pulcherrima** -- *جلو بردن* |
| **Achird** -- *دوستانه* | **Zubenelgenubi** -- *Casual* | **Vindemiatrix** -- *Gentle* |
| **سعدالخبایا** -- *سرزنده* | **Sadaltager** -- *آگاه* | **Sulafat** -- *گرم* |

### «کتابخانه صدای گسترده» و فیلتر کردن

علاوه‌بر ۳۰ صدای استودیویی ویژه در جدول بالا، **کتابخانه گسترده صدا** صدها صدای دیگر را در زبان‌ها، لهجه‌های منطقه‌ای، شخصیت‌های کاراکتر، و دامنه‌های مختلف ارائه می‌دهد. می‌توانید به‌صورت تعاملی در [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fa) کل «کتابخانه صدا» را مرور، فیلتر، و امتحان کنید یا بااستفاده از `client.voices.list()` (`GET /v1beta/voices`، بااستفاده از `google-genai` نسخه ۲.۲۵.۰ به بالا / `@google/genai` نسخه ۲.۲۴.۰ به بالا) آن را به‌صورت برنامه‌نویسی‌شده پُرسمان کنید.

`ListVoices` صداهای ذخیره‌شده سفارشی شما را (به‌ترتیب از جدیدترین) و سپس صداهای کاتالوگ ازپیش‌ساخته‌شده‌ای را که با معیارهای فیلتر شما مطابقت دارند برمی‌گرداند. وقتی چند مقدار
برای فیلتر فهرست ارسال می‌شود، صداهای منطبق با **هر** مقداری در آن فیلتر
برگردانده می‌شود (`OR`)، درحالی‌که پارامترهای فیلتر متمایز با `AND` ترکیب می‌شوند:

| پارامتر | نوع | شرح |
| --- | --- | --- |
| `language_code` | `list[str]` | برچسب(های) زبان BCP-47 (برای مثال، `["en-US", "en-GB"]`). مطابقت دقیق غیرحساس به حروف بزرگ و کوچک. |
| `region_code` | `list[str]` | کد(های) منطقه ISO 3166-1 alpha-2 یا UN M.49 (برای مثال، `["US", "GB"]`). |
| `accent` | `list[str]` | توصیف‌گر(های) لهجه منطقه‌ای (برای مثال، `["American", "British"]`). |
| `gender` | `list[str]` | ارائه جنسیت درک‌شده (`"female"`، `"male"`، یا `"neutral"`). |
| `pitch` | `list[str]` | طبقه‌بندی زیروبم صدا (`"low"`، `"medium"`، یا `"high"`). |
| `persona` | `list[str]` | شخصیت صوتی یا کهن‌الگوی شخصیت (برای مثال، `["Warm, Friendly"]`، `["Narrator"]`). |
| ‫`contexts` (`context` در REST) | `list[str]` | دامنه استفاده بهینه (برای مثال، `["Audiobook", "Conversational", "News"]`). |
| ‫`type` (`type_` در Python) | `list[str]` | فیلتر کردن براساس منبع صدا: `"prebuilt"`، `"prompted"` ([طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa))، یا `"replicated"` ([همانندسازی صدا](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fa)). |
| `search` | `str` | جستجوی رشته فرعی نوشتار آزاد بدون حساسیت به حروف بزرگ و کوچک با `display_name` و `description` مطابقت دارد. |
| `page_size` | `int` | حداکثر تعداد صداهای برگشتی در هر صفحه (پیش‌فرض `50`، حداکثر `1000`). |
| `page_token` | `str` | نشان از `response.next_page_token` برای واکشی صفحه بعدی نتایج. |

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

### استراحت

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

## زبان‌های پشتیبانی‌شده

مدل‌های تبدیل نوشتار به گفتار زبان ورودی را به‌طور خودکار تشخیص می‌دهند.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fa)
(`gemini-3.8-flash-tts`) از **بیش‌از ۱۳۰ زبان** پشتیبانی می‌کند، و
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fa)
(`gemini-3.8-flash-lite-tts`) از **بیش‌از ۱۰۰ زبان** پشتیبانی می‌کند:

| زبان | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| آچه‌ای (خط عربی) | ✔️ | ✔️ |
| آفریکانس | ✔️ | ✔️ |
| آکان | ✔️ | ✔️ |
| آمهاریک | ✔️ | ✔️ |
| ارمنی | ✔️ | ✔️ |
| آسامی | ✔️ | ✔️ |
| اودهی | ✔️ | ✔️ |
| بالیایی | ✔️ | ✔️ |
| بنگالی | ✔️ | ✔️ |
| بنجری (الفبای عربی) | ✔️ | — |
| بَنجَری (خط لاتین) | ✔️ | ✔️ |
| باشقیری | ✔️ | — |
| باسک | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| بمبا | ✔️ | — |
| بوجپوری | ✔️ | ✔️ |
| بوسنیایی | ✔️ | ✔️ |
| بوگیایی | ✔️ | ✔️ |
| بلغاری | ✔️ | ✔️ |
| برمه‌ای | ✔️ | — |
| کانتونی | ✔️ | ✔️ |
| کاتالان | ✔️ | ✔️ |
| سبوانو | ✔️ | ✔️ |
| کردی میانی | ✔️ | ✔️ |
| چتیسگری | ✔️ | ✔️ |
| چینی (نویسه هان ساده‌شده) | ✔️ | ✔️ |
| چینی (خط هانت) | ✔️ | ✔️ |
| تاتاری کریمه | ✔️ | — |
| کرواتی | ✔️ | ✔️ |
| چک | ✔️ | ✔️ |
| دانمارکی | ✔️ | ✔️ |
| هلندی | ✔️ | ✔️ |
| دیولا | ✔️ | — |
| دزونگخا | ✔️ | — |
| عربی مصری | ✔️ | ✔️ |
| انگلیسی | ✔️ | ✔️ |
| استونیایی | ✔️ | ✔️ |
| فیلیپینی | ✔️ | ✔️ |
| فنلاندی | ✔️ | — |
| فرانسوی | ✔️ | ✔️ |
| گالیسی | ✔️ | ✔️ |
| گاندا | ✔️ | ✔️ |
| گرجستانی | ✔️ | ✔️ |
| آلمانی | ✔️ | ✔️ |
| یونانی | ✔️ | ✔️ |
| گورانی | ✔️ | — |
| گجراتی | ✔️ | ✔️ |
| کریول هائیتی | ✔️ | ✔️ |
| مغولی خالخا | ✔️ | ✔️ |
| هوسایی | ✔️ | ✔️ |
| عبری | ✔️ | ✔️ |
| هندی | ✔️ | ✔️ |
| مجارستانی | ✔️ | ✔️ |
| ایسلندی | ✔️ | ✔️ |
| ایگبو | ✔️ | — |
| ایلوکو | ✔️ | ✔️ |
| اندونزیایی | ✔️ | ✔️ |
| فارسی ایرانی | ✔️ | ✔️ |
| ایتالیایی | ✔️ | ✔️ |
| ژاپنی | ✔️ | ✔️ |
| جاوه‌ای | ✔️ | ✔️ |
| کابیل | ✔️ | — |
| کامبا | ✔️ | ✔️ |
| کنادا | ✔️ | ✔️ |
| کشمیری (خط عربی) | ✔️ | ✔️ |
| کشمیری (خط دیواناگری) | ✔️ | ✔️ |
| قزاقی | ✔️ | ✔️ |
| خمر | ✔️ | ✔️ |
| کیکویو | ✔️ | ✔️ |
| کینیارواندایی | ✔️ | ✔️ |
| کنگو | ✔️ | ✔️ |
| کره‌ای | ✔️ | ✔️ |
| قرقیزی | ✔️ | ✔️ |
| لائوسی | ✔️ | ✔️ |
| لاتگالی | ✔️ | — |
| لینگالا | ✔️ | ✔️ |
| لیتوانیایی | ✔️ | — |
| لوگزامبورگی | ✔️ | — |
| مقدونی | ✔️ | ✔️ |
| ماگهی | ✔️ | ✔️ |
| مایتهیلی | ✔️ | ✔️ |
| مالایالام | ✔️ | ✔️ |
| مالتی | ✔️ | ✔️ |
| مانیپوری | ✔️ | ✔️ |
| ماراتی | ✔️ | ✔️ |
| مینانگ‌کابو (الفبای عربی) | ✔️ | ✔️ |
| مینانگ‌کابائو (الفبای لاتین) | ✔️ | — |
| میزو | ✔️ | ✔️ |
| نپالی (زبان فردی) | ✔️ | ✔️ |
| فولانی نیجریه | ✔️ | ✔️ |
| آذربایجانی شمالی | ✔️ | ✔️ |
| سوتوی شمالی | ✔️ | ✔️ |
| ازبکی شمالی | ✔️ | ✔️ |
| بوکسمال نروژی | ✔️ | ✔️ |
| نروژی (نینورسک) | ✔️ | ✔️ |
| نیانجا | ✔️ | ✔️ |
| اوسیتان | ✔️ | — |
| اودیا (زبان فردی) | ✔️ | ✔️ |
| پانگاسینانی | ✔️ | — |
| فارسی (افغانستان) | ✔️ | ✔️ |
| لهستانی | ✔️ | ✔️ |
| پرتغالی | ✔️ | ✔️ |
| پنجابی | ✔️ | ✔️ |
| رومانیایی | ✔️ | ✔️ |
| روسی | ✔️ | ✔️ |
| سنتالی | ✔️ | ✔️ |
| صربی | ✔️ | ✔️ |
| سیندهی | ✔️ | — |
| سینهالی | ✔️ | ✔️ |
| اسلوواک | ✔️ | ✔️ |
| Slovenian | ✔️ | — |
| سومالی | ✔️ | — |
| آذربایجانی جنوبی | ✔️ | ✔️ |
| پشتوی جنوبی | ✔️ | ✔️ |
| سوتویی جنوبی | ✔️ | — |
| اسپانیایی | ✔️ | ✔️ |
| عربی معیار (الفبای عربی) | ✔️ | ✔️ |
| عربی معیار (الفبای لاتین) | ✔️ | ✔️ |
| لتونیایی استاندارد | ✔️ | ✔️ |
| مالایی استاندارد | ✔️ | ✔️ |
| سواحیلی (زبان فردی) | ✔️ | — |
| سواتی | ✔️ | — |
| سوئدی | ✔️ | — |
| تاجیکی | ✔️ | — |
| تامیل | ✔️ | ✔️ |
| تلوگو | ✔️ | ✔️ |
| تایلندی | ✔️ | — |
| تیگرینیا | ✔️ | — |
| توسک آلبانیایی | ✔️ | — |
| ترکی | ✔️ | ✔️ |
| اویغوری | ✔️ | — |
| ویتنامی | ✔️ | ✔️ |

## مدل‌های پشتیبانی‌شده

| مدل | تک گوینده | چندبلندگویی | طراحی صدا | همانندسازی صدا |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fa) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fa) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=fa) | ✔️ | ✔️ | — | — |
| [پیش‌نمایش Gemini 2.5 Pro TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=fa) | ✔️ | ✔️ | — | — |

### چه زمانی از کدام مدل استفاده کنیم

هر دو مدل Gemini 3.8 TTS از طرح‌واره ای‌پی‌آی و قالب پیام‌واره کاملاً یکسانی استفاده می‌کنند،
که به شما امکان می‌دهد با تغییر یک پارامتر بین آن‌ها جابه‌جا شوید:

- **از [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fa)
  (`gemini-3.8-flash-tts`)** زمانی استفاده کنید که حداکثر وفاداری صوتی، بازیگری ظریف،
  و کنترل بیانی در اولویت باشد. این مدل برای کارهای خلاقانه در سطح استودیو، مکالمه‌های پیچیده با چند گوینده، برچسب‌های سنگین فوران صوتی، تلفظ‌های دشوار، گویش‌های منطقه‌ای یا اقلیت، و روایت‌های طولانی که به صدای بسیار پایدار و ثبات صدای محیط نیاز دارند ایده‌آل است.
- **از [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fa)
  (`gemini-3.8-flash-lite-tts`)** به‌عنوان جایگزین سریع و مقرون‌به‌صرفه برای `gemini-3.1-flash-tts-preview` استفاده کنید. این مدل برای
  تولید انبوه با حجم بالا، آبشارهای عامل صوتی مکالمه‌ای، ویژگی‌های
  بلندخوانی، تکثیر صدای قابل‌اعتماد، و گفتار تک‌بلندگوی روزمره
  در زبان‌های اصلی بهینه‌سازی شده است.

### راهنمای انتقال

اگر از `gemini-3.1-flash-tts-preview` یا مدل‌های قدیمی‌تر Gemini TTS به Gemini 3.8 TTS مهاجرت می‌کنید:

1. **انتقال دستورالعمل‌های سطح گردش به `speech_metadata`:** «نوشتار به گفتار Gemini 3.8» با
   نوشتار ورودی دقیقاً مثل یک آوانویسی کلمه‌به‌کلمه رفتار می‌کند. دستورالعمل‌های تحویل پایدار (`style`—مانند `"whispering"`، `"out of breath"`، یا `"speaking slowly"`) و برچسب‌های گوینده (`speaker`) را به‌جای جاسازی دستورالعمل‌های صحنه در متن ترانویسی، به حاشیه‌نویسی‌های ساختاریافته `speech_metadata` منتقل کنید.
2. **از برچسب‌های درون‌خطی براکت زاویه‌دار فقط برای رویدادهای صوتی نقطه‌ای استفاده کنید:**
   آواسازی‌های غیرگفتاری و مکث‌های لحظه‌ای را بااستفاده از براکت‌های زاویه‌دار (مانند `<laugh>`، `<sigh>`، `<cough>`، `<breath>`، یا `<short pause>`) به‌صورت درون‌خطی در ترانویسی نگه دارید. از برچسب‌های جلوه صوتی (مانند تشویق یا صدای ضربه) اجتناب کنید و سبک‌های ارائه را در `speech_metadata.style` قرار دهید.
3. **در هر نوبت در درخواست‌های چند بلندگو، `speaker` را مشخص کنید:** هر نوبت در
   درخواست چند بلندگو باید به‌طور صریح شامل `speaker` در
   `speech_metadata` باشد که با یکی از بلندگوهای پیکربندی‌شده مطابقت داشته باشد.
4. **طراحی شخصیت‌ها از ابتدا با «طراحی صدا»:** بلوک‌های چندپاراگرافی
   `"Audio Profile"` یا `"Director's Notes"` را با صدای سفارشی ایجادشده
   در [طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa) جایگزین کنید، سپس آن شناسه `voice_...`
   را ازطریق درخواست‌های «نوشتار به گفتار» با حداقل رشته‌های `style` یا رشته‌های خالی منتقل کنید.
5. **حساب برای برونداد پیش‌فرض WAV (`audio/wav`) در درخواست‌های یک‌تایی:** برخلاف
   `gemini-3.1-flash-tts-preview` و مدل‌های قدیمی‌تر «نوشتار به گفتار» (که به‌طور پیش‌فرض
   PCM خام بدون سرایند `audio/l16` برمی‌گرداندند)، «نوشتار به گفتار Gemini 3.8» به‌طور پیش‌فرض برای درخواست‌های یک‌تایی صدای WAV
   (`audio/wav`) با سرایند استاندارد RIFF برمی‌گرداند.
   - اگر کد شما قبلاً بایت‌های PCM خام را در سرصفحه WAV می‌پیچید (برای مثال، بااستفاده از واحد `wave` یا `ffmpeg` در Python)، بسته‌بندی سرصفحه دستی را بردارید و بایت‌های برگشتی را مستقیماً در فایل `.wav` بنویسید.
   - اگر خط لوله شما به صدای PCM خام بدون سرصفحه، mu-law، یا A-law نیاز دارد،
     `response_format.mime_type` را صریحاً روی `"audio/l16"`، `"audio/mulaw"`، یا
     `"audio/alaw"` تنظیم کنید (برای مثال، `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}`
     در Interactions API، یا `AUDIO_L16` در `generateContent`). به
     [قالب‌های خروجی صوتی](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#audio-output-formats) مراجعه کنید.

## راهنمای پیام‌واره‌ها

مدل‌های TTS‏ Gemini 3.8 با نوشتار ورودی دقیقاً به‌عنوان **ترانویسی کلمه‌به‌کلمه** رفتار می‌کنند.
برخلاف مدل‌های پیش‌نمایش قبلی که دستورات صحنه در نوشتار ساده جاسازی می‌شدند،
‫Gemini 3.8 TTS دستورات سطح نوبت پایدار (`speech_metadata`) را
از برچسب‌های صوتی درون‌خطی نقطه‌ای جدا می‌کند.

### فیلد سبک درمقابل برچسب‌های به‌خط

دستورالعمل‌های عملکرد را براساس دامنه تقسیم کنید:

- **ارائه در سطح نوبت (`speech_metadata.style`):** مشخصه‌های ارائه پایدار (مانند احساس، عروض، سرعت کلی، یا سبک ارائه (مانند `"whispering"`، `"out of breath"`، `"muttering"`، یا `"sarcastic"`)) را در فیلد `style` از `speech_metadata` قرار دهید. برای ایجاد شخصیت و عملکردی پایدار درطول نوبت‌ها، ابتدا شخصیت را در [طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa) طراحی کنید و از `style` فقط برای تغییرات جزئی اختیاری در سطح نوبت استفاده کنید.
- **رویدادهای نقطه‌ای (برچسب‌های درون‌خطی):** صداهای غیرگفتاری لحظه‌ای، نفس کشیدن، یا مکث‌ها را بااستفاده از پرانتزهای زاویه‌دار (`<cough>`، `<breath>`، `<sigh>`، `<short pause>`) به‌صورت درون‌خطی در ترانویسی قرار دهید. برای بالاترین کیفیت صدا، از پرانتزهای زاویه‌دار (`<...>`) استفاده کنید و به‌جای جلوه‌های صوتی غیرکلامی، از صداهای کلامی انسانی استفاده کنید.

| حوزه | کجا قرار دهید | مثال‌ها |
| --- | --- | --- |
| **سطح نوبت** (درطول نوبت حفظ می‌شود) | `speech_metadata.style` | ‫`"angry tone"`،‏ `"speaking rapidly"`،‏ `"out of breath"`،‏ `"whispers"`،‏ `"sarcastic"` |
| **نقطه زمانی** (در کلمه خاصی رخ می‌دهد) | درون‌خطی در `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### سرعت و مکث‌ها

می‌توانید ریتم و سکوت را در سه سطح جزئیات کنترل کنید:

- **نشانه‌های سجاوندی و سه‌نقطه:** از ویرگول، خط تیره (`--`)، و سه‌نقطه (`...`)
  برای مکث‌های طبیعی در مکالمه استفاده کنید.
- **برچسب‌های مکث درون‌خطی:** `<short pause>` یا `<long pause>` را دقیقاً در جاهایی از متن که گوینده باید مکث کند درج کنید:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **سرعت در سطح نوبت:** `"style": "speaking rapidly"` یا
  `"style": "speaking slowly"` را در `speech_metadata` تنظیم کنید تا
  نرخ صحبت کردن را در کل نوبت کنترل کنید.

### عروض و زیروبمی

از **`speech_metadata.style`** برای کنترل آهنگ، زیروبمی، و نواخت در سراسر
یک نوبت استفاده کنید (برای مثال، `"style": "high pitch, cheerful and excited inflection"` یا
`"style": "monotone and flat"`). اگر احساس یا آهنگ در میان گفتگو تغییر می‌کند،
نوشته را به نوبت‌های جداگانه با مقادیر `style` متمایز برای هر نوبت تقسیم کنید.

### تأکید

کلمات خاصی را در ترانویسی با حروف بزرگ بنویسید و آن‌ها را با علائم سجاوندی و برچسب‌های صوتی درون‌خطی ترکیب کنید تا تأکید صوتی طبیعی روی کلمات کلیدی قرار گیرد:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### صداهای غیرگفتاری و انفجارهای صوتی

صداهای غیرگفتاری انسان را بااستفاده از علامت‌های بزرگ‌تر و کوچک‌تر (`<...>`) در همان جایی که صدا باید شنیده شود، به‌صورت درون‌خطی قرار دهید. برچسب‌های صوتی توصیه‌شده شامل موارد زیر است:

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

### کانال‌های برگشتی و گفتار هم‌پوشان

در گفتگوی چند گوینده، واکنش‌های شنونده را در نویسه‌های لوله
(`|reaction|`) در نوبت گوینده بپیچید تا کانال‌های پشتی طبیعی یا
گفتار هم‌پوشان ایجاد کنید بدون اینکه برای هر واکنش نوبت جداگانه‌ای ایجاد کنید.

- **تبادل‌های کوتاه کانال پشتیبان:** واکنش‌های شنونده مختصر لایه (`|oh hmm|`،
  `|oh really?|`، `|absolutely|`) را در نوبت سخنران فعال قرار دهید:
  - **نوبت ۱ (گوینده الف):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **نوبت ۲ (گوینده ب):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **نوبت ۳ (گوینده A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **گفتار هم‌پوشان و درهم‌بافته:** از چند بخش خط عمودی برای شبیه‌سازی گفتار هم‌زمان یا درهم‌بافته بین دو گوینده استفاده کنید (بهترین عملکرد را با `gemini-3.8-flash-tts` دارد):
  - **شمارش معکوس/هم‌سرایی هم‌زمان:** `"Let's surprise him on three |ok| ready?"` و سپس `"one. two. three. |happy| happy |birthday| birthday!"`
  - **هم‌پوشانی کامل بلندگو:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### هماهنگی در همه موارد تولیدشده و چیزهایی که باید از آن‌ها اجتناب کرد

برای حفظ ثبات هویت صوتی در نوبت‌های مختلف، این دستورالعمل‌ها را دنبال کنید:

- **شخصیت‌های طراحی را ازقبل در «طراحی صدا» به‌جای بلوک‌های سبک طولانی طراحی کنید:**
  بخش‌های `"Audio Profile"` طولانی و چند گلوله `"Director's Notes"`
  که از مدل‌های قبلی منتقل شده‌اند، رایج‌ترین دلیل انحراف صدا هستند.
  از همان شهود خلاقانه در
  [طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa) استفاده کنید تا یک شخصیت سفارشی `voice_...` دائمی ایجاد کنید، سپس آن شناسه صدا را در تماس‌های نوشتار به گفتار خود به‌کار ببرید.
- **برای پایداری به مرجع صوتی تکیه کنید (دستورالعمل‌های متا را حذف کنید):**
  مدل‌های Gemini 3.8 TTS آموزش دیده‌اند تا ابتدا به مرجع صوتی تکیه کنند.
  دستورالعمل‌هایی را که به مدل می‌گوید صدا را ثابت نگه دارد (مانند `"do not switch speaker identity"` یا `"maintain identical timbre"`) اضافه نکنید—نوشتار پیام‌واره اضافی باعث افزایش انحراف می‌شود. دستورالعمل‌های سبک غیرضروری را حذف کنید و اجازه دهید مدل به‌طور طبیعی حول نقطه ثابتی که مرجع صوتی ارائه می‌دهد تغییر کند.
- **سعی نکنید ویژگی‌های تغییرناپذیر گوینده را در `style` تغییر دهید:** از قرار دادن
  سن، جنسیت، نام‌ها، یا تغییرات لهجه دائمی در `speech_metadata.style` خودداری کنید.
  به‌جای آن، صدایی منطقه‌ای از «کتابخانه صدای گسترده» انتخاب کنید یا با [طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa) صدایی ایجاد کنید.

### گردش کار توصیه‌شده

1. **شخصیت را یک‌بار بسازید:** شخصیت خود را در
   [طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa) بسازید یا صدایی منطقه‌ای از
   «کتابخانه صدای گسترده» که با زبان و شخصیت هدف شما مطابقت دارد انتخاب کنید.
2. **ترانویسی‌های گفتاری طبیعی با ناروانی‌های گفتاری بنویسید:** برای حداکثر
   طبیعی بودن، `text` را به‌عنوان ترانویسی گفتاری واقعی بنویسید—ازجمله ناروانی‌های گفتاری
   و تردیدهای مکالمه‌ای طبیعی (برای مثال،
   `"Oh uh yeah I think... hm, so that's interesting"`).
3. **ابتدا نوشتار به گفتار ساده را آزمایش کنید:** ابتدا ترانویسی‌تان را با فیلد `style` خالی ترکیب کنید—اکثر درخواست‌ها اصلاً به دستورالعمل `style` نیاز ندارند.
4. **فقط برای اصلاحات، پیام‌واره‌های کوتاه `style` اضافه کنید:** فقط برای نوبت‌هایی که نیاز به اصلاح خاصی در ارائه دارند، `style` رشته‌ای
   (مانند `"casual, friendly"` یا `"muttering, then reassuring"`) مختصر اضافه کنید، و وقتی می‌خواهید خط پایه یکسانی داشته باشید، آن رشته کوتاه دقیق را در نوبت‌های مختلف استفاده مجدد کنید.

### مکالمه چندنوبتی و عامل‌های صوتی

هنگام ساختن عامل‌های صوتی مکالمه‌ای هم‌زمان یا برنامه‌های چندنوبتی:

- با رسیدن تکه‌های نوشتار مدل زبانی بزرگ، **یک تماس نوشتار به گفتار در هر نوبت** برقرار کنید.
- اجازه دهید `voice` پیکربندی‌شده (ازپیش‌ساخته، طراحی‌شده `voice_...`، یا تکرارشده
  `voice_...` / `voicekey_...`) هویت گوینده را درطول نوبت‌ها حفظ کند—هرگز
  یک شخصیت طولانی را در هر نوبت دوباره ارسال نکنید.
- فیلد `style` را برای هر نوبت خالی بگذارید، یا یک رشته ثابت کوتاه
  (مانند `"casual, friendly"`) برای کل مکالمه ارسال کنید.
- پاسخ‌های طولانی نماینده را به‌جای استفاده از پیام‌واره‌های سبک قوی‌تر، به نوبت‌های کوتاه‌تر تقسیم کنید.

## محدودیت‌ها

- مدل‌های «تبدیل نوشتار به گفتار» فقط ورودی‌های نوشتاری را می‌پذیرند و فقط خروجی‌های صوتی تولید می‌کنند.
- تولید چندگوینده با یک درخواست (`speech_config.speakers`) از
  حداکثر ۲ گوینده بااستفاده از صداهای پیش‌ساخته پشتیبانی می‌کند. برای ترکیب صداهای طراحی‌شده سفارشی (`voice_...`) یا تکرارشده (`voice_...` / `voicekey_...`) در مکالمه چندشخصیتی، نوبت هر گوینده را به‌طور جداگانه ترکیب کنید.
  ازآنجایی‌که درخواست‌های یک‌تایی به‌طور پیش‌فرض `audio/wav` را با سرایند RIFF ۴۴ بایتی برمی‌گردانند، PCM خام (`{"type": "audio", "mime_type": "audio/l16"}`) را درخواست کنید یا سرایند WAV را از هر نوبت قبل‌از به‌هم پیوستن قاب‌های صوتی PCM ۲۴ کیلوهرتزی حذف کنید.
- **محدودیت‌های ذخیره‌سازی صدای سفارشی و TTL:**
  - **صداهای حالت‌دار (`store=True`، با پیام‌واره یا تکثیرشده):** حداکثر
    **۲۰۰ صدا در هر پروژه** با **زمان بقای ۱ ساله** (زمان بقا).
  - **کلیدهای صوتی بدون وضعیت (`store=False`، `voicekey_...`):** **‫TTL‏ ۷ روزه**
    (زمان زنده بودن).
- بخش [زبان‌های پشتیبانی‌شده](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa#languages)
  را برای پوشش زبان بررسی کنید.

## قدم بعدی چیست

- با [طراحی صدا](https://ai.google.dev/gemini-api/docs/voice-design?hl=fa)، از زبان طبیعی شخصیت‌های صوتی سفارشی ایجاد کنید.
- صدای گوینده موجود را در
  [همانندسازی صدا](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fa) همانندسازی کنید.
- مشخصات مدل را در صفحه‌های مدل
  [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fa) و
  [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fa)
  مقایسه کنید.
- با [Live API](https://ai.google.dev/gemini-api/docs/live?hl=fa)، صدای دوطرفه تعاملی را کاوش کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-12 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-12 به‌وقت ساعت هماهنگ جهانی."],[],[]]
