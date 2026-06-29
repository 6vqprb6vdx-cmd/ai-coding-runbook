---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar
fetched_at: 2026-06-29T05:30:41.092995+00:00
title: "\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# واجهة برمجة التطبيقات Interactions API

‫Interactions API هي واجهتنا الجديدة وأبسط طريقة للاستفادة من نماذج Gemini والوكلاء. اعتبارًا من يونيو 2026، ستصبح الواجهة متاحة للجميع وهي الواجهة المقترَحة لجميع المشاريع الجديدة.

على الرغم من أنّها تُعتبر الآن واجهة قديمة، لا تزال واجهة برمجة التطبيقات الأصلية
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar)API
متوافقة تمامًا.

## أهمية استخدام Interactions API

- **إمكانات جديدة جاهزة للاستخدام**: حالة المحادثة الاختيارية من جهة الخادم
  باستخدام `previous_interaction_id`، وخطوات التنفيذ القابلة للمراقبة لأغراض
  تصحيح الأخطاء وعرض واجهة المستخدم، و[التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) للمهام الطويلة الأمد
  باستخدام `background=true`.
- **تكلفة أقل مع معدّلات أعلى لنتائج ذاكرة التخزين المؤقت**: تتيح إدارة الحالة من جهة الخادم تخزين السياق مؤقتًا بشكل أكثر فعالية على مستوى المحادثات المترابطة، ما يقلّل من تكاليف الرموز المميّزة للمحادثات المترابطة.
- **مصمَّمة للنماذج والوكلاء المتقدّمين**: تم تصميمها خصيصًا لنماذج التفكير
  واستخدام الأدوات المتعدّد الخطوات وعمليات الاستدلال المعقّدة، ما يسهّل
  عملية إنشاء التطبيقات التي تستخدم الوكلاء وتصحيح أخطائها وتنظيمها.
- **واجهة برمجة تطبيقات واحدة للنماذج والوكلاء**: واجهة موحّدة لاستدعاء
  نماذج Gemini والوكلاء مباشرةً، مثل Deep Research والوكلاء المُدارين المخصّصين
  ، بدون الحاجة إلى تعلُّم نقاط نهاية أو أنماط منفصلة.
- **مكان إطلاق الميزات الجديدة**: من الآن فصاعدًا، سيتم إطلاق النماذج والإمكانات الجديدة التي تتجاوز عائلة النماذج الأساسية، بالإضافة إلى الإمكانات والأدوات الجديدة التي تستخدم إمكانات بالذكاء الاصطناعي الوكيل على Interactions API.

