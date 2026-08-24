---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=ar
fetched_at: 2026-08-24T02:29:52.329794+00:00
title: "\u0623\u062e\u0637\u0627\u0621 \u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# أخطاء واجهة برمجة التطبيقات

تقدّم هذه الصفحة مرجعًا لرموز أخطاء الخلفية التي تعرضها واجهة برمجة التطبيقات `GenerateContent`، وتصف تنسيق استجابة أخطاء gRPC، وتوفّر خطوات تحديد المشاكل وحلّها.

## رموز أخطاء HTTP

يسرد الجدول التالي رموز أخطاء الخلفية الشائعة، وتفسيرات لأسبابها، والحلول المقترَحة:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **رمز HTTP** | **الحالة** | **الوصف** | **مثال** | **Solution** |
| 400 | INVALID\_ARGUMENT | تمت صياغة نص الطلب بشكل غير صحيح. | هناك خطأ إملائي أو حقل مطلوب مفقود في طلبك. | راجِع [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api?hl=ar) لمعرفة تنسيق الطلب والأمثلة والإصدارات المتوافقة. يمكن أن يؤدي استخدام ميزات من إصدار أحدث من واجهة برمجة التطبيقات مع نقطة نهاية أقدم إلى حدوث أخطاء. |
| 400 | FAILED\_PRECONDITION | المستوى المجاني من Gemini API غير متاح في بلدك. يُرجى تفعيل الفوترة في مشروعك في Google AI Studio. | أنت تُرسِل طلبًا في منطقة لا يتوفّر فيها المستوى المجاني، ولم تفعِّل الفوترة في مشروعك في Google AI Studio. | لاستخدام Gemini API، عليك إعداد خطة مدفوعة باستخدام [Google AI Studio](https://aistudio.google.com/apikey?hl=ar). |
| 403 | PERMISSION\_DENIED | لا يملك مفتاح واجهة برمجة التطبيقات الأذونات المطلوبة. | أنت تستخدم مفتاح واجهة برمجة تطبيقات غير صحيح، وتحاول استخدام نموذج تم ضبطه بدون إجراء [المصادقة بشكل صحيح](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ar). | تأكَّد من ضبط مفتاح واجهة برمجة التطبيقات ومنحه إذن الوصول المناسب. وتأكَّد من إجراء المصادقة بشكل صحيح لاستخدام النماذج التي تم ضبطها. |
| 404 | NOT\_FOUND | لم يتم العثور على المصدر المطلوب. | لم يتم العثور على ملف صورة أو ملف صوت أو ملف فيديو تمت الإشارة إليه في طلبك. | تأكَّد من أنّ جميع المَعلمات في طلبك صالحة لإصدار واجهة برمجة التطبيقات. |
| 429 | RESOURCE\_EXHAUSTED | تجاوزت أحد الحدود القصوى لمعدّل الطلبات في واجهة برمجة التطبيقات (الطلبات في الدقيقة أو الرموز المميّزة في الدقيقة أو الطلبات في اليوم أو الإنفاق وما إلى ذلك). | أنت تُرسِل عددًا كبيرًا جدًا من الطلبات، أو تستخدم عددًا كبيرًا جدًا من الرموز المميّزة، أو تتجاوز الحدود المستندة إلى الإنفاق لسجلّ الفوترة والمستوى في حسابك. | تأكَّد من أنّك ضمن [الحدود القصوى لمعدّل الطلبات](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar) في النموذج. انتظِر وأعِد المحاولة بعد فترة قصيرة. قلِّل معدّل طلباتك أو حجمها. [اطلب زيادة الحدّ الأقصى لمعدّل الطلبات](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar#request-rate-limit-increase) إذا لزم الأمر. |
| 499 | CANCELLED | تم إلغاء العملية، وعادةً ما يكون ذلك من قِبل المتصل. | أغلق العميل الاتصال قبل أن تتمكّن واجهة برمجة التطبيقات من إنهاء الردّ. | تأكَّد مما إذا كان العميل أو البنية الأساسية للشبكة يغلقان الاتصال قبل الأوان (على سبيل المثال، بسبب انتهاء مهلة من جهة العميل). |
| 500 | INTERNAL | حدث خطأ غير متوقَّع من جانب Google. | سياق الإدخال طويل جدًا. | راجِع [صفحة حالة Gemini API](https://aistudio.google.com/status?hl=ar) لمعرفة أي حوادث مستمرة. قلِّل سياق الإدخال أو انتقِل مؤقتًا إلى نموذج آخر (على سبيل المثال، من Gemini 2.5 Pro إلى Gemini 2.5 Flash) وتحقَّق مما إذا كان ذلك يحل المشكلة. أو انتظِر قليلاً وأعِد محاولة طلبك. إذا استمرت المشكلة بعد إعادة المحاولة، يُرجى الإبلاغ عنها باستخدام الزر **إرسال ملاحظات** في Google AI Studio. |
| 503 | UNAVAILABLE | قد يكون الخادم محمّلاً بشكل مؤقت أو غير متاح. | توشك الخدمة مؤقتًا على استنفاد سعتها. | راجِع [صفحة حالة Gemini API](https://aistudio.google.com/status?hl=ar) لمعرفة أي حوادث مستمرة. انتقِل مؤقتًا إلى نموذج آخر (على سبيل المثال، من Gemini 2.5 Pro إلى Gemini 2.5 Flash) وتحقَّق مما إذا كان ذلك يحل المشكلة. أو انتظِر قليلاً وأعِد محاولة طلبك. إذا استمرت المشكلة بعد إعادة المحاولة، يُرجى الإبلاغ عنها باستخدام الزر **إرسال ملاحظات** في Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | يتعذّر على الخدمة إنهاء المعالجة خلال المهلة المحدّدة. | الطلب (أو السياق) كبير جدًا بحيث لا يمكن معالجته في الوقت المناسب. | اضبط قيمة أكبر لـ "المهلة" في طلب العميل لتجنُّب هذا الخطأ. |

## تنسيق استجابة الخطأ

عندما يفشل طلب `GenerateContent`، تضبط واجهة برمجة التطبيقات رمز حالة HTTP (مثل `400 Bad Request` أو `403 Forbidden` أو `429 Too Many Requests`) وتعرض نص استجابة JSON يحتوي على تفاصيل حالة gRPC:

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
| `details` | صفيف | سياق إضافي للخطأ، مثل `ErrorInfo` أو `LocalizedMessage` |

## الخطوات التالية

- [تحديد المشاكل وحلّها في واجهة برمجة التطبيقات](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ar): حلّ المشاكل الشائعة وسيناريوهات الأخطاء
- [الحدود القصوى لمعدّل الطلبات](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar): التعرّف على الحدود القصوى للطلبات وكيفية التعامل مع الحصص

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
