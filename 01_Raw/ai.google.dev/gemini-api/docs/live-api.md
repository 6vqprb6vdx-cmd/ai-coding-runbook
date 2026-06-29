---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=ar
fetched_at: 2026-06-29T05:25:33.252983+00:00
title: "\u0646\u0638\u0631\u0629 \u0639\u0627\u0645\u0629 \u0639\u0644\u0649 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# نظرة عامة على Gemini Live API

تتيح Live API التفاعل مع Gemini في الوقت الفعلي باستخدام الصوت والصورة وبزمن انتقال منخفض، إذ تعالج هذه الواجهة تدفقات مستمرة من الصوت والصور والنصوص لتقديم ردود فورية شبيهة بالردود البشرية، ما يتيح للمستخدمين الاستفادة من تجربة محادثة طبيعية.

![نظرة عامة على Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=ar)

[تجربة Live API في Google AI Studiomic](https://aistudio.google.com/live?hl=ar)
[استنساخ تطبيقات نموذجية من GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[استخدام مهارات وكيل الترميزterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)

## حالات الاستخدام

يمكن استخدام Live API لإنشاء وكلاء صوتيين في الوقت الفعلي لمجموعة متنوعة من المجالات، بما في ذلك:

- **التجارة الإلكترونية والبيع بالتجزئة:** مساعدو التسوّق الذين يقدّمون اقتراحات مخصّصة ووكلاء الدعم الذين يحلّون مشاكل العملاء
- **الألعاب:** شخصيات تفاعلية لا يتحكّم بها اللاعب (NPC) ومساعدون داخل اللعبة وترجمة في الوقت الفعلي للمحتوى داخل اللعبة
- **واجهات الجيل التالي:** تجارب مزوّدة بإمكانية استخدام الصوت والفيديو في الروبوتات والنظارات الذكية والمركبات
- **الرعاية الصحية:** مرافقون صحيون لتقديم الدعم للمرضى وتثقيفهم
- **الخدمات المالية:** مستشارون يعملون بالذكاء الاصطناعي لإدارة الثروات وتقديم إرشادات بشأن الاستثمار
- **التعليم:** مرشدون ومرافقون للمتعلّمين يستندون إلى الذكاء الاصطناعي ويقدّمون تعليمات وملاحظات مخصّصة.
- **الترجمة والتعريب:** ترجمة المحادثات الشفهية في الوقت الفعلي وبزمن استجابة منخفض، ما يتيح التواصل بسلاسة بلغات متعددة

## الميزات الرئيسية

تقدّم Live API مجموعة شاملة من الميزات لإنشاء وكلاء صوتيين فعّالين:

- [**دعم اللغات المتعددة**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#supported-languages):
  تحدّث بـ 70 لغة مدعومة.
- [**المقاطعة**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#interruptions):
  يمكن للمستخدمين مقاطعة النموذج في أي وقت لإجراء تفاعلات سريعة الاستجابة.
- [**استخدام الأدوات**](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar):
  يدمج هذا الخيار أدوات مثل ميزة &quot;طلب تنفيذ وظيفة&quot; و&quot;بحث Google&quot; لإجراء تفاعلات ديناميكية.
- [**تحويل الصوت إلى نص**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#audio-transcription):
  توفّر هذه الميزة نصوصًا لبيانات أدخلها المستخدم ومخرجات النموذج.
- [**الاستجابة الصوتية الاستباقية**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#proactive-audio):
  تتيح لك التحكّم في وقت استجابة النموذج والسياقات التي يستجيب فيها.
- [**حوار تفاعلي تعاطفي**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#affective-dialog):
  يعدّل أسلوب الرد ونبرته ليناسبا تعبيرات المستخدم.
- [**الترجمة المباشرة**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ar):
  ترجمة الصوت في الوقت الفعلي بأكثر من 70 لغة

## المواصفات الفنية

يوضّح الجدول التالي المواصفات الفنية لواجهة Live API:

| الفئة | التفاصيل |
| --- | --- |
| طُرق الإدخال | الصوت (صوت PCM خام بمعدل 16 بت، و16 كيلوهرتز، وترتيب وحدات البايت الأصغر أولاً)، والصور (JPEG <= 1 لقطة في الثانية)، والنص |
| طُرق الإخراج | الصوت (صوت PCM خام بمعدل 16 بت، و24 كيلوهرتز، وترتيب وحدات البايت الأصغر أولاً) |
| البروتوكول | اتصال WebSocket ذو الحالة (WSS) |

## اختيار طريقة التنفيذ

عند الدمج مع Live API، عليك اختيار أحد أساليب التنفيذ التالية:

- **من الخادم إلى الخادم**: يتصل الخلفية بواجهة Live API باستخدام [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). وعادةً، يرسل العميل بيانات البث (الصوت والفيديو والنص) إلى الخادم، الذي يعيد توجيهها إلى Live API.
- **من العميل إلى الخادم**: يتصل الرمز البرمجي للواجهة الأمامية مباشرةً بواجهة برمجة التطبيقات Live API
  باستخدام [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) لبث البيانات، مع تجاوز الخلفية.

للحد من المخاطر الأمنية.

## البدء

اختَر الدليل الذي يتوافق مع بيئة التطوير:

التتبُّع من خادم إلى خادم

### [برنامج تعليمي حول حزمة تطوير البرامج (SDK) الخاصة بالذكاء الاصطناعي التوليدي](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ar)

يمكنك الربط بواجهة Gemini Live API باستخدام حزمة GenAI SDK لإنشاء تطبيق متعدّد الوسائط في الوقت الفعلي مع خادم خلفي بلغة Python.

من العميل إلى الخادم

### [برنامج تعليمي حول WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ar)

يمكنك الربط بواجهة Gemini Live API باستخدام WebSockets لإنشاء تطبيق متعدّد الوسائط في الوقت الفعلي مع واجهة أمامية JavaScript ورموز مميّزة مؤقتة.

مجموعة أدوات تطوير الوكيل

### [برنامج تعليمي حول "حزمة تطوير التطبيقات لنظام Android"](https://google.github.io/adk-docs/streaming/)

إنشاء وكيل واستخدام ميزة "البث المباشر" في Agent Development Kit (ADK) لتفعيل التواصل الصوتي والمرئي

## عمليات الدمج مع الشركاء

لتسهيل عملية تطوير تطبيقات الصوت والفيديو في الوقت الفعلي، يمكنك استخدام عملية دمج تابعة لجهة خارجية تتوافق مع واجهة برمجة التطبيقات Gemini Live عبر WebRTC أو WebSockets.

[LiveKit

استخدام Gemini Live API مع LiveKit Agents](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

إنشاء روبوت دردشة بالذكاء الاصطناعي في الوقت الفعلي باستخدام Gemini Live وPipecat](https://docs.pipecat.ai/guides/features/gemini-live)
[‫Fishjam من Software Mansion

يمكنك إنشاء تطبيقات لبث الفيديو المباشر والصوت باستخدام Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[وكلاء Vision حسب البث

يمكنك إنشاء تطبيقات ذكاء اصطناعي للصوت والفيديو في الوقت الفعلي باستخدام Vision Agents.](https://visionagents.ai/integrations/gemini)
[Voximplant

ربط المكالمات الواردة والصادرة بواجهة برمجة التطبيقات Live API باستخدام Voximplant](https://voximplant.com/products/gemini-client)
[Agora

يمكنك إنشاء تطبيقات ذكاء اصطناعي حوارية في الوقت الفعلي باستخدام Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

ابدأ استخدام Gemini Live API من خلال Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
