---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=hi
fetched_at: 2026-05-11T12:33:49.630778+00:00
title: "\u090f\u092a\u0940\u0906\u0908 \u0935\u0930\u094d\u0936\u0928 \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u091c\u093e\u0928\u0915\u093e\u0930\u0940 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [एपीआई का संदर्भ](https://ai.google.dev/api?hl=hi)

सुझाव भेजें

# एपीआई वर्शन के बारे में जानकारी

इस दस्तावेज़ में, Gemini API के `v1` और `v1beta` वर्शन के बीच के अंतर के बारे में खास जानकारी दी गई है.

- **v1**: एपीआई का स्टेबल वर्शन. स्टेबल वर्शन में मौजूद सुविधाएं, मुख्य वर्शन के पूरे लाइफ़टाइम में पूरी तरह से काम करती हैं. अगर कोई बड़ा बदलाव होता है, तो एपीआई का अगला मुख्य वर्शन बनाया जाएगा. साथ ही, मौजूदा वर्शन को कुछ समय बाद बंद कर दिया जाएगा.
  एपीआई के मुख्य वर्शन में बदलाव किए बिना, एपीआई में ऐसे बदलाव किए जा सकते हैं जिनसे मौजूदा सिस्टम पर कोई असर नहीं पड़ता.
- **v1beta**: इस वर्शन में शुरुआती सुविधाएँ शामिल हैं. ये सुविधाएँ अभी डेवलपमेंट के चरण में हो सकती हैं और इनमें बड़े बदलाव किए जा सकते हैं. इस बात की भी कोई गारंटी नहीं है कि बीटा वर्शन में मौजूद सुविधाएं, स्टेबल वर्शन में भी उपलब्ध होंगी. **अगर आपको प्रोडक्शन एनवायरमेंट में स्थिरता चाहिए और आप बदलावों को लागू करने का जोखिम नहीं ले सकते, तो आपको प्रोडक्शन में इस वर्शन का इस्तेमाल नहीं करना चाहिए.**

| सुविधा | v1 | v1beta |
| --- | --- | --- |
| कॉन्टेंट जनरेट करना - सिर्फ़ टेक्स्ट वाला इनपुट |  |  |
| कॉन्टेंट जनरेट करना - टेक्स्ट और इमेज का इनपुट |  |  |
| कॉन्टेंट जनरेट करना - टेक्स्ट आउटपुट |  |  |
| कॉन्टेंट जनरेट करना - कई बार बातचीत करना (चैट) |  |  |
| कॉन्टेंट जनरेट करना - फ़ंक्शन कॉल |  |  |
| कॉन्टेंट जनरेट करना - स्ट्रीमिंग |  |  |
| कॉन्टेंट एम्बेड करना - सिर्फ़ टेक्स्ट वाला इनपुट |  |  |
| जवाब जनरेट करें |  |  |
| सिमैंटिक रिट्रीवर |  |  |
| Interactions API |  |  |

- - काम करता है
- - इसका इस्तेमाल कभी नहीं किया जा सकेगा

## किसी एसडीके में एपीआई का वर्शन कॉन्फ़िगर करना

Gemini API SDK का डिफ़ॉल्ट वर्शन `v1beta` है. हालांकि, एपीआई वर्शन को सेट करके, अन्य वर्शन का इस्तेमाल किया जा सकता है. इसके लिए, यहां दिए गए कोड सैंपल का इस्तेमाल करें:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया."],[],[]]
