---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ar
fetched_at: 2026-11-02T07:19:56.655622+00:00
title: "\u0641\u0647\u0645 \u0627\u0644\u0641\u064a\u062f\u064a\u0648 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الفيديو

يمكن لـ Gemini Robotics ER 2 تتبُّع تقدّم المهام من خلاصات الفيديوهات المستمرة باستخدام ميزتَين:

- العثور على اللحظات: تحدِّد هذه الميزة الطابع الزمني الدقيق لوقوع حدث رئيسي.
- تصنيف التقدّم: تصنِّف هذه الميزة كل فيديو ضمن إحدى فئات الإكمال الخمس (0–20% أو 20–40% أو 40–60% أو 60–80% أو 80–100%).

## العثور على اللحظات

تحدِّد ميزة "العثور على اللحظات" إطار الفيديو الدقيق الذي يقع فيه حدث مهم، مثلاً عندما يمتلئ كوب أو يتم ربط عقدة. تستخدم الروبوتات هذه الميزة للتحقّق من النجاح وتسلسل الخطوات وبدء التصحيحات.

يطلب نموذج التعليمة البرمجية التالي من النموذج تحديد لحظة الإكمال لمهمة معيّنة في فيديو:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

تعرض الصورة التالية أمثلة على إطارات من فيديو للعثور على اللحظات، حيث يحدِّد النموذج الطابع الزمني لإكمال المهمة:

![مثال على لقطات فيديو تعرض نتيجة البحث عن اللحظة مع طابع زمني](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=ar)

## تصنيف التقدّم

تصنِّف ميزة "تصنيف التقدّم" الفيديو ضمن إحدى فئات الإكمال الخمس: 0–20% أو 20–40% أو 40–60% أو 60–80% أو 80–100%. يمنح ذلك الروبوتات وعيًا بالوضع في الوقت الفعلي، ما يتيح لها تعديل الإجراءات أو إعادة محاولة الخطوات التي تعذّر إكمالها بدون إعادة بدء سير عمل كامل.

يطلب نموذج التعليمة البرمجية التالي من النموذج تصنيف مستوى التقدّم الحالي من فيديو:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

تعرض الصورة التالية أمثلة على إطارات من فيديو لتصنيف التقدّم، حيث يحدِّد النموذج فئة التقدّم:

![أمثلة على لقطات فيديو تعرض ناتج تصنيف مستوى التقدّم مع تصنيف بين قوسين](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=ar)

## أمثلة

للاطّلاع على أمثلة كاملة قابلة للتنفيذ تتضمّن تتبُّع المهام المتعدّدة الخطوات، يُرجى مراجعة الـ
[Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## الخطوات التالية

- [Live API للروبوتات](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar): بث ثنائي الاتجاه في الوقت الفعلي
- [تنسيق المهام](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ar): مهام طويلة الأجل تتضمّن التفكير المكاني
- [نظرة عامة على Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar): مقارنة النماذج والإمكانات

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-08 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-08 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
