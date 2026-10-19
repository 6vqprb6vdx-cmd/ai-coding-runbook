---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=hi
fetched_at: 2026-10-19T05:40:51.093687+00:00
title: "\u092a\u094d\u0930\u093e\u0925\u092e\u093f\u0915\u0924\u093e \u0915\u0947 \u0906\u0927\u093e\u0930 \u092a\u0930 \u0905\u0928\u0941\u092e\u093e\u0928 \u0932\u0917\u093e\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# प्राथमिकता के आधार पर अनुमान लगाना

जानकारी: प्रायॉरिटी इन्फ़्रेंस टियर की मदद से, इंतज़ार के समय को ऑप्टिमाइज़ करने का तरीका जानें

Gemini Priority API, प्रीमियम इन्फ़्रेंस टियर है. इसे कारोबार के लिए ज़रूरी वर्कलोड को ध्यान में रखकर डिज़ाइन किया गया है. इसके लिए, आपको प्रीमियम कीमत चुकानी होगी. इसमें आपको कम इंतज़ार का समय और सबसे ज़्यादा भरोसेमंद सेवा मिलेगी. प्रायॉरिटी टियर के ट्रैफ़िक को स्टैंडर्ड एपीआई और फ़्लेक्स टियर के ट्रैफ़िक से ज़्यादा प्राथमिकता दी जाती है.

