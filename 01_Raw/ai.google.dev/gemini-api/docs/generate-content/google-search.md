---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=ar
fetched_at: 2026-07-06T05:15:56.678492+00:00
title: "\u0627\u0644\u0623\u0633\u0627\u0633\u064a\u0627\u062a \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \"\u0628\u062d\u062b Google\" \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الأساسيات باستخدام "بحث Google"

تتيح ميزة "تحديد المصدر من خلال بحث Search" ربط نموذج Gemini بمحتوى الويب في الوقت الفعلي، وهي تعمل بجميع اللغات المتاحة. يتيح ذلك لـ Gemini تقديم إجابات أكثر دقة والإشارة إلى مصادر يمكن التحقّق منها بعد تاريخ آخر تحديث للبيانات.

تساعدك عملية التأسيس على إنشاء تطبيقات يمكنها إجراء ما يلي:

- **زيادة الدقة الواقعية:** يمكنك تقليل حالات الهلوسة في النموذج من خلال الاستناد إلى معلومات واقعية عند تقديم الردود.
- **الوصول إلى معلومات في الوقت الفعلي:** الإجابة عن أسئلة حول الأحداث والمواضيع الحديثة
- **تضمين اقتباسات:** يمكنك كسب ثقة المستخدمين من خلال عرض مصادر المعلومات التي يقدّمها النموذج.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

يمكنك الاطّلاع على مزيد من المعلومات من خلال تجربة [دفتر ملاحظات "أداة البحث"](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).

## طريقة عمل ميزة "تحديد المصدر من خلال بحث Google"

عند تفعيل أداة `google_search`، يتعامل النموذج مع سير العمل الكامل
للبحث عن المعلومات ومعالجتها والاقتباس منها تلقائيًا.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ar)

1. **طلب المستخدم:** يرسل تطبيقك طلب المستخدم إلى Gemini API مع تفعيل الأداة `google_search`.
2. **تحليل الطلب:** يحلّل النموذج الطلب ويحدّد ما إذا كان بإمكان &quot;بحث Google&quot; تحسين الإجابة.
3. **بحث Google:** إذا لزم الأمر، ينشئ النموذج تلقائيًا طلب بحث واحدًا أو أكثر وينفّذها.
4. **معالجة نتائج البحث:** يعالج النموذج نتائج البحث، ويلخّص المعلومات، ويصيغ ردًا.
5. **الردّ المستند إلى معلومات موثوقة:** تعرض واجهة برمجة التطبيقات ردًا نهائيًا سهل الاستخدام يستند إلى نتائج البحث. يتضمّن هذا الرد الإجابة النصية التي قدّمها النموذج و`groundingMetadata` مع طلبات البحث ونتائج الويب والاقتباسات.

## فهم الردّ المستند إلى معلومات أساسية

عندما يتم إنشاء ردّ بنجاح، يتضمّن الردّ الحقل `groundingMetadata`. هذه البيانات المنظَّمة ضرورية للتحقّق من صحة الادعاءات وتوفير تجربة اقتباس غنية في تطبيقك.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

تعرض Gemini API المعلومات التالية مع `groundingMetadata`:

- ‫`webSearchQueries` : مصفوفة طلبات البحث المستخدَمة. ويفيد ذلك في تصحيح الأخطاء وفهم عملية الاستدلال في النموذج.
- ‫`searchEntryPoint` : يحتوي على HTML وCSS لعرض &quot;اقتراحات البحث&quot; المطلوبة. تتوفّر متطلبات الاستخدام الكاملة في [بنود الخدمة](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-search).
- ‫`groundingChunks` : مصفوفة من العناصر التي تحتوي على مصادر الويب (`uri` و`title`).
- ‫`groundingSupports` : مصفوفة من الأجزاء لربط ردّ النموذج `text` بالمستندات المصدر في `groundingChunks`. يربط كل جزء نصًا `segment` (محدّدًا بواسطة `startIndex` و`endIndex`) بواحد أو أكثر من `groundingChunkIndices`. هذا هو المفتاح لإنشاء استشهادات مضمّنة.

يمكن أيضًا استخدام ميزة "تحديد المصدر من خلال "بحث Search"" مع [أداة السياق في عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) لتحديد المصدر في البيانات العلنية على الويب وعناوين URL المحدّدة التي تقدّمها.

## تحديد مصادر الأعمال من خلال اقتباسات مضمّنة

تعرض واجهة برمجة التطبيقات بيانات الاقتباس المنظَّمة، ما يمنحك تحكّمًا كاملاً في طريقة عرض المصادر في واجهة المستخدم. يمكنك استخدام الحقلَين `groundingSupports` و`groundingChunks` لربط عبارات النموذج مباشرةً بمصادرها. في ما يلي نمط شائع لمعالجة البيانات الوصفية من أجل إنشاء رد يتضمّن اقتباسات مضمّنة قابلة للنقر.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

ستبدو الإجابة الجديدة مع الاقتباسات المضمّنة على النحو التالي:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## الأسعار

عند استخدام ميزة "تحديد المصدر من خلال بحث Google" مع Gemini 3، يتم تحصيل رسوم من مشروعك مقابل كل طلب بحث يقرّر النموذج تنفيذه. إذا قرر النموذج تنفيذ طلبات بحث متعددة للإجابة عن طلب واحد (على سبيل المثال، البحث عن `"UEFA Euro 2024 winner"` و`"Spain vs England Euro 2024 final
score"` ضمن طلب واحد من واجهة برمجة التطبيقات)، سيتم احتساب ذلك كاستخدامَين قابلَين للفوترة للأداة لهذا الطلب. لأغراض الفوترة، نتجاهل طلبات البحث الفارغة على الويب عند احتساب طلبات البحث الفريدة. لا ينطبق نموذج الفوترة هذا إلا على نماذج Gemini 3، وعند استخدام ميزة &quot;الاستناد إلى البحث&quot; مع Gemini 2.5 أو النماذج الأقدم، تتم فوترة مشروعك لكل طلب.

للحصول على معلومات مفصّلة حول الأسعار، يُرجى الاطّلاع على [صفحة أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

يمكنك الاطّلاع على الإمكانات الكاملة في صفحة [النظرة العامة على الطراز](https://ai.google.dev/gemini-api/docs/models?hl=ar).

| الطراز | تحديد المصدر من خلال "بحث Search" |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| معاينة Gemini 3.1 Flash Image | ✔️ |
| معاينة Gemini 3.1 Pro | ✔️ |
| معاينة الصور في Gemini 3 Pro | ✔️ |
| معاينة Gemini 3 Flash | ✔️ |
| معاينة Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## مجموعات الأدوات المتوافقة

يمكنك استخدام ميزة تحديد المصدر من خلال "بحث Search" مع أدوات أخرى، مثل [تطبيق الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)، لتشغيل حالات استخدام أكثر تعقيدًا.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "تحديد المصدر من خلال بحث Google") والأدوات المخصّصة (استدعاء الدوال البرمجية). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## الخطوات التالية

- جرِّب [كتاب الطبخ الخاص بميزة تحديد المصدر من خلال "بحث Search" في Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).
- تعرَّف على الأدوات الأخرى المتاحة، مثل [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).
- [كيفية إضافة عناوين URL محدّدة إلى الطلبات باستخدام أداة "سياق عنوان URL"](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-23 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-23 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
