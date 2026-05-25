---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi
fetched_at: 2026-05-25T12:58:25.015349+00:00
title: "\u092a\u094d\u0930\u093e\u0925\u092e\u093f\u0915\u0924\u093e \u0915\u0947 \u0906\u0927\u093e\u0930 \u092a\u0930 \u0905\u0928\u0941\u092e\u093e\u0928 \u0932\u0917\u093e\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# प्राथमिकता के आधार पर अनुमान लगाना

Gemini Priority API, अनुमान लगाने के लिए प्रीमियम लेवल का एपीआई है. इसे कारोबार के लिए ज़रूरी उन वर्कलोड के लिए डिज़ाइन किया गया है जिनके लिए कम इंतज़ार का समय और ज़्यादा भरोसेमंद परफ़ॉर्मेंस की ज़रूरत होती है. इसके लिए, प्रीमियम कीमत चुकानी पड़ती है. Priority लेवल के ट्रैफ़िक को, स्टैंडर्ड एपीआई और Flex लेवल के ट्रैफ़िक से ज़्यादा प्राथमिकता दी जाती है.

GenerateContent API
और Interactions API के एंडपॉइंट पर, [Tier 2 और Tier 3](https://ai.google.dev/gemini-api/docs/billing?hl=hi#about-billing) के उपयोगकर्ता, प्राथमिकता के साथ अनुमान लगाने की सुविधा का इस्तेमाल कर सकते हैं.

## प्राथमिकता के साथ अनुमान लगाने की सुविधा का इस्तेमाल करना

Priority लेवल का इस्तेमाल करने के लिए, अनुरोध के मुख्य हिस्से में मौजूद `service_tier` फ़ील्ड को `priority` पर सेट करें. अगर फ़ील्ड को छोड़ दिया जाता है, तो डिफ़ॉल्ट लेवल स्टैंडर्ड होता है.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.5-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## प्राथमिकता के साथ अनुमान लगाने की सुविधा कैसे काम करती है

प्राथमिकता के साथ अनुमान लगाने की सुविधा, अनुरोधों को ज़्यादा अहमियत वाली कंप्यूटिंग क्यू में भेजती है. इससे, उपयोगकर्ता के लिए बने ऐप्लिकेशन के लिए, अनुमान के मुताबिक और तेज़ परफ़ॉर्मेंस मिलती है. इसका मुख्य तरीका यह है कि डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक होने पर, सर्वर-साइड पर स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड किया जाता है. इससे अनुरोध को अस्वीकार करने के बजाय, ऐप्लिकेशन की स्थिरता बनी रहती है.

| सुविधा | प्राथमिकता | स्टैंडर्ड | Flex | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | स्टैंडर्ड से 75-100% ज़्यादा | फ़ुल टिकट | 50% की छूट | 50% की छूट |
| **Latency** | सेकंड | सेकंड से मिनट | मिनट (1–15 मिनट का टारगेट) | 24 घंटे तक |
| **भरोसेमंद परफ़ॉर्मेंस** | ज़्यादा (इसे कम नहीं किया जा सकता) | ज़्यादा / मीडियम-ज़्यादा | बेस्ट-एफ़र्ट (इसे कम किया जा सकता है) | ज़्यादा (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **कम इंतज़ार का समय**: इसे इंटरैक्टिव,
  उपयोगकर्ता के लिए बने एआई टूल के लिए, सेकंड में जवाब देने के हिसाब से डिज़ाइन किया गया है.
- **ज़्यादा भरोसेमंद परफ़ॉर्मेंस**: ट्रैफ़िक को सबसे ज़्यादा अहमियत दी जाती है और इसे
  कम नहीं किया जा सकता.
- **अनुकूल गिरावट**: डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक बढ़ने पर, इसे प्रोसेस करने के लिए, स्टैंडर्ड लेवल पर अपने-आप डाउनग्रेड कर दिया जाता है.
  इससे, सेवा में रुकावट नहीं आती.
- **कम मुश्किल**: यह `generateContent` तरीके का इस्तेमाल,
  स्टैंडर्ड और Flex लेवल की तरह ही करता है.

### इस्तेमाल के उदाहरण

प्राथमिकता के साथ प्रोसेसिंग, कारोबार के लिए ज़रूरी उन वर्कफ़्लो के लिए सबसे सही है जिनमें परफ़ॉर्मेंस और भरोसेमंद परफ़ॉर्मेंस सबसे अहम होती है.

- **इंटरैक्टिव एआई ऐप्लिकेशन**: ग्राहक सेवा के चैटबॉट और कोपायलट. इनके लिए
  उपयोगकर्ता प्रीमियम चुकाते हैं और उन्हें तेज़ और लगातार जवाब मिलने की उम्मीद होती है.
- **रीयल-टाइम डिसिजन इंजन**: ऐसे सिस्टम जिनमें ज़्यादा भरोसेमंद और कम इंतज़ार के समय वाले
  नतीजों की ज़रूरत होती है. जैसे, लाइव टिकट ट्राइएज या धोखाधड़ी का पता लगाना.
- **प्रीमियम ग्राहकों के लिए सुविधाएं**: ऐसे डेवलपर जिन्हें पैसे चुकाने वाले ग्राहकों के लिए, बेहतर सर्विस
  लेवल ऑब्जेक्टिव (एसएलओ) की गारंटी देनी होती है.

### रेट लिमिट

प्राथमिकता के साथ अनुमान लगाने की सुविधा के लिए, अलग से रेट लिमिट होती हैं. हालांकि, इसके इस्तेमाल को,
[इंटरैक्टिव ट्रैफ़िक की कुल रेट लिमिट](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता है. प्राथमिकता के साथ अनुमान लगाने की सुविधा के लिए, डिफ़ॉल्ट रेट लिमिट **मॉडल / लेवल के लिए स्टैंडर्ड रेट लिमिट का 0.3 गुना** होती हैं

### अनुकूल डाउनग्रेड लॉजिक

अगर कंजेशन की वजह से, प्राथमिकता के साथ अनुमान लगाने की सुविधा की सीमाएं पार हो जाती हैं, तो ओवरफ़्लो वाले अनुरोधों को **अपने-आप और आसानी से** स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड कर दिया जाता है. ऐसा 503 या 429 गड़बड़ी के साथ अनुरोध को अस्वीकार करने के बजाय किया जाता है. डाउनग्रेड किए गए अनुरोधों के लिए, प्राथमिकता के साथ अनुमान लगाने की सुविधा की प्रीमियम दर के बजाय, स्टैंडर्ड दर से बिल भेजा जाता है.

### क्लाइंट की ज़िम्मेदारी

- **जवाब की निगरानी करना**: डेवलपर को एपीआई के जवाब में मौजूद `x-gemini-service-tier`
  हेडर की निगरानी करनी चाहिए, ताकि यह पता लगाया जा सके कि अनुरोधों को बार-बार
  `standard` पर डाउनग्रेड किया जा रहा है या नहीं.
- **फिर से कोशिश करना**: क्लाइंट को
  स्टैंडर्ड गड़बड़ियों के लिए, फिर से कोशिश करने का लॉजिक/एक्सपोनेंशियल बैकऑफ़ लागू करना होगा. जैसे, `DEADLINE_EXCEEDED`.

## कीमत

प्राथमिकता के साथ अनुमान लगाने की सुविधा की कीमत, [स्टैंडर्ड एपीआई](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) से 75-100% ज़्यादा होती है. इसके लिए, हर टोकन के हिसाब से बिल भेजा जाता है.

## काम करने वाले मॉडल

इन मॉडल पर, प्राथमिकता के साथ अनुमान लगाने की सुविधा काम करती है:

| मॉडल | प्राथमिकता के साथ अनुमान लगाने की सुविधा |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Pro का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3 Flash का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 3 Pro Image का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## आगे क्या करना है

Gemini के अनुमान लगाने और ऑप्टिमाइज़ेशन के अन्य [विकल्पों](https://ai.google.dev/gemini-api/docs/optimization?hl=hi) के बारे में पढ़ें:

- [लागत में 50% की कमी के लिए, Flex के साथ अनुमान लगाने की सुविधा](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi).
- [बैच एपीआई](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi), 24 घंटे के अंदर एसिंक्रोनस प्रोसेसिंग के लिए.
- इनपुट टोकन की लागत कम करने के लिए, [कॉन्टेक्स्ट कैशिंग](https://ai.google.dev/gemini-api/docs/caching?hl=hi).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-19 (UTC) को अपडेट किया गया."],[],[]]