تخزّن Interactions API الطلبات تلقائيًا حتى تتمكّن من الاستفادة من ميزات إدارة الحالة من جهة الخادم باستخدام `previous_interaction_id`. يمكنك تفعيل السلوك غير المرتبط بحالة المحادثة من خلال ضبط `store=false`. راجِع قسم [الاحتفاظ بالبيانات](#data-storage-retention) لمعرفة
التفاصيل.

## البدء

- **إعداد وكيل الترميز**: يمكنك الاتصال بخادم **Gemini Docs MCP** وتثبيت
  مهارة `gemini-interactions-api` لمنح مساعدك إمكانية الوصول المباشر إلى
  أحدث مستندات المطوّرين وأفضل الممارسات.
  [إعداد وكيل الترميز ←](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)
- **نقل البيانات من `generateContent`**: إذا كان لديك عملية دمج حالية،
  اتّبِع [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar) للانتقال إلى Interactions API.
- **البدء**: يمكنك البدء في استخدام [Interactions API من خلال دليل البدء](https://ai.google.dev/gemini-api/docs/get-started?hl=ar).

### أدلة الميزات

يمكنك استكشاف الإمكانات المحدّدة في Interactions API من خلال هذه الأدلة. يمكنك استخدام الزرّ في هذه الصفحات للتبديل بين generateContent وInteractions API:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar)
- [فهم الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar)
- [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar)
- [معالجة المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar)
- [استدعاء الوظائف](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
- [ناتج منظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)
- [وكيل Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)
- [الاستدلال المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar)
- [الاستدلال حسب الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)

## طريقة عمل Interactions API

تتمحور Interactions API حول مورد أساسي: الـ [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction). يمثّل `Interaction` دورًا كاملاً في محادثة أو مهمة. ويعمل كسجلّ جلسة، يحتوي على السجلّ الكامل لتفاعل ما كسلسلة زمنية من **خطوات التنفيذ**. تتضمّن هذه الخطوات أفكار النموذج واستدعاءات الأدوات ونتائجها من جهة الخادم أو من جهة العميل (مثل `function_call` و`function_result`)، و`model_output` النهائي. يتضمّن المورد المخزَّن (الذي يتم استرداده من خلال `interactions.get`) أيضًا خطوات `user_input` للحصول على السياق الكامل، على الرغم من أنّ استجابة `interactions.create` لا تعرض سوى الخطوات التي تم إنشاؤها بواسطة النموذج.

عند إجراء طلب إلى
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ar#CreateInteraction)، أنت
تنشئ موردًا جديدًا `Interaction`.

### إدارة الحالة من جهة الخادم

يمكنك استخدام `id` لتفاعل مكتمل في طلب لاحق باستخدام
`previous_interaction_id` لمواصلة المحادثة. يستخدم الخادم هذا المعرّف لاسترداد سجلّ المحادثة، ما يوفّر عليك إعادة إرسال سجلّ المحادثة بالكامل.

تحتفظ المَعلمة `previous_interaction_id` بسجلّ المحادثة فقط (المدخلات والمخرجات) باستخدام `previous_interaction_id`. أما المَعلمات الأخرى، فهي **ضمن نطاق التفاعل** ولا تنطبق إلا على التفاعل المحدّد الذي تنشئه حاليًا:

- `tools`
- `system_instruction`
- `generation_config` (بما في ذلك `thinking_level` و`temperature` وما إلى ذلك)

يعني ذلك أنّه عليك إعادة تحديد هذه المَعلمات في كل تفاعل جديد إذا كنت تريد تطبيقها. إنّ إدارة الحالة من جهة الخادم اختيارية، ويمكنك أيضًا العمل في وضع غير مرتبط بحالة المحادثة من خلال إرسال سجلّ المحادثة الكامل في كل طلب.

### تخزين البيانات والاحتفاظ بها

تخزّن واجهة برمجة التطبيقات تلقائيًا جميع عناصر التفاعل (`store=true`) لتسهيل استخدام ميزات إدارة الحالة من جهة الخادم (باستخدام `previous_interaction_id`)، [التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) (باستخدام `background=true`) ولأغراض إمكانية تتبّع البيانات.

- **الخطة المدفوعة**: يحتفظ النظام بالتفاعلات لمدة **55 يومًا**.
- **الخطة المجانية**: يحتفظ النظام بالتفاعلات لمدة **يوم واحد**.

إذا كنت لا تريد ذلك، يمكنك ضبط `store=false` في طلبك. يختلف عنصر التحكّم هذا عن إدارة الحالة، ويمكنك إيقاف التخزين لأي تفاعل. يُرجى العِلم أنّ
`store=false` غير متوافق مع [التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) ويمنع استخدام
`previous_interaction_id` للأدوار اللاحقة.

يمكنك حذف التفاعلات المخزَّنة في أي وقت باستخدام طريقة الحذف الواردة في
[مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar). لا يمكنك حذف التفاعلات إلا إذا كنت تعرف معرّف التفاعل.

بعد انتهاء فترة التخزين، سيتم حذف بياناتك تلقائيًا.

يعالج النظام عناصر `التفاعل` وفقًا للأحكام .

## أفضل الممارسات

- **معدّل نتائج ذاكرة التخزين المؤقت**: يتيح استخدام `previous_interaction_id` لمواصلة المحادثات للنظام استخدام التخزين المؤقت الضمني لـ سجلّ المحادثة بسهولة أكبر، ما يحسّن الأداء ويقلّل التكاليف.
- **دمج التفاعلات**: يمكنك دمج تفاعلات الوكيل و
  النموذج ومطابقتها ضمن محادثة. على سبيل المثال، يمكنك استخدام وكيل متخصّص، مثل وكيل Deep Research، لجمع البيانات الأولية، ثم استخدام نموذج Gemini عادي للمهام اللاحقة، مثل التلخيص أو إعادة التنسيق، وربط هذه الخطوات باستخدام `previous_interaction_id`.

## النماذج والوكلاء المتوافقون

| اسم النموذج | النوع | رقم تعريف الطراز |
| --- | --- | --- |
| Gemini 3.5 Flash | الطراز | `gemini-3.5-flash` |
| ‫Gemini 3.1 Pro (معاينة) | الطراز | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | الطراز | `gemini-3.1-flash-lite` |
| ‫Gemini 3 Flash (معاينة) | الطراز | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | الطراز | `gemini-2.5-pro` |
| Gemini 2.5 Flash | الطراز | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | الطراز | `gemini-2.5-flash-lite` |
| ‫Gemini 3 Pro Image | الطراز | `gemini-3-pro-image` |
| ‫Gemini 3.1 Flash Image | الطراز | `gemini-3.1-flash-image` |
| ‫Gemini 3.1 Flash TTS (معاينة) | الطراز | `gemini-3.1-flash-tts-preview` |
| ‫Gemma 4 31B IT | الطراز | `gemma-4-31b-it` |
| ‫Gemma 4 26B MoE IT | الطراز | `gemma-4-26b-a4b-it` |
| ‫Lyria 3 Clip (معاينة) | الطراز | `lyria-3-clip-preview` |
| ‫Lyria 3 Pro (معاينة) | الطراز | `lyria-3-pro-preview` |
| ‫Deep Research (معاينة) | الوكيل | `deep-research-preview-04-2026` |
| ‫Deep Research (معاينة) | الوكيل | `deep-research-max-preview-04-2026` |
| ‫Antigravity (معاينة) | الوكيل | `antigravity-preview-05-2026` |

## حزم SDK

يمكنك استخدام أحدث إصدار من حزم Google GenAI SDK للوصول إلى Interactions API.

- في Python، هذه هي حزمة `google-genai` من الإصدار `2.3.0` والإصدارات الأحدث.
- في JavaScript، هذه هي حزمة `@google/genai` من الإصدار `2.3.0` والإصدارات الأحدث.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية تثبيت حزم SDK في صفحة
[المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar).

## القيود

- **خادم MCP عن بُعد**: لا يتيح Gemini 3 استخدام خادم MCP عن بُعد، ولكن سيتم توفير هذه الميزة قريبًا.

تتوفّر الميزات التالية في واجهة برمجة التطبيقات
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar)، ولكنها **غير متاحة بعد** في Interactions API:

- **[البيانات الوصفية للفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar)**: الحقل `video_metadata`، الذي يُستخدم لضبط فواصل الاقتصاص
  ومعدّلات الإطارات المخصّصة لفهم الفيديوهات.
- **[واجهة برمجة التطبيقات المجمّعة](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**
- **[استدعاء الوظائف التلقائي (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ar#automatic_function_calling_python_only)**
- **[التخزين المؤقت الصريح](https://ai.google.dev/gemini-api/docs/caching?hl=ar)**: يُرجى العِلم أنّ التخزين المؤقت الضمني من جهة الخادم متاح في Interactions API
  عبر `previous_interaction_id`.

## الملاحظات

ملاحظاتك ضرورية لتطوير Interactions API.
يمكنك مشاركة أفكارك أو الإبلاغ عن الأخطاء أو طلب ميزات في
[منتدى Google AI Developer Community](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

- يمكنك تجربة [دفتر الملاحظات الخاص بالبدء السريع في Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar).
- مزيد من المعلومات حول [وكيل Deep Research في Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-26 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-26 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
