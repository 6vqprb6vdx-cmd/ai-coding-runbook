---
source_url: https://ai.google.dev/gemini-api/docs/interactions/music-generation?hl=ar
fetched_at: 2026-05-11T12:32:40.552579+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء الموسيقى باستخدام Lyria 3

‫Lyria 3 هي مجموعة نماذج من Google لإنشاء الموسيقى، وهي متاحة من خلال Gemini API. باستخدام Lyria 3، يمكنك إنشاء مقاطع صوتية استيريو عالية الجودة بمعدّل 44.1 كيلوهرتز من الطلبات النصية أو الصور. تقدّم هذه النماذج اتساقًا بنيويًا، بما في ذلك الغناء والكلمات الموقّتة والترتيبات الموسيقية الكاملة.

تتضمّن مجموعة Lyria 3 نموذجَين:

| الطراز | رقم تعريف الطراز | الأفضل لـ | المدة | الناتج |
| --- | --- | --- | --- | --- |
| **مقطع Lyria 3** | `lyria-3-clip-preview` | المقاطع القصيرة والحلقات المتكررة والمعاينات | ‫30 ثانية | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | أغانٍ كاملة تتضمّن مقاطع ولوازم وجسورًا موسيقية | بضع دقائق (يمكن التحكّم فيها باستخدام الطلب) | MP3 |

يمكن استخدام كلا النموذجين من خلال [واجهة برمجة التطبيقات الجديدة Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) التي تتيح إدخال بيانات بتنسيقات متعدّدة (نصوص وصور)، كما يمكنهما إنتاج صوت **استريو عالي الدقة بتردد 44.1 كيلو هرتز**.

## إنشاء مقطع موسيقي

ينشئ نموذج Lyria 3 Clip دائمًا مقطعًا مدته **30 ثانية**. لإنشاء مقطع، استدعِ الدالة `interactions.create` مع طلب نصي. يتضمّن الرد دائمًا كلمات الأغنية وبنيتها إلى جانب الصوت في مخطط `steps`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="Create a 30-second cheerful acoustic folk song with guitar and harmonica.",
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                print(f"Generated audio with mime_type: {content_block.mime_type}")
                with open("music.mp3", "wb") as f:
                    f.write(base64.b64decode(content_block.data))
            elif content_block.type == "text":
                print(f"Lyrics: {content_block.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'Create a 30-second cheerful acoustic folk song with ' +
           'guitar and harmonica.',
});

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                console.log(`Generated audio with mime_type: ${contentBlock.mimeType}`);
                fs.writeFileSync('music.mp3', Buffer.from(contentBlock.data, 'base64'));
            } else if (contentBlock.type === 'text') {
                console.log(`Lyrics: ${contentBlock.text}`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "Create a 30-second cheerful acoustic folk song with guitar and harmonica."
}'
```

## إنشاء أغنية كاملة

استخدِم نموذج `lyria-3-pro-preview` لإنشاء أغانٍ كاملة المدة تستغرق بضع دقائق. يفهم نموذج Pro البنية الموسيقية ويمكنه إنشاء مقطوعات موسيقية تتضمّن مقاطع شعرية ولازمة وجسرًا موسيقيًا. يمكنك التأثير في المدة من خلال تحديدها في طلبك (مثلاً، "إنشاء أغنية مدتها دقيقتان") أو باستخدام [الطوابع الزمنية](#timing) لتحديد البنية.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'An epic cinematic orchestral piece about a journey home. ' +
           'Starts with a solo piano intro, builds through sweeping ' +
           'strings, and climaxes with a massive wall of sound.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."
}'
```

## اختيار تنسيق الإخراج

تنشئ نماذج Lyria 3 المحتوى الصوتي بتنسيق **MP3** تلقائيًا. في Lyria 3 Pro، يمكنك أيضًا طلب الحصول على الناتج بتنسيق **WAV** من خلال ضبط `response_mime_type`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An atmospheric ambient track.",
    response_modalities=["audio", "text"],
    response_mime_type="audio/wav",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'An atmospheric ambient track.',
    responseModalities: ["audio", "text"],
    responseMimeType: "audio/wav",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "An atmospheric ambient track.",
    "responseModalities": ["audio", "text"],
    "responseMimeType": "audio/wav"
  }'
