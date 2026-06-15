---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ar
fetched_at: 2026-06-15T06:27:37.391874+00:00
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

# التخزين المؤقت للسياق

في سير عمل نموذجي للذكاء الاصطناعي، قد يتم تمرير الرموز المميزة نفسها بشكل متكرر إلى أحد النماذج. توفّر Gemini API التخزين المؤقت الضمني لتحسين الأداء والتكاليف.

## التخزين المؤقت الضمني

يتم تفعيل التخزين المؤقت الضمني تلقائيًا لجميع نماذج Gemini 2.5 والإصدارات الأحدث. ننقل تلقائيًا
عروض التوفير في التكاليف إذا وصل طلبك إلى ذاكرات التخزين المؤقت. ليس عليك اتّخاذ أي إجراء لتفعيل هذه الميزة. يتم إدراج الحد الأدنى لعدد الرموز المميزة للإدخال المطلوب لتخزين السياق مؤقتًا في الجدول التالي لكل نموذج:

| الطراز | الحد الأدنى لعدد الرموز المميزة |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| معاينة Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

لزيادة فرصة حدوث نتيجة ذاكرة التخزين المؤقت الضمنية، اتّبِع الخطوات التالية:

- جرِّب وضع المحتوى الكبير والشائع في بداية طلبك
- محاولة إرسال طلبات تتضمّن بادئة مشابهة خلال فترة زمنية قصيرة

يمكنك الاطّلاع على عدد الرموز المميزة التي تم العثور عليها في ذاكرة التخزين المؤقت في الحقل `usage_metadata` (Python) أو `usageMetadata` (JavaScript) ضمن عنصر الاستجابة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-02 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-02 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
