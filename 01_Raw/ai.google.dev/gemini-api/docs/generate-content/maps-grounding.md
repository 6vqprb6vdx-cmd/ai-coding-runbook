---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=hi
fetched_at: 2026-08-10T03:13:17.575507+00:00
title: "Google Maps \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0917\u094d\u0930\u093e\u0909\u0902\u0921\u093f\u0902\u0917 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
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
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Google Maps से जानकारी लेने की सुविधा कैसे काम करती है

Google Maps के साथ ग्राउंडिंग की सुविधा, Gemini API को Google Geo के साथ इंटिग्रेट करती है. इसके लिए, Maps API को ग्राउंडिंग सोर्स के तौर पर इस्तेमाल किया जाता है. जब किसी उपयोगकर्ता की क्वेरी में भौगोलिक कॉन्टेक्स्ट शामिल होता है, तो Gemini मॉडल, Google Maps से जानकारी लेने की सुविधा को चालू कर सकता है. इसके बाद, मॉडल, दी गई जगह से जुड़े Google Maps के डेटा के आधार पर जवाब जनरेट कर सकता है.

आम तौर पर, इस प्रोसेस में ये शामिल होते हैं:

1. **उपयोगकर्ता की क्वेरी:** कोई उपयोगकर्ता आपके ऐप्लिकेशन में क्वेरी सबमिट करता है.इसमें भौगोलिक जानकारी भी शामिल हो सकती है. उदाहरण के लिए, "मेरे आस-पास की कॉफ़ी शॉप", "सैन फ़्रांसिस्को के म्यूज़ियम".
2. **टूल शुरू करना:** Gemini मॉडल, भौगोलिक जानकारी से जुड़ी क्वेरी को पहचानकर, Google Maps के साथ ग्राउंडिंग टूल शुरू करता है. इस टूल को उपयोगकर्ता के `latitude` और `longitude` के साथ भी इस्तेमाल किया जा सकता है. यह टूल, टेक्स्ट के आधार पर खोज करने वाला टूल है. यह Maps पर खोज करने के तरीके से मिलता-जुलता है. जैसे, स्थानीय क्वेरी ("मेरे आस-पास") के लिए निर्देशांकों का इस्तेमाल किया जाएगा. वहीं, खास या गैर-स्थानीय क्वेरी पर, जगह की जानकारी का असर नहीं पड़ेगा.
3. **डेटा वापस पाना:** 'Google Maps के साथ ग्राउंडिंग' सेवा, Google Maps से काम की जानकारी (जैसे, जगहें, समीक्षाएं, फ़ोटो, पते, कारोबार के खुले होने का समय) के बारे में क्वेरी करती है.
4. **भरोसेमंद सोर्स से जानकारी लेकर जवाब जनरेट करना:** Maps से मिले डेटा का इस्तेमाल, Gemini मॉडल के जवाब में किया जाता है. इससे यह पक्का किया जाता है कि जवाब में दी गई जानकारी सही और काम की हो.
5. **जवाब:** मॉडल, टेक्स्ट के रूप में जवाब देता है. इसमें Google Maps के सोर्स के उद्धरण शामिल होते हैं.

## Google Maps से जानकारी लेने की सुविधा का इस्तेमाल कब और क्यों करना चाहिए

Google Maps के साथ ग्राउंडिंग की सुविधा उन ऐप्लिकेशन के लिए सबसे सही है जिन्हें सटीक, अप-टू-डेट, और जगह के हिसाब से जानकारी की ज़रूरत होती है. यह लोगों को काम का और उनके हिसाब से कॉन्टेंट उपलब्ध कराता है. इससे लोगों को बेहतर अनुभव मिलता है. यह कॉन्टेंट, Google Maps के विशाल डेटाबेस से लिया जाता है. इस डेटाबेस में दुनिया भर की 25 करोड़ से ज़्यादा जगहों की जानकारी मौजूद है.

Google Maps से जानकारी लेने की सुविधा का इस्तेमाल तब करना चाहिए, जब आपके ऐप्लिकेशन को:

- जगह के हिसाब से पूछे गए सवालों के पूरे और सटीक जवाब दें.
- बातचीत करके यात्रा का प्लान बनाने वाले टूल और स्थानीय गाइड तैयार करें.
- जगह की जानकारी और उपयोगकर्ता की प्राथमिकताओं के आधार पर, लोकप्रिय जगहों के सुझाव देना. जैसे, रेस्टोरेंट या दुकानें.
- सामाजिक, खुदरा या खाना डिलीवर करने वाली सेवाओं के लिए, जगह की जानकारी के हिसाब से अनुभव बनाएं.

Google Maps के डेटा का इस्तेमाल करके जवाब देने की सुविधा, उन मामलों में सबसे ज़्यादा काम आती है जहां आस-पास की जगहों और मौजूदा तथ्यों से जुड़ा डेटा ज़रूरी होता है. जैसे, "मेरे आस-पास सबसे अच्छी कॉफ़ी शॉप ढूंढना" या "रास्ता ढूंढना".

## एपीआई के तरीके और पैरामीटर

Google Maps से जानकारी लेने की सुविधा, Gemini API के ज़रिए [`generateContent`](https://ai.google.dev/api/generate-content?hl=hi) तरीके के टूल के तौर पर उपलब्ध है. Google Maps की मदद से ग्राउंडिंग की सुविधा चालू और कॉन्फ़िगर करने के लिए, अपने अनुरोध के `tools` पैरामीटर में [`googleMaps`](https://ai.google.dev/api/caching?hl=hi#GoogleMaps) ऑब्जेक्ट शामिल करें.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

इसके अलावा, यह टूल कॉन्टेक्स्ट के हिसाब से जगह की जानकारी को `toolConfig` के तौर पर पास करने की सुविधा देता है.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### भरोसेमंद स्रोतों से मिले जवाब को समझना

जब Google Maps के डेटा के आधार पर जवाब तैयार किया जाता है, तब जवाब में [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=hi#GroundingMetadata) फ़ील्ड शामिल होता है.
दावों की पुष्टि करने और अपने ऐप्लिकेशन में उद्धरणों को बेहतर तरीके से दिखाने के लिए, यह स्ट्रक्चर्ड डेटा ज़रूरी है. साथ ही, इससे सेवा के इस्तेमाल से जुड़ी ज़रूरी शर्तों को पूरा करने में भी मदद मिलती है.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API, [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=hi#GroundingMetadata) के साथ यह जानकारी दिखाता है:

- `groundingChunks`: यह ऑब्जेक्ट का ऐसा कलेक्शन है जिसमें `maps` के सोर्स (`uri`, `placeId`, और `title`) शामिल होते हैं.
- `groundingSupports`: यह `groundingChunks` में मौजूद सोर्स से मॉडल के जवाब के टेक्स्ट को कनेक्ट करने के लिए, चंक का कलेक्शन होता है. हर चंक, टेक्स्ट स्पैन (`startIndex` और `endIndex` से तय किया गया) को एक या उससे ज़्यादा `groundingChunkIndices` से लिंक करता है. यह इनलाइन उद्धरण बनाने की कुंजी है.

टेक्स्ट में इनलाइन उद्धरण रेंडर करने का तरीका दिखाने वाले कोड स्निपेट के लिए, Google Search के दस्तावेज़ों में [उदाहरण](https://ai.google.dev/gemini-api/docs/google-search?hl=hi#attributing_sources_with_inline_citations) देखें.

## उपयोग के उदाहरण

Google Maps से जानकारी लेने की सुविधा, जगह की जानकारी के हिसाब से अलग-अलग तरह के कामों में इस्तेमाल की जा सकती है. यहां दिए गए उदाहरणों से पता चलता है कि अलग-अलग प्रॉम्प्ट और पैरामीटर, Google Maps के साथ ग्राउंडिंग की सुविधा का इस्तेमाल कैसे कर सकते हैं. ऐसा हो सकता है कि Google Maps के भरोसेमंद स्रोतों से मिले नतीजों में दी गई जानकारी, असल स्थितियों से अलग हो.

### किसी जगह के बारे में पूछे गए सवालों के जवाब देना

किसी जगह के बारे में ज़्यादा जानकारी वाले सवाल पूछें, ताकि Google पर लोगों की समीक्षाओं और Maps के अन्य डेटा के आधार पर जवाब मिल सकें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### जगह के हिसाब से मनमुताबिक अनुभव देने की सुविधा उपलब्ध कराना

किसी उपयोगकर्ता की प्राथमिकताओं और किसी खास इलाके के हिसाब से सुझाव पाएं.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### यात्रा का प्लान बनाने में मदद करना

कई दिनों की यात्रा के प्लान जनरेट करें. इनमें अलग-अलग जगहों के बारे में जानकारी और वहाँ जाने का रास्ता शामिल हो. ये प्लान, यात्रा से जुड़े ऐप्लिकेशन के लिए सबसे सही होते हैं.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## सेवा के इस्तेमाल से जुड़ी ज़रूरी शर्तें

इस सेक्शन में, Google Maps के साथ Grounding की सुविधा इस्तेमाल करने की ज़रूरी शर्तों के बारे में बताया गया है.

### उपयोगकर्ता को Google Maps के सोर्स के इस्तेमाल के बारे में जानकारी देना

Google Maps से मिले हर भरोसेमंद जवाब के साथ, आपको `groundingChunks` में सोर्स मिलेंगे. इनसे हर जवाब की पुष्टि की जा सकती है. यह मेटाडेटा भी दिखता है:

- सोर्स यूआरआई
- title
- आईडी

Google Maps से जानकारी लेने की सुविधा के ज़रिए मिले नतीजों को दिखाते समय, आपको Google Maps से जुड़े सोर्स के बारे में बताना होगा. साथ ही, उपयोगकर्ताओं को यह जानकारी देनी होगी:

- Google Maps के सोर्स, जनरेट किए गए कॉन्टेंट के ठीक बाद होने चाहिए. साथ ही, सोर्स में मौजूद जानकारी, जनरेट किए गए कॉन्टेंट से मेल खानी चाहिए. जनरेट किए गए इस कॉन्टेंट को Google Maps के भरोसेमंद नतीजे भी कहा जाता है.
- Google Maps के सोर्स, उपयोगकर्ता के एक इंटरैक्शन में दिखने चाहिए.

### Google Maps के लिंक के साथ Google Maps के सोर्स दिखाना

`groundingChunks` और `grounding_chunks.maps.placeAnswerSources.reviewSnippets` में मौजूद हर सोर्स के लिए, लिंक की झलक इन ज़रूरी शर्तों के मुताबिक जनरेट की जानी चाहिए:

- Google Maps के टेक्स्ट [एट्रिब्यूशन के दिशा-निर्देशों](#maps-attribution-guidelines) का पालन करते हुए, हर सोर्स को Google Maps के लिए एट्रिब्यूट करें.
- जवाब में दिए गए सोर्स का टाइटल दिखाएं.
- जवाब में मौजूद `uri` या `googleMapsUri` का इस्तेमाल करके, सोर्स का लिंक दें.

इन इमेज में, सोर्स और Google Maps के लिंक दिखाने के लिए ज़रूरी शर्तें बताई गई हैं.

![जवाब के साथ सोर्स दिखाने वाला प्रॉम्प्ट](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=hi)

सोर्स के व्यू को छोटा किया जा सकता है.

![जवाब और सोर्स को छोटा करके दिखाया गया प्रॉम्प्ट](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=hi)

ज़रूरी नहीं: लिंक की झलक को बेहतर बनाने के लिए, इसमें यह कॉन्टेंट जोड़ें:

- Google Maps के टेक्स्ट एट्रिब्यूशन से पहले, [Google Maps का फ़ेविकॉन](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=hi) डाला जाता है.
- सोर्स यूआरएल (`og:image`) से ली गई फ़ोटो.

Google Maps के लिए डेटा उपलब्ध कराने वाली कुछ कंपनियों और उनके लाइसेंस की शर्तों के बारे में ज़्यादा जानने के लिए, [Google Maps और Google Earth की कानूनी सूचनाएं](https://www.google.com/help/legalnotices_maps/?hl=hi) देखें.

### Google Maps में टेक्स्ट एट्रिब्यूशन के दिशा-निर्देश

टेक्स्ट में Google Maps को सोर्स के तौर पर एट्रिब्यूट करते समय, इन दिशा-निर्देशों का पालन करें:

- Google Maps के टेक्स्ट में किसी भी तरह का बदलाव न करें:
  - Google Maps के कैपिटल लेटर में लिखे गए अक्षरों में बदलाव न करें.
  - Google Maps को एक से ज़्यादा लाइनों में न लिखें.
  - Google Maps को किसी दूसरी भाषा में स्थानीयकृत न करें.
  - ब्राउज़र को Google Maps का अनुवाद करने से रोकने के लिए, HTML एट्रिब्यूट translate="no" का इस्तेमाल करें.
- यहां दी गई टेबल में बताए गए तरीके से, Google Maps के टेक्स्ट को स्टाइल करें:

| प्रॉपर्टी | शैली |
| --- | --- |
| `Font family` | Roboto. फ़ॉन्ट लोड करना ज़रूरी नहीं है. |
| `Fallback font family` | आपके प्रॉडक्ट में पहले से इस्तेमाल किया गया कोई भी sans serif बॉडी फ़ॉन्ट या डिफ़ॉल्ट सिस्टम फ़ॉन्ट को चालू करने के लिए "Sans-Serif" |
| `Font style` | सामान्य |
| `Font weight` | 400 |
| `Font color` | सफ़ेद, काला (#1F1F1F) या स्लेटी (#5E5E5E). बैकग्राउंड के साथ, कम से कम 4.5:1 का कंट्रास्ट बनाए रखें. |
| `Font size` | - कम से कम फ़ॉन्ट साइज़: 12 एसपी - फ़ॉन्ट का ज़्यादा से ज़्यादा साइज़: 16sp - sp के बारे में जानने के लिए, [मटीरियल डिज़ाइन की वेबसाइट](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc) पर फ़ॉन्ट साइज़ की इकाइयां देखें. |
| `Spacing` | सामान्य |

#### सीएसएस का उदाहरण

नीचे दी गई सीएसएस, Google Maps को सही टाइपोग्राफ़िक स्टाइल और रंग के साथ रेंडर करती है. यह सीएसएस, सफ़ेद या हल्के रंग के बैकग्राउंड पर काम करती है.

### सीएसएस

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### जगह का आईडी और समीक्षा आईडी

Google Maps के डेटा में, जगह का आईडी और समीक्षा का आईडी शामिल होता है. जवाब के इस डेटा को कैश मेमोरी में सेव किया जा सकता है, सेव किया जा सकता है, और एक्सपोर्ट किया जा सकता है:

- `placeId`
- `reviewId`

Google Maps से जानकारी लेने की सुविधा की शर्तों में, कैश मेमोरी में सेव करने से जुड़ी पाबंदियां लागू नहीं होती हैं.

### पाबंदी वाली गतिविधि और इलाका

Google Maps के साथ ग्राउंडिंग की सुविधा का इस्तेमाल करने पर, कुछ कॉन्टेंट और गतिविधियों पर अतिरिक्त पाबंदियां लगाई जाती हैं. ऐसा इसलिए किया जाता है, ताकि प्लैटफ़ॉर्म को सुरक्षित और भरोसेमंद बनाए रखा जा सके. [शर्तों](https://ai.google.dev/gemini-api/terms?hl=hi#grounding-with-google-maps) में बताई गई, इस्तेमाल की पाबंदियों के अलावा:

- ज़्यादा जोखिम वाली गतिविधियों के लिए, Google Maps के साथ ग्राउंडिंग का इस्तेमाल नहीं किया जाएगा. जैसे, आपातकालीन प्रतिक्रिया सेवाएं.
- आप ऐसे देश या इलाके में अपना ऐप्लिकेशन डिस्ट्रिब्यूट या उसका प्रमोशन नहीं करेंगे जहां Google Maps के साथ ग्राउंडिंग की सुविधा उपलब्ध नहीं है. ज़्यादा जानकारी के लिए, [Google Maps Platform के लिए पाबंदी वाली जगहें](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=hi) देखें.
  जिन देशों/इलाकों में YouTube TV उपलब्ध नहीं है उनकी सूची को समय-समय पर अपडेट किया जा सकता है.

## सबसे सही तरीके

- **उपयोगकर्ता की जगह की जानकारी दें:** सबसे काम के और उपयोगकर्ता की दिलचस्पी के हिसाब से जवाब पाने के लिए, `googleMapsGrounding` कॉन्फ़िगरेशन में हमेशा `user_location` (अक्षांश और देशांतर) शामिल करें. ऐसा तब करें, जब उपयोगकर्ता की जगह की जानकारी उपलब्ध हो.
- **आखिरी उपयोगकर्ताओं को जानकारी दें:** अपने आखिरी उपयोगकर्ताओं को साफ़ तौर पर बताएँ कि उनकी क्वेरी के जवाब देने के लिए, Google Maps के डेटा का इस्तेमाल किया जा रहा है. ऐसा खास तौर पर तब करें, जब टूल चालू हो.
- **लेटेंसी पर नज़र रखें:** बातचीत वाले ऐप्लिकेशन के लिए, पक्का करें कि भरोसेमंद स्रोतों से मिले जवाबों के लिए P95 लेटेंसी, स्वीकार्य थ्रेशोल्ड के अंदर हो. इससे उपयोगकर्ता को बेहतर अनुभव मिलता है.
- **ज़रूरत न होने पर टॉगल बंद करें:** Google Maps से जानकारी लेने की सुविधा डिफ़ॉल्ट रूप से बंद होती है. इसे सिर्फ़ तब चालू करें (`"tools": [{"googleMaps": {}}]`), जब किसी क्वेरी में जगह की जानकारी साफ़ तौर पर दी गई हो. इससे परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ किया जा सकेगा.

## सीमाएं

- **भौगोलिक दायरा:** Google Maps के साथ ग्राउंडिंग की सुविधा दुनिया भर में उपलब्ध है
- **मॉडल के साथ काम करने की सुविधा:** [काम करने वाले मॉडल](#supported-models) सेक्शन देखें.
- **मल्टीमॉडल इनपुट/आउटपुट:** फ़िलहाल, Grounding with Google Maps में टेक्स्ट के अलावा, मल्टीमॉडल इनपुट या आउटपुट का इस्तेमाल नहीं किया जा सकता.
- **डिफ़ॉल्ट स्थिति:** 'Google Maps से मिली जानकारी का इस्तेमाल करके जवाब दो' टूल डिफ़ॉल्ट रूप से बंद होता है.
  आपको एपीआई अनुरोधों में इसे साफ़ तौर पर चालू करना होगा.

## कीमत और दर की सीमाएं

Google Maps से जानकारी लेने की सुविधा की कीमत, क्वेरी के आधार पर तय की जाती है. मौजूदा दर **25 डॉलर / 1,000 ग्राउंडेड प्रॉम्प्ट** है. निःशुल्क टियर में, हर दिन ज़्यादा से ज़्यादा 500 अनुरोध किए जा सकते हैं. किसी अनुरोध को सिर्फ़ तब कोटे में गिना जाता है, जब प्रॉम्प्ट से कम से कम एक Google Maps का भरोसेमंद नतीजा मिलता है. जैसे, ऐसे नतीजे जिनमें कम से कम एक Google Maps का सोर्स शामिल हो. अगर एक ही अनुरोध से Google Maps पर कई क्वेरी भेजी जाती हैं, तो इसे दर सीमा के हिसाब से एक अनुरोध माना जाता है.

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

- [Gemini API की कुकबुक में, Google Search की मदद से जानकारी पाने की सुविधा](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=hi) आज़माएं.
- [उपलब्ध अन्य टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi) के बारे में जानें.
- ज़िम्मेदारी से एआई का इस्तेमाल करने के सबसे सही तरीकों और Gemini API के सुरक्षा फ़िल्टर के बारे में ज़्यादा जानने के लिए, [सुरक्षा सेटिंग की गाइड](https://ai.google.dev/gemini-api/docs/safety-settings?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
