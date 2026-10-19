---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi
fetched_at: 2026-10-19T05:35:43.531741+00:00
title: "\u092a\u094d\u0930\u093e\u0925\u092e\u093f\u0915\u0924\u093e \u0915\u0947 \u0906\u0927\u093e\u0930 \u092a\u0930 \u0905\u0928\u0941\u092e\u093e\u0928 \u0932\u0917\u093e\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# प्राथमिकता के आधार पर अनुमान लगाना

जानकारी: Interactions API में, प्राथमिकता वाले इन्फ़रेंस टियर की मदद से, इंतज़ार के समय को ऑप्टिमाइज़ करने का तरीका जानें

Gemini Priority API, प्रीमियम इन्फ़रेंस टियर है. इसे कारोबार के लिए ज़रूरी उन वर्कलोड के लिए डिज़ाइन किया गया है जिनके लिए कम इंतज़ार का समय और ज़्यादा भरोसेमंद परफ़ॉर्मेंस की ज़रूरत होती है. इसके लिए, प्रीमियम कीमत चुकानी पड़ती है. प्राथमिकता वाले टियर के ट्रैफ़िक को, स्टैंडर्ड API और Flex टियर के ट्रैफ़िक से ज़्यादा प्राथमिकता दी जाती है.

प्राथमिकता वाला अनुमान, Interactions API के सभी एंडपॉइंट पर उपलब्ध है.

## प्राथमिकता वाले टियर का इस्तेमाल करना

प्राथमिकता वाले टियर का इस्तेमाल करने के लिए, अपने अनुरोध में `service_tier` फ़ील्ड को `priority` पर सेट करें. अगर फ़ील्ड को छोड़ दिया जाता है, तो डिफ़ॉल्ट टियर स्टैंडर्ड होता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## प्राथमिकता वाला इन्फ़रेंस कैसे काम करता है

प्राथमिकता वाला इन्फ़रेंस, अनुरोधों को ज़्यादा अहमियत वाली कंप्यूटिंग क्यू में भेजता है. इससे, इस्तेमाल करने वाले लोगों के लिए उपलब्ध ऐप्लिकेशन के लिए, अनुमान के मुताबिक और तेज़ परफ़ॉर्मेंस मिलती है. इसका मुख्य तरीका यह है कि डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक होने पर, सर्वर-साइड को स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड कर दिया जाता है. इससे, अनुरोध को पूरा न कर पाने के बजाय, ऐप्लिकेशन की स्थिरता बनी रहती है.

