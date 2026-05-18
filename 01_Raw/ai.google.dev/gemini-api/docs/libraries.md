---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=hi
fetched_at: 2026-05-18T13:11:23.689545+00:00
title: "Gemini API \u0932\u093e\u0907\u092c\u094d\u0930\u0947\u0930\u0940 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini API लाइब्रेरी

Gemini API का इस्तेमाल करके ऐप्लिकेशन बनाने के लिए, हम **Google GenAI SDK** का इस्तेमाल करने का सुझाव देते हैं.
ये आधिकारिक तौर पर इस्तेमाल के लिए तैयार लाइब्रेरी हैं. इन्हें हम सबसे ज़्यादा इस्तेमाल की जाने वाली भाषाओं के लिए बनाते हैं और इनका रखरखाव करते हैं. ये [सामान्य तौर पर उपलब्ध हैं](https://ai.google.dev/gemini-api/docs/libraries?hl=hi#new-libraries) और इनका इस्तेमाल हमारे सभी आधिकारिक दस्तावेज़ों और उदाहरणों में किया जाता है.

अगर आपने Gemini API का इस्तेमाल पहले कभी नहीं किया है, तो इसे इस्तेमाल करने के लिए हमारी [क्विकस्टार्ट गाइड](https://ai.google.dev/gemini-api/docs/quickstart?hl=hi) पढ़ें.

## भाषा से जुड़ी सहायता और इंस्टॉलेशन

Google GenAI SDK, Python, JavaScript/TypeScript, Go, और Java भाषाओं के लिए उपलब्ध है. पैकेज मैनेजर का इस्तेमाल करके, हर भाषा की लाइब्रेरी इंस्टॉल की जा सकती है. इसके अलावा, ज़्यादा जानकारी के लिए, उनकी GitHub रिपॉज़िटरी पर जाएं:

### Python

- लाइब्रेरी: [`google-genai`](https://pypi.org/project/google-genai)
- GitHub डेटा स्टोर करने की जगह: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- इंस्टॉलेशन: `pip install google-genai`

### JavaScript

- लाइब्रेरी: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- GitHub रिपॉज़िटरी: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- इंस्टॉलेशन: `npm install @google/genai`

### ऐप पर जाएं

- लाइब्रेरी: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- GitHub रिपॉज़िटरी: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- इंस्टॉलेशन: `go get google.golang.org/genai`

### Java

- लाइब्रेरी: `google-genai`
- GitHub रिपॉज़िटरी: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- इंस्टॉल करना: अगर Maven का इस्तेमाल किया जा रहा है, तो अपनी डिपेंडेंसी में यह जानकारी जोड़ें:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- लाइब्रेरी: `Google.GenAI`
- GitHub डेटा स्टोर करने की जगह: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- इंस्टॉलेशन: `dotnet add package Google.GenAI`

## सामान्य रूप से उपलब्ध

मई 2025 तक, Google GenAI SDK, सामान्य रूप से उपलब्ध (जीए) हो गया है. यह सभी प्लैटफ़ॉर्म पर उपलब्ध है. साथ ही, Gemini API को ऐक्सेस करने के लिए, इन लाइब्रेरी का इस्तेमाल करने का सुझाव दिया जाता है.
ये स्टेबल होते हैं. साथ ही, प्रोडक्शन में इस्तेमाल करने के लिए पूरी तरह से काम करते हैं. इसके अलावा, इन्हें लगातार अपडेट किया जाता है.
इनसे आपको नई सुविधाओं का ऐक्सेस मिलता है. साथ ही, ये Gemini के साथ काम करने पर सबसे अच्छी परफ़ॉर्मेंस देते हैं.

अगर हमारी किसी लेगसी लाइब्रेरी का इस्तेमाल किया जा रहा है, तो हमारा सुझाव है कि आप माइग्रेट करें. इससे आपको नई सुविधाओं का ऐक्सेस मिलेगा. साथ ही, Gemini के साथ काम करते समय आपको बेहतर परफ़ॉर्मेंस मिलेगी. ज़्यादा जानकारी के लिए, [लेगसी लाइब्रेरी](https://ai.google.dev/gemini-api/docs/libraries?hl=hi#previous-sdks) सेक्शन देखें.

## लेगसी लाइब्रेरी और माइग्रेशन

अगर हमारी किसी लेगसी लाइब्रेरी का इस्तेमाल किया जा रहा है, तो हमारा सुझाव है कि आप [नई लाइब्रेरी पर माइग्रेट करें](https://ai.google.dev/gemini-api/docs/migrate?hl=hi).

लेगसी लाइब्रेरी से, नई सुविधाओं (जैसे कि [लाइव एपीआई](https://ai.google.dev/gemini-api/docs/live?hl=hi) और [Veo](https://ai.google.dev/gemini-api/docs/video?hl=hi)) का ऐक्सेस नहीं मिलता. साथ ही, ये 30 नवंबर, 2025 से काम नहीं करेंगी.

हर लेगसी लाइब्रेरी के लिए, सहायता की स्थिति अलग-अलग होती है. इसके बारे में यहां दी गई टेबल में बताया गया है:

| भाषा | लेगसी लाइब्रेरी | सहायता का स्टेटस | सुझाई गई लाइब्रेरी |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | इसकी देखभाल नहीं की जा रही है | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | इसकी देखभाल नहीं की जा रही है | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | इसकी देखभाल नहीं की जा रही है | `google.golang.org/genai` |
| **Dart और Flutter** | `google_generative_ai` | इसकी देखभाल नहीं की जा रही है | [Genkit Dart](https://genkit.dev/docs/dart/get-started/) या [Firebase AI Logic](https://pub.dev/packages/firebase_ai) का इस्तेमाल करना |
| **Swift** | `generative-ai-swift` | इसकी देखभाल नहीं की जा रही है | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=hi) का इस्तेमाल करना |
| **Android** | `generative-ai-android` | इसकी देखभाल नहीं की जा रही है | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=hi) का इस्तेमाल करना |

**Java डेवलपर के लिए ध्यान दें:** Gemini API के लिए, Google की ओर से उपलब्ध कराया गया कोई लेगसी Java SDK टूल नहीं था. इसलिए, Google की पिछली लाइब्रेरी से माइग्रेट करने की ज़रूरत नहीं है. [भाषा से जुड़ी सहायता और इंस्टॉलेशन](#install) सेक्शन में जाकर, सीधे नई लाइब्रेरी का इस्तेमाल शुरू किया जा सकता है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-13 (UTC) को अपडेट किया गया."],[],[]]
