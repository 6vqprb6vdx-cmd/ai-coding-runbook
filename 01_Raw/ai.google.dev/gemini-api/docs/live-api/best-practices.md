---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=hi
fetched_at: 2026-09-21T05:57:42.344940+00:00
title: "Live API \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0928\u0947 \u0915\u0947 \u0938\u092c\u0938\u0947 \u0938\u0939\u0940 \u0924\u0930\u0940\u0915\u0947 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Live API इस्तेमाल करने के सबसे सही तरीके

इस गाइड में, Live API का बेहतर तरीके से इस्तेमाल करने के लिए सबसे सही तरीके बताए गए हैं.
लाइव एपीआई के बारे में खास जानकारी और इस्तेमाल के सामान्य उदाहरणों के लिए सैंपल कोड देखने के लिए, [लाइव एपीआई का इस्तेमाल शुरू करना](https://ai.google.dev/gemini-api/docs/live?hl=hi) पेज पर जाएं.

## सिस्टम के लिए सटीक निर्देश डिज़ाइन करना

Live API से बेहतर परफ़ॉर्मेंस पाने के लिए, हमारा सुझाव है कि आपके पास सिस्टम के निर्देशों (एसआई) का एक ऐसा सेट होना चाहिए जिसमें एजेंट की पर्सोना, बातचीत के नियम, और सुरक्षा से जुड़े दिशा-निर्देश साफ़ तौर पर बताए गए हों. यह जानकारी इसी क्रम में होनी चाहिए.

सबसे अच्छे नतीजों के लिए, हर एजेंट को अलग-अलग एसआई में बांटें.

1. **एजेंट का पर्सोना तय करें:** एजेंट के नाम, भूमिका, और उसकी किसी भी पसंदीदा विशेषता के बारे में जानकारी दें. अगर आपको लहजे के बारे में बताना है, तो आउटपुट के लिए अपनी पसंदीदा भाषा के बारे में भी ज़रूर बताएं. जैसे, अंग्रेज़ी बोलने वाले व्यक्ति के लिए ब्रिटिश लहजा.
2. **बातचीत से जुड़े नियम तय करें:** इन नियमों को उस क्रम में रखें जिसमें आपको मॉडल से इनका पालन करवाना है. बातचीत के एक बार के एलिमेंट और बातचीत के लूप के बीच अंतर करना. उदाहरण के लिए:

   - **एक बार इस्तेमाल किया जाने वाला एलिमेंट:** ग्राहक की जानकारी एक बार इकट्ठा करना. जैसे, नाम, जगह, लॉयल्टी कार्ड नंबर.
   - **बातचीत का लूप:** उपयोगकर्ता, सुझावों, कीमत, सामान लौटाने, और डिलीवरी के बारे में बातचीत कर सकता है. साथ ही, वह एक विषय से दूसरे विषय पर जा सकता है. मॉडल को बताएं कि जब तक उपयोगकर्ता चाहे, तब तक वह इस बातचीत को जारी रख सकता है.
3. **किसी फ़्लो में टूल कॉल को अलग-अलग वाक्यों में बताएं:** उदाहरण के लिए, अगर किसी ग्राहक की जानकारी इकट्ठा करने के लिए, एक बार में `get_user_info` फ़ंक्शन को लागू करना ज़रूरी है, तो आपको यह कहना चाहिए: *आपका पहला चरण, उपयोगकर्ता की जानकारी इकट्ठा करना है. सबसे पहले, उपयोगकर्ता से उसका नाम, जगह की जानकारी, और लॉयल्टी कार्ड नंबर माँगो. इसके बाद, `get_user_info` को इस जानकारी के साथ शुरू करें.*
4. **ज़रूरी दिशा-निर्देश जोड़ें:** बातचीत से जुड़े ऐसे सामान्य दिशा-निर्देश दें जिन्हें आपको मॉडल से नहीं करवाना है. अगर *x* होता है, तो आपको मॉडल से *y* करवाना है. इसके लिए, बेझिझक होकर उदाहरण दें. अगर आपको अब भी सटीक जवाब नहीं मिल रहा है, तो मॉडल को सटीक जवाब देने के लिए, *साफ़ तौर पर* शब्द का इस्तेमाल करें.

## टूल के बारे में सटीक जानकारी देना

Live API के साथ टूल इस्तेमाल करते समय, टूल की परिभाषाओं के बारे में साफ़ तौर पर जानकारी दें.
Gemini को यह ज़रूर बताएँ कि टूल कॉल को किन शर्तों के तहत शुरू किया जाना चाहिए. ज़्यादा जानकारी के लिए, उदाहरण वाले सेक्शन में [टूल की परिभाषाएं](#tool-definitions-example) देखें.

## असरदार प्रॉम्प्ट लिखना

- **साफ़ तौर पर प्रॉम्प्ट दें:** उदाहरण देकर बताएं कि मॉडल को प्रॉम्प्ट में क्या करना चाहिए और क्या नहीं. साथ ही, कोशिश करें कि एक समय में एक पर्सोना या भूमिका के लिए सिर्फ़ एक प्रॉम्प्ट दिया जाए. ज़्यादा लंबे और कई पेजों वाले प्रॉम्प्ट के बजाय, प्रॉम्प्ट चेनिंग का इस्तेमाल करें. यह मॉडल, एक फ़ंक्शन कॉल वाले टास्क पर सबसे अच्छा परफ़ॉर्म करता है.
- **शुरुआती निर्देश और जानकारी दें:** Live API को जवाब देने से पहले, उपयोगकर्ता के इनपुट की ज़रूरत होती है. अगर आपको Live API से बातचीत शुरू करानी है, तो प्रॉम्प्ट में उपयोगकर्ता का अभिवादन करने या बातचीत शुरू करने के लिए कहें. उपयोगकर्ता के बारे में जानकारी शामिल करें, ताकि Live API उस बधाई को उनकी पसंद के मुताबिक बना सके.

## भाषा तय करना

लाइव एपीआई के ऑडियो मॉडल, उपयोगकर्ता की बोली जाने वाली भाषा का अपने-आप पता लगा लेते हैं और उसके हिसाब से काम करते हैं. इसके लिए, भाषा के कोड की ज़रूरत नहीं होती.

अगर आपको मॉडल से किसी खास भाषा में जवाब चाहिए, तो सिस्टम के निर्देशों में यह निर्देश शामिल करें:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## स्ट्रीमिंग

रीयल-टाइम ऑडियो लागू करते समय, इन सबसे सही तरीकों को अपनाएं:

- **चंक का साइज़ और इंतज़ार का समय (लेटेंसी)**: ऑडियो को 20 से 40 मि॰से॰ के चंक में भेजें.
- **बातचीत में रुकावट आने पर**: जब मॉडल के जवाब देने के दौरान उपयोगकर्ता बोलता है, तो सर्वर `"interrupted": true` के साथ `server_content` मैसेज भेजता है. आपको क्लाइंट-साइड ऑडियो बफ़र को तुरंत हटाना होगा, ताकि एजेंट उपयोगकर्ता के ऊपर न बोलता रहे.

## पिछली बातचीत से जुड़ा डेटा मैनेज करना

लंबे सेशन के लिए `ContextWindowCompressionConfig` का इस्तेमाल करें, क्योंकि नेटिव ऑडियो टोकन तेज़ी से इकट्ठा होते हैं (ऑडियो के हर सेकंड के लिए करीब 25 टोकन).

## क्लाइंट बफ़रिंग

इनपुट ऑडियो को भेजने से पहले, उसे ज़्यादा समय तक बफ़र न करें. जैसे, एक सेकंड तक. इंतज़ार का समय कम करने के लिए, छोटे-छोटे हिस्से (20 मि॰से॰ से 100 मि॰से॰) भेजें.

## फिर से सैंपलिंग करना

पक्का करें कि आपका क्लाइंट ऐप्लिकेशन, ट्रांसमिशन से पहले माइक्रोफ़ोन के इनपुट (अक्सर 44.1 किलोहर्ट्ज़ या 48 किलोहर्ट्ज़) को 16 किलोहर्ट्ज़ पर फिर से सैंपल करे.

## सेशन मैनेजमेंट

सेशन के लाइफ़साइकल को मैनेज करने और उपयोगकर्ताओं को भरोसेमंद अनुभव देने के लिए, इन दिशा-निर्देशों का पालन करें:

- **कॉन्टेक्स्ट विंडो को कंप्रेस करने की सुविधा चालू करें:** ऑडियो टोकन, हर सेकंड में करीब 25 टोकन के हिसाब से इकट्ठा होते हैं. ऑडियो-ओनली सेशन को कंप्रेस किए बिना, सिर्फ़ 15 मिनट तक चलाया जा सकता है. वहीं, ऑडियो-वीडियो सेशन को सिर्फ़ दो मिनट तक चलाया जा सकता है. सेशन की अवधि को अनलिमिटेड करने के लिए, [कॉन्टेक्स्ट विंडो कंप्रेस करने की सुविधा](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=hi#context-window-compression) चालू करें.
- **सेशन फिर से शुरू करने की सुविधा लागू करें:** सर्वर, WebSocket कनेक्शन को समय-समय पर रीसेट कर सकता है. [सेशन फिर से शुरू करने की सुविधा](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=hi#session-resumption) का इस्तेमाल करके, कॉन्टेक्स्ट को सेव रखते हुए आसानी से फिर से कनेक्ट करें. `SessionResumptionUpdate` मैसेज से मिले, सेशन फिर से शुरू करने के सबसे नए टोकन को सेव करें. साथ ही, फिर से कनेक्ट करते समय इसे हैंडल के तौर पर पास करें. रेज़्युम करने के टोकन, आखिरी सेशन खत्म होने के दो घंटे तक मान्य होते हैं.
- **GoAway मैसेज मैनेज करना:** सर्वर, कनेक्शन बंद करने से पहले [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=hi#goaway-message) मैसेज भेजता है. इस मैसेज को सुनें और कनेक्शन बंद होने से पहले, `timeLeft` फ़ील्ड का इस्तेमाल करके कनेक्शन को बंद करें या फिर से कनेक्ट करें.
- **generationComplete सिग्नल मैनेज करें:** [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=hi#generation-complete-message) मैसेज का इस्तेमाल करके यह जानें कि मॉडल ने जवाब जनरेट करना कब पूरा किया, ताकि आपका ऐप्लिकेशन अपने यूज़र इंटरफ़ेस (यूआई) को अपडेट कर सके या अगली कार्रवाई कर सके.

लागू करने से जुड़ी जानकारी के लिए, [सेशन मैनेजमेंट](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=hi) देखें.

## उदाहरण

इस उदाहरण में, करियर कोच के तौर पर मॉडल की परफ़ॉर्मेंस को बेहतर बनाने के लिए, सबसे सही तरीकों और [सिस्टम के निर्देशों को डिज़ाइन करने से जुड़ी गाइडलाइन](#system-instruction-guidelines), दोनों को शामिल किया गया है.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### टूल की परिभाषाएं

इस JSON में, करियर कोच के उदाहरण में इस्तेमाल किए गए काम के फ़ंक्शन के बारे में बताया गया है.
फ़ंक्शन तय करते समय, उनके नाम, ब्यौरे, पैरामीटर, और लागू होने की शर्तें शामिल करें. इससे आपको बेहतर नतीजे मिलेंगे.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## कीमत तय करना और बिलिंग

Gemini Live API के लिए, टोकन के इस्तेमाल के हिसाब से बिलिंग की जाती है. लाइव एपीआई, WebSocket सेशन को लगातार चालू रखता है. इसलिए, बिलिंग, कॉन्टेक्स्ट विंडो के चालू होने पर आधारित होती है.

### सेशन कॉन्टेक्स्ट विंडो (बढ़ती लागत)

एपीआई, सेशन कॉन्टेक्स्ट विंडो में मौजूद सभी टोकन के लिए, आपसे हर टर्न के हिसाब से शुल्क लेता है. "टर्न" का मतलब है, उपयोगकर्ता का एक इनपुट और मॉडल का उससे जुड़ा जवाब.

- **एकत्रित करना:** कॉन्टेक्स्ट विंडो में, मौजूदा टर्न के नए टोकन के साथ-साथ पिछले टर्न के सभी टोकन शामिल होते हैं.
- **फिर से बिलिंग:** पिछले टोकन को फिर से प्रोसेस किया जाता है और हर नए टर्न में उनका हिसाब लगाया जाता है. ऐसा, कॉन्फ़िगर की गई कॉन्टेक्स्ट विंडो के साइज़ तक किया जाता है. सेशन की अवधि बढ़ने पर, हर बातचीत की लागत बढ़ जाती है. ऐसा इसलिए होता है, क्योंकि बातचीत के इतिहास को फिर से प्रोसेस किया जाता है.

### ऑडियो टोकन और ट्रांसक्रिप्शन

Live API, मूल रूप से मल्टीमॉडल है. यह बातचीत के इतिहास को रॉ ऑडियो टोकन के तौर पर सेव करता है, ताकि आवाज़ की बारीकियों और टोन को बरकरार रखा जा सके.

- **ऑडियो बिलिंग:** एपीआई, हर बार ऑडियो इनपुट के स्टैंडर्ड रेट के हिसाब से, आपके नेटिव ऑडियो टोकन के लिए बिल करता है.
- **ट्रांसक्रिप्शन का सरचार्ज:** ऑडियो को टेक्स्ट में बदलने की सुविधा चालू होने पर (`inputAudioTranscription` या `outputAudioTranscription`), एपीआई, ट्रांसक्रिप्शन के लिए जनरेट किए गए सभी टेक्स्ट टोकन के लिए शुल्क लेता है. यह शुल्क, ऑडियो टोकन के स्टैंडर्ड शुल्क के अलावा, टेक्स्ट टोकन के आउटपुट रेट पर लिया जाता है.

### कॉन्टेक्स्ट की सीमाओं की मदद से लागत मैनेज करना

लंबे सेशन में लागत बढ़ने से रोकने के लिए, `contextWindowCompression` का इस्तेमाल करके कॉन्टेक्स्ट विंडो का साइज़ कॉन्फ़िगर करें.

कंप्रेशन ट्रिगर (जैसे, 25,000 टोकन) और स्लाइडिंग विंडो (जैसे, 8,000 टोकन) सेट करने पर, थ्रेशोल्ड तक पहुंचने के बाद एपीआई पुराने टोकन अपने-आप हटा देता है. इसके बाद, एपीआई सिर्फ़ सेव की गई हिस्ट्री और नए टोकन के लिए बिल भेजता है.

### आवाज़ सुनकर ज़रूरत के मुताबिक जवाब देने की सुविधा

'प्रोऐक्टिव ऑडियो' सुविधा चालू होने पर, Live API के सुनने के दौरान, एपीआई इनपुट टोकन के लिए शुल्क लेता है. साथ ही, एपीआई के जवाब देने पर ही आउटपुट टोकन के लिए शुल्क लेता है.

- **Gemini 3.8 के लिए नोट:** `gemini-3.8-live` और `gemini-3.8-live-extended-thinking` में, प्रोएक्टिव ऑडियो हमेशा के लिए चालू रहता है.
- **Gemini 3.1 के लिए ध्यान दें:** `gemini-3.1-flash-live-preview` में, अपने-आप ऑडियो शुरू होने की सुविधा काम नहीं करती. इस मॉडल के लिए, एपीआई सिर्फ़ ऑडियो के लिए बिल भेजता है. ऐसा तब होता है, जब इनपुट को स्ट्रीम किया जा रहा हो.

शुल्क के बारे में ज़्यादा जानकारी के लिए, [Gemini API के शुल्क वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-17 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-17 (UTC) को अपडेट किया गया."],[],[]]