| सुविधा | प्राथमिकता | स्टैंडर्ड | Flex | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | स्टैंडर्ड से 75-100% ज़्यादा | फ़ुल टिकट | 50% की छूट | 50% की छूट |
| **Latency** | सेकंड | सेकंड से मिनट | मिनट (1–15 मिनट का टारगेट) | 24 घंटे लग सकते हैं |
| **भरोसेमंद परफ़ॉर्मेंस** | ज़्यादा (इसे कम नहीं किया जा सकता) | ज़्यादा / मीडियम-ज़्यादा | बेस्ट-एफ़र्ट (इसे कम किया जा सकता है) | ज़्यादा (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **कम इंतज़ार का समय**: इसे इंटरैक्टिव, इस्तेमाल करने वाले लोगों के लिए उपलब्ध एआई टूल के लिए, दूसरे रिस्पॉन्स टाइम के लिए डिज़ाइन किया गया है.
- **ज़्यादा भरोसेमंद परफ़ॉर्मेंस**: ट्रैफ़िक को सबसे ज़्यादा अहमियत दी जाती है और इसे
  कम नहीं किया जा सकता.
- **अनुकूल गिरावट**: डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक होने पर, इसे प्रोसेस करने के लिए, स्टैंडर्ड टियर पर अपने-आप डाउनग्रेड कर दिया जाता है.
  इससे, सेवा में रुकावट नहीं आती.
- **कम मुश्किल**: स्टैंडर्ड और Flex टियर की तरह ही, सिंक्रोनस `create` तरीके का इस्तेमाल करता है.

### इस्तेमाल के उदाहरण

प्राथमिकता वाली प्रोसेसिंग, कारोबार के लिए ज़रूरी उन वर्कफ़्लो के लिए सही है जिनमें परफ़ॉर्मेंस और भरोसेमंद सेवा सबसे अहम होती है.

- **इंटरैक्टिव एआई ऐप्लिकेशन**: ग्राहक सेवा के चैटबॉट और कोपायलट. इनके लिए, उपयोगकर्ता प्रीमियम चुकाते हैं और उन्हें तेज़ और लगातार जवाब मिलने की उम्मीद होती है.
- **रीयल-टाइम डिसिजन इंजन**: ऐसे सिस्टम जिनमें भरोसेमंद और कम इंतज़ार के समय वाले
  नतीजों की ज़रूरत होती है. जैसे, लाइव टिकट ट्राइएज या धोखाधड़ी का पता लगाना.
- **प्रीमियम ग्राहकों के लिए सुविधाएं**: ऐसे डेवलपर जिन्हें पैसे चुकाने वाले ग्राहकों के लिए, बेहतर सर्विस
  लेवल ऑब्जेक्टिव (एसएलओ) की गारंटी देनी होती है.

### अनुरोध संख्या सीमित करना

प्राथमिकता वाले टियर के इस्तेमाल के लिए, अपनी रेट लिमिट होती है. भले ही, इसके इस्तेमाल को
[इंटरैक्टिव ट्रैफ़िक की कुल रेट लिमिट](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता हो. प्राथमिकता वाले इन्फ़रेंस के लिए, डिफ़ॉल्ट रेट लिमिट **मॉडल / टियर के लिए स्टैंडर्ड रेट लिमिट का 0.3 गुना** होती है

### अनुकूल डाउनग्रेड लॉजिक

अगर कंजेशन की वजह से, प्राथमिकता वाली सीमाएं पार हो जाती हैं, तो ओवरफ़्लो अनुरोधों को 503 या 429 गड़बड़ी के साथ पूरा न कर पाने के बजाय, **अपने-आप और आसानी से** स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड कर दिया जाता है. डाउनग्रेड किए गए अनुरोधों के लिए, प्राथमिकता वाले प्रीमियम रेट के बजाय, स्टैंडर्ड रेट के हिसाब से बिल भेजा जाता है.

### क्लाइंट की ज़िम्मेदारी

- **रिस्पॉन्स की निगरानी करना**: डेवलपर को API रिस्पॉन्स में, `x-gemini-service-tier`
  हेडर की निगरानी करनी चाहिए, ताकि यह पता लगाया जा सके कि अनुरोधों को बार-बार
  `standard` पर डाउनग्रेड किया जा रहा है या नहीं.
- **फिर से कोशिश करना**: क्लाइंट को
  स्टैंडर्ड गड़बड़ियों के लिए, फिर से कोशिश करने का लॉजिक/एक्सपोनेंशियल बैकऑफ़ लागू करना होगा. जैसे, `DEADLINE_EXCEEDED`.

## कीमत

प्राथमिकता वाले इन्फ़रेंस की कीमत, [स्टैंडर्ड API](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) से 75-100% ज़्यादा होती है. इसके लिए, हर टोकन के हिसाब से बिल भेजा जाता है.

## इस्तेमाल किए जा सकने वाले मॉडल

इन मॉडल में, प्राथमिकता वाले इन्फ़रेंस की सुविधा उपलब्ध है:

| मॉडल | प्राथमिकता वाला इन्फ़रेंस |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=hi) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3 Flash का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## आगे क्या करना है

- लागत कम करने के लिए, [Flex इन्फ़रेंस](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi).
- [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi): टोकन के बारे में जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
