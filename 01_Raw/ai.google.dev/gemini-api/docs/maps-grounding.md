---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi
fetched_at: 2026-08-31T06:31:23.571132+00:00
title: "Google Maps \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0917\u094d\u0930\u093e\u0909\u0902\u0921\u093f\u0902\u0917 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google Maps की मदद से ग्राउंडिंग करना

Google Maps से सटीक जानकारी पाने की सुविधा, Gemini की जनरेटिव क्षमताओं को Google Maps के सटीक, तथ्यों पर आधारित, और अप-टू-डेट डेटा से कनेक्ट करती है. इस सुविधा की मदद से डेवलपर, अपने ऐप्लिकेशन में आसानी से जगह की जानकारी का इस्तेमाल कर सकते हैं. जब किसी उपयोगकर्ता की क्वेरी में Maps के डेटा से जुड़ा कॉन्टेक्स्ट होता है, तो Gemini मॉडल, Google Maps का इस्तेमाल करता है. इससे वह उपयोगकर्ता को तथ्यों पर आधारित और नई जानकारी दे पाता है. यह जानकारी, उपयोगकर्ता की बताई गई जगह या जगह की अनुमानित जानकारी के हिसाब से होती है.

- **सटीक जवाब, जो जगह के हिसाब से हों:** भौगोलिक रूप से खास क्वेरी के लिए, Google Maps के बड़े और मौजूदा डेटा का इस्तेमाल करें.
- **बेहतर तरीके से मनमुताबिक बनाना:** उपयोगकर्ता की दी गई जगहों की जानकारी के आधार पर, सुझाव और जानकारी को मनमुताबिक बनाना.

## अपनी प्रोफ़ाइल बनाना शुरू करें

इस उदाहरण में, Google Maps के साथ ग्राउंडिंग को अपने ऐप्लिकेशन में इंटिग्रेट करने का तरीका बताया गया है. इससे उपयोगकर्ता की क्वेरी के जवाब सटीक और जगह के हिसाब से दिए जा सकते हैं. इस प्रॉम्प्ट में, स्थानीय सुझावों के बारे में पूछा गया है. इसमें उपयोगकर्ता की जगह की जानकारी देने का विकल्प भी है. इससे Gemini मॉडल को Google Maps का डेटा इस्तेमाल करने की अनुमति मिलती है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google Maps से जानकारी लेने की सुविधा कैसे काम करती है

Google Maps के साथ ग्राउंडिंग की सुविधा, Gemini API को Google Geo के साथ इंटिग्रेट करती है. इसके लिए, Maps API को ग्राउंडिंग सोर्स के तौर पर इस्तेमाल किया जाता है. जब किसी उपयोगकर्ता की क्वेरी में भौगोलिक कॉन्टेक्स्ट शामिल होता है, तो Gemini मॉडल, Google Maps से जानकारी लेने की सुविधा को चालू कर सकता है. इसके बाद, मॉडल, दी गई जगह से जुड़े Google Maps के डेटा के आधार पर जवाब जनरेट कर सकता है.

आम तौर पर, इस प्रोसेस में ये शामिल होते हैं:

1. **उपयोगकर्ता की क्वेरी:** कोई उपयोगकर्ता आपके ऐप्लिकेशन में क्वेरी सबमिट करता है.इसमें भौगोलिक जानकारी भी शामिल हो सकती है. उदाहरण के लिए, "मेरे आस-पास की कॉफ़ी शॉप", "सैन फ़्रांसिस्को के म्यूज़ियम".
2. **टूल शुरू करना:** Gemini मॉडल, भौगोलिक जानकारी से जुड़ी क्वेरी को पहचानकर, Google Maps के साथ ग्राउंडिंग टूल शुरू करता है. इस टूल को उपयोगकर्ता के `latitude` और `longitude` के साथ भी इस्तेमाल किया जा सकता है. यह टूल, टेक्स्ट के आधार पर खोज करने वाला टूल है. यह Maps पर खोज करने के तरीके से मिलता-जुलता है. जैसे, स्थानीय क्वेरी ("मेरे आस-पास") के लिए निर्देशांकों का इस्तेमाल किया जाएगा. वहीं, खास या गैर-स्थानीय क्वेरी पर, जगह की जानकारी का असर नहीं पड़ेगा.
3. **डेटा वापस पाना:** 'Google Maps के साथ ग्राउंडिंग' सेवा, Google Maps से काम की जानकारी (जैसे, जगहें, समीक्षाएं, फ़ोटो, पते, कारोबार के खुले होने का समय) के बारे में क्वेरी करती है.
4. **भरोसेमंद सोर्स से जानकारी लेकर जवाब जनरेट करना:** Maps से मिले डेटा का इस्तेमाल, Gemini मॉडल के जवाब में किया जाता है. इससे यह पक्का किया जाता है कि जवाब में दी गई जानकारी सही और काम की हो.
5. **जवाब और एनोटेशन:** मॉडल, Google Maps के सोर्स से लिंक करने वाले इनलाइन एनोटेशन के साथ टेक्स्ट वाला जवाब देता है. इससे डेवलपर, उद्धरण दिखा पाते हैं.

## Google Maps से जानकारी लेने की सुविधा का इस्तेमाल कब और क्यों करना चाहिए

Google Maps के साथ ग्राउंडिंग की सुविधा उन ऐप्लिकेशन के लिए सबसे सही है जिन्हें सटीक, अप-टू-डेट, और जगह के हिसाब से जानकारी की ज़रूरत होती है. यह लोगों को काम का और उनके हिसाब से कॉन्टेंट उपलब्ध कराता है. इससे लोगों को बेहतर अनुभव मिलता है. यह कॉन्टेंट, Google Maps के विशाल डेटाबेस से लिया जाता है. इस डेटाबेस में दुनिया भर की 25 करोड़ से ज़्यादा जगहों की जानकारी मौजूद है.

Google Maps से जानकारी लेने की सुविधा का इस्तेमाल तब करना चाहिए, जब आपके ऐप्लिकेशन को:

- जगह के हिसाब से पूछे गए सवालों के पूरे और सटीक जवाब दें.
- बातचीत करके यात्रा का प्लान बनाने वाले टूल और स्थानीय गाइड तैयार करें.
- जगह की जानकारी और उपयोगकर्ता की प्राथमिकताओं के आधार पर, लोकप्रिय जगहों के सुझाव देना. जैसे, रेस्टोरेंट या दुकानें.
- सामाजिक, खुदरा या खाना डिलीवर करने वाली सेवाओं के लिए, जगह की जानकारी के हिसाब से अनुभव बनाएं.

Google Maps के डेटा का इस्तेमाल करके जवाब देने की सुविधा, उन मामलों में सबसे ज़्यादा काम आती है जहां आस-पास की जगहों और मौजूदा तथ्यों से जुड़ा डेटा ज़रूरी होता है. जैसे, "मेरे आस-पास सबसे अच्छी कॉफ़ी शॉप ढूंढना" या "रास्ता ढूंढना".

## उपयोग के उदाहरण

Google Maps से जानकारी लेने की सुविधा, जगह की जानकारी के हिसाब से अलग-अलग तरह के कामों में इस्तेमाल की जा सकती है.

### किसी जगह के बारे में पूछे गए सवालों के जवाब देना

किसी जगह के बारे में ज़्यादा जानकारी वाले सवाल पूछें, ताकि Google पर लोगों की समीक्षाओं और Maps के अन्य डेटा के आधार पर जवाब मिल सकें.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### जगह के हिसाब से मनमुताबिक अनुभव देने की सुविधा उपलब्ध कराना

किसी उपयोगकर्ता की प्राथमिकताओं और किसी खास इलाके के हिसाब से सुझाव पाएं.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### यात्रा का प्लान बनाने में मदद करना

