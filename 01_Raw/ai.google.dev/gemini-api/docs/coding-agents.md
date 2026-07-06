---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar
fetched_at: 2026-07-06T05:17:49.689413+00:00
title: "\u0625\u0639\u062f\u0627\u062f \u0645\u0633\u0627\u0639\u062f \u0627\u0644\u062a\u0631\u0645\u064a\u0632 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini MCP \u0648\"\u0627\u0644\u0645\u0647\u0627\u0631\u0627\u062a\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إعداد مساعد الترميز باستخدام Gemini MCP و"المهارات"

مساعدو الترميز بالذكاء الاصطناعي فعّالون ولكن لديهم قيود، إذ تتوقف بيانات التدريب عند تاريخ معيّن، ولا تتضمّن الميزات والتغييرات الجديدة في واجهة برمجة التطبيقات. بدون الوصول إلى مستندات Gemini المحدّدة، قد يقترح الوكلاء أنماطًا عامة بدلاً من الأساليب المحسّنة.

للحفاظ على تحديث مساعد الترميز بما يتناسب مع Gemini API المتطورة واستخدامها المقترَح، ننصحك بإعداد **Gemini Docs MCP** وتحسين بيئتك باستخدام **مهارات Gemini API**. على الرغم من إمكانية استخدام هذه الأدوات بشكلٍ مستقل، تم تصميمها للعمل معًا لتوفير تغطية كاملة.

## ربط Gemini Docs MCP

تستضيف Gemini خادمًا عامًا لبروتوكول سياق النموذج (MCP) على `https://gemini-api-docs-mcp.dev`. يضمن ربط وكيل الترميز بهذا الخادم وصول جميع طلبات البحث إلى أحدث واجهات برمجة التطبيقات وتعديلات الرموز البرمجية وأمثلة الإعدادات المثالية.

نفِّذ الأمر التالي في الوحدة الطرفية للوكيل أو في جذر المشروع لتثبيت الخادم:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

يضيف هذا الخادم دالة `search_documentation` يمكن لوكيلك استخدامها لاسترداد تعريفات واجهة برمجة التطبيقات وأنماط التكامل في الوقت الفعلي من ملفات مستندات Gemini الرسمية.

## إضافة مهارات تطوير واجهة برمجة التطبيقات

توفّر المهارات **قواعد وأفضل الممارسات مضمّنة** (مثل فرض إصدارات حزمة SDK الصحيحة وإصدارات النموذج الحالية) مباشرةً في سياق مساعدك. تعمل المهارة مع خدمة Gemini Docs MCP: إذا ثبّتَ كلاً منهما، تستخدم المهارة خدمة MCP للوصول إلى المستندات، ولكن حتى بدون تثبيت MCP، ستسترد المهارة ملف `llms.txt` من `ai.google.dev` كحلّ احتياطي.

لتثبيت هذه المهارات، يمكنك استخدام إحدى الأدوات المتوافقة التالية. يتم توفير تعليمات التثبيت لكلتا الأداتَين أسفل كل وحدة مهارة:

- **[skills.sh](https://skills.sh)**: ننصحك باستخدامها. المعيار المفتوح لسلوكيات الوكلاء المحمولة
- **[Context7](https://context7.com)**: متوافقة مع المستخدمين الذين يستخدمون حاليًا المنظومة المتكاملة Context7

### ‫gemini-api-dev

المهارة الأساسية لتطوير Gemini للأغراض العامة توفّر هذه المهارة مستندات وأفضل الممارسات لما يلي:

- توجيه الطلبات إلى النماذج الحالية (مثل Gemini 3.1 Pro/Flash) وتجنُّب النماذج التي تم إيقافها
- إنشاء الطلبات المتعددة الوسائط واستدعاء الدوال والنتائج المنظَّمة وأنماط التكامل الشائعة

#### التثبيت باستخدام skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### التثبيت باستخدام Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

مهارة لإنشاء تطبيقات ذكاء اصطناعي محادثة في الوقت الفعلي باستخدام Gemini Live API توفّر هذه المهارة مستندات وأفضل الممارسات لما يلي:

- اتصالات WebSocket للبث منخفض وقت الاستجابة
- بث الصوت والفيديو والنص
- رصد النشاط الصوتي ودعم المقاطعة

#### التثبيت باستخدام skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### التثبيت باستخدام Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### ‫gemini-interactions-api

مهارة لإنشاء تطبيقات باستخدام الـ
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar). ‫Interactions API هي واجهة موحّدة للتفاعل مع نماذج Gemini والوكلاء، وهي مصمّمة للتطبيقات التي تعتمد على الوكلاء. تغطّي هذه المهارة ما يلي:

- إنشاء النصوص والمحادثات المترابطة والبث
- استدعاء الدوال والنتائج المنظَّمة وإنشاء الصور
- التنفيذ في الخلفية ووكلاء Deep Research
- إدارة حالة المحادثة من جهة الخادم
- أنماط حزمة SDK في Python وTypeScript

#### التثبيت باستخدام skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### التثبيت باستخدام Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## التحقق من التثبيت

بعد التثبيت، تأكَّد من أنّ مساعد الترميز يمكنه الاتصال بخادم Gemini Docs MCP واستخدام المهارات التي ثبّتها.

### 1. التحقّق من سلوك الوكيل

الطريقة الأكثر موثوقية للتحقّق هي طرح سؤال فني على وكيلك حول Gemini API.

**الطلب:** "كيف يمكنني استخدام ميزة تخزين السياق مؤقتًا مع Gemini API؟"

سيؤدي الإعداد الناجح إلى ما يلي:

- **توفير رمز دقيق**: يمكنك الرجوع إلى طرق Gemini المحدّدة، مثل `cacheContent` أو `cachedContents.create` من أحدث نقاط النهاية.
- **استخدام أداة MCP**: يمكنك التأكّد من أنّها متصلة **بخادم Gemini Docs MCP** أو تستخدم أداة `search_documentation` لاسترداد البيانات.
- **استدعاء المهارات المحمَّلة**: يمكنك عرض مؤشر يشير إلى أنّه "يستخدم المهارة: gemini-api-dev" (إذا كان يعتمد على برنامج تضمين ثانوي).

### 2. التحقّق من البيانات والأدوات

إذا قدّم الوكيل إجابة عامة، استخدِم أوامر Discovery أو Status المحدّدة لبيئتك للتحقّق من تحميل Docs MCP أو المهارة في الذاكرة.

| البيئة | التحقّق من MCP | التحقّق من المهارات |
| --- | --- | --- |
| ‫**Claude Code** | اكتب `/mcp` في الوحدة الطرفية لعرض الخوادم النشطة وأدوات `search_documentation`. | اكتب `/skills` في الوحدة الطرفية لعرض جميع البيانات النشطة. |
| ‫**Cursor** | انتقِل إلى **الإعدادات > الميزات > MCP**. تأكَّد من أنّ الخادم "متصل". | افتح **الإعدادات > القواعد**. تأكَّد من ظهور المهارة ضمن "يقرّر الوكيل". |
| **Antigravity** | راجِع الشريط الجانبي **التخصيصات > الاتصالات** لمعرفة حالة MCP. | اكتب `/skills list` أو راجِع الشريط الجانبي **التخصيصات > القواعد**. |
| ‫**Gemini CLI** | نفِّذ `gemini mcp list` أو استخدِم `/mcp list`. | نفِّذ `gemini skills list` أو استخدِم أمر يبدأ بشرطة مائلة `/skills` أثناء الجلسة. |
| ‫**Copilot** | اكتب `@gemini /mcp` لعرض موصِّلات البيانات النشطة. | اكتب `@gemini /skills` (أو `/skills`) لعرض الإضافات النشطة. |

## تحديد المشاكل وحلّها

إذا كان وكيلك يقدّم معلومات عامة فقط أو لا يتعرّف على طرق Gemini المحدّدة، تحقَّق مما يلي:

### لم يعثر الوكيل على المهارة

تُنشئ معظم الوكلاء فهرسًا للمهارات عند بدء التشغيل فقط.

**الحلّ:** أعِد تشغيل بيئة IDE (‫Cursor/VS Code) بالكامل أو اخرج من الوكيل المستند إلى الوحدة الطرفية (‫Claude Code) وأعِد فتحه.

### تعارض عالمي مقابل تعارض محلي

إذا ثبّتَ المهارة باستخدام العلامة `--global`، قد يتجاهلها وكيلك لصالح القواعد الخاصة بالمشروع.

**الحلّ:** حاوِل تثبيت المهارة مباشرةً في جذر مشروعك بدون العلامة العامة:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## الموارد

- [مهارات Gemini API على GitHub](https://github.com/google-gemini/gemini-skills)
- [‫Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar)
- [البدء](https://ai.google.dev/gemini-api/docs/get-started?hl=ar)
- [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
