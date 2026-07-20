---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=hi
fetched_at: 2026-07-20T04:44:36.844833+00:00
title: "\u092a\u094d\u0930\u093e\u0925\u092e\u093f\u0915\u0924\u093e \u0915\u0947 \u0906\u0927\u093e\u0930 \u092a\u0930 \u0905\u0928\u0941\u092e\u093e\u0928 \u0932\u0917\u093e\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# प्राथमिकता के आधार पर अनुमान लगाना

जानकारी: Priority inference tier की मदद से, इंतज़ार के समय को ऑप्टिमाइज़ करने का तरीका जानें

Gemini Priority API, प्रीमियम inference tier है. इसे कारोबार के लिए ज़रूरी उन वर्कलोड के लिए डिज़ाइन किया गया है जिनमें कम इंतज़ार का समय और ज़्यादा भरोसेमंद परफ़ॉर्मेंस की ज़रूरत होती है. इसके लिए, प्रीमियम कीमत चुकानी पड़ती है. Priority tier के ट्रैफ़िक को, स्टैंडर्ड API और Flex tier के ट्रैफ़िक से ज़्यादा प्राथमिकता दी जाती है.

Priority inference, GenerateContent API
और Interactions API के एंडपॉइंट पर, [Tier 2 और Tier 3](https://ai.google.dev/gemini-api/docs/billing?hl=hi#about-billing) के उपयोगकर्ताओं के लिए उपलब्ध है.

## Priority का इस्तेमाल करने का तरीका

Priority tier का इस्तेमाल करने के लिए, अनुरोध के मुख्य हिस्से में मौजूद `service_tier` फ़ील्ड को `priority` पर सेट करें. अगर फ़ील्ड को छोड़ दिया जाता है, तो डिफ़ॉल्ट tier, स्टैंडर्ड होता है.

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

## Priority inference कैसे काम करता है

Priority inference, अनुरोधों को ज़्यादा अहमियत वाली कंप्यूटिंग कतारों पर भेजता है. इससे, उपयोगकर्ता के लिए बने ऐप्लिकेशन को अनुमान के मुताबिक और तेज़ परफ़ॉर्मेंस मिलती है. इसका मुख्य तरीका यह है कि डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक होने पर, सर्वर-साइड पर स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड किया जाता है. इससे अनुरोध को पूरा न करने के बजाय, ऐप्लिकेशन की स्थिरता बनी रहती है.

| सुविधा | प्राथमिकता | स्टैंडर्ड | Flex | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | स्टैंडर्ड से 75-100% ज़्यादा | फ़ुल टिकट | 50% की छूट | 50% की छूट |
| **इंतज़ार का समय** | सेकंड | सेकंड से मिनट | मिनट (1–15 मिनट का टारगेट) | 24 घंटे लग सकते हैं |
| **भरोसेमंद परफ़ॉर्मेंस** | ज़्यादा (इसे कम नहीं किया जा सकता) | ज़्यादा / मध्यम-ज़्यादा | पूरी कोशिश (इसे कम किया जा सकता है) | ज़्यादा (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **कम इंतज़ार का समय**: इसे इंटरैक्टिव,
  उपयोगकर्ता के लिए बने एआई टूल के लिए, दूसरे रिस्पॉन्स टाइम के हिसाब से डिज़ाइन किया गया है.
- **ज़्यादा भरोसेमंद परफ़ॉर्मेंस**: ट्रैफ़िक को सबसे ज़्यादा अहमियत दी जाती है और इसे
  कम नहीं किया जा सकता.
- **अनुकूल गिरावट**: डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक होने पर, इसे प्रोसेस करने के लिए,
  Standard tier पर अपने-आप डाउनग्रेड कर दिया जाता है. इससे, सेवा में रुकावट नहीं आती.
- **कम मुश्किल**: स्टैंडर्ड और Flex tier की तरह ही, सिंक्रोनस `generateContent` तरीके का इस्तेमाल करता है.

### इस्तेमाल के उदाहरण

Priority processing, कारोबार के लिए ज़रूरी उन वर्कफ़्लो के लिए सबसे सही है जिनमें परफ़ॉर्मेंस और भरोसेमंद परफ़ॉर्मेंस सबसे अहम होती है.

- **इंटरैक्टिव एआई ऐप्लिकेशन**: ग्राहक सेवा के चैटबॉट और कोपायलट. इनमें
  उपयोगकर्ता प्रीमियम चुकाते हैं और उन्हें तेज़ और लगातार जवाब मिलने की उम्मीद होती है.
- **रीयल-टाइम डिसिजन इंजन**: ऐसे सिस्टम जिनमें ज़्यादा भरोसेमंद और कम इंतज़ार के समय वाले
  नतीजों की ज़रूरत होती है. जैसे, लाइव टिकट ट्राइएज या धोखाधड़ी का पता लगाना.
- **प्रीमियम ग्राहक सुविधाएं**: ऐसे डेवलपर जिन्हें पैसे चुकाने वाले ग्राहकों के लिए, बेहतर सर्विस
  लेवल ऑब्जेक्टिव (एसएलओ) की गारंटी देनी होती है.

### दर की सीमाएं

Priority के इस्तेमाल के लिए, दर की अपनी सीमाएं होती हैं. हालांकि, इसके इस्तेमाल को
[इंटरैक्टिव ट्रैफ़िक की दर की कुल सीमाओं](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता है. Priority inference के लिए, दर की डिफ़ॉल्ट सीमाएं **मॉडल / टियर के लिए, स्टैंडर्ड दर की सीमा का 0.3 गुना** होती हैं

### अनुकूल डाउनग्रेड लॉजिक

अगर कंजेशन की वजह से, Priority की सीमाएं पार हो जाती हैं, तो ओवरफ़्लो अनुरोधों को **अपने-आप और आसानी से** Standard processing पर डाउनग्रेड कर दिया जाता है. ऐसा 503 या 429 गड़बड़ी के साथ अनुरोध को पूरा न करने के बजाय किया जाता है. डाउनग्रेड किए गए अनुरोधों के लिए, स्टैंडर्ड दर के हिसाब से बिल भेजा जाता है. न कि Priority की प्रीमियम दर के हिसाब से.

### क्लाइंट की ज़िम्मेदारी

- **जवाब की निगरानी करना**: डेवलपर को एपीआई के जवाब में मौजूद `x-gemini-service-tier`
  हेडर की निगरानी करनी चाहिए, ताकि यह पता लगाया जा सके कि अनुरोधों को अक्सर
  `standard` पर डाउनग्रेड किया जा रहा है या नहीं.
- **फिर से कोशिश करना**: क्लाइंट को
  स्टैंडर्ड गड़बड़ियों के लिए, फिर से कोशिश करने का लॉजिक/एक्सपोनेंशियल बैकऑफ़ लागू करना होगा. जैसे, `DEADLINE_EXCEEDED`.

## कीमत

Priority inference की कीमत, [स्टैंडर्ड एपीआई](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) से 75-100% ज़्यादा होती है. इसके लिए, हर टोकन के हिसाब से बिल भेजा जाता है.

## काम करने वाले मॉडल

ये मॉडल, Priority inference के साथ काम करते हैं:

| मॉडल | Priority inference |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 3 Pro इमेज की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash इमेज](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## आगे क्या करना है

Gemini के अन्य [inference और ऑप्टिमाइज़ेशन](https://ai.google.dev/gemini-api/docs/optimization?hl=hi) विकल्पों के बारे में पढ़ें:

- लागत में 50% की कमी के लिए, [Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi).
- [24 घंटे के अंदर एसिंक्रोनस प्रोसेसिंग के लिए, Batch API.](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)
- इनपुट टोकन की लागत कम करने के लिए, [कॉन्टेक्स्ट कैशिंग](https://ai.google.dev/gemini-api/docs/caching?hl=hi).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-23 (UTC) को अपडेट किया गया."],[],[]]
