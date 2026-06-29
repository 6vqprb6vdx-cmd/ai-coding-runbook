---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar
fetched_at: 2026-06-29T05:35:19.835500+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0645\u062d\u062a\u0648\u0649 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 \"\u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u0646\u0635 \u0625\u0644\u0649 \u0643\u0644\u0627\u0645\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء محتوى باستخدام تكنولوجيا "تحويل النص إلى كلام"

يمكن لواجهة Gemini API تحويل إدخال النص إلى صوت أحادي المتحدث أو متعدد المتحدثين باستخدام إمكانات إنشاء النص إلى كلام (TTS) في Gemini.
إنّ عملية إنشاء الصوت باستخدام ميزة "تحويل النص إلى كلام" *[قابلة للتحكّم](#controllable)*، ما يعني أنّه يمكنك استخدام اللغة الطبيعية لتنظيم التفاعلات وتحديد *الأسلوب* و*اللهجة* و*السرعة* و*النبرة* في الصوت.

تختلف إمكانية تحويل النص إلى كلام عن إمكانية إنشاء الكلام المقدَّمة من خلال
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar)، وهي مصمَّمة لتوفير صوت تفاعلي وغير منظَّم، بالإضافة إلى مدخلات ومخرجات متعددة الوسائط. في حين أنّ واجهة Live API تتفوّق في سياقات المحادثات الديناميكية، تم تصميم ميزة تحويل النص إلى كلام من خلال Gemini API لتناسب السيناريوهات التي تتطلّب تلاوة نصية دقيقة مع إمكانية التحكّم بدقة في الأسلوب والصوت، مثل إنشاء البودكاست أو الكتب المسموعة.

يوضّح لك هذا الدليل كيفية إنشاء محتوى صوتي يتضمّن متحدثًا واحدًا أو عدة متحدثين من نص.

## قبل البدء

