---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=hi
fetched_at: 2026-08-17T02:23:59.654528+00:00
title: "Google AI Studio \u0938\u0947 \u091c\u0941\u0921\u093c\u0940 \u0938\u092e\u0938\u094d\u092f\u093e \u0939\u0932 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google AI Studio से जुड़ी समस्या हल करना

इस पेज पर, Google AI Studio में आने वाली समस्याओं को हल करने के सुझाव दिए गए हैं.

## ऐक्सेस से जुड़ी पाबंदी की वजह से दिखने वाली 403 गड़बड़ी के बारे में जानकारी

[अगर आपको 'ऐक्सेस से जुड़ी पाबंदी की वजह से दिखने वाली 403 गड़बड़ी' दिखती है, तो इसका मतलब है कि आपने Google AI Studio का इस्तेमाल, सेवा की शर्तों के मुताबिक नहीं किया है.](https://ai.google.dev/terms?hl=hi) इसकी एक आम वजह यह है कि
आप किसी ऐसे [इलाके में मौजूद नहीं हैं जहां यह सुविधा उपलब्ध है](https://ai.google.dev/available_regions?hl=hi).

## Google AI Studio पर, 'कोई कॉन्टेंट नहीं है' के जवाब से जुड़ी समस्या हल करना

अगर किसी वजह से कॉन्टेंट को ब्लॉक किया जाता है, तो
Google AI Studio पर warning **कोई कॉन्टेंट नहीं है** की चेतावनी दिखती है. ज़्यादा जानकारी देखने के लिए,
**कोई कॉन्टेंट नहीं है** पर कर्सर घुमाएं और
warning **सुरक्षा** पर क्लिक करें.

अगर [सुरक्षा सेटिंग](https://ai.google.dev/docs/safety_setting?hl=hi) की वजह से जवाब ब्लॉक किया गया है और आपने अपने इस्तेमाल के उदाहरण के लिए [सुरक्षा से जुड़े जोखिमों](https://ai.google.dev/docs/safety_guidance?hl=hi) पर विचार किया है, तो [सुरक्षा सेटिंग](https://ai.google.dev/docs/safety_setting?hl=hi#safety_settings_in_makersuite) में बदलाव करके, दिखाए गए जवाब को बदला जा सकता है.

अगर जवाब को सुरक्षा सेटिंग की वजह से ब्लॉक नहीं किया गया है, तो हो सकता है कि क्वेरी या
जवाब, [सेवा की शर्तों](https://ai.google.dev/terms?hl=hi) का उल्लंघन करता हो या यह सुविधा उपलब्ध न हो.

## टोकन के इस्तेमाल और उसकी सीमाओं की जानकारी देखना

प्रॉम्प्ट खुला होने पर, स्क्रीन पर सबसे नीचे मौजूद **टेक्स्ट का प्रीव्यू** बटन, आपके प्रॉम्प्ट के कॉन्टेंट के लिए इस्तेमाल किए गए मौजूदा टोकन और इस्तेमाल किए जा रहे मॉडल के लिए टोकन की ज़्यादा से ज़्यादा संख्या दिखाता है.

## AI Studio के लिए Google Cloud IAM अनुमतियां

Google AI Studio में कार्रवाइयां करने के लिए, Google Cloud प्रोजेक्ट के सदस्यों के पास, पहचान और ऐक्सेस मैनेजमेंट (आईएएम) की खास अनुमतियां होनी चाहिए. इन पहचानों के बारे में ज़्यादा जानने के लिए, [IAM प्रिंसिपल की खास जानकारी](https://cloud.google.com/iam/docs/principals?hl=hi) देखें.

लिंक किए गए Google Cloud प्रोजेक्ट में **एडिटर** या **मालिक** की भूमिका वाले उपयोगकर्ताओं के पास, डैशबोर्ड देखने और Gemini API पासकोड मैनेज करने की पूरी अनुमतियां होती हैं. **व्यूअर** की भूमिका वाले उपयोगकर्ता, डैशबोर्ड और एपीआई पासकोड देख सकते हैं. हालांकि, वे इन्हें बना, अपडेट या मिटा नहीं सकते.

ज़्यादा कंट्रोल के लिए, हर AI Studio सुविधा के लिए ज़रूरी खास अनुमतियों के बारे में जानने के लिए, यह टेबल देखें. इन अनुमतियों को देने के तरीके के बारे में जानने के लिए, Google Cloud के दस्तावेज़ में, [संसाधनों का ऐक्सेस देना, बदलना, और वापस लेना](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=hi) लेख पढ़ें.

| AI Studio की सुविधा | आईएएम की ज़रूरी अनुमतियां | अन्य ज़रूरी शर्तें |
| --- | --- | --- |
| **प्रोजेक्ट खोजना** (प्रोजेक्ट इंपोर्ट करना) | `resourcemanager.projects.get` |  |
| **प्रोजेक्ट का नाम बदलना** | `resourcemanager.projects.update` |  |
| **कोटा टियर दिखाना** | लागू नहीं |  |
| **एपीआई पासकोड बनाना** | **प्रोजेक्ट खोजने** की अनुमतियां होना और:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **एपीआई पासकोड की सूची देखना** | **प्रोजेक्ट खोजने** की अनुमतियां होना और:  `apikeys.keys.list` `serviceusage.services.get` | Google Cloud प्रोजेक्ट में, [जनरेटिव लैंग्वेज एपीआई](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=hi) चालू होना चाहिए. |
| **एपीआई पासकोड के नाम बदलना** | `apikeys.keys.update` |  |
| **एपीआई पासकोड मिटाना** | `apikeys.keys.delete` |  |
| **इस्तेमाल की जानकारी वाला डैशबोर्ड** | **प्रोजेक्ट खोजने** की अनुमतियां होना और:  `monitoring.timeSeries.list` |  |
| **रेट लिमिट डैशबोर्ड** | **इस्तेमाल की जानकारी वाले डैशबोर्ड** की अनुमतियां होना और:  `cloudquotas.quotas.get` |  |
| **खर्च की सीमा (बिलिंग कैप)** | `billing.resourceCosts.get` (खर्च देखने के लिए) `billing.resourcebudgets.read` (कैप देखने के लिए) `billing.resourcebudgets.write` (कैप सेट करने के लिए) |  |
| **बिलिंग डैशबोर्ड** | `billing.accounts.get` |  |

### ऐक्सेस की अन्य जांच

Google Cloud IAM अनुमतियों के अलावा, AI Studio सुरक्षा और अनुपालन की जांच भी करता है. अगर आपने यहां दी गई ज़रूरी शर्तें पूरी नहीं की हैं, तो आपको AI Studio इंटरफ़ेस या एपीआई के जवाबों में, `PERMISSION_DENIED` या ऐक्सेस से जुड़ी पाबंदी की गड़बड़ी दिख सकती है:

- **सुरक्षा जांच:** आपका अनुरोध, सुरक्षा से जुड़ी ऑटोमैटिक जांच में पास होना चाहिए.
- **सेवा की शर्तें:** आपको Google की सेवा की शर्तें और जनरेटिव एआई (AI) की सेवा की अन्य शर्तें स्वीकार करनी होंगी.
- **उपलब्धता वाला इलाका:** आपका किसी ऐसे इलाके में होना ज़रूरी है जहां यह सुविधा [उपलब्ध है](https://ai.google.dev/gemini-api/docs/available-regions?hl=hi).
- **भरोसेमंद और सुरक्षित होने से जुड़ी ज़रूरी शर्तें:** Google Cloud प्रोजेक्ट को, गलत इस्तेमाल के लिए फ़्लैग नहीं किया जाना चाहिए.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-29 (UTC) को अपडेट किया गया."],[],[]]