कई दिनों की यात्रा के प्लान जनरेट करें. इनमें अलग-अलग जगहों के बारे में जानकारी और वहाँ जाने का रास्ता शामिल हो. ये प्लान, यात्रा से जुड़े ऐप्लिकेशन के लिए सबसे सही होते हैं.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## सेवा के इस्तेमाल से जुड़ी ज़रूरी शर्तें

इस सेक्शन में, Google Maps के साथ Grounding की सुविधा इस्तेमाल करने की ज़रूरी शर्तों के बारे में बताया गया है.

### उपयोगकर्ता को Google Maps के सोर्स के इस्तेमाल के बारे में जानकारी देना

Google Maps के हर भरोसेमंद नतीजे के साथ, आपको `model_output` चरण के कॉन्टेंट ब्लॉक पर सोर्स एनोटेशन मिलेंगे. ये एनोटेशन, हर जवाब के साथ मौजूद होते हैं. यह मेटाडेटा दिखता है:

- सोर्स यूआरएल
- नाम

Google Maps से जानकारी लेने की सुविधा के ज़रिए मिले नतीजों को दिखाते समय, आपको Google Maps से जुड़े सोर्स के बारे में बताना होगा. साथ ही, उपयोगकर्ताओं को यह जानकारी देनी होगी:

- Google Maps के सोर्स, जनरेट किए गए कॉन्टेंट के ठीक बाद होने चाहिए. साथ ही, सोर्स में मौजूद जानकारी, जनरेट किए गए कॉन्टेंट से मेल खानी चाहिए. जनरेट किए गए इस कॉन्टेंट को Google Maps के भरोसेमंद नतीजे भी कहा जाता है.
- Google Maps के सोर्स, उपयोगकर्ता के एक इंटरैक्शन में दिखने चाहिए.

### Google Maps के लिंक के साथ Google Maps के सोर्स दिखाना

हर सोर्स एनोटेशन के लिए, लिंक की झलक इन ज़रूरी शर्तों के मुताबिक जनरेट की जानी चाहिए:

- Google Maps के टेक्स्ट [एट्रिब्यूशन के दिशा-निर्देशों](#maps-attribution-guidelines) का पालन करते हुए, हर सोर्स को Google Maps के लिए एट्रिब्यूट करें.
- जवाब में दिए गए सोर्स का नाम दिखाएं.
- एनोटेशन में मौजूद `url` का इस्तेमाल करके, सोर्स से लिंक करें.

### Google Maps में टेक्स्ट एट्रिब्यूशन के दिशा-निर्देश

टेक्स्ट में Google Maps को सोर्स के तौर पर एट्रिब्यूट करते समय, इन दिशा-निर्देशों का पालन करें:

- Google Maps के टेक्स्ट में किसी भी तरह का बदलाव न करें:
  - Google Maps के कैपिटल लेटर में लिखे गए अक्षरों में बदलाव न करें.
  - Google Maps को एक से ज़्यादा लाइनों में न लिखें.
  - Google Maps को किसी दूसरी भाषा में स्थानीयकृत न करें.
  - ब्राउज़र को Google Maps का अनुवाद करने से रोकने के लिए, HTML एट्रिब्यूट translate="no" का इस्तेमाल करें.

Google Maps के लिए डेटा उपलब्ध कराने वाली कुछ कंपनियों और उनके लाइसेंस की शर्तों के बारे में ज़्यादा जानने के लिए, [Google Maps और Google Earth की कानूनी सूचनाएं](https://www.google.com/help/legalnotices_maps/?hl=hi) देखें.

## सबसे सही तरीके

- **उपयोगकर्ता की जगह की जानकारी दें:** उपयोगकर्ता की जगह की जानकारी मिलने पर, `google_maps` टूल कॉन्फ़िगरेशन में हमेशा `latitude` और `longitude` शामिल करें. इससे, उपयोगकर्ता को उसकी दिलचस्पी के हिसाब से सबसे काम के जवाब मिलेंगे.
- **आखिरी उपयोगकर्ताओं को जानकारी दें:** अपने आखिरी उपयोगकर्ताओं को साफ़ तौर पर बताएँ कि उनकी क्वेरी के जवाब देने के लिए, Google Maps के डेटा का इस्तेमाल किया जा रहा है. ऐसा खास तौर पर तब करें, जब टूल चालू हो.
- **ज़रूरत न होने पर टॉगल बंद करें:** Google Maps से जानकारी लेने की सुविधा डिफ़ॉल्ट रूप से बंद होती है. इसे सिर्फ़ तब चालू करें (`"tools": [{"type": "google_maps"}]`), जब किसी क्वेरी में जगह की जानकारी साफ़ तौर पर दी गई हो. इससे परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ किया जा सकेगा.

## सीमाएं

- फ़िलहाल, Google Maps से मिली जानकारी का इस्तेमाल करके जवाब देने की सुविधा सिर्फ़ अंग्रेज़ी भाषा में उपलब्ध है.
- ऐसा हो सकता है कि यह टूल सभी देशों/इलाकों में उपलब्ध न हो.
- नतीजे, जगह की सटीक जानकारी और Maps पर उपलब्ध डेटा के हिसाब से अलग-अलग हो सकते हैं.
- **भौगोलिक दायरा:** Google Maps के साथ ग्राउंडिंग की सुविधा दुनिया भर में उपलब्ध है.
- **डिफ़ॉल्ट स्थिति:** 'Google Maps से मिली जानकारी का इस्तेमाल करके जवाब दो' टूल डिफ़ॉल्ट रूप से बंद होता है.
  आपको एपीआई अनुरोधों में इसे साफ़ तौर पर चालू करना होगा.

## कीमत और दर की सीमाएं

Google Maps से जानकारी लेने की सुविधा की कीमत, मॉडल जनरेशन के हिसाब से अलग-अलग होती है:

- **Gemini 3 मॉडल:** आपके प्रोजेक्ट के लिए, हर उस **खोज क्वेरी** का बिल भेजा जाता है जिसे मॉडल पूरा करता है. एक **खोज के लिए दिए गए प्रॉम्प्ट** (मॉडल को भेजा गया आपका एपीआई अनुरोध) के जवाब में, मॉडल ज़रूरी जानकारी ढूंढने के लिए कई खोज क्वेरी चला सकता है. इनमें से हर क्वेरी को, टूल के बिल किए जाने वाले इस्तेमाल के तौर पर गिना जाता है.
- **Gemini 2.5 और इससे पुराने मॉडल:** आपके प्रोजेक्ट के लिए, हर **खोज प्रॉम्प्ट** के हिसाब से बिल भेजा जाता है.
  किसी अनुरोध के लिए सिर्फ़ तब बिल भेजा जाता है, जब प्रॉम्प्ट से Google Maps के कम से कम एक भरोसेमंद नतीजे मिलते हैं. इससे कोई फ़र्क़ नहीं पड़ता कि उस नतीजे को पाने के लिए, मॉडल ने कितनी अलग-अलग खोज क्वेरी की हैं.

शुल्क के बारे में ज़्यादा जानकारी के लिए, [Gemini API के शुल्क वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

## इन मॉडल के साथ काम करता है

Google Maps से जानकारी लेने की सुविधा, इन मॉडल पर काम करती है:

| मॉडल | Google Maps से जानकारी लेने की सुविधा |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## साथ-साथ इस्तेमाल किए जा सकने वाले टूल

Gemini 3 मॉडल, बिल्ट-इन टूल (जैसे, Google Maps के साथ ग्राउंडिंग) को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ इस्तेमाल करने की सुविधा देते हैं. [टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर, इस बारे में ज़्यादा जानें.

## आगे क्या करना है

- [उपलब्ध अन्य टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi) के बारे में जानें.
- ज़िम्मेदारी से एआई का इस्तेमाल करने के सबसे सही तरीकों और Gemini API के सुरक्षा फ़िल्टर के बारे में ज़्यादा जानने के लिए, [सुरक्षा सेटिंग की गाइड](https://ai.google.dev/gemini-api/docs/safety-settings?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
