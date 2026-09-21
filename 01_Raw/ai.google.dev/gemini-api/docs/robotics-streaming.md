---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar
fetched_at: 2026-09-21T05:53:44.306798+00:00
title: "\u0627\u0644\u0631\u0648\u0628\u0648\u062a\u0627\u062a \u0645\u0639 \u0627\u0644\u0628\u062b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الروبوتات مع البث

تعرض نقطة نهاية نموذج `gemini-robotics-er-2-streaming-preview` نقطة نهاية مخصّصة للبث المباشر تتكامل مع [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ar)، ما يتيح تفاعلاً ثنائي الاتجاه في الوقت الفعلي بين تطبيقك والروبوت. وهذا يجعلها مناسبة للوكلاء الذين يحتاجون إلى حلقات ملاحظات سريعة وردود فعلية على البيئة.

[تجربة التطبيق في Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=ar)
[استنساخ تطبيقات نموذجية من GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## حالات الاستخدام

- **التنسيق بين الروبوتات المتعددة**: روبوتات متعددة تتواصل بشأن حالة المهام وتفوّض المهام الفرعية من خلال جلسة مشتركة.
- **المراقبة المستمرة**: هي برامج آلية تراقب مشهدًا معيّنًا وتنفّذ إجراءات
  عند وقوع أحداث معيّنة، مثل وصول حاوية إلى مستوى تعبئة معيّن.
- **المستودع والخدمات اللوجستية**: وكلاء التعبئة والتغليف الذين يتحقّقون من السلع بشكل مرئي ويتتبّعون تقدّم عملية التغليف ويتعافون من الأخطاء

## المواصفات الفنية

يوضّح الجدول التالي المواصفات الفنية لواجهة Live API:

| الفئة | التفاصيل |
| --- | --- |
| طُرق الإدخال | الصوت (صوت PCM خام بمعدل 16 بت، و16 كيلوهرتز، وترتيب وحدات البايت الصغيرة أولاً)، والصور (JPEG <= 1 لقطة في الثانية)، والنصوص |
| طُرق الإخراج | نص |
| البروتوكول | اتصال WebSocket ذو الحالة (WSS) |

## إنشاء إعدادات تستند إلى الذكاء الاصطناعي الوكيل

تتّبع كل أداة روبوتية مستندة إلى Live API ثلاث خطوات:

1. **التعريف بإمكانات الروبوت كأدوات.** يصبح كل إجراء يمكن للروبوت تنفيذه، مثل التنقّل والإمساك والتحدّث، تعريف دالة يتضمّن اسمًا ووصفًا ومخططًا للمعلمات. يجب أن تستخدم الإجراءات المادية
   `"behavior": "BLOCKING"` لكي ينتظر النموذج إلى أن ينتهي الروبوت من تنفيذ الإجراء قبل
   اختيار الخطوة التالية.
2. **بث إدخال متعدد الوسائط في جلسة مستمرة** افتح جلسة `live.connect`
   وأبقِها مفتوحة طوال مدة المهمة. إرسال إطارات الفيديو أو الصوت أو النص عند وصولها من مستشعرات الروبوت
3. **التعامل مع طلبات استخدام الأدوات في حلقة تلقّي** في كل مرة يختار فيها النموذج إجراءً، يرسل رسالة `tool_call`. ينفّذ حلقة الاستلام الدالة على حزمة تطوير البرامج (SDK) الخاصة بالروبوت ويرسل `tool_response`. ستبقى الجلسة مفتوحة، وسيختار النموذج الإجراء التالي استنادًا إلى النتيجة.

توضّح الأقسام التالية كيفية تطبيق هذه الخطوات على ثلاثة أنماط شائعة:
حلقة وكيل أساسية، ومراقبة المشهد بشكل استباقي باستخدام إشارة نبض، وتوجيه
الكلام من خلال ميزة "تحويل النص إلى كلام" كأداة.

## تنسيق عمل روبوت من خلال استدعاء الدوال

يوضّح المثال التالي الخطوات الثلاث معًا في نص برمجي واحد بلغة Python.

الخطوة 1 — تعريفات الأدوات — تعلن عن إمكانات الروبوت كتعريفات للدوال. تستخدم الدالة `navigate` `"behavior": "BLOCKING"`، لذا ينتظر النموذج وصول الروبوت إلى نقطة على المسار قبل استدعاء أداة أخرى.
أضِف المزيد من تعريفات الدوال في القائمة نفسها لعرض إمكانات إضافية للروبوت.

تعرض الخطوة 2، أي أدوات المساعدة في الإدخال، ثلاث دوال تنقل أنواعًا مختلفة من بيانات الإدخال إلى الجلسة: `send_text` للأوامر، و`send_image` لإطارات الكاميرا مع طلب نصي اختياري، و`send_audio` لصوت PCM الأولي من الميكروفون.

تعمل الخطوة 3، أي حلقة الاستلام، بشكل متزامن وتتعامل مع نوعَين من الرسائل: رسائل `server_content` (الناتج النصي للنموذج) ورسائل `tool_call` (النموذج يطلب تنفيذ إجراء من الروبوت). عندما يصل طلب استدعاء أداة، تستدعي الحلقة `execute_tool`، وهو رمز بديل يمكنك استبداله بحزمة SDK الخاصة بالروبوت، ثم ترسل `tool_response` حتى يتمكّن النموذج من اختيار الإجراء التالي.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

تظل حلقة الاستلام نشطة بعد كل ردّ من الأداة. ينشئ النموذج خطة طويلة الأمد ويراجعها بدون أن ترمز تسلسل الإجراءات بأكمله مسبقًا.

## التفكير الاستباقي المكاني الزماني

تتيح Live API بث الفيديو، ولكنّ إطارات الفيديو وحدها لا تؤدي إلى بدء دورة استنتاج جديدة. يجب أن تكون لقطات الفيديو مصحوبة بطلب نصي أو صوتي لتفعيل استجابة النموذج. يمكنك الاطّلاع على [إمكانات Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ar) لمزيد من التفاصيل.

لتفعيل ميزة "الاستدلال الاستباقي"، عليك تنفيذ **إشارة نبض**: أرسِل بشكل دوري أحدث إطار من الكاميرا متبوعًا بطلب نصي قصير يجبر النموذج على فحص المشهد واتخاذ قرار واضح. يتم الحدّ من معدّل نقل بيانات الفيديو الوارد إلى لقطة واحدة في الثانية.

### تنفيذ الإشارات الدورية

يتم تشغيل روتين القلب كوظيفة `asyncio` منفصلة في الجلسة نفسها.
يستهدف هذا الإعداد بشكل انتهازي معدّل تكرار يبلغ 1 هرتز (يتطابق مع الحد الأقصى لمعدّل إدخال الفيديو)
أثناء انتظار اكتمال كل دورة (`er_turn_done`) لتجنُّب مقاطعة
الاستدلال أثناء التنفيذ:

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### تعديل حلقة الاستلام

للإشارة إلى أنّ النموذج قد أكمل دوره، عدِّل `receive_loop`
لضبط `er_turn_done`:

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## مصدر إخراج الصوت من خلال تقنية TTS خارجية

يعرض Gemini Robotics ER 2 نصًا. يوجه تطبيقك الردود المكتملة إلى مقدّم خدمة منفصل لتحويل النص إلى كلام (مثل [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)) من خلال دالة ردّ تم إدخالها.
يساعد ذلك في إبقاء وقت استجابة الكلام واختيار الصوت وسلوك المقاطعة تحت سيطرتك، كما يتيح لك تبديل الأنظمة الخلفية لتحويل النص إلى كلام بدون تغيير منطق الوكيل.

يمكنك أيضًا تعريف تحويل النص إلى كلام كأداة لكي يتعامل النموذج مع "قل شيئًا" بالطريقة نفسها التي يتعامل بها مع "حرِّك الذراع". أضِف تعريف الدالة التالي إلى قائمة `tools`
من القسم الأول:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

من خلال تضمين TTS في تعريف دالة، يتعامل النموذج مع الكلام من خلال مسار استدعاء الأدوات نفسه الذي تستخدمه أي إجراءات أخرى يتخذها الروبوت. يستوفي تطبيقك
طلب البيانات من خلال دالة ردّ نداء تم إدخالها.

## أمثلة على GitHub

للاطّلاع على أمثلة عملية كاملة، بما في ذلك العرض التوضيحي الخاص بجلب الوجبات الخفيفة باستخدام الروبوت Spot، والعرض التوضيحي الخاص بالتحريك الأفقي والرأسي باستخدام الروبوت Tinybot، يُرجى الاطّلاع على [أمثلة على Robotics Live API](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## الخطوات التالية

- [فهم الفيديو](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ar): العثور على اللحظات وتصنيف مستوى التقدّم
- [تنظيم المهام](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ar): مهام طويلة الأمد بدون بث
- [نظرة عامة على Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ar): مستندات Live API الكاملة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-16 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-16 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
