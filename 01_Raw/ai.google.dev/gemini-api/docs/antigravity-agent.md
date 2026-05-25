---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar
fetched_at: 2026-05-25T12:56:46.205454+00:00
title: "Antigravity Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Antigravity Agent

‫Antigravity agent هو وكيل مُدار للأغراض العامة على Gemini API. يمنحك طلب بيانات من واجهة برمجة التطبيقات وكيلاً يمكنه الاستدلال وتنفيذ الرموز البرمجية وإدارة الملفات وتصفُّح الويب داخل وضع الحماية الآمن الخاص بك على Linux الذي تستضيفه Google.

يستند هذا الوكيل إلى Gemini 3.5 Flash ويستخدم نفس مجموعة الأدوات التي تستخدمها بيئة التطوير المتكاملة Antigravity IDE. يمكنك الوصول إليه من خلال [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) و[Google AI Studio](https://aistudio.google.com?hl=ar).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## الإمكانات

يمكن لكل طلب توفير وضع حماية على Linux وبدء حلقة استخدام الأدوات. يخطّط الوكيل ويتخذ إجراءات ويراقب النتائج ويكرّر العملية إلى أن تكتمل المهمة.

- **تنفيذ الرموز البرمجية:** يمكنك تشغيل أوامر Bash وPython وNode.js. وتثبيت الحِزم وتشغيل الاختبارات وإنشاء التطبيقات.
- **إدارة الملفات:** يمكنك قراءة الملفات وكتابتها وتعديلها والبحث عنها وإدراجها في وضع الحماية. وتظل الملفات محفوظة خلال التفاعلات.
- **الوصول إلى الويب:** يمكنك استخدام "بحث Google" وجلب عناوين URL للبيانات.
- **ضغط السياق:** يتم ضغط السياق تلقائيًا (عند بلوغ عدد الرموز 135 ألفًا تقريبًا) لدعم الجلسات الطويلة المتعددة بدون فقدان السياق أو بلوغ الحدود القصوى للرموز.

يمكنك الاطّلاع على دليل البدء السريع [هنا](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar) لمعرفة كيفية استخدام المحادثات المتعددة والبيانات المتدفقة.

## الأدوات المتوافقة

يتمكّن الوكيل تلقائيًا من الوصول إلى `code_execution` و`google_search` و`url_context`. ويتم تفعيل أدوات نظام الملفات تلقائيًا عند تحديد المَعلمة `environment`. لا تحتاج إلى تحديد المَعلمة `tools` إلا عند تخصيص المجموعة التلقائية أو تقييدها.

| الأداة | قيمة النوع | الوصف |
| --- | --- | --- |
| تنفيذ الرموز البرمجية | `code_execution` | يمكنك تشغيل أوامر shell (مثل bash وPython وNode) مع تسجيل الإخراج العادي/الأخطاء. |
| بحث Google | `google_search` | يمكنك البحث في شبكة الويب المتاحة للجميع. |
| سياق عنوان URL | `url_context` | يمكنك جلب صفحات الويب وقراءتها. |
| نظام الملفات | *(مفعَّل من خلال `environment`)* | يمكنك قراءة الملفات وكتابتها وتعديلها والبحث عنها وإدراجها في وضع الحماية. لا يتوفّر نوع أداة منفصل، ويتم تفعيلها تلقائيًا عند ضبط `environment`. |

لتقييد الوكيل بأدوات معيّنة، مرِّر الأدوات التي تحتاج إليها فقط:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## الإدخال المتعدد الوسائط

يتوافق Antigravity agent مع الإدخالات المتعددة الوسائط. لا تتوافق هذه الميزة حاليًا إلا مع إدخالات `text` و`image`. يجب تقديم الصور كسلاسل مضمّنة مشفّرة بترميز base64 (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## تخصيص الوكيل

يمكنك توسيع نطاق Antigravity agent من خلال تخصيص التعليمات والأدوات والبيئة. يتوافق الوكيل مع طريقة تخصيص نظام الملفات: يمكنك ربط ملفات مثل `AGENTS.md` للتعليمات والمهارات ضمن `.agents/skills/` مباشرةً في وضع الحماية، أو تمرير الإعدادات المضمّنة في وقت التفاعل. يمكنك تكرار الإعدادات المضمّنة ثم حفظها كوكيل مُدار عندما تكون جاهزًا.

لمعرفة التفاصيل الكاملة حول كيفية إنشاء وكلاء مخصّصين، يُرجى الاطّلاع على مقالة [إنشاء وكلاء مُدارين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar).

## البيئات

ينشئ كل طلب وضع حماية على Linux أو يعيد استخدامه. تتخذ المَعلمة `environment` ثلاثة أشكال:

| الوضعية | الوصف |
| --- | --- |
| `"remote"` | يمكنك توفير وضع حماية جديد بالإعدادات التلقائية. |
| `"env_abc123"` | يمكنك إعادة استخدام بيئة حالية حسب رقم التعريف، مع الاحتفاظ بجميع الملفات والحالة. |
| `{...}` | ‫`EnvironmentConfig` كاملة مع مصادر وقواعد شبكة مخصّصة |

يمكنك الاطّلاع على [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar) لمعرفة التفاصيل حول المصادر (Git وGCS والمضمّنة) والشبكات ودورة الحياة والحدود القصوى للموارد.

## التوفّر والأسعار

يتوفّر Antigravity agent في المعاينة من خلال [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) في Google AI Studio وGemini API.

تستند الأسعار إلى نموذج [الدفع حسب الاستخدام](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#pricing-for-agents) استنادًا إلى رموز نموذج Gemini الأساسي والأدوات التي يستخدمها الوكيل. على عكس طلب المحادثة العادي الذي ينتج عنه ناتج واحد، يكون تفاعل Antigravity عبارة عن سير عمل للوكيل. ويؤدي طلب واحد إلى تشغيل حلقة مستقلة من الاستنتاج وتنفيذ الأدوات وتشغيل الرموز البرمجية وإدارة الملفات.

### التكاليف المقدَّرة

تختلف التكاليف حسب مدى تعقيد المهمة. يحدّد الوكيل بشكل مستقل عدد طلبات الأدوات وعمليات تنفيذ الرموز البرمجية وعمليات الملفات المطلوبة. تستند التقديرات التالية إلى عمليات التشغيل.

| فئة المهمة | رموز الإدخال | رموز الإخراج | التكلفة النموذجية |
| --- | --- | --- | --- |
| **البحث وتجميع المعلومات** | 100 ألف - 500 ألف | 10 آلاف - 40 ألف | 0.30–1.00 دولار أمريكي |
| **إنشاء المستندات والمحتوى** | 100 ألف - 500 ألف | 15 ألف - 50 ألف | 0.30–1.30 دولار أمريكي |
| **تصميم العمليات والأنظمة** | 100 ألف - 400 ألف | 10 آلاف - 30 ألف | 0.25–0.80 دولار أمريكي |
| **معالجة البيانات وتحليلها** | 300 ألف - 3 ملايين | 30 ألف - 150 ألف | 0.70–3.25 دولار أمريكي |

عادةً ما يتم تخزين 50 إلى 70% من رموز الإدخال مؤقتًا. يمكن أن تؤدي عمليات سير عمل الوكيل المعقدة التي تتضمّن العديد من طلبات الأدوات إلى تجميع 3 إلى 5 ملايين رمز في تفاعل واحد، بتكاليف تصل إلى 5 دولارات أمريكية تقريبًا.

**لا يتم تحصيل رسوم** عن **حوسبة البيئة** (وحدة المعالجة المركزية والذاكرة وتنفيذ وضع الحماية) خلال فترة المعاينة.

## القيود

- **حالة المعاينة:** يتوفّر Antigravity agent وInteractions API في المعاينة. وقد تتغيّر الميزات والمخططات.
- **إعدادات الإنشاء غير المتوافقة:** لا تتوافق هذه الميزة مع المَعلمات التالية وتعرض خطأ 400: `temperature` و`top_p` و`top_k` و`stop_sequences` و`max_output_tokens`.
- **ناتج منظَّم:** لا يتوافق Antigravity agent مع النواتج المنظَّمة.
- **الأدوات غير المتاحة:** لا تتوافق هذه الميزة بعد مع `file_search` و`computer_use` و`google_maps` و`function_calling` و`mcp`.
- **أداة نظام الملفات:** لا تتوفّر حاليًا أداة نظام الملفات. وهي جزء من `environment`.
- **الخلفية:** لا يتيح الوكيل استخدام `background=True` ويتطلب `store=True`.
- **الأنواع المتعددة الوسائط غير المتوافقة** لا تتوافق هذه الميزة حاليًا مع إدخالات الصوت والفيديو والمستندات. ويُسمح فقط بالنص والصورة.

## الخطوات التالية

- [دليل البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): المحادثات المتعددة والبيانات المتدفقة
- [إنشاء وكلاء مخصّصين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar): التعليمات والمهارات المخصّصة وحفظ الوكلاء
- [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): إعداد وضع الحماية والمصادر والشبكات
- ‫[Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar): مهام البحث الطويلة
- ‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar): واجهة برمجة التطبيقات الأساسية

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-20 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-20 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
