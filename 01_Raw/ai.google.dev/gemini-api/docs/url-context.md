---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=hi
fetched_at: 2026-07-06T05:16:19.213385+00:00
title: "\u092f\u0942\u0906\u0930\u090f\u0932 \u0915\u093e \u0915\u0949\u0928\u094d\u091f\u0947\u0915\u094d\u0938\u094d\u091f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# यूआरएल का कॉन्टेक्स्ट

यूआरएल कॉन्टेक्स्ट टूल की मदद से, मॉडल को यूआरएल के तौर पर अतिरिक्त कॉन्टेक्स्ट दिया जा सकता है. अपने अनुरोध में यूआरएल शामिल करके, मॉडल उन पेजों का कॉन्टेंट ऐक्सेस कर पाएगा. हालांकि, ऐसा तब ही होगा, जब यूआरएल का टाइप [सीमाएं सेक्शन](#limitations) में दिए गए यूआरएल टाइप में शामिल न हो. इससे मॉडल को जवाब देने और उसे बेहतर बनाने में मदद मिलेगी.

यूआरएल कॉन्टेक्स्ट टूल, इन जैसे कामों के लिए मददगार होता है:

- **डेटा निकालना**: एक से ज़्यादा यूआरएल से खास जानकारी निकालना. जैसे, कीमतें, नाम या मुख्य नतीजे.
- **दस्तावेज़ों की तुलना करना**: रुझानों का पता लगाने और अंतरों की पहचान करने के लिए, एक से ज़्यादा रिपोर्ट, लेख या PDF का विश्लेषण करें.
- **कॉन्टेंट बनाना और जानकारी इकट्ठा करना**: सटीक जवाब, ब्लॉग पोस्ट या रिपोर्ट जनरेट करने के लिए, कई सोर्स यूआरएल से जानकारी इकट्ठा करें.
- **कोड और दस्तावेज़ों का विश्लेषण करना**: कोड के बारे में जानकारी देने, सेटअप करने के निर्देश जनरेट करने या सवालों के जवाब देने के लिए, GitHub रिपॉज़िटरी या तकनीकी दस्तावेज़ पर जाएं.

यहां दिए गए उदाहरण में, अलग-अलग वेबसाइटों की दो रेसिपी की तुलना करने का तरीका बताया गया है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## यह कैसे काम करता है

यूआरएल कॉन्टेक्स्ट टूल, डेटा को दो चरणों में इकट्ठा करता है. इससे, तेज़ी से डेटा इकट्ठा करने, कम लागत, और नए डेटा को ऐक्सेस करने के बीच संतुलन बनाए रखने में मदद मिलती है. यूआरएल देने पर, यह टूल सबसे पहले इंटरनल इंडेक्स कैश मेमोरी से कॉन्टेंट फ़ेच करने की कोशिश करता है. यह एक ऑप्टिमाइज़ की गई कैश मेमोरी के तौर पर काम करता है. अगर कोई यूआरएल इंडेक्स में उपलब्ध नहीं है (उदाहरण के लिए, अगर यह बहुत नया पेज है), तो टूल अपने-आप लाइव फ़ेच करने की सुविधा पर वापस चला जाता है.
यह सीधे तौर पर यूआरएल को ऐक्सेस करता है, ताकि रीयल टाइम में उसका कॉन्टेंट वापस पाया जा सके.

## अन्य टूल के साथ इस्तेमाल करना

यूआरएल के कॉन्टेक्स्ट की जानकारी देने वाले टूल को अन्य टूल के साथ मिलाकर, ज़्यादा असरदार वर्कफ़्लो बनाए जा सकते हैं.

[Gemini 3 मॉडल](#supported-models), कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ-साथ, पहले से मौजूद टूल (जैसे, यूआरएल कॉन्टेक्स्ट) को एक साथ इस्तेमाल करने की सुविधा देते हैं. [टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर, इस बारे में ज़्यादा जानें.

### खोज के नतीजों से जानकारी पाना

यूआरएल कॉन्टेक्स्ट और [Google Search से जानकारी पाना](https://ai.google.dev/gemini-api/docs/grounding?hl=hi), दोनों सुविधाएं चालू होने पर मॉडल, खोज से जुड़ी अपनी क्षमताओं का इस्तेमाल करके, ऑनलाइन काम की जानकारी ढूंढ सकता है. इसके बाद, यूआरएल कॉन्टेक्स्ट टूल का इस्तेमाल करके, उसे मिले पेजों के बारे में ज़्यादा जानकारी पा सकता है. यह तरीका उन प्रॉम्प्ट के लिए बहुत कारगर है जिनमें किसी विषय के बारे में ज़्यादा से ज़्यादा जानकारी खोजने के साथ-साथ, किसी खास पेज का बारीकी से विश्लेषण करने की ज़रूरत होती है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## जवाब को समझना

जब मॉडल, यूआरएल कॉन्टेक्स्ट टूल का इस्तेमाल करता है, तो उसके टेक्स्ट वाले जवाब में टेक्स्ट कॉन्टेंट ब्लॉक पर इनलाइन `url_citation` एनोटेशन शामिल होते हैं. हर एनोटेशन, जवाब के टेक्स्ट के एक सेगमेंट को उस सोर्स यूआरएल से लिंक करता है जिससे वह लिया गया है. ऐसा `start_index` और `end_index` के ज़रिए किया जाता है. अपने आवेदन में उद्धरण दिखाने का यह मुख्य तरीका है. इन्हें निकालने का तरीका जानने के लिए, [ऊपर दिया गया मुख्य उदाहरण](#get-started) देखें.

जवाब में `url_context_result` चरण भी शामिल होता है. इसमें, हर यूआरएल को वापस पाने की कोशिश के बारे में मेटाडेटा होता है. जैसे, स्थिति, वापस पाया गया यूआरएल. यह मुख्य रूप से डीबग करने के लिए
उपयोगी है.

### सुरक्षा जांच

सिस्टम, यूआरएल पर कॉन्टेंट मॉडरेशन की जांच करता है. इससे यह पुष्टि की जाती है कि यूआरएल, सुरक्षा मानकों के मुताबिक हैं. अगर कोई यूआरएल इस जांच में पास नहीं होता है, तो उससे जुड़े `url_context_result` चरण में `"unsafe"` का `status` दिखेगा.

### टोकन की संख्या

आपके प्रॉम्प्ट में दिए गए यूआरएल से वापस पाए गए कॉन्टेंट को, इनपुट टोकन के तौर पर गिना जाता है. इंटरैक्शन के `usage` ऑब्जेक्ट में, टोकन की संख्या देखी जा सकती है. यहां एक उदाहरण दिया गया है:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

हर टोकन की कीमत, इस्तेमाल किए गए मॉडल पर निर्भर करती है. ज़्यादा जानकारी के लिए, [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज देखें.

## इन मॉडल के साथ काम करता है

| मॉडल | यूआरएल का कॉन्टेक्स्ट |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## सबसे सही तरीके

- **खास यूआरएल दें**: बेहतर नतीजे पाने के लिए, उस कॉन्टेंट के डायरेक्ट यूआरएल दें जिसका आपको मॉडल से विश्लेषण कराना है. मॉडल सिर्फ़ आपके दिए गए यूआरएल से कॉन्टेंट को फिर से हासिल करेगा. यह नेस्ट किए गए लिंक से कोई कॉन्टेंट हासिल नहीं करेगा.
- **पक्का करें कि यूआरएल ऐक्सेस किए जा सकते हों**: पुष्टि करें कि आपके दिए गए यूआरएल, ऐसे पेजों पर रीडायरेक्ट न करते हों जिन्हें ऐक्सेस करने के लिए लॉग इन करने या पैसे चुकाने की ज़रूरत होती है.
- **पूरा यूआरएल इस्तेमाल करें**: पूरा यूआरएल दें.इसमें प्रोटोकॉल भी शामिल करें. उदाहरण के लिए, सिर्फ़ google.com के बजाय https://www.google.com.

## सीमाएं

- अनुरोध की सीमा: यह टूल, हर अनुरोध में ज़्यादा से ज़्यादा 20 यूआरएल प्रोसेस कर सकता है.
- यूआरएल के कॉन्टेंट का साइज़: किसी एक यूआरएल से लिए गए कॉन्टेंट का साइज़ 34 एमबी से ज़्यादा नहीं होना चाहिए.
- सार्वजनिक तौर पर ऐक्सेस किया जा सकने वाला यूआरएल: यूआरएल ऐसे होने चाहिए जिन्हें वेब पर सार्वजनिक तौर पर ऐक्सेस किया जा सके.
  लोकलहोस्ट पते (जैसे, localhost, 127.0.0.1), निजी नेटवर्क, और टनलिंग सेवाएं (जैसे, ngrok, pinggy) काम नहीं करती हैं.
- सिर्फ़ Gemini API के लिए: यूआरएल कॉन्टेक्स्ट की सुविधा सिर्फ़ Gemini API में उपलब्ध है. यह Gemini Enterprise Agent Platform के ज़रिए उपलब्ध नहीं है.

### इस्तेमाल किए जा सकने वाले और इस्तेमाल न किए जा सकने वाले कॉन्टेंट टाइप

यह टूल, इन तरह के कॉन्टेंट वाले यूआरएल से कॉन्टेंट निकाल सकता है:

- टेक्स्ट (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- इमेज (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

इस तरह के कॉन्टेंट के लिए, यह सुविधा **काम नहीं करती**:

- Paywall की गई सामग्री
- YouTube वीडियो (YouTube के यूआरएल प्रोसेस करने का तरीका जानने के लिए, [वीडियो समझने की सुविधा](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi#youtube) देखें)
- Google Workspace की फ़ाइलें, जैसे कि Google Docs या स्प्रेडशीट
- वीडियो और ऑडियो फ़ाइलें

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