```

## تحليل الردّ

يتضمّن الردّ من Lyria 3 عدة أقسام من المحتوى ضمن المخطط `steps`.
تعرض التفاعلات سلسلة من الخطوات، حيث تحتوي الخطوات `model_output` على المحتوى الذي تم إنشاؤه.
تحتوي مربّعات المحتوى النصي على كلمات الأغنية التي تم إنشاؤها أو وصف بتنسيق JSON لبنية الأغنية.
تحتوي مربّعات المحتوى من النوع `audio` على بيانات الصوت المشفرة بترميز Base64.

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

## إنشاء موسيقى من الصور

يتوافق Lyria 3 مع الإدخالات المتعدّدة الوسائط، إذ يمكنك تقديم ما يصل إلى **10 صور** إلى جانب طلبك النصي في قائمة `input`، وسيقوم النموذج بتأليف موسيقى مستوحاة من المحتوى المرئي.

### Python

```
uploaded_image = client.files.upload(file="desert_sunset.jpg")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
        {
            "type": "image",
            "uri": uploaded_image.uri,
            "mime_type": uploaded_image.mime_type
        }
    ],
)
```

### JavaScript

```
const uploadedImage = await client.files.upload({
    file: "desert_sunset.jpg",
    config: { mimeType: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: [
        { type: 'text', text: 'An atmospheric ambient track inspired by the mood and colors in this image.' },
        {
            type: 'image',
            uri: uploadedImage.uri,
            mimeType: uploadedImage.mimeType
        }
    ],
});
```

### REST

```
# First upload the image using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "uri": "YOUR_FILE_URI", "mime_type": "image/jpeg"}
    ]
  }'
