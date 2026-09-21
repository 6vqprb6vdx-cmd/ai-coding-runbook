---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi
fetched_at: 2026-09-21T05:46:19.874535+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Interactions API

Interactions API, Gemini मॉडल और एजेंटों के साथ काम करने का सबसे अच्छा तरीक़ा है. जून 2026 से, यह सामान्य तौर पर उपलब्ध है. साथ ही, सभी नए प्रोजेक्ट के लिए इसका सुझाव दिया जाता है. हालांकि, अब इसे लेगसी माना जाता है, लेकिन ओरिजनल [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=hi) एपीआई का इस्तेमाल अब भी किया जा सकता है.

## Interactions API का इस्तेमाल क्यों करना चाहिए?

- **सभी ऐप्लिकेशन के लिए यूनिवर्सल इंटरफ़ेस**: इसे इस्तेमाल के हर तरीके के लिए स्टैंडर्ड इंटरफ़ेस के तौर पर डिज़ाइन किया गया है. जैसे, एक बार में टेक्स्ट जनरेट करना, मल्टीमॉडल को समझना, स्ट्रक्चर्ड आउटपुट, टूल ऑर्केस्ट्रेशन, और एजेंटिक वर्कफ़्लो.
- **मॉडल और एजेंट के लिए एक ही एपीआई**: स्टैंडर्ड Gemini मॉडल के साथ-साथ, सीधे तौर पर खास एजेंट (जैसे, Deep Research और कस्टम मैनेज किए गए एजेंट) को कॉल करने के लिए, एक ही यूनीफ़ाइड एंडपॉइंट और पैटर्न.
- **नई सुविधाएं**: जैसे, `previous_interaction_id` का इस्तेमाल करके सर्वर-साइड कन्वर्सेशन की स्थिति को वैकल्पिक तौर पर सेव करने की सुविधा, डीबग करने और यूज़र इंटरफ़ेस (यूआई) रेंडर करने के लिए, एक्ज़ीक्यूशन के चरणों को मॉनिटर करने की सुविधा, और `background=true` का इस्तेमाल करके लंबे समय तक चलने वाले टास्क के लिए [बैकग्राउंड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/background-execution?hl=hi) की सुविधा.
- **कैश मेमोरी के हिट रेट ज़्यादा होने पर लागत कम लगती है**: सिलसिलेवार बातचीत का इस्तेमाल करते समय, सर्वर-साइड स्टेट मैनेजमेंट की सुविधा चालू करने पर, हर बार के हिसाब से कॉन्टेक्स्ट को ज़्यादा बेहतर तरीके से कैश किया जा सकता है. इससे टोकन की लागत कम हो जाती है.
- **नई सुविधाएं कहाँ लॉन्च होंगी**: आने वाले समय में, सभी नए मॉडल, मल्टीमॉडल सुविधाएं, टूल, और एजेंटिक सुविधाएं, Interactions API पर लॉन्च होंगी.