प्राथमिकता का अनुमान लगाने की सुविधा, GenerateContent API और Interactions API के एंडपॉइंट पर, [टियर 2 और टियर 3](https://ai.google.dev/gemini-api/docs/billing?hl=hi#about-billing) के उपयोगकर्ताओं के लिए उपलब्ध है.

## प्राथमिकता सेक्शन का इस्तेमाल करने का तरीका

प्रायॉरिटी टियर का इस्तेमाल करने के लिए, अनुरोध के मुख्य हिस्से में `service_tier` फ़ील्ड को `priority` पर सेट करें. अगर फ़ील्ड को शामिल नहीं किया जाता है, तो डिफ़ॉल्ट टियर स्टैंडर्ड होता है.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
          model: "gemini-3.8-flash",
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
        "gemini-3.8-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## प्राथमिकता का अनुमान लगाने की सुविधा कैसे काम करती है

प्रायॉरिटी इन्फ़रेंस, अनुरोधों को ज़्यादा ज़रूरी कंप्यूट क्यू में भेजता है. इससे, इस्तेमाल करने वाले लोगों के लिए उपलब्ध ऐप्लिकेशन के लिए, अनुमानित और तेज़ परफ़ॉर्मेंस मिलती है. इसका मुख्य तरीका यह है कि डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक के लिए, सर्वर-साइड पर स्टैंडर्ड प्रोसेसिंग को डाउनग्रेड किया जाए. इससे अनुरोध को पूरा न करने के बजाय, ऐप्लिकेशन को स्टेबल बनाए रखने में मदद मिलती है.

| सुविधा | प्राथमिकता | स्टैंडर्ड | Flex | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | स्टैंडर्ड प्लान के मुकाबले 75-100% ज़्यादा | फ़ुल टिकट | 50% की छूट | 50% की छूट |
| **इंतज़ार का समय** | सेकंड | सेकंड से मिनट | मिनट (1 से 15 मिनट का टारगेट) | 24 घंटे तक |
| **भरोसेमंद होना** | ज़्यादा (कम नहीं किया जा सकता) | ज़्यादा / सामान्य से ज़्यादा | सबसे अच्छी कोशिश (शेड किया जा सकता है) | हाई (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **कम इंतज़ार का समय**: इसे इंटरैक्टिव और इस्तेमाल करने वाले लोगों के लिए उपलब्ध एआई टूल के लिए डिज़ाइन किया गया है, ताकि वे कुछ ही सेकंड में जवाब दे सकें.
- **ज़्यादा भरोसेमंद**: ट्रैफ़िक को सबसे ज़्यादा अहमियत दी जाती है और इसे किसी भी तरह से कम नहीं किया जा सकता.
- **ग्रेसफ़ुल डिग्रेडेशन**: डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक बढ़ने पर, उसे प्रोसेस करने के लिए अपने-आप स्टैंडर्ड टियर पर डाउनग्रेड कर दिया जाता है. इससे सेवा में रुकावट नहीं आती.
- **Low friction**: यह स्टैंडर्ड और Flex टियर की तरह ही, सिंक्रोनस `generateContent` तरीके का इस्तेमाल करता है.

### उपयोग के उदाहरण

प्रायॉरिटी प्रोसेसिंग, कारोबार के लिए ज़रूरी वर्कफ़्लो के लिए सबसे सही है. इसमें परफ़ॉर्मेंस और विश्वसनीयता सबसे अहम होती है.

- **इंटरैक्टिव एआई ऐप्लिकेशन**: ग्राहक सेवा के लिए चैटबॉट और कोपायलट. इनमें उपयोगकर्ता प्रीमियम चुकाते हैं और उन्हें तुरंत और लगातार जवाब मिलने की उम्मीद होती है.
- **रीयल-टाइम में फ़ैसला लेने वाले इंजन**: ऐसे सिस्टम जिन्हें भरोसेमंद और कम इंतज़ार के समय वाले नतीजों की ज़रूरत होती है. जैसे, लाइव टिकट की जांच करना या धोखाधड़ी का पता लगाना.
- **प्रीमियम ग्राहक के लिए सुविधाएं**: ऐसे डेवलपर जिन्हें पैसे चुकाने वाले ग्राहकों के लिए, सेवा स्तर के बेहतर उद्देश्यों (एसएलओ) की गारंटी देनी होती है.

### अनुरोधों की संख्या की सीमाएं

प्राथमिकता के आधार पर इस्तेमाल किए जाने वाले संसाधनों के लिए, अनुरोध संख्या सीमित करने से जुड़ी अपनी सीमाएं होती हैं. भले ही, इस्तेमाल को [इंटरैक्टिव ट्रैफ़िक की दर से जुड़ी कुल सीमाओं](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता हो. प्राथमिकता इन्फ़्रेंस के लिए, अनुरोध संख्या सीमित करने की डिफ़ॉल्ट सीमाएं, **मॉडल / टियर के लिए अनुरोध संख्या सीमित करने की स्टैंडर्ड सीमा का 0.3 गुना** होती हैं

### ग्रेसफ़ुल डाउनग्रेड लॉजिक

अगर ज़्यादा ट्रैफ़िक की वजह से, प्राथमिकता वाले अनुरोधों की सीमाएं पार हो जाती हैं, तो ओवरफ़्लो अनुरोधों को **अपने-आप और आसानी से** स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड कर दिया जाता है. ऐसा करने से, 503 या 429 गड़बड़ी नहीं होती. डाउनग्रेड किए गए अनुरोधों के लिए, स्टैंडर्ड रेट के हिसाब से बिलिंग की जाती है, न कि प्राथमिकता वाले प्रीमियम रेट के हिसाब से.

### क्लाइंट की ज़िम्मेदारी

- **जवाब की निगरानी करना**: डेवलपर को एपीआई से मिले जवाब में `x-gemini-service-tier` हेडर की निगरानी करनी चाहिए. इससे यह पता लगाया जा सकता है कि अनुरोधों को बार-बार `standard` पर डाउनग्रेड किया जा रहा है या नहीं.
- **फिर से कोशिश करना**: क्लाइंट को स्टैंडर्ड गड़बड़ियों के लिए, फिर से कोशिश करने का लॉजिक/एक्सपोनेंशियल बैकऑफ़ लागू करना होगा. जैसे, `DEADLINE_EXCEEDED`.

## कीमत

प्राथमिकता के आधार पर अनुमान लगाने की सुविधा, [स्टैंडर्ड एपीआई](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) से 75 से 100% ज़्यादा महंगी है. इसका शुल्क, हर टोकन के हिसाब से लिया जाता है.

## इन मॉडल के साथ काम करता है

इन मॉडल में, अनुमान लगाने की सुविधा काम करती है:

| मॉडल | प्राथमिकता के आधार पर अनुमान लगाना |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=hi) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash की इमेज](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## आगे क्या करना है

Gemini के अन्य [इनफ़्रेंस और ऑप्टिमाइज़ेशन](https://ai.google.dev/gemini-api/docs/optimization?hl=hi) विकल्पों के बारे में पढ़ें:

- लागत में 50% की कमी के लिए, [फ़्लेक्स इन्फ़रेंस](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi) का इस्तेमाल करें.
- 24 घंटों के अंदर एसिंक्रोनस प्रोसेसिंग के लिए [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi).
- इनपुट टोकन की लागत कम करने के लिए, [कॉन्टेक्स्ट के लिए कैश की सुविधा](https://ai.google.dev/gemini-api/docs/caching?hl=hi).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