```

## تقديم كلمات أغنية مخصّصة

يمكنك كتابة كلمات الأغنية الخاصة بك وتضمينها في الطلب. استخدِم علامات الأقسام، مثل `[Verse]` و`[Chorus]` و`[Bridge]`، لمساعدة النموذج في فهم بنية الأغنية:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## التحكّم في التوقيت والبنية

يمكنك تحديد ما يحدث بالضبط في لحظات معيّنة من الأغنية باستخدام الطوابع الزمنية. يفيد ذلك في التحكّم في وقت بدء الآلات الموسيقية ووقت عرض كلمات الأغنية وطريقة تقدّم الأغنية:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## إنشاء مقاطع موسيقية بدون غناء

بالنسبة إلى الموسيقى الخلفية أو المقاطع الصوتية للألعاب أو أي حالة استخدام لا تتطلّب أصواتًا بشرية، يمكنك أن تطلب من النموذج إنشاء مقاطع موسيقية فقط:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## إنشاء موسيقى بلغات مختلفة

تنشئ Lyria 3 كلمات الأغاني باللغة التي تستخدمها في طلبك. لإنشاء أغنية
بكلمات فرنسية، اكتب طلبك باللغة الفرنسية. ويعدّل النموذج أسلوبه الصوتي وطريقة لفظه لتتطابق مع اللغة.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## ذكاء النموذج

يحلّل Lyria 3 عملية الطلب التي تتضمّن
النموذج الذي يحلّل البنية الموسيقية (المقدمة، والمقطع، والجوقة، والجسر الموسيقي، وما إلى ذلك)
استنادًا إلى طلبك.
يحدث ذلك قبل إنشاء الصوت ويضمن التماسك البنيوي والانسجام الموسيقي.

## دليل كتابة الطلبات

كلما كان طلبك أكثر تحديدًا، كانت النتائج أفضل. في ما يلي ما يمكنك تضمينه لتوجيه عملية الإنشاء:

- **النوع**: حدِّد نوعًا أو مزيجًا من الأنواع (مثلاً "هيب هوب منخفض الدقة" أو "موسيقى جاز" أو "موسيقى أوركسترا سينمائية").
- **الآلات الموسيقية**: اسم الآلات الموسيقية المحدّدة (مثلاً "بيانو Fender Rhodes" أو "غيتار منزلق" أو "آلة الطبول TR-808")
- **عدد النبضات في الدقيقة**: ضبط الإيقاع (مثلاً، "120 نبضة في الدقيقة" أو "إيقاع بطيء يبلغ حوالي 70 نبضة في الدقيقة")
- **المفتاح الموسيقي/المقياس الموسيقي**: حدِّد مفتاحًا موسيقيًا (مثل "في سلم G الكبير" أو "في سلم D الصغير").
- **المزاج والأجواء**: استخدِم صفات وصفية (مثل "حنين" أو "عدواني" أو "أثيري" أو "حالم").
- **البنية**: استخدِم علامات مثل `[Verse]` أو `[Chorus]` أو `[Bridge]` أو `[Intro]` أو `[Outro]` أو الطوابع الزمنية للتحكّم في تقدّم الأغنية.
- **المدة**: ينتج نموذج "المقطع" دائمًا مقاطع مدتها 30 ثانية. بالنسبة إلى طراز Pro، حدِّد المدة المطلوبة في طلبك (مثلاً، "إنشاء أغنية مدتها دقيقتان") أو استخدِم الطوابع الزمنية للتحكّم في المدة.

### أمثلة على الطلبات

إليك بعض الأمثلة على الطلبات الفعّالة:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## أفضل الممارسات

- **التكرار باستخدام Clip أولاً** استخدِم النموذج الأسرع `lyria-3-clip-preview` لتجربة الطلبات قبل الالتزام بإنشاء أغنية كاملة باستخدام `lyria-3-pro-preview`.
- **الدقة** تؤدي الطلبات الغامضة إلى نتائج عامة. اذكر الآلات الموسيقية وسرعة الإيقاع والمفتاح الموسيقي والحالة المزاجية والبنية للحصول على أفضل نتيجة.
- **مطابقة لغتك** اكتب الطلب باللغة التي تريد عرض كلمات الأغنية بها.
- **استخدام علامات الأقسام** تمنح العلامات `[Verse]` و`[Chorus]` و`[Bridge]` النموذج بنية واضحة يجب اتّباعها.
- **فصل كلمات الأغنية عن التعليمات:** عند تقديم كلمات أغنية مخصّصة، يجب فصلها بوضوح عن تعليمات التوجيه الموسيقي.

## القيود

- **الأمان**: تتحقّق فلاتر الأمان من جميع الطلبات. سيتم حظر الطلبات التي تؤدي إلى تشغيل الفلاتر. ويشمل ذلك الطلبات التي تطلب أصوات فنّانين معيّنين أو إنشاء كلمات أغاني محمية بحقوق الطبع والنشر.
- **وضع العلامات المائية**: تتضمّن جميع المقاطع الصوتية التي يتم إنشاؤها [علامة مائية لمقطع صوتي من SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ar) لتحديدها. هذه العلامة المائية غير مسموعة بالأذن البشرية ولا تؤثر في تجربة الاستماع.
- **التعديل المتعدد**: عملية إنشاء الموسيقى هي عملية من خطوة واحدة.
  لا يتيح الإصدار الحالي من Lyria 3 تعديل المقاطع التي تم إنشاؤها أو تحسينها بشكل متكرر من خلال طلبات متعددة.
- **المدة**: ينشئ نموذج "المقطع" دائمًا مقاطع مدتها 30 ثانية. ينشئ نموذج Pro أغاني تستغرق بضع دقائق، ويمكن التأثير في المدة الدقيقة من خلال الطلب.
- **التحديد**: قد تختلف النتائج بين المكالمات، حتى مع استخدام الطلب نفسه.

## الخطوات التالية

- اطّلِع على [الأسعار](https://ai.google.dev/gemini-api/docs/interactions/pricing?hl=ar) لنماذج Lyria 3
- جرِّب [إنشاء الموسيقى بالبث المباشر في الوقت الفعلي](https://ai.google.dev/gemini-api/docs/interactions/realtime-music-generation?hl=ar)
  باستخدام Lyria RealTime.
- إنشاء محادثات بين عدة أشخاص باستخدام
  [نماذج تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/interactions/audio-generation?hl=ar)
- تعرَّف على كيفية إنشاء [صور](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ar) أو [فيديوهات](https://ai.google.dev/gemini-api/docs/interactions/video?hl=ar).
- تعرَّف على كيفية [فهم Gemini للملفات الصوتية](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ar)،
- إجراء محادثة فورية مع Gemini باستخدام
  [Live API](https://ai.google.dev/gemini-api/docs/interactions/live?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