डिफ़ॉल्ट रूप से, Interactions API अनुरोधों को सेव करता है, ताकि `previous_interaction_id` का इस्तेमाल करके, सर्वर-साइड स्टेट मैनेजमेंट की सुविधाओं का फ़ायदा लिया जा सके. `store=false` को सेट करके, स्टेटलेस व्यवहार के लिए ऑप्ट इन किया जा सकता है. ज़्यादा जानकारी के लिए, [डेटा के रखरखाव](#data-storage-retention) सेक्शन देखें.

## अपनी प्रोफ़ाइल बनाना शुरू करें

- **कोडिंग एजेंट सेट अप करना**: **Gemini Docs MCP** से कनेक्ट करें और `gemini-api-dev` स्किल इंस्टॉल करें. इससे आपके असिस्टेंट को डेवलपर के लिए उपलब्ध नए दस्तावेज़ों और सबसे सही तरीकों का सीधा ऐक्सेस मिलेगा. ज़्यादा जानकारी के लिए, [कोडिंग एजेंट सेट अप करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi) देखें
- **`generateContent` से माइग्रेट करें**: अगर आपने पहले से ही इंटिग्रेशन किया हुआ है, तो Interactions API पर स्विच करने के लिए, [माइग्रेशन गाइड](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=hi) में दिए गए निर्देशों का पालन करें.
- **शुरू करें**: [Interactions API का इस्तेमाल शुरू करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/get-started?hl=hi) में दिए गए चरणों का पालन करें.

### सुविधा की गाइड

इन गाइड की मदद से, Interactions API की खास सुविधाओं के बारे में जानें. इन पेजों पर मौजूद टॉगल का इस्तेमाल करके, generateContent और Interactions API के बीच स्विच किया जा सकता है:

- [टेक्स्ट जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi)
- [इमेज जनरेट करना](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)
- [इमेज की बारीक़ी से पहचान](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi)
- [ऑडियो को समझना](https://ai.google.dev/gemini-api/docs/audio?hl=hi)
- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi)
- [दस्तावेज़ की प्रोसेसिंग](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi)
- [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)
- [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)
- [Deep Research एजेंट](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi)
- [Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)
- [प्राथमिकता का अनुमान लगाना](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)

## Interactions API कैसे काम करता है

Interactions API, मुख्य संसाधन [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=hi#Resource:Interaction) पर आधारित है. `Interaction` का मतलब है कि बातचीत या टास्क पूरा हो गया है. यह सेशन रिकॉर्ड के तौर पर काम करता है. इसमें इंटरैक्शन का पूरा इतिहास, **एक्ज़ीक्यूशन के चरणों** के क्रम के तौर पर शामिल होता है. इन चरणों में मॉडल के विचार, सर्वर-साइड या क्लाइंट-साइड टूल कॉल और नतीजे (जैसे, `function_call` और `function_result`) और फ़ाइनल `model_output` शामिल हैं. स्टोर किए गए संसाधन (`interactions.get` के ज़रिए वापस पाया गया) में, पूरे कॉन्टेक्स्ट के लिए `user_input` चरण भी शामिल होते हैं. हालांकि, `interactions.create` से मिले जवाब में सिर्फ़ मॉडल से जनरेट किए गए चरण शामिल होते हैं.

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=hi#CreateInteraction) पर कॉल करने का मतलब है कि
आपने एक नई `Interaction` रिसॉर्स बनाई है.

### सर्वर-साइड स्टेट मैनेजमेंट

बातचीत जारी रखने के लिए,
`previous_interaction_id` पैरामीटर का इस्तेमाल करके, पूरी हो चुकी बातचीत के `id` का इस्तेमाल किया जा सकता है. सर्वर इस आईडी का इस्तेमाल, बातचीत का इतिहास वापस पाने के लिए करता है. इससे आपको चैट का पूरा इतिहास फिर से भेजने की ज़रूरत नहीं पड़ती.

`previous_interaction_id` पैरामीटर, सिर्फ़ बातचीत के इतिहास (इनपुट और आउटपुट) को सेव करता है. इसके लिए, `previous_interaction_id` का इस्तेमाल किया जाता है. अन्य पैरामीटर **इंटरैक्शन के स्कोप वाले पैरामीटर** होते हैं. ये सिर्फ़ उस इंटरैक्शन पर लागू होते हैं जिसे अभी जनरेट किया जा रहा है:

- `tools`
- `system_instruction`
- `generation_config` (इसमें `thinking_level`, `temperature` वगैरह शामिल हैं)

इसका मतलब है कि अगर आपको इन पैरामीटर को लागू करना है, तो आपको हर नई बातचीत में इन्हें फिर से तय करना होगा. सर्वर-साइड स्टेट मैनेजमेंट का इस्तेमाल करना ज़रूरी नहीं है. हर अनुरोध में बातचीत का पूरा इतिहास भेजकर, बिना स्टेट वाले मोड में भी काम किया जा सकता है.

### डेटा स्टोरेज और रखरखाव

डिफ़ॉल्ट रूप से, एपीआई सभी इंटरैक्शन ऑब्जेक्ट (`store=true`) को सेव करता है, ताकि सर्वर-साइड स्टेट मैनेजमेंट की सुविधाओं (`previous_interaction_id` के साथ), [बैकग्राउंड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/background-execution?hl=hi) (`background=true` का इस्तेमाल करके) और जांचने की क्षमता के मकसद से इनका इस्तेमाल आसान हो सके.

- **पैसे चुकाकर ली जाने वाली सदस्यता**: सिस्टम, इंटरैक्शन को **55 दिनों** तक सेव रखता है.
- **मुफ़्त टियर**: सिस्टम, इंटरैक्शन को **एक दिन** तक सेव रखता है.

अगर आपको ऐसा नहीं करना है, तो अपने अनुरोध में `store=false` सेट करें. यह कंट्रोल, स्टेट मैनेजमेंट से अलग है. आपके पास किसी भी इंटरैक्शन के लिए स्टोरेज से ऑप्ट आउट करने का विकल्प होता है. हालांकि, ध्यान दें कि `store=false`, [बैकग्राउंड में काम करने की सुविधा](https://ai.google.dev/gemini-api/docs/background-execution?hl=hi) के साथ काम नहीं करता है. साथ ही, यह बाद के टर्न के लिए `previous_interaction_id` का इस्तेमाल करने से रोकता है.

पैसे चुकाकर इस्तेमाल किए जाने वाले टियर के प्रोजेक्ट के लिए, [AI Studio](https://aistudio.google.com/logs?hl=hi) में जाकर, डेटा के रखरखाव की अवधि को कॉन्फ़िगर किया जा सकता है. इससे, प्रोजेक्ट स्टोरेज से लॉग अपने-आप मिटने के लिए मार्क हो जाते हैं. ऐसा 7, 14, 28 या 55 दिनों के बाद होता है. डेटा को कम समय तक सेव रखने से, पिछली बातचीत को वापस पाने में समस्या आ सकती है.

[`delete`](https://ai.google.dev/api/interactions-api?hl=hi#deleteInteraction) तरीके का इस्तेमाल करके, सेव किए गए इंटरैक्शन को किसी भी समय मिटाया जा सकता है. इसके लिए, इंटरैक्शन आईडी की ज़रूरत होती है. [AI Studio](https://aistudio.google.com/logs?hl=hi) में जाकर, सेव किए गए इंटरैक्शन के लॉग देखे और मैनेज किए जा सकते हैं. इनमें प्रोजेक्ट स्टोरेज से लॉग मिटाना भी शामिल है.

डेटा के रखरखाव की अवधि खत्म होने के बाद, आपका डेटा अपने-आप मिट जाएगा.

इंटरैक्शन ऑब्जेक्ट को [शर्तों](https://ai.google.dev/gemini-api/terms?hl=hi) के मुताबिक प्रोसेस किया जाता है.

### AI Studio में इंटरैक्शन देखना

यह एपीआई, पैसे चुकाकर ली गई सदस्यता वाले टियर के प्रोजेक्ट के लिए, `store=true` के साथ किए गए Interactions API के अनुरोधों को सेव करता है. इन्हें सीधे तौर पर [Google AI Studio के लॉग पेज](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=hi) पर देखा जा सकता है. ज़्यादा जानकारी के लिए, [लॉग गाइड](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=hi) देखें.

## सबसे सही तरीके

- **कैश हिट रेट**: इंप्लिसिट कैश मेमोरी, स्टेटफ़ुल और स्टेटलेस, दोनों मोड में काम करती है. इसके बारे में जानने के लिए, [क्विकस्टार्ट गाइड](https://ai.google.dev/gemini-api/docs/get-started?hl=hi#4_multi-turn_conversations) देखें. बातचीत जारी रखने के लिए, `previous_interaction_id` (स्टेटफ़ुल) का इस्तेमाल करने से सिस्टम को बातचीत के इतिहास के लिए, इंप्लिसिट कैश मेमोरी का इस्तेमाल करने में आसानी होती है. इससे परफ़ॉर्मेंस बेहतर होती है और लागत कम होती है.
- **एजेंट और मॉडल के साथ इंटरैक्शन को मिक्स करना**: आपके पास बातचीत के दौरान, एजेंट और मॉडल के साथ इंटरैक्शन को मिक्स करने का विकल्प होता है. उदाहरण के लिए, शुरुआती डेटा इकट्ठा करने के लिए, Deep Research एजेंट जैसे किसी खास एजेंट का इस्तेमाल किया जा सकता है. इसके बाद, फ़ॉलो-अप टास्क के लिए, Gemini के स्टैंडर्ड मॉडल का इस्तेमाल किया जा सकता है. जैसे, खास जानकारी देना या फ़ॉर्मैट बदलना. इन चरणों को `previous_interaction_id` से लिंक किया जा सकता है.

## काम करने वाले मॉडल और एजेंट

| मॉडल का नाम | टाइप | मॉडल आईडी |
| --- | --- | --- |
| Gemini 3.8 Flash | मॉडल | `gemini-3.8-flash` |
| Gemini 3.7 Flash | मॉडल | `gemini-3.7-flash` |
| Gemini 3.6 Flash | मॉडल | `gemini-3.6-flash` |
| Gemini 3.5 Flash | मॉडल | `gemini-3.5-flash` |
| Gemini 3.1 Pro की झलक | मॉडल | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | मॉडल | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | मॉडल | `gemini-3.1-flash-lite` |
| Gemini 3 Flash की झलक | मॉडल | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | मॉडल | `gemini-2.5-pro` |
| Gemini 2.5 Flash | मॉडल | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | मॉडल | `gemini-2.5-flash-lite` |
| Gemini 3 Pro की इमेज | मॉडल | `gemini-3-pro-image` |
| Gemini 3.1 Flash की इमेज | मॉडल | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS की झलक | मॉडल | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | मॉडल | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | मॉडल | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | मॉडल | `lyria-3.5` |
| Lyria 3 की क्लिप की झलक | मॉडल | `lyria-3-clip-preview` |
| Lyria 3 Pro की झलक | मॉडल | `lyria-3-pro-preview` |
| Deep Research की झलक | एजेंट | `deep-research-preview-04-2026` |
| Deep Research की झलक | एजेंट | `deep-research-max-preview-04-2026` |
| Antigravity की झलक | एजेंट | `antigravity-preview-09-2026` |

## एसडीके

Interactions API को ऐक्सेस करने के लिए, Google GenAI SDK टूल के नए वर्शन का इस्तेमाल किया जा सकता है.

- Python में, यह `2.3.0` वर्शन से `google-genai` पैकेज है.
- JavaScript पर, यह `2.3.0` वर्शन से `@google/genai` पैकेज है.

[लाइब्रेरी](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) पेज पर जाकर, एसडीके इंस्टॉल करने के तरीके के बारे में ज़्यादा जानें.

## सीमाएं

- **रिमोट एमसीपी**: Gemini 3 में रिमोट एमसीपी की सुविधा काम नहीं करती. यह सुविधा जल्द ही उपलब्ध होगी.
- **सिलसिलेवार बातचीत करने वाले मॉडल के साथ काम करने की क्षमता**: बातचीत में अलग-अलग मॉडल (स्टेटफ़ुल या स्टेटलेस) का इस्तेमाल करते समय, बाद के मॉडल को पिछले मॉडल के आउटपुट मोड को इनपुट के तौर पर इस्तेमाल करने की सुविधा देनी होगी. उदाहरण के लिए, अगर आपने `gemini-3.1-flash-image` का इस्तेमाल करके कोई इमेज जनरेट की है, तो उस बातचीत को ऐसे मॉडल के साथ जारी नहीं रखा जा सकता जो इमेज इनपुट स्वीकार नहीं करता. जैसे, सिर्फ़ टेक्स्ट वाला मॉडल या संगीत जनरेट करने वाला मॉडल, जैसे कि Lyria.

नीचे दी गई सुविधाएं, [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=hi) एपीआई के साथ काम करती हैं. हालांकि, ये सुविधाएं Interactions API में **अभी उपलब्ध नहीं हैं**:

- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**
- **[फ़ंक्शन को अपने-आप कॉल करने की सुविधा (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=hi#automatic_function_calling_python_only)**
- **[एक्सप्लिसिट कैश मेमोरी](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**: ध्यान दें कि सर्वर साइड पर इंप्लिसिट कैश मेमोरी, Interactions API में `previous_interaction_id` के ज़रिए उपलब्ध होती है.
- **[सुरक्षा सेटिंग](https://ai.google.dev/gemini-api/docs/safety-settings?hl=hi)**: Interactions API में, सुरक्षा से जुड़ी कस्टम सेटिंग मौजूद नहीं हैं.

## सुझाव/राय दें या शिकायत करें

Interactions API को बेहतर बनाने के लिए, आपका सुझाव/राय या शिकायत हमारे लिए अहम है.
अपने विचार शेयर करें, बग की शिकायत करें या हमारी [Google AI डेवलपर कम्यूनिटी फ़ोरम](https://discuss.ai.google.dev/c/gemini-api/4?hl=hi) पर सुविधाओं का अनुरोध करें.

## आगे क्या करना है

- [Interactions API का इस्तेमाल शुरू करने के लिए क्विकस्टार्ट नोटबुक](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=hi) आज़माएं.
- [Gemini Deep Research एजेंट](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) के बारे में ज़्यादा जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया."],[],[]]
