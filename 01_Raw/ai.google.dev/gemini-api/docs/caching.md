---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=hi
fetched_at: 2026-09-14T05:49:16.370778+00:00
title: "\u0915\u0949\u0928\u094d\u091f\u0947\u0915\u094d\u0938\u094d\u091f \u0915\u0948\u0936 \u092e\u0947\u092e\u094b\u0930\u0940 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# कॉन्टेक्स्ट कैश मेमोरी

एआई के सामान्य वर्कफ़्लो में, किसी मॉडल को एक ही इनपुट टोकन बार-बार पास किया जा सकता है. Gemini API, परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ करने के लिए, इंप्लिसिट कैशिंग की सुविधा देता है.

## इंप्लिसिट कैशिंग

Gemini 2.5 और इसके बाद के सभी मॉडल के लिए, इंप्लिसिट कैशिंग की सुविधा डिफ़ॉल्ट रूप से चालू होती है. यह सुविधा, [स्टेटफ़ुल](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#multi-turn-conversations) (जिसमें `previous_interaction_id` का इस्तेमाल किया जाता है)
और [स्टेटलेस](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#stateless-conversations), दोनों तरह के बातचीत के मोड के लिए उपलब्ध है.
अगर आपका अनुरोध कैश हिट करता है, तो हम लागत में होने वाली बचत को अपने-आप पास कर देते हैं. इसे चालू करने के लिए, आपको कुछ भी करने की ज़रूरत नहीं है. कॉन्टेक्स्ट कैशिंग के लिए, हर मॉडल के लिए इनपुट टोकन की गिनती की कम से कम संख्या यहां दी गई है:

| मॉडल | टोकन की कम से कम सीमा |
| --- | --- |
| Gemini 3.8 Flash | 4,096 |
| Gemini 3.7 Flash | 4,096 |
| Gemini 3.6 Flash | 4,096 |
| Gemini 3.5 Flash | 4,096 |
| Gemini 3.1 Pro का प्रीव्यू | 4,096 |
| Gemini 2.5 Flash | 2,048 |
| Gemini 2.5 Pro | 2,048 |

इंप्लिसिट कैश हिट होने की संभावना बढ़ाने के लिए:

- अपने प्रॉम्प्ट की शुरुआत में, बड़ा और सामान्य कॉन्टेंट शामिल करें
- कम समय में, एक जैसे प्रीफ़िक्स वाले अनुरोध भेजने की कोशिश करें

रिस्पॉन्स ऑब्जेक्ट के `usage.total_cached_tokens` (Python और JavaScript) फ़ील्ड में, कैश हिट करने वाले टोकन की संख्या देखी जा सकती है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-10 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-10 (UTC) को अपडेट किया गया."],[],[]]
