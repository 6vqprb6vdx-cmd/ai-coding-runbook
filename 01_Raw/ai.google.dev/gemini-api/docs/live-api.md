---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=hi
fetched_at: 2026-09-07T05:30:29.139996+00:00
title: "Gemini Live API \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u0916\u093e\u0938 \u091c\u093e\u0928\u0915\u093e\u0930\u0940 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Live API के बारे में खास जानकारी

Live API की मदद से, Gemini के साथ कम समय में रीयल-टाइम में बोलकर और देखकर बातचीत की जा सकती है. यह ऑडियो, इमेज, और टेक्स्ट की लगातार स्ट्रीम को प्रोसेस करता है, ताकि तुरंत, इंसानों की तरह बोलकर जवाब दिए जा सकें. इससे आपके उपयोगकर्ताओं को बातचीत का स्वाभाविक अनुभव मिलता है.

![Live API के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=hi)

[Google AI Studio में Live API आज़माएंmic](https://aistudio.google.com/live?hl=hi)
[GitHub पर मौजूद उदाहरण वाले ऐप्लिकेशन क्लोन करेंcode](https://github.com/google-gemini/gemini-live-api-examples)
[कोडिंग एजेंट की स्किल का इस्तेमाल करेंterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi)

## इस्तेमाल के उदाहरण

Live API का इस्तेमाल करके, कई इंडस्ट्री के लिए रीयल-टाइम में बोलकर बातचीत करने वाले एजेंट बनाए जा सकते हैं. इनमें ये इंडस्ट्री शामिल हैं:

- **ई-कॉमर्स और खुदरा कारोबार:** शॉपिंग असिस्टेंट, जो लोगों की पसंद के हिसाब से सुझाव देते हैं. साथ ही, ग्राहक सहायता एजेंट, जो ग्राहकों की समस्याओं को हल करते हैं.
- **गेमिंग:** इंटरैक्टिव नॉन-प्लेयर कैरेक्टर (एनपीसी), इन-गेम सहायता असिस्टेंट, और इन-गेम कॉन्टेंट का रीयल-टाइम में अनुवाद.
- **नेक्स्ट-जनरेशन इंटरफ़ेस:** रोबोटिक्स, स्मार्ट ग्लास, और वाहनों में आवाज़ और वीडियो की सुविधा वाले अनुभव.
- **स्वास्थ्य सेवा:** मरीज़ों की मदद और उन्हें जानकारी देने के लिए, हेल्थ कंपैनियन.
- **वित्तीय सेवाएं:** धन के प्रबंधन और निवेश के बारे में सलाह देने के लिए, एआई सलाहकार.
- **शिक्षा:** एआई मेंटर और लर्नर कंपैनियन, जो लोगों की ज़रूरतों के हिसाब से निर्देश और सुझाव देते हैं.
- **अनुवाद और स्थानीयकरण:** बोली जाने वाली बातचीत का रीयल-टाइम में, कम समय में अनुवाद. इससे अलग-अलग भाषाओं में आसानी से बातचीत की जा सकती है.

## मुख्य सुविधाएं

Live API, बोलकर बातचीत करने वाले मज़बूत एजेंट बनाने के लिए कई सुविधाएं उपलब्ध कराता है:

- [**कई भाषाओं में काम करने की सुविधा**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#supported-languages):
  70 भाषाओं में बातचीत की जा सकती है.
- [**बार्ज-इन**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#interruptions):
  उपयोगकर्ता, बातचीत के दौरान किसी भी समय मॉडल को रोक सकते हैं, ताकि उन्हें तुरंत जवाब मिल सकें.
- [**टूल का इस्तेमाल**](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi):
  इसमें फ़ंक्शन कॉलिंग और Google Search जैसे टूल इंटिग्रेट किए जा सकते हैं, ताकि डाइनैमिक तरीके से बातचीत की जा सके.
- [**ऑडियो ट्रांसक्रिप्ट**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#audio-transcription):
  इसमें उपयोगकर्ता के इनपुट और मॉडल आउटपुट, दोनों की टेक्स्ट ट्रांसक्रिप्ट मिलती हैं.
- [**प्रोऐक्टिव ऑडियो**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#proactive-audio):
  इससे यह कंट्रोल किया जा सकता है कि मॉडल कब और किन संदर्भों में जवाब दे.
- [**अफ़ेक्टिव डायलॉग**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#affective-dialog):
  यह उपयोगकर्ता के इनपुट एक्सप्रेशन के हिसाब से, जवाब देने के तरीके और टोन को अडजस्ट करता है.
- [**लाइव ट्रांसलेशन**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=hi):
  70 से ज़्यादा भाषाओं में, आवाज़ से आवाज़ में रीयल-टाइम में अनुवाद की सुविधा.

## तकनीकी जानकारी

यहां दी गई टेबल में, Live API की तकनीकी जानकारी दी गई है:

| कैटगरी | विवरण |
| --- | --- |
| इनपुट मोडेलिटी | ऑडियो (रॉ 16-बिट पीसीएम ऑडियो, 16 किलोहर्ट्ज़, लिटिल-एंडियन), इमेज (जेपीईजी <= 1एफ़पीएस), टेक्स्ट |
| आउटपुट मोडेलिटी | ऑडियो (रॉ 16-बिट पीसीएम ऑडियो, 24 किलोहर्ट्ज़, लिटिल-एंडियन) |
| प्रोटोकॉल | स्टेटफ़ुल WebSocket कनेक्शन (WSS) |

## इस सुविधा को लागू करने का तरीका चुनना

Live API को इंटिग्रेट करते समय, आपको इस सुविधा को लागू करने के लिए इनमें से कोई एक तरीका चुनना होगा:

- **सर्वर-टू-सर्वर**: आपका बैकएंड,
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) का इस्तेमाल करके Live API से कनेक्ट होता है. आम तौर पर, आपका क्लाइंट स्ट्रीम डेटा (ऑडियो, वीडियो, टेक्स्ट) आपके सर्वर को भेजता है. इसके बाद, आपका सर्वर इसे Live API को फ़ॉरवर्ड करता है.
- **क्लाइंट-टू-सर्वर**: आपका फ़्रंटएंड कोड, डेटा स्ट्रीम करने के लिए [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) का इस्तेमाल करके सीधे Live API
  से कनेक्ट होता है. इसमें आपके बैकएंड की ज़रूरत नहीं होती.

## शुरू करें

वह गाइड चुनें जो आपके डेवलपमेंट एनवायरमेंट से मेल खाती हो:

सर्वर-टू-सर्वर

### [GenAI SDK का ट्यूटोरियल](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=hi)

Python बैकएंड वाले रीयल-टाइम मल्टीमॉडल ऐप्लिकेशन बनाने के लिए, GenAI SDK का इस्तेमाल करके Gemini Live API से कनेक्ट करें.

क्लाइंट-टू-सर्वर

### [WebSocket का ट्यूटोरियल](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=hi)

JavaScript फ़्रंटएंड और कुछ समय के लिए मान्य टोकन वाले रीयल-टाइम मल्टीमॉडल ऐप्लिकेशन बनाने के लिए, WebSockets का इस्तेमाल करके Gemini Live API से कनेक्ट करें.

एजेंट डेवलपमेंट किट

### [ADK का ट्यूटोरियल](https://google.github.io/adk-docs/streaming/)

कोई एजेंट बनाएं और आवाज़ और वीडियो के ज़रिए बातचीत करने की सुविधा चालू करने के लिए, एजेंट डेवलपमेंट किट (एडीके) स्ट्रीमिंग का इस्तेमाल करें.

## पार्टनर इंटीग्रेशन

रीयल-टाइम में ऑडियो और वीडियो ऐप्लिकेशन के डेवलपमेंट को आसान बनाने के लिए, तीसरे पक्ष के इंटिग्रेशन का इस्तेमाल किया जा सकता है.
यह इंटिग्रेशन, WebRTC या WebSockets पर Gemini Live
API के साथ काम करता है.

[LiveKit

LiveKit एजेंट के साथ Gemini Live API का इस्तेमाल करें.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Daily का Pipecat

Gemini Live और Pipecat का इस्तेमाल करके, रीयल-टाइम में एआई चैटबॉट बनाएं.](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion का Fishjam

Fishjam की मदद से, लाइव वीडियो और ऑडियो स्ट्रीमिंग ऐप्लिकेशन बनाएं.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Stream के Vision Agents

Vision Agents की मदद से, रीयल-टाइम में आवाज़ और वीडियो की सुविधा वाले एआई ऐप्लिकेशन बनाएं.](https://visionagents.ai/integrations/gemini)
[Voximplant

Voximplant की मदद से, इनबाउंड और आउटबाउंड कॉल को Live API से कनेक्ट करें.](https://voximplant.com/products/gemini-client)
[Agora

अगोरा की मदद से, रीयल-टाइम में बातचीत करने वाले एआई ऐप्लिकेशन बनाएं.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Firebase AI Logic का इस्तेमाल करके, Gemini Live API का इस्तेमाल शुरू करें.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-12 (UTC) को अपडेट किया गया."],[],[]]
