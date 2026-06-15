---
source_url: https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar
fetched_at: 2026-06-15T06:27:14.877938+00:00
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

# التفكير في Gemini

تستخدم [نماذج Gemini 3 و2.5 سلسلة](https://ai.google.dev/gemini-api/docs/models?hl=ar)
"عملية تفكير" تُحسِّن بشكل كبير قدرات الاستدلال والتخطيط المتعدّد الخطوات، ما يجعلها فعّالة للغاية في المهام المعقدة، مثل
الترميز والرياضيات المتقدّمة وتحليل البيانات.

عند استخدام نموذج تفكير، يستدلّ Gemini داخليًا قبل الردّ. تعرض Interactions API هذا الاستدلال من خلال خطوات `thought`، وهي خطوات مخصّصة تظهر بترتيب زمني إلى جانب استدعاءات الدوال أو إدخالات المستخدم أو نواتج النموذج في مصفوفة `steps`.

تحتوي كل خطوة تفكير على حقلَين:

| الحقل | مطلوب أو اختياري | الوصف |
| --- | --- | --- |
| `signature` | ✅ نعم | تمثيل مشفّر لحالة الاستدلال الداخلي للنموذج يظهر دائمًا، حتى عندما يُجري النموذج الحد الأدنى من الاستدلال |
| `summary` | ❌ لا | مصفوفة من المحتوى (نص و/أو صور) تلخّص الاستدلال قد تكون فارغة استنادًا إلى إعداد [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=ar)، أو ما إذا كان النموذج قد أجرى ما يكفي من الاستدلال، أو نوع المحتوى (على سبيل المثال، قد لا تتضمّن الصور الكامنة ملخّصات نصية) |

## التفاعلات مع التفكير

إنّ بدء تفاعل مع نموذج تفكير مشابه لأيّ طلب تفاعل آخر. حدِّد أحد [النماذج التي تتوافق مع التفكير](#thinking-levels) في الحقل `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## ملخّصات الأفكار

تقدّم ملخّصات الأفكار إحصاءات عن عملية الاستدلال الداخلي للنموذج.
لا يتم عرض سوى الناتج النهائي تلقائيًا. يمكنك تفعيل ملخّصات الأفكار باستخدام `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

قد تحتوي كتلة الأفكار **على توقيع فقط بدون ملخّص** في الحالات التالية:

- الطلبات البسيطة التي لم يستدلّ فيها النموذج بما يكفي لإنشاء ملخّص
- `thinking_summaries: "none"`، حيث يتم إيقاف الملخّصات بشكل صريح
- قد لا تتضمّن أنواع معيّنة من محتوى الأفكار، مثل الصور، ملخّصات نصية

يجب أن يتعامل الرمز البرمجي دائمًا مع كتل الأفكار التي يكون فيها `summary` فارغًا أو غير متوفّر.

## البث مع التفكير

استخدِم البث لتلقّي ملخّصات الأفكار المتزايدة أثناء الإنشاء.
يتم تسليم كتل الأفكار باستخدام أحداث Server-Sent Events (SSE) مع نوعَين مختلفَين من التغييرات الجزئية:

| نوع التغيير الجزئي | يحتوي على | وقت إرسال البيانات |
| --- | --- | --- |
| `thought_summary` | محتوى ملخّص نصي أو صورة | تغيير جزئي واحد أو أكثر مع ملخّص متزايد |
| `thought_signature` | التوقيع المشفّر | آخر دلتا قبل `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

يستخدم الردّ على البث أحداث Server-Sent Events (SSE) ويتألف من خطوات وأحداث، على سبيل المثال:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## التحكّم في التفكير

تستخدم نماذج Gemini التفكير الديناميكي تلقائيًا، ما يؤدي إلى تعديل مقدار جهد الاستدلال تلقائيًا استنادًا إلى مدى تعقيد الطلب. يمكنك التحكّم في هذا السلوك باستخدام المعلمة `thinking_level`.

| الطراز | التفكير التلقائي | المستويات المتوافقة |
| --- | --- | --- |
| gemini-3.1-pro-preview | مفعّل (مرتفع) | منخفض، متوسط، مرتفع |
| gemini-3-flash-preview | مفعّل (مرتفع) | أدنى، منخفض، متوسط، مرتفع |
| gemini-3-pro-preview | مفعّل (مرتفع) | منخفض، مرتفع |
| gemini-2.5-pro | مفعّل | منخفض، متوسط، مرتفع |
| gemini-2.5-flash | مفعّل | منخفض، متوسط، مرتفع |
| gemini-2.5-flash-lite | غير مفعّل | منخفض، متوسط، مرتفع |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## توقيعات الأفكار

توقيعات الأفكار هي تمثيلات مشفّرة للاستدلال الداخلي للنموذج. وهي مطلوبة للحفاظ على استمرارية الاستدلال في التفاعلات المتعدّدة الأدوار.

تسهّل Interactions API التعامل مع توقيعات الأفكار بشكل كبير مقارنةً بـ `generateContent` API.

### الوضع الذي يحفظ الحالة (مقترَح)

تلقائيًا، عند استخدام Interactions API في الوضع الذي يحفظ الحالة (من خلال ضبط `store: true` وتمرير `previous_interaction_id` في الأدوار اللاحقة)، يدير الخادم تلقائيًا حالة المحادثة، بما في ذلك جميع كتل الأفكار والتوقيعات. في هذا الوضع، ليس عليك إجراء أيّ شيء بشأن التوقيعات. تتم معالجتها بالكامل على جانب الخادم.

### الوضع الذي لا يحفظ الحالة

إذا كنت تدير حالة المحادثة بنفسك (الوضع الذي لا يحفظ الحالة) وتمرِّر السجلّ الكامل للإدخالات والنواتج في كل طلب:

- **يجب** دائمًا إعادة إرسال جميع كتل `thought` تمامًا كما تم استلامها من النموذج.
- **لا** يجب إزالة كتل الأفكار أو تعديلها من السجلّ، لأنّها تحتوي على التوقيعات المطلوبة ليواصل النموذج استدلاله.
- عند التبديل بين النماذج ضمن جلسة، يجب أن تظل تعيد إرسال كتل الأفكار الخاصة بالنموذج السابق. تتولّى الأنظمة الخلفية إدارة التوافق.

## الأسعار

عند تفعيل التفكير، يكون سعر الردّ هو مجموع رموز الإخراج ورموز التفكير. يمكنك الحصول على إجمالي عدد رموز التفكير التي تم إنشاؤها من حقل `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

تُنشئ نماذج التفكير أفكارًا كاملة لتحسين جودة الردّ النهائي
، ثم تعرض [ملخّصات](#summaries) لتقديم إحصاءات عن عملية التفكير. تستند الأسعار إلى رموز التفكير الكاملة التي يحتاج النموذج إلى إنشائها، على الرغم من أنّ واجهة برمجة التطبيقات لا تعرض سوى الملخّص.

يمكنك الاطّلاع على مزيد من المعلومات عن الرموز في دليل [احتساب الرموز](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ar).

## أفضل الممارسات

استخدِم نماذج التفكير بكفاءة من خلال اتّباع هذه الإرشادات.

- **مراجعة الاستدلال**: حلِّل ملخّصات الأفكار لفهم حالات الفشل وتحسين الطلبات.
- **التحكّم في ميزانية التفكير**: اطلب من النموذج التفكير بشكل أقل في النواتج الطويلة لتوفير الرموز.
- **المهام البسيطة**: استخدِم الحد الأدنى من التفكير لاسترداد الحقائق أو التصنيف (على سبيل المثال، "أين تم تأسيس DeepMind؟").
- **المهام المتوسّطة**: استخدِم التفكير التلقائي لمقارنة المفاهيم أو الاستدلال الإبداعي (على سبيل المثال، مقارنة السيارات الكهربائية والسيارات الهجينة).
- **المهام المعقدة**: استخدِم الحد الأقصى من التفكير للترميز المتقدّم أو الرياضيات أو التخطيط المتعدّد الخطوات (على سبيل المثال، حلّ مسائل الرياضيات في مسابقة AIME).

## الخطوات التالية

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar): الردود النصية الأساسية
- [استدعاء الدالة](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar): الاتصال بالأدوات
- [دليل Gemini 3](https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=ar): الميزات الخاصة بالنموذج

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
