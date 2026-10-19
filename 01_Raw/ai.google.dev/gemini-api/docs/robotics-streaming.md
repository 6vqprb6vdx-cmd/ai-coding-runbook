---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi
fetched_at: 2026-10-19T05:36:16.789537+00:00
title: "\u0938\u094d\u091f\u094d\u0930\u0940\u092e\u093f\u0902\u0917 \u0915\u0947 \u0938\u093e\u0925 \u0930\u094b\u092c\u094b\u091f\u093f\u0915\u094d\u0938 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# स्ट्रीमिंग के साथ रोबोटिक्स

`gemini-robotics-er-2-streaming-preview` मॉडल एंडपॉइंट, एक खास स्ट्रीमिंग एंडपॉइंट दिखाता है. यह [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=hi) के साथ इंटिग्रेट होता है. इससे आपके ऐप्लिकेशन और रोबोट के बीच रीयल-टाइम में दोनों तरफ़ से इंटरैक्शन किया जा सकता है. इस वजह से, यह उन एजेंट के लिए सही है जिन्हें तेज़ी से फ़ीडबैक लूप और एनवायरमेंट के हिसाब से प्रतिक्रिया देने की ज़रूरत होती है.

[Google AI Studio में आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=hi)
[GitHub से उदाहरण ऐप्लिकेशन क्लोन करें](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## उपयोग के उदाहरण

- **एक से ज़्यादा रोबोट के बीच तालमेल**: एक से ज़्यादा रोबोट, शेयर किए गए सेशन के ज़रिए टास्क की स्थिति के बारे में बताते हैं और उप-टास्क सौंपते हैं.
- **लगातार निगरानी करना**: ऐसे रोबोट जो किसी सीन को देखते हैं और खास इवेंट होने पर कार्रवाइयों को ट्रिगर करते हैं. जैसे, किसी कंटेनर का पूरा भर जाना.
- **वेयरहाउस और लॉजिस्टिक्स**: पिक-एंड-पैक एजेंट, जो आइटम की पुष्टि करते हैं. साथ ही, पैकिंग की प्रोग्रेस को ट्रैक करते हैं और गड़बड़ियों को ठीक करते हैं.

## तकनीकी जानकारी

यहां दी गई टेबल में, Live API की तकनीकी खास जानकारी दी गई है:

| कैटगरी | विवरण |
| --- | --- |
| इनपुट के तरीके | ऑडियो (रॉ 16-बिट पीसीएम ऑडियो, 16 किलोहर्ट्ज़, लिटिल-एंडियन), इमेज (JPEG <= 1 एफ़पीएस), टेक्स्ट |
| आउटपुट के तरीके | टेक्स्ट |
| प्रोटोकॉल | स्टेटफ़ुल WebSocket कनेक्शन (WSS) |

## एजेंट की तरह काम करने वाला सेटअप बनाना

Live API पर बनाए गए हर रोबोटिक्स एजेंट को तीन चरणों का पालन करना होता है:

1. **रोबोट की क्षमताओं को टूल के तौर पर दिखाएं.** रोबोट की हर कार्रवाई — जैसे कि नेविगेट करना, पकड़ना, बोलना — एक फ़ंक्शन डिक्लेरेशन बन जाती है. इसमें नाम, ब्यौरा, और पैरामीटर स्कीमा होता है. फ़िज़िकल ऐक्शन के लिए, `"behavior": "BLOCKING"` का इस्तेमाल करना ज़रूरी है, ताकि मॉडल, रोबोट के काम पूरा करने का इंतज़ार कर सके. इसके बाद ही, वह अगला चरण चुन सके.
2. **मल्टीमोडल इनपुट को किसी परसिस्टेंट सेशन में स्ट्रीम करें.** `live.connect` सेशन खोलें और उसे टास्क पूरा होने तक खुला रखें. रोबोट के सेंसर से मिलने वाले वीडियो फ़्रेम, ऑडियो या टेक्स्ट को तुरंत भेजें.
3. **receive लूप में टूल कॉल मैनेज करें.** जब भी मॉडल कोई कार्रवाई चुनता है, तब वह `tool_call` मैसेज भेजता है. आपका रिसीव लूप, आपके रोबोट एसडीके के ख़िलाफ़ फ़ंक्शन को एक्ज़ीक्यूट करता है और `tool_response` वापस भेजता है. सेशन खुला रहता है और मॉडल, नतीजे के आधार पर अगली कार्रवाई चुनता है.

यहां दिए गए सेक्शन में, इन चरणों को तीन सामान्य पैटर्न पर लागू करने का तरीका बताया गया है:
बेसललाइन एजेंट लूप, हार्टबीट के साथ प्रॉऐक्टिव सीन मॉनिटरिंग, और टीटीएस को टूल के तौर पर इस्तेमाल करके स्पीच को रूट करना.

## फ़ंक्शन कॉलिंग की मदद से किसी रोबोट को कंट्रोल करना

नीचे दिए गए उदाहरण में, तीनों चरणों को एक ही Python स्क्रिप्ट में एक साथ दिखाया गया है.

पहला चरण — टूल की परिभाषाएं — इसमें रोबोट की क्षमताओं को फ़ंक्शन के तौर पर बताया जाता है. `navigate` फ़ंक्शन, `"behavior": "BLOCKING"` का इस्तेमाल करता है. इसलिए, मॉडल किसी दूसरे टूल को कॉल करने से पहले, रोबोट के वेपॉइंट तक पहुंचने का इंतज़ार करता है.
रोबोट की अन्य क्षमताओं को दिखाने के लिए, उसी सूची में फ़ंक्शन के और एलान जोड़ें.

दूसरे चरण — इनपुट हेल्पर — में तीन फ़ंक्शन दिखाए गए हैं. ये फ़ंक्शन, सेशन में अलग-अलग मोडैलिटी के इनपुट स्ट्रीम करते हैं: `send_text` कमांड के लिए, `send_image` कैमरा फ़्रेम के लिए (इसमें टेक्स्ट प्रॉम्प्ट का इस्तेमाल किया जा सकता है), और `send_audio` माइक्रोफ़ोन से मिले रॉ पीसीएम ऑडियो के लिए.

तीसरा चरण — रिसीव लूप — एक साथ चलता है और दो तरह के मैसेज हैंडल करता है:
`server_content` मैसेज (मॉडल का टेक्स्ट आउटपुट) और `tool_call` मैसेज (मॉडल, रोबोट से कोई कार्रवाई करने का अनुरोध कर रहा है). जब टूल कॉल आता है, तो लूप `execute_tool` को कॉल करता है. यह एक स्टब होता है, जिसे आपको अपने असली रोबोट एसडीके से बदलना होता है. इसके बाद, यह `tool_response` वापस भेजता है, ताकि मॉडल अगली कार्रवाई चुन सके.

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

हर टूल के जवाब के बाद, रिसीव लूप चालू रहता है. यह मॉडल, लंबी अवधि की योजना बनाता है और उसमें बदलाव करता है. इसके लिए, आपको कार्रवाई के पूरे क्रम को पहले से कोड करने की ज़रूरत नहीं होती.

## स्पेशल-टेम्परल रीज़निंग की सुविधा अपने-आप काम करना

लाइव एपीआई, वीडियो स्ट्रीम करता है. हालांकि, सिर्फ़ वीडियो फ़्रेम से, जवाब देने की नई बारी शुरू नहीं होती. वीडियो फ़्रेम के साथ टेक्स्ट या ऑडियो प्रॉम्प्ट होना चाहिए, ताकि मॉडल जवाब दे सके. ज़्यादा जानकारी के लिए, [लाइव एपीआई की सुविधाएं](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=hi) देखें.

पहले से ही अनुमान लगाने की सुविधा चालू करने के लिए, **हार्टबीट** लागू करें: समय-समय पर, कैमरे का सबसे नया फ़्रेम भेजें. इसके बाद, एक छोटा टेक्स्ट प्रॉम्प्ट भेजें. इससे मॉडल को सीन की जांच करने और साफ़ तौर पर फ़ैसला लेने के लिए मजबूर किया जा सकेगा. वीडियो इनपुट के लिए, फ़्रेम रेट की सीमा तय की गई है. इसके तहत, हर सेकंड में सिर्फ़ एक फ़्रेम इस्तेमाल किया जा सकता है.

### हार्टबीट लागू करना

हार्टबीट कोरूटीन, उसी सेशन में एक अलग `asyncio` टास्क के तौर पर चलता है.
यह 1 हर्ट्ज़ की कैडेंस को टारगेट करता है. यह वीडियो इनपुट की दर की सीमा से मेल खाती है. साथ ही, यह हर टर्न के पूरा होने (`er_turn_done`) का इंतज़ार करता है, ताकि फ़्लाइट में मौजूद तर्क में रुकावट न आए:

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

### लूप पाने की सुविधा अपडेट करना

मॉडल के जवाब देने के बाद, यह बताने के लिए कि अब आपकी बारी है, `receive_loop` को अपडेट करें. इसके लिए, `er_turn_done` को सेट करें:

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## बाहरी टीटीएस के ज़रिए ऑडियो आउटपुट

Gemini Robotics ER 2, टेक्स्ट दिखाता है. आपका ऐप्लिकेशन, पूरे किए गए जवाबों को इंजेक्ट किए गए कॉलबैक के ज़रिए, टीटीएस की सेवा देने वाली किसी दूसरी कंपनी (जैसे, [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)) को भेजता है.
इससे, बोलने में लगने वाला समय, आवाज़ चुनने की सुविधा, और बीच में रोकने की सुविधा आपके कंट्रोल में रहती है. साथ ही, एजेंट के लॉजिक में बदलाव किए बिना, टीटीएस बैकएंड को बदला जा सकता है.

टीटीएस को टूल के तौर पर भी सेट किया जा सकता है, ताकि मॉडल "कुछ बोलो" को "हाथ हिलाओ" के तौर पर ही ट्रीट करे. पहले सेक्शन से, अपनी `tools` सूची में फ़ंक्शन का यह एलान जोड़ें:

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

टीटीएस को फ़ंक्शन डिक्लेरेशन में रैप करके, मॉडल स्पीच को उसी टूल-कॉल पाथ से हैंडल करता है जिस तरह से किसी अन्य रोबोट ऐक्शन को हैंडल किया जाता है. आपका ऐप्लिकेशन, इंजेक्ट किए गए कॉलबैक के साथ कॉल को पूरा करता है.

## GitHub पर उदाहरण

Spot रोबोट के स्नैक-फ़ेच डेमो और Tinybot के पैन-टिल्ट हेलो वर्ल्ड के साथ-साथ, काम करने वाले सभी उदाहरणों के लिए, [Robotics Live API के उदाहरण](https://github.com/google-gemini/robotics-samples/tree/main/live-api) देखें.

## आगे क्या करना है

- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=hi) — इसमें खास पल ढूंढना और प्रोग्रेस को कैटगरी में बांटना शामिल है.
- [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=hi) — लंबे समय तक चलने वाले टास्क, जिनमें स्ट्रीमिंग नहीं होती.
- [Live API की खास जानकारी](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=hi) — Live API का पूरा दस्तावेज़.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-16 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-16 (UTC) को अपडेट किया गया."],[],[]]
