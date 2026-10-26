---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=ar
fetched_at: 2026-10-26T06:00:38.779886+00:00
title: "\u0623\u062e\u0637\u0627\u0621 \u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# أخطاء واجهة برمجة التطبيقات

تقدّم هذه الصفحة مرجعًا لرموز الأخطاء في الخلفية التي تعرضها واجهة برمجة التطبيقات `GenerateContent`، وتصف تنسيق استجابة الخطأ في gRPC، وتوفّر خطوات لتحديد المشاكل وحلّها.

## رموز الخطأ في بروتوكول HTTP

يسرد الجدول التالي رموز الأخطاء الشائعة في الخلفية، وتفسيرات لأسبابها، والحلول المقترَحة:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **رمز HTTP** | **الحالة** | **الوصف** | **مثال** | **Solution** |
| 400 | INVALID\_ARGUMENT | تمت صياغة نص الطلب بشكل غير صحيح. | هناك خطأ إملائي أو حقل مطلوب لم يتم ملؤه في طلبك. | اطّلِع على [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api?hl=ar) لمعرفة تنسيق الطلب والأمثلة والإصدارات المتوافقة. قد يؤدي استخدام ميزات من إصدار أحدث من واجهة برمجة التطبيقات مع نقطة نهاية قديمة إلى حدوث أخطاء. |
| 400 | FAILED\_PRECONDITION | لا يتوفّر المستوى المجاني من Gemini API في بلدك. يُرجى تفعيل الفوترة في مشروعك على Google AI Studio. | إذا كنت ترسل طلبًا في منطقة لا تتوفّر فيها الفئة المجانية، ولم تفعّل الفوترة في مشروعك في Google AI Studio. | لاستخدام Gemini API، عليك إعداد خطة مدفوعة من خلال [Google AI Studio](https://aistudio.google.com/apikey?hl=ar). |
| 402 | RESOURCE\_EXHAUSTED | نفد رصيد الدفع المُسبَق. | نفدت أرصدة الدفع المُسبق في حساب الفوترة، لذا تتوقف جميع مفاتيح واجهة برمجة التطبيقات المرتبطة بحساب الفوترة هذا عن العمل. | [أضِف رصيدًا](https://ai.google.dev/gemini-api/docs/billing?hl=ar#buy-credits) إلى حساب الفوترة أو فعِّل ميزة [إعادة التعبئة التلقائية](https://ai.google.dev/gemini-api/docs/billing?hl=ar#auto-reload). يُرجى عدم إعادة محاولة إرسال هذا الطلب، لأنّه لن ينجح إلا بعد إضافة رصيد. |
| 403 | PERMISSION\_DENIED | لا يملك مفتاح واجهة برمجة التطبيقات الأذونات المطلوبة، أو أنّ إمكانية وصول مشروعك إلى واجهة برمجة التطبيقات مقيّدة. | أنت تستخدم مفتاح واجهة برمجة تطبيقات خاطئًا أو تم تسريبه، أو مشروعك غير مؤهَّل للاستفادة من المستوى المجاني، أو يتضمّن حساب الفوترة رصيدًا مستحقًا، أو تحاول استخدام نموذج تم ضبطه بدون إجراء [المصادقة المناسبة](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ar). | يُرجى التأكّد من أنّ مفتاح واجهة برمجة التطبيقات صالح ونشط، والتحقّق من حالة الفوترة والمستوى لمشروعك في [Google AI Studio](https://aistudio.google.com/billing?hl=ar)، أو الاطّلاع على مقالة [تحديد المشاكل وحلّها في حال كان المشروع محظورًا أو غير متاح](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ar#project-unavailable). |
| 404 | NOT\_FOUND | لم يتم العثور على المورد المطلوب. | لم يتم العثور على ملف صورة أو صوت أو فيديو تمت الإشارة إليه في طلبك. | يُرجى التحقّق مما إذا كانت جميع المَعلمات في طلبك صالحة لإصدار واجهة برمجة التطبيقات. |
| 429 | RESOURCE\_EXHAUSTED | لقد تجاوزت أحد حدود معدّل الطلبات في واجهة برمجة التطبيقات (عدد الطلبات في الدقيقة أو عدد الرموز المميّزة في الدقيقة أو عدد الطلبات في اليوم أو الإنفاق أو غير ذلك). | أنت ترسل عددًا كبيرًا جدًا من الطلبات، أو تستخدم عددًا كبيرًا جدًا من الرموز المميّزة، أو تتجاوز الحدود القصوى المستندة إلى الإنفاق لسجلّ الفوترة وفئة حسابك. | تأكَّد من أنّك لم تتجاوز [حدود معدّل الاستخدام](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar) للنموذج. يُرجى الانتظار وإعادة المحاولة بعد فترة قصيرة. يُرجى تقليل معدّل الطلبات أو حجمها. [اطلب زيادة الحدّ الأقصى للمعدّل](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar#request-rate-limit-increase) إذا لزم الأمر. |
| 499 | تم إلغاؤها | تم إلغاء العملية، عادةً من قِبل المتصل. | أغلق العميل الاتصال قبل أن تتمكّن واجهة برمجة التطبيقات من إنهاء الردّ. | تحقَّق مما إذا كان العميل أو البنية الأساسية للشبكة يغلقان الاتصال قبل الأوان (على سبيل المثال، بسبب انتهاء مهلة من جهة العميل). |
| 500 | للاستخدام الداخلي | حدث خطأ غير متوقَّع من جانب Google. | سياق الإدخال طويل جدًا. | يُرجى مراجعة [صفحة حالة Gemini API](https://aistudio.google.com/status?hl=ar) لمعرفة أي مشاكل جارية. يمكنك تقليل سياق الإدخال أو التبديل مؤقتًا إلى نموذج آخر (مثل من Gemini 2.5 Pro إلى Gemini 2.5 Flash) ومعرفة ما إذا كان ذلك يحلّ المشكلة. أو يمكنك الانتظار قليلاً وإعادة محاولة إرسال طلبك. إذا استمرت المشكلة بعد إعادة المحاولة، يُرجى الإبلاغ عنها باستخدام الزر **إرسال ملاحظات** في Google AI Studio. |
| 503 | UNAVAILABLE | قد يكون هناك حمل زائد على الخدمة أو قد تكون متوقفة مؤقتًا. | الخدمة غير متاحة مؤقتًا بسبب نفاد السعة. | يُرجى مراجعة [صفحة حالة Gemini API](https://aistudio.google.com/status?hl=ar) لمعرفة أي مشاكل جارية. التبديل مؤقتًا إلى نموذج آخر (مثل من Gemini 2.5 Pro إلى Gemini 2.5 Flash) ومعرفة ما إذا كان يعمل. أو يمكنك الانتظار قليلاً وإعادة محاولة إرسال طلبك. إذا استمرت المشكلة بعد إعادة المحاولة، يُرجى الإبلاغ عنها باستخدام الزر **إرسال ملاحظات** في Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | لا يمكن للخدمة إنهاء المعالجة خلال الموعد النهائي. | طلبك (أو سياقك) كبير جدًا ولا يمكن معالجته في الوقت المناسب. | اضبط مهلة أكبر في طلب العميل لتجنُّب هذا الخطأ. |

## تنسيق الاستجابة للخطأ

عند تعذُّر طلب `GenerateContent`، تضبط واجهة برمجة التطبيقات رمز حالة HTTP (مثل `400 Bad Request` أو `403 Forbidden` أو `429 Too Many Requests`) وتعرض نص استجابة JSON يحتوي على تفاصيل حالة gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `code` | عدد صحيح | رمز حالة HTTP |
| `message` | سلسلة | وصف للخطأ يمكن لشخص عادي قراءته |
| `status` | سلسلة | رمز حالة gRPC في `SCREAMING_CASE` |
| `details` | صفيف | سياق الخطأ الإضافي، مثل `ErrorInfo` أو `LocalizedMessage` |

## الخطوات التالية

- [تحديد مشاكل واجهة برمجة التطبيقات وحلّها](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ar): يمكنك حلّ المشاكل الشائعة وسيناريوهات الأخطاء.
- [حدود المعدّل](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar): تعرَّف على حدود الطلبات ومعالجة الحصص.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-23 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-23 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
