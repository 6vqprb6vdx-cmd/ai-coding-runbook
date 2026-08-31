---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=ar
fetched_at: 2026-08-31T06:29:43.615369+00:00
title: "\u062a\u0641\u0643\u064a\u0631 Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تفكير Gemini

تستخدم [نماذج سلسلة Gemini 3 و2.5](https://ai.google.dev/gemini-api/docs/models?hl=ar) "عملية تفكير" تحسّن بشكل كبير قدراتها على الاستدلال والتخطيط المتعدّد الخطوات، ما يجعلها فعّالة للغاية في المهام المعقّدة، مثل الترميز والرياضيات المتقدّمة وتحليل البيانات.

عند استخدام نموذج التفكير، يحلّل Gemini طلبك داخليًا قبل الردّ. تعرض Interactions API هذا التفسير من خلال `thought` خطوات مخصّصة تظهر بترتيب زمني إلى جانب طلبات الدوال أو إدخالات المستخدم أو نواتج النموذج في مصفوفة `steps`.

تحتوي كل خطوة تفكير على حقلَين:

| الحقل | مطلوب أو اختياري | الوصف |
| --- | --- | --- |
| `signature` | ✅ نعم | تمثيل مشفّر لحالة الاستدلال الداخلي للنموذج تكون هذه السمة متوفّرة دائمًا، حتى عندما يقدّم النموذج الحد الأدنى من الاستنتاج. |
| `summary` | ❌ لا | مجموعة من المحتوى (نصوص و/أو صور) تلخّص أسباب القرار. قد يكون هذا الحقل فارغًا استنادًا إلى إعدادات [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=ar)، أو ما إذا كان النموذج قد قدّم أسبابًا كافية، أو نوع المحتوى (على سبيل المثال، قد لا تتضمّن الصور الكامنة ملخّصات نصية). |

## التفاعلات مع التفكير

إنّ بدء تفاعل مع نموذج تفكير يشبه أي طلب تفاعل آخر. حدِّد أحد [النماذج التي تتيح استخدام ميزة "التفكير"](#thinking-levels) في الحقل `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## ملخّصات الأفكار

تقدّم ملخّصات الأفكار إحصاءات حول عملية الاستدلال الداخلية للنموذج.
يتم عرض الناتج النهائي فقط بشكل تلقائي. يمكنك تفعيل ملخّصات الأفكار
باستخدام `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

قد تحتوي فقرة التفكير على **توقيع فقط بدون ملخّص** في الحالات التالية:

- الطلبات البسيطة التي لم يقدّم فيها النموذج أسبابًا كافية لإنشاء ملخّص
- ‫`thinking_summaries: "none"`، حيث تكون الملخّصات غير مفعّلة بشكل صريح
- قد لا تتضمّن بعض أنواع المحتوى الفكري، مثل الصور، ملخّصات نصية

يجب أن يتعامل الرمز البرمجي دائمًا مع مربّعات الأفكار التي يكون فيها `summary` فارغًا أو غير متوفّر.

## البث مع التفكير

استخدِم ميزة البث لتلقّي ملخّصات الأفكار التزايدية أثناء إنشائها.
يتم عرض &quot;فقرات الأفكار&quot; باستخدام Server-Sent Events (SSE) مع نوعَين مختلفَين من التغييرات التفاضلية:

| نوع التغيير | يحتوي على | وقت الإرسال |
| --- | --- | --- |
| `thought_summary` | محتوى ملخّص نصي أو مرئي | واحد أو أكثر من التغييرات مع ملخّص تدريجي |
| `thought_signature` | التوقيع المشفّر | آخر فرق قبل `step.stop` |

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

تستخدم الاستجابة المتدفّقة أحداث Server-Sent Events (SSE) وتتألف من خطوات وأحداث، على سبيل المثال:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

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

تعتمد نماذج Gemini التفكير الديناميكي تلقائيًا، ما يعني أنّها تعدّل تلقائيًا مقدار الجهد المبذول في الاستدلال استنادًا إلى مدى تعقيد الطلب. يمكنك التحكّم في هذا السلوك باستخدام المَعلمة `thinking_level`.

| الطراز | التفكير التلقائي | المستويات المتاحة |
| --- | --- | --- |
| gemini-3.6-flash | مفعَّل (متوسط) | الحد الأدنى، منخفض، متوسط، مرتفع |
| gemini-3.5-flash-lite | مفعَّل (بحدّ أدنى) | الحد الأدنى، منخفض، متوسط، مرتفع |
| gemini-3.1-pro-preview | مفعَّل (عالي) | منخفض، متوسط، مرتفع |
| gemini-3.1-flash-lite-image | مفعَّل (بحدّ أدنى) | الحد الأدنى، الحد الأقصى |
| gemini-3-flash-preview | مفعَّل (عالي) | الحد الأدنى، منخفض، متوسط، مرتفع |
| gemini-3-pro-preview | مفعَّل (عالي) | منخفض، مرتفع |
| gemini-3.5-flash | مفعَّل (متوسط) | الحد الأدنى، منخفض، متوسط، مرتفع |
| gemini-2.5-pro | مفعّل | منخفض، متوسط، مرتفع |
| gemini-2.5-flash | مفعّل | منخفض، متوسط، مرتفع |
| gemini-2.5-flash-lite | إيقاف | منخفض، متوسط، مرتفع |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## توقيعات الأفكار

توقيعات الأفكار هي تمثيلات مشفّرة لعمليات الاستدلال الداخلية التي يجريها النموذج. ويجب أن تحافظ على استمرارية عملية الاستدلال في المحادثات المترابطة.

تسهّل Interactions API التعامل مع توقيعات الأفكار مقارنةً بواجهة `generateContent` API.

### وضع الاحتفاظ بالحالة (يُنصح به)

عند استخدام Interactions API في الوضع ذي الحالة (من خلال ضبط `store: true` وتمرير `previous_interaction_id` في الأدوار اللاحقة)، يدير الخادم تلقائيًا حالة المحادثة، بما في ذلك جميع كتل الأفكار والتوقيعات. في هذا الوضع، ليس عليك اتّخاذ أي إجراء بشأن التواقيع. ويتم التعامل معها بالكامل من جهة الخادم.

### وضع عدم الاحتفاظ بالحالة

إذا كنت تدير حالة المحادثة بنفسك (الوضع غير الاحتفاظ بالحالة) وتمرّر السجلّ الكامل للمدخلات والمخرجات في كل طلب:

- **يجب** دائمًا إعادة إرسال جميع كتل `thought` تمامًا كما تم تلقّيها من النموذج.
- **لا** ننصح بإزالة أو تعديل "مكعبات الأفكار" من السجلّ، لأنّها تحتوي على التوقيعات المطلوبة ليواصل النموذج عملية الاستنتاج.
- عند تبديل النماذج خلال جلسة واحدة، يجب إعادة إرسال كتل الأفكار الخاصة بالنموذج السابق. يتولّى الخلفية إدارة التوافق.

## الأسعار

عند تفعيل ميزة "التفكير"، يكون سعر الردّ هو مجموع الرموز المميزة للناتج والرموز المميزة للتفكير. يمكنك الحصول على إجمالي عدد الرموز المميزة التي تم إنشاؤها من حقل `total_thought_tokens`.

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

تنشئ نماذج التفكير أفكارًا كاملة لتحسين جودة الرد النهائي، ثم تعرض [ملخّصات](#summaries) لتقديم نظرة ثاقبة حول عملية التفكير. تستند الأسعار إلى الرموز المميزة الكاملة التي يحتاج النموذج إلى إنشائها، على الرغم من أنّ الملخّص فقط هو الناتج من واجهة برمجة التطبيقات.

يمكنك الاطّلاع على مزيد من المعلومات حول الرموز المميزة في دليل [احتساب الرموز المميزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

## أفضل الممارسات

استخدِم نماذج التفكير بكفاءة من خلال اتّباع الإرشادات التالية.

- **مراجعة الاستدلال**: يمكنك تحليل ملخّصات الأفكار لفهم أسباب الرفض وتحسين الطلبات.
- **التحكّم في ميزانية التفكير**: اطلب من النموذج التفكير بشكل أقل في النواتج الطويلة لتوفير الرموز المميزة.
- **المهام البسيطة**: استخدام الحد الأدنى من التفكير أو التفكير البسيط لاسترجاع الحقائق أو التصنيف (مثل "أين تأسست DeepMind؟")
- **المهام المعتدلة**: استخدِم التفكير التلقائي لمقارنة المفاهيم أو التفكير الإبداعي (مثلاً، مقارنة السيارات الكهربائية والسيارات الهجينة).
- **المهام المعقّدة**: استخدِم الحدّ الأقصى للتفكير في الترميز المتقدّم أو الرياضيات أو التخطيط المتعدّد الخطوات (مثل حلّ مسائل الرياضيات في مسابقة AIME).

## الخطوات التالية

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar): الردود النصية الأساسية
- [استدعاء الدالة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar): الاتصال بالأدوات
- [دليل Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=ar): ميزات خاصة بالنموذج

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