تأكَّد من استخدام إصدار من نموذج Gemini 2.5 يتضمّن إمكانات تحويل النص إلى كلام (TTS) من Gemini، كما هو موضّح في قسم [النماذج المتوافقة](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#supported-models). للحصول على أفضل النتائج، حدِّد النموذج الأنسب لحالة الاستخدام المحدّدة.

قد يكون من المفيد [اختبار نماذج تحويل النص إلى كلام في Gemini 2.5 في AI Studio]

## تحويل النص إلى كلام بصوت شخص واحد

لتحويل النص إلى صوت متحدث واحد، اضبط طريقة الرد على "صوت"،
وامرر كائن `speech_config` مع اسم صوت.
عليك اختيار اسم صوت من [أصوات الإخراج](#voices) المُنشأة مسبقًا.

يحفظ هذا المثال الصوت الناتج من النموذج في ملف موجي:

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
       "type": "audio"
     },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

يمكنك استرداد بيانات الصوت التي تم إنشاؤها باستخدام السمة `interaction.output_audio`، والتي تعرض آخر مقطع صوتي تم إنشاؤه. للحصول على تفاصيل حول سمات الراحة، يُرجى الاطّلاع على [نظرة عامة على التفاعلات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar#convenience-properties).

## تحويل النص إلى كلام لعدة متحدثين

بالنسبة إلى الصوت الصادر من مكبّرات صوت متعددة، ستحتاج إلى جهاز `multi_speaker_voice_config` مع إعداد كل مكبّر صوت (بحد أقصى 2) كجهاز `speaker_voice_config`.
عليك تحديد كل `speaker` باستخدام الأسماء نفسها المستخدَمة في [الطلب](#controllable):

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_format={"type": "audio"},
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_format": {
       "type": "audio"
     },
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## التحكّم في أسلوب الكلام باستخدام الطلبات

يمكنك التحكّم في الأسلوب والنبرة واللهجة والسرعة باستخدام طلبات باللغة الطبيعية
لكل من ميزة تحويل النص إلى كلام بصوت متحدث واحد وبأصوات متحدثين متعددين.
على سبيل المثال، في طلب يتضمّن متحدثًا واحدًا، يمكنك قول:

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

في طلب يتضمّن عدة متحدثين، قدِّم إلى النموذج اسم كل متحدث والنص الخاص به. يمكنك أيضًا تقديم إرشادات لكل متحدث على حدة:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

جرِّب استخدام [خيار صوتي](#voices) يتوافق مع الأسلوب أو المشاعر التي تريد التعبير عنها، وذلك للتأكيد عليها بشكل أكبر. في الطلب السابق، على سبيل المثال، قد يؤكّد صوت *إنسيلادوس* على حالتَي "التعب" و"الملل"، بينما قد تتناسب نبرة *بوك* المبهجة مع حالتَي "الحماس" و"السعادة".

## إنشاء طلب لتحويل النص إلى صوت

تنتج نماذج تحويل النص إلى كلام الصوت فقط، ولكن يمكنك استخدام [نماذج أخرى](https://ai.google.dev/gemini-api/docs/models?hl=ar) لإنشاء نص أولاً، ثم تمرير هذا النص إلى نموذج تحويل النص إلى كلام لقراءته بصوت مرتفع.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.5-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_format={"type": "audio"},
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.5-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_format: { type: 'audio' },
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

## إنشاء الكلام أثناء البث

يمكنك بث الصوت الذي تم إنشاؤه أثناء إنشائه بواسطة النموذج من خلال ضبط `stream: true`.

### Python

```
from google import genai
import base64

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    },
    stream=True
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
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
      stream: true
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"       -H "x-goog-api-key: $GEMINI_API_KEY"       -H "Content-Type: application/json"       -H "Api-Revision: 2026-05-20"       --no-buffer       -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
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

## خيارات الصوت

تتيح نماذج "تحويل النص إلى كلام" 30 خيارًا صوتيًا في الحقل `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *ساطع* | **Puck** -- *موسيقى مبهجة* | **شارون** -- *مفيدة* |
| **كوريا** -- *شركة* | **Fenrir** -- *متحمّس* | **Leda** -- *Youthful* |
| **Orus** -- *شركة* | **Aoede** -- *Breezy* | **Callirrhoe** -- *مريح* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *شخصية سهلة* | **الجبهة** -- *ناعمة* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *مفيدة* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *الشركة* |
| **Schedar** -- *Even* | **Gacrux** -- *ناضج* | ‫**Pulcherrima** -- *واثق* |
| **Achird** -- *Friendly* | **Zubenelgenubi** -- *غير رسمي* | ‫**Vindemiatrix** -- *لطيف* |
| **Sadachbia** -- *مفعم بالحيوية* | **Sadaltager** -- *مُلمّ* | **سولافات** -- *دافئ* |

يمكنك الاستماع إلى جميع خيارات الصوت في

## اللغات المتاحة

ترصد نماذج تحويل النص إلى كلام لغة الإدخال تلقائيًا. تتوفّر اللغات التالية:

| اللغة | رمز BCP-47 | اللغة | رمز BCP-47 |
| --- | --- | --- | --- |
| العربية | ar | الفلبينية | fil |
| البنغالية | bn | الفنلندية | fi |
| الهولندية | nl | الغليشيانية | gl |
| الإنجليزية | en | الجورجية | ka |
| الفرنسية | fr | اليونانية | el |
| الألمانية | de | الغوجاراتية | gu |
| الهندية | hi | الكريولية الهايتية | ht |
| الإندونيسية | id | العبرية | هو |
| الإيطالية | it | الهنغارية | hu |
| اليابانية | ja | الأيسلندية | هو |
| الكورية | ko | الجافانية | jv |
| المراثية | mr | الكانادا | kn |
| البولندية | pl | الكونكانية | kok |
| البرتغالية | pt | لاو | lo |
| الرومانية | ro | اللاتينية | la |
| الروسية | ru | اللاتفية | lv |
| الإسبانية | es | الليتوانية | lt |
| التاميلية | ta | اللوكسمبورغية | لبنان |
| التيلوغوية | te | المقدونية | mk |
| التايلاندية | th | المايثيلية | mai |
| التركية | tr | الملغاشية | مليغرام |
| الأوكرانية | uk | الماليزية | مللي ثانية |
| الفيتنامية | vi | المالايالامية | ml |
| الأفريقانية | af | المنغولية | mn |
| الألبانية | sq | النيبالية | ne |
| الأمهرية | am | النرويجية، بوكمال | nb |
| الأرمينية | hy | النرويجية، نينورسك | nn |
| أذربيجان | az | الأوديا | أو |
| الباسك | eu | البشتو | ps |
| البيلاروسية | be | الفارسية | fa |
| البلغارية | bg | البنجابية | pa |
| البورمية | my | الصربية | sr |
| الكتالانية | ca | السندية | دقة عادية |
| السيبيوانية | ceb | السنهالية | si |
| الصينية، المندرينية | cmn | السلوفاكية | sk |
| الكرواتية | ساعة | السلوفينية | sl |
| التشيكية | cs | السواحيلية | sw |
| الدانماركية | da | السويدية | sv |
| الإستونية | et | الأوردية | ur |

## النماذج المتوافقة

| الطراز | متحدّث واحد | المتحدثون المتعدّدون |
| --- | --- | --- |
| [معاينة Gemini 3.1 Flash لتحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ar) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=ar) | ✔️ | ✔️ |
| [إصدار تجريبي من Gemini 2.5 Pro لتحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=ar) | ✔️ | ✔️ |

## الدليل الإرشادي لكتابة الطلبات

يتميّز نموذج **الإنشاء الصوتي المدمج لتحويل النص إلى كلام (TTS) من Gemini** عن نماذج تحويل النص إلى كلام التقليدية باستخدام نموذج لغوي كبير يعرف ***ليس فقط ما يجب قوله، بل أيضًا كيفية قوله***.

يمكنك اعتبار الطلب المتقدّم بمثابة تعليمات نظامية يقدّمها المستخدم للنموذج لكي يتّبعها. وهي طريقة لتزويد النموذج بمزيد من السياق والتحكّم في الأداء.

للاستفادة من هذه الإمكانية، يمكن للمستخدمين التفكير في أنفسهم كمدراء يضبطون مشهدًا ليؤديه ممثل صوتي افتراضي. لإنشاء طلب، ننصحك بمراعاة المكوّنات التالية: **الملف الصوتي** الذي يحدّد الهوية الأساسية للشخصية ونمطها، و**وصف المشهد** الذي يحدّد البيئة المادية و"الأجواء" العاطفية، و**ملاحظات المخرج** التي تقدّم إرشادات أكثر دقة حول الأداء من حيث الأسلوب واللهجة والتحكّم في السرعة.

من خلال تقديم تعليمات دقيقة، مثل لهجة إقليمية محددة أو ميزات لغوية محددة (مثل التنفس) أو سرعة الكلام، يمكن للمستخدمين الاستفادة من قدرة النموذج على فهم السياق لإنشاء أداء صوتي ديناميكي وطبيعي ومعبّر. للحصول على أفضل أداء، ننصح بأن تتطابق **النصوص** مع الطلبات الإخراجية، *بحيث يتطابق "من يقول ذلك"* مع *"ماذا يُقال"* و*"كيف يُقال".*

الغرض من هذا الدليل هو تقديم توجيهات أساسية وإثارة الأفكار عند تطوير تجارب صوتية باستخدام ميزة &quot;إنشاء الصوت&quot; من Gemini لتحويل النص إلى كلام. نحن متحمّسون لرؤية إبداعاتك.

### علامات صوتية

العلامات هي معدِّلات مضمّنة، مثل `[whispers]` أو `[laughs]`، تمنحك تحكّمًا دقيقًا في عملية التسليم. يمكنك استخدامها لتغيير نبرة الصوت وسرعته
والإحساس العاطفي في سطر أو قسم من النص. يمكنك أيضًا استخدامها لإضافة عبارات اعتراضية وبعض الأصوات غير اللفظية الأخرى إلى الأداء، مثل `[cough]` أو `[sighs]` أو `[gasp]`.

لا تتوفّر قائمة شاملة بالعلامات التي تعمل وتلك التي لا تعمل، وننصحك بتجربة مشاعر وتعبيرات مختلفة لمعرفة كيف يتغيّر الناتج.

إذا لم تكن النسخة مكتوبة باللغة الإنجليزية، ننصحك باستخدام علامات صوتية باللغة الإنجليزية للحصول على أفضل النتائج.

**استخدام علامات صوتية مبتكرة**

لعرض نوع التباين الذي يمكن الحصول عليه باستخدام علامات الصوت، إليك مجموعة من الأمثلة التي تعبّر عن المعنى نفسه، ولكن يختلف أسلوب التعبير حسب العلامات المستخدَمة.

يمكنك تغيير طريقة إلقاء الكلام من خلال إضافة علامات في بداية السطر لجعل المتحدث يبدو متحمسًا أو متضايقًا أو مترددًا:

- `[excitedly]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام، ويمكنني التحدّث بطرق مختلفة. كيف يمكنني مساعدتك اليوم؟
- `[bored]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[reluctantly]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…

يمكن أيضًا استخدام العلامات لتغيير سرعة العرض أو لدمج السرعة مع التأكيد:

- `[very fast]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[very slow]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[sarcastically, one painfully slow word at a time]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…

يمكنك أيضًا التحكّم بدقة في أقسام معيّنة، ما يعني أنّه يمكنك التحدث بصوت منخفض في جزء واحد من الفيديو والصراخ في جزء آخر.

- `[whispers]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام، اسمي `[shouting]`، ويمكنني التحدّث بطرق مختلفة. `[whispers]` كيف يمكنني مساعدتك اليوم؟

يمكنك أيضًا تجربة أي فكرة إبداعية تريدها:

- `[like a cartoon dog]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[like dracula]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…

تشمل العلامات الشائعة الاستخدام ما يلي:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

تتيح لك العلامات التحكّم بسرعة في عرض نص الفيديو. ولمزيد من التحكّم، يمكنك دمجها مع طلب سياقي لتحديد النبرة العامة
والأسلوب العام للأغنية.

### بنية الطلب

يتضمّن نص الطلب الفعّال العناصر التالية التي تتكامل معًا لتحقيق أداء رائع:

- **الملف الصوتي**: يحدّد شخصية الصوت، ويحدد هوية الشخصية ونمطها وأي خصائص أخرى مثل العمر والخلفية وما إلى ذلك.
- **المشهد**: يضبط المشهد. يصف هذا الحقل البيئة المادية و"الأجواء".
- **ملاحظات المخرج**: إرشادات الأداء التي يمكنك من خلالها تحديد التعليمات المهمة التي يجب أن يضعها الممثل الافتراضي في اعتباره. وتشمل الأمثلة
  الأسلوب والتنفس والسرعة والتعبير واللهجة.
- **مثال على السياق**: يوفّر هذا الخيار للنموذج نقطة بداية سياقية، ما يتيح للممثل الافتراضي الدخول إلى المشهد الذي أعددته بشكل طبيعي.
- **النص**: النص الذي سينطقه النموذج. للحصول على أفضل أداء، تذكَّر أنّ موضوع النص وأسلوب الكتابة يجب أن يكونا مرتبطَين بالتعليمات التي تقدّمها.
- **علامات الصوت**: هي معدِّلات يمكنك إضافتها إلى نص لتغيير طريقة عرض جزء من النص، مثل `[whispers]` أو `[shouting]`.

مثال على الطلب الكامل:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### استراتيجيات مفصّلة لإنشاء الطلبات

قسِّم كل عنصر من عناصر الطلب على النحو التالي:

#### ملف تعريف الصوت

صف بإيجاز شخصية الشخصية.

- **الاسم:** يساعد منح الشخصية اسمًا في ترسيخ النموذج وربط الأداء معًا. لذا، يُرجى الإشارة إلى الشخصية بالاسم عند تحديد المشهد والسياق.
- **الدور:** الهوية الأساسية والنموذج الأصلي للشخصية التي تؤدي دورها في المشهد، مثل منسّق موسيقى في الراديو أو مقدّم بودكاست أو مراسل إخباري وما إلى ذلك

أمثلة:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### منظر

حدِّد سياق المشهد، بما في ذلك الموقع الجغرافي والأجواء والتفاصيل البيئية التي تحدّد النبرة والإحساس. صِف ما يحدث حول الشخصية وتأثيره فيها. يوفّر المشهد السياق البيئي للتفاعل بأكمله، ويوجه الأداء التمثيلي بطريقة طبيعية دقيقة.

أمثلة:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### ملاحظات المخرجين

يتضمّن هذا القسم المهم إرشادات محدّدة بشأن الأداء. يمكنك تخطّي جميع العناصر الأخرى، ولكن ننصحك بتضمين هذا العنصر.

حدِّد فقط ما هو مهم للأداء، مع الحرص على عدم المبالغة في التحديد. سيؤدي وضع الكثير من القواعد الصارمة إلى الحدّ من إبداع النماذج وقد يؤدي إلى تراجع الأداء. وازِن بين وصف الدور والمشهد وقواعد الأداء المحدّدة.

إنّ التوجيهات الأكثر شيوعًا هي **الأسلوب والوتيرة واللهجة**، ولكن النموذج لا يقتصر على هذه التوجيهات ولا يتطلّبها. يمكنك تضمين تعليمات مخصّصة لتغطية أي تفاصيل إضافية مهمة لأدائك، ويمكنك تقديم التفاصيل بالقدر الذي تراه مناسبًا.

على سبيل المثال:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**النمط:**

يضبط هذا الحقل نبرة الكلام الذي يتم إنشاؤه وأسلوبه. يمكنك تضمين كلمات مثل "مبهج" أو "نشيط" أو "مسترخٍ" أو "ملل" وما إلى ذلك لتوجيه الأداء. يجب أن تكون الأوصاف وافية
وتتضمّن أكبر قدر ممكن من التفاصيل اللازمة: *"حماس معدٍ. إنّ عبارة "يجب أن يشعر المستمع بأنّه يشارك في حدث ضخم ومثير"* أفضل من عبارة *"نشيط وحماسي".*

يمكنك حتى تجربة عبارات شائعة في مجال التعليق الصوتي، مثل "ابتسامة صوتية". يمكنك إضافة أي عدد تريده من خصائص الأنماط.

أمثلة:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

مزيد من العمق

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

متقدّم

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**اللهجة:**

وصف اللهجة المحدّدة وكلّما كانت التفاصيل أكثر، كانت النتائج أفضل. على سبيل المثال، استخدِم "*لهجة إنجليزية بريطانية كما تُسمع في كرويدون، إنجلترا*" بدلاً من "*لهجة بريطانية*".

أمثلة:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**معدّل تسجيل مرات الظهور:**

الوتيرة الإجمالية وتفاوت الوتيرة في جميع أنحاء المقطوعة

أمثلة:

بسيط

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

مزيد من التفاصيل

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

متقدّم

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**تجربة هذه الميزة**

جرِّب بعض هذه الأمثلة بنفسك على
[تطبيق TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=ar) ودَع
Gemini يضعك في مقعد المخرج. إليك بعض النصائح التي يجب وضعها في الاعتبار لتقديم أداء صوتي رائع:

- تذكَّر أن تحافظ على تماسك الطلب بأكمله، فالنص والإخراج يسيران جنبًا إلى جنب في تقديم أداء رائع.
- لا تتردد في ترك بعض التفاصيل ليملأها النموذج، فهذا يساعد في جعل النص يبدو طبيعيًا. (تمامًا مثل ممثل موهوب)
- إذا واجهت صعوبة في كتابة نص أو أداء أغنية، يمكن أن يساعدك Gemini في ذلك.

## القيود

- يمكن لنماذج تحويل النص إلى كلام تلقّي مدخلات نصية فقط وإنشاء مخرجات صوتية.
- تبلغ قدرة [الاستيعاب](https://ai.google.dev/gemini-api/docs/long-context?hl=ar) لجلسة تحويل النص إلى كلام 32 ألف رمز مميّز.
- راجِع قسم [اللغات](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#languages) لمعرفة اللغات المتاحة.
- لا تتيح ميزة "تحويل النص إلى كلام" البث، إلا عند استخدام `gemini-3.1-flash-tts-preview`.

تنطبق القيود التالية تحديدًا عند استخدام نموذج Gemini 3.1 Flash
TTS Preview لإنشاء الكلام:

- **عدم تطابق الصوت مع تعليمات الطلب:** قد لا يتطابق الناتج الذي تقدّمه النماذج دائمًا مع الصوت الذي تم اختياره، ما يؤدي إلى اختلاف الصوت عن المتوقع. لتجنُّب عدم تطابق النبرات (مثل صوت رجل عميق يحاول التحدث مثل فتاة صغيرة)، تأكَّد من أنّ النبرة والسياق المكتوبَين في الطلب يتوافقان بشكل طبيعي مع الملف الشخصي للمتحدث المحدّد.
- **جودة النتائج الأطول:** قد تبدأ جودة الكلام واتساقه في الانخفاض مع النتائج التي تزيد مدتها عن بضع دقائق. ننصحك بتقسيم النصوص إلى أجزاء أصغر.
- **عرض رموز نصية بشكل متقطّع:** يعرض النموذج أحيانًا رموزًا نصية بدلاً من رموز صوتية، ما يؤدي إلى تعذُّر تنفيذ الطلب على الخادم وظهور الخطأ `500`. بما أنّ هذا يحدث بشكل عشوائي في نسبة صغيرة جدًا من الطلبات، عليك تنفيذ منطق إعادة المحاولة المبرمَج في تطبيقك للتعامل مع هذه الحالات.
- **الرفض الخاطئ من مصنّف الطلبات:** قد لا تؤدي الطلبات الغامضة إلى تشغيل مصنّف تركيب الكلام، ما يؤدي إلى رفض الطلب (`PROHIBITED_CONTENT`) أو جعل النموذج يقرأ تعليمات الأسلوب وملاحظات المخرج بصوت عالٍ. تحقّق من صحة الطلبات من خلال إضافة مقدمة واضحة
  تطلب من النموذج تركيب الكلام، وحدِّد بوضوح موضع بدء
  النص الفعلي المنطوق.

## الخطوات التالية

- توفّر [واجهة برمجة التطبيقات Live](https://ai.google.dev/gemini-api/docs/live?hl=ar) من Gemini خيارات تفاعلية لإنشاء الصوت يمكنك دمجها مع وسائط أخرى.
- للتعرّف على كيفية استخدام *مدخلات* الصوت، يُرجى الانتقال إلى دليل [فهم الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
