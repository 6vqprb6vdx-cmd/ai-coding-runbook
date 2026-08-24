---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=hi
fetched_at: 2026-08-24T02:32:47.209467+00:00
title: "Gemini \u0915\u0947 \u0928\u090f \u092e\u0949\u0921\u0932 \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini के नए मॉडल का इस्तेमाल करना

[यह पेज](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=hi) मॉडल के बारे में है

Gemini 3.6 Flash (`gemini-3.6-flash`) और Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) मॉडल, सामान्य तौर पर उपलब्ध (जीए) हैं. इन्हें प्रोडक्शन के लिए इस्तेमाल किया जा सकता है.

- **Gemini 3.6 Flash**: यह मॉडल, एजेंटिक और मल्टीमॉडल से जुड़े मुश्किल टास्क को बेहतर तरीके से पूरा करता है. साथ ही, इसमें टोकन का इस्तेमाल भी कम होता है. इसकी कीमत, 3.5 Flash मॉडल से कम है.
- **Gemini 3.5 Flash-Lite**: यह मॉडल, 3.5 मॉडल फ़ैमिली में सबसे तेज़ और सबसे कम कीमत वाला मॉडल है. यह मॉडल, ज़्यादा थ्रूपुट वाले टास्क को पूरा करने के मामले में, Flash-Lite की पिछली जनरेशन के मॉडल से बेहतर है.

इस गाइड में, हर मॉडल में नई सुविधाओं के बारे में बताया गया है. साथ ही, यह भी बताया गया है कि एपीआई में किए गए किन बदलावों का असर आपके कोड पर पड़ेगा और माइग्रेट कैसे करें.

### Gemini 3.6 Flash

1. स्किल इंस्टॉल करना:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करना:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. स्किल इंस्टॉल करना:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करना:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## नए मॉडल

| मॉडल | मॉडल आईडी | सोचने-समझने का डिफ़ॉल्ट लेवल | कीमत | ब्यौरा |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | इनपुट टोकन के लिए 1.50 डॉलर/मिलियन और आउटपुट टोकन के लिए 7.50 डॉलर/मिलियन | यह मॉडल, एजेंटिक और मल्टीमॉडल से जुड़े टास्क को तेज़ी से और सटीक तरीके से पूरा करता है. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | इनपुट टोकन के लिए 0.30 डॉलर/मिलियन और आउटपुट टोकन के लिए 2.50 डॉलर/मिलियन | यह मॉडल, 3.5 मॉडल फ़ैमिली में सबसे तेज़ और सबसे कम कीमत वाला मॉडल है. यह ज़्यादा थ्रूपुट वाले टास्क को पूरा करने के मामले में भी बेहतर है. |

इन दोनों मॉडल में, 10 लाख टोकन वाली कॉन्टेक्स्ट विंडो, ज़्यादा से ज़्यादा 64 हज़ार आउटपुट टोकन, सोच-समझकर जवाब देने की सुविधा, और [कंप्यूटर के इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) की सुविधा के साथ-साथ, पहले से मौजूद सभी टूल का ऐक्सेस मिलता है.

पूरी जानकारी के लिए, मॉडल के ये पेज देखें:

- [Gemini 3.6 Flash मॉडल का पेज](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi)
- [Gemini 3.5 Flash-Lite मॉडल का पेज](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi)

कीमत के बारे में ज़्यादा जानकारी के लिए, [कीमत वाला पेज देखें](https://ai.google.dev/gemini-api/docs/pricing?hl=hi).

## क्विकस्टार्ट

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Gemini 3.6 Flash में नया क्या है

- **टोकन और टर्न की संख्या में कमी:** यह मॉडल, Gemini 3.5 की तुलना में, कम चरणों में गहराई से विश्लेषण करने की सुविधा, बातचीत के कम टर्न, और टूल कॉल की मदद से, कई चरणों वाले वर्कफ़्लो को पूरा करता है. इससे, एक्ज़ीक्यूशन लूप स्पाइरलिंग भी कम होती है.
- **कोड जनरेट करने की बेहतर सुविधा:** यह मॉडल, बेहतर क्वालिटी वाला ऐसा कोड जनरेट करता है जिसे तुरंत इस्तेमाल किया जा सकता है. इसमें, अनचाहे बदलाव और डीबग करने के लिए कम लूप की ज़रूरत पड़ती है.
- **निर्देशों को बेहतर तरीके से फ़ॉलो करना**: यह मॉडल, डायग्नोस्टिक टास्क के दौरान, अनचाहे फ़ाइल बदलावों को कम करता है.
- **मल्टीमॉडल और स्पैटियल रीज़निंग की बेहतर सुविधा:** यह मॉडल, चार्ट की व्याख्या करने, विज़ुअल ब्लूप्रिंट को बदलने, और मल्टी-एलिमेंट वेब लेआउट जनरेट करने के मामले में बेहतर परफ़ॉर्मेंस देता है.
- **प्रोग्राम के हिसाब से पहले से जांच करने की सुविधा:** यह मॉडल, Gemini 3.5 Flash की तुलना में, बदलाव करने से पहले, डायग्नोस्टिक कोड स्क्रिप्ट को ज़्यादा बार चलाता है. इससे, मुश्किल टास्क को सटीक तरीके से पूरा किया जा सकता है. हालांकि, आसान फ़्रंटएंड काम के लिए, एक्सप्लोरेटरी चरणों की संख्या बढ़ सकती है.
- **कंप्यूटर के इस्तेमाल की सुविधा:** यह सुविधा, एजेंटिक यूज़र इंटरफ़ेस (यूआई) ऑटोमेशन के लिए, नेटिव टूल के तौर पर उपलब्ध है.
- **यूज़र इंटरफ़ेस (यूआई) स्टाइलिंग की प्राथमिकता**: यह मॉडल, काम करने वाला कोड बेहतर तरीके से जनरेट करता है. हालांकि, मैन्युअल तरीके से समीक्षा करने वाले लोगों ने विज़ुअल लेआउट और स्टाइलिंग के लिए, पहले के मॉडल को ज़्यादा पसंद किया. डिजाइन से जुड़े साफ़ तौर पर निर्देश देकर, इस समस्या को कम किया जा सकता है.
- **सोचने-समझने की डिफ़ॉल्ट कोशिश (मीडियम):** यह मॉडल, Gemini 3.5 Flash की तरह ही, सोचने-समझने के `medium` डिफ़ॉल्ट लेवल का इस्तेमाल करता है.
- **कीमत में कमी**: आउटपुट टोकन की लागत कम हुई है (3.5 Flash के लिए 9.00 डॉलर/मिलियन के मुकाबले 7.50 डॉलर/मिलियन). इनपुट टोकन की लागत 1.50 डॉलर/मिलियन ही है.

## Gemini 3.5 Flash-Lite में नया क्या है

- **टास्क को पूरा करने में लगने वाले समय में कमी:** यह मॉडल, ज़्यादा वॉल्यूम वाले डेटा को पार्स करने और दस्तावेज़ों से जानकारी निकालने के मामले में, 3.5 मॉडल फ़ैमिली में सबसे ज़्यादा थ्रूपुट देता है.
- **सोच-समझकर जवाब देने और मल्टीमॉडल परफ़ॉर्मेंस की बेहतर सुविधा:** यह मॉडल, Gemini 2.5 Flash से बेहतर है. साथ ही, HLE (18.0% बनाम 11.0%) जैसे रीज़निंग टास्क और CharXIV (74.5% बनाम 63.7%) जैसे मल्टीमॉडल बेंचमार्क में, इसके स्कोर बेहतर हैं.
- **सब-एजेंट ऑर्केस्ट्रेशन और टूल की भरोसेमंद सुविधा:** यह मॉडल, कोड को लागू करने, खोज करने, और एमसीपी वर्कफ़्लो के लिए, टूल के एक्ज़ीक्यूशन की भरोसेमंद सुविधा को बेहतर बनाता है. ऑटोनॉमस प्लानिंग और सब-एजेंट के मुश्किल टास्क के लिए, सोचने-समझने का लेवल बढ़ाएं.
- **दस्तावेज़ों को बेहतर तरीके से समझने की सुविधा:** यह मॉडल, दस्तावेज़ों को पार्स करने और स्ट्रक्चर्ड डेटा से जानकारी निकालने के मामले में, ज़्यादा सटीक तरीके से काम करता है. दस्तावेज़ की मुश्किल के हिसाब से, सोचने-समझने के minimal और high, दोनों लेवल के साथ एक्सपेरिमेंट करें.
- **इंटरैक्टिव वेब कोडिंग और टेबल के फ़ॉर्मैट में मौजूद डेटा को प्रोसेस करने की सुविधा:** यह मॉडल, हल्के-फुल्के कोड एक्ज़ीक्यूशन के ज़रिए प्लानिंग करके, फ़्रंटएंड JavaScript और टेबल के फ़ॉर्मैट में मौजूद डेटा को प्रोसेस करने के मामले में, बेहतर परफ़ॉर्मेंस देता है.
- **चैटबॉट और परसोना की सुविधा:** यह मॉडल, Gemini 3.1 Flash-Lite की तुलना में, कई टर्न वाले निर्देशों को बेहतर तरीके से फ़ॉलो करता है. साथ ही, इसमें परसोना की सुविधा भी बेहतर है.
- **कंप्यूटर के इस्तेमाल की सुविधा:** यह सुविधा, एजेंटिक यूज़र इंटरफ़ेस (यूआई) ऑटोमेशन के लिए, नेटिव टूल के तौर पर उपलब्ध है.

## Flash या Flash-Lite का सही मॉडल चुनना

अपने वर्कलोड के लिए सही मॉडल और माइग्रेशन पाथ चुनने के लिए, इस टेबल का इस्तेमाल करें.

इन दोनों मॉडल के लिए, सैंपलिंग के बंद किए जा चुके पैरामीटर (`temperature`, `top_p`, `top_k`) और पहले से भरे गए मॉडल टर्न हटाने होंगे. ज़्यादा जानकारी के लिए, [एपीआई में किए गए बदलाव](#api-changes-and-parameter-updates) देखें.

| मॉडल | इस्तेमाल के मुख्य उदाहरण | माइग्रेशन के लिए सुझाया गया टारगेट |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | कोड जनरेट करना, स्पैटियल/मल्टीमॉडल रीज़निंग, एजेंटिक वर्कफ़्लो के कई चरण | **Gemini 3.5 Flash**, **Gemini 3 Flash (प्रीव्यू)** या **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | ऑटोनॉमस सब-एजेंट एक्ज़ीक्यूशन, ज़्यादा वॉल्यूम वाले डेटा का विश्लेषण और दस्तावेज़ों से जानकारी निकालना, स्ट्रक्चर्ड JSON को पार्स करना | **Gemini 3.1 Flash-Lite** या **Gemini 2.5 Flash** |

## Antigravity एजेंट का अपडेट किया गया वर्शन

Gemini 3.6 Flash की बेहतर परफ़ॉर्मेंस की वजह से, अब यह Gemini Managed Agents में [Antigravity एजेंट](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=hi) के लिए डिफ़ॉल्ट मॉडल है. एपीआई में नया फ़ील्ड सेट करके, इसे बदला जा सकता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## एपीआई में किए गए बदलाव और पैरामीटर के अपडेट

Gemini 3.6 Flash और Gemini 3.5 Flash-Lite के साथ, एपीआई में किए गए ये बदलाव, इन मॉडल के साथ-साथ Gemini के आने वाले सभी मॉडल पर लागू होंगे.

- **सैंपलिंग पैरामीटर को बंद करना**: `temperature`, `top_p`, और `top_k` को बंद कर दिया गया है. एपीआई, इन पैरामीटर को अनदेखा करता है. साथ ही, मॉडल की आने वाली जनरेशन में, गड़बड़ी का मैसेज दिखाता है.
- **पहले से भरे गए मॉडल टर्न की पुष्टि करना**: पहले से मॉडल टर्न भरने की सुविधा अब उपलब्ध नहीं है. अगर अनुरोध में, आखिरी नॉन-एम्टी टर्न, `model` टर्न है, तो एपीआई `400` गड़बड़ी का मैसेज दिखाता है.

यहां, एपीआई में किए गए हर बदलाव के बारे में पूरी जानकारी और कोड के सैंपल दिए गए हैं.

### 1. सैंपलिंग पैरामीटर (`temperature`, `top_p`, `top_k`) को बंद करना

`temperature`, `top_p`, और `top_k` को बंद कर दिया गया है. इन्हें अनदेखा किया जाता है. मॉडल की आने वाली जनरेशन में, इन पैरामीटर को देने पर, एचटीटीपी 400 गड़बड़ी का मैसेज दिखता है. **सभी अनुरोधों से इन पैरामीटर को हटाएं.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

डिटरमिनिज़म को बेहतर बनाने के लिए, अपने इस्तेमाल के उदाहरण के हिसाब से साफ़ तौर पर नियम तय करके, सिस्टम के लिए निर्देश तय करें.

### 2. पहले से भरे गए मॉडल टर्न की पुष्टि करना

एपीआई के ऐसे अनुरोधों की अनुमति नहीं है जो नॉन-एम्टी मॉडल रोल टर्न के साथ खत्म होते हैं. ऐसे अनुरोधों के लिए, **एचटीटीपी 400 गड़बड़ी** का मैसेज दिखता है.

#### ⚠️ इस्तेमाल करने से बचें

लेगसी `generateContent` या रॉ REST पेलोड में, मॉडल रोल टर्न के साथ खत्म होने की अनुमति अब नहीं है:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ माइग्रेशन के लिए सुझाया गया तरीका

अगर आपका ऐप्लिकेशन, पहले से भरे गए मॉडल टर्न का इस्तेमाल करके, प्रीऐम्बल को छिपाता था या JSON फ़ॉर्मैट को लागू करता था, तो इसके बजाय `system_instruction` या [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) का इस्तेमाल करें.

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## माइग्रेशन के लिए चेकलिस्ट

### Gemini 3.6 Flash

1. स्किल इंस्टॉल करना:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करना:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. स्किल इंस्टॉल करना:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करना:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### gemini-3.6-flash पर माइग्रेट करना

- **मॉडल आईडी अपडेट करना:** अपने टारगेट मॉडल स्ट्रिंग को `gemini-3.6-flash` में बदलें.
- **सैंपलिंग के बंद किए जा चुके पैरामीटर हटाना:**
  - जनरेशन कॉन्फ़िगरेशन से `temperature`, `top_p`, और `top_k` हटाएं.
  - `thinking_budget` को स्ट्रिंग enum `thinking_level` से बदलें. इसकी वैल्यू `"medium"` या `"high"` पर सेट करें.
  - `candidate_count` हटाएं. यह पैरामीटर, Gemini 3.x में काम नहीं करता.
- **टर्न की पुष्टि करने के नियमों को लागू करना:**
  - पहले से भरे गए मॉडल टर्न हटाएं.
  - पक्का करें कि उपयोगकर्ता के आखिरी टर्न में, नॉन-एम्टी टेक्स्ट शामिल हो.
- **फ़ंक्शन कॉल का ऑडिट करना:**
  - पक्का करें कि सभी `FunctionResponse` ऑब्जेक्ट में `call_id` और `name` शामिल हों.
  - रिस्पॉन्स पेलोड में, मल्टीमॉडल ऐसेट शामिल करें.
  - `\\n\\n` का इस्तेमाल करके, इनलाइन निर्देशों को फ़ॉर्मैट करें.
  - अगर आपको टूल से पहले के टेक्स्ट से जुड़ी `Malformed_Function_Call` गड़बड़ियां दिखती हैं, तो टूल से पहले के टेक्स्ट की ज़रूरी शर्तों के लिए, [कामचलाऊ समाधान देखें](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=hi#workarounds-for-pre-tool-text-requirements).
- **Gemini 3.x की बुनियादी ज़रूरी शर्तें:** एसडीके अपडेट और थॉट सिग्नेचर को बनाए रखने के लिए, [Gemini 3.5 के लिए माइग्रेशन की चेकलिस्ट](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=hi#migration) देखें.

### gemini-3.5-flash-lite पर माइग्रेट करना

- **मॉडल आईडी अपडेट करना:** अपने टारगेट मॉडल स्ट्रिंग को `gemini-3.5-flash-lite` में बदलें.
- **सोचने-समझने के लेवल को कॉन्फ़िगर करना:**
  - ज़्यादा वॉल्यूम में जानकारी निकालने, राउटिंग या क्लासिफ़िकेशन के लिए: ज़्यादा थ्रूपुट पाने के लिए, `thinking_level` को `"minimal"` (डिफ़ॉल्ट) पर छोड़ दें.
  - टूल कॉल, कोड एक्ज़ीक्यूशन या कई चरणों में सोच-समझकर जवाब देने की सुविधा वाले ऑटोनॉमस सब-एजेंट के लिए: टूल को समय से पहले बंद होने से रोकने के लिए, `thinking_level` को `"medium"` या `"high"` पर सेट करें.
- **बंद किए जा चुके पैरामीटर हटाना और फ़ंक्शन कॉल की पुष्टि करना:** [3.6 Flash के लिए लागू होने वाले नियमों को ही लागू करें](#migrate-to-gemini-3-6-flash).
- **Gemini 3.x की बुनियादी ज़रूरी शर्तें:** [Gemini 3.5 के लिए माइग्रेशन की चेकलिस्ट](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=hi#migration) देखें.

## अगले चरण

- [मॉडल की खास जानकारी वाले पेज पर, एपीआई की खास जानकारी देखें.](https://ai.google.dev/gemini-api/docs/models?hl=hi)
- [Interactions API की गाइड में, मल्टी-एजेंट ऑर्केस्ट्रेशन के बारे में जानें.](https://ai.google.dev/gemini-api/docs/interactions?hl=hi)
- [Google AI Studio में, प्रॉम्प्ट को टेस्ट करें और उन्हें बेहतर बनाएं.](https://aistudio.google.com/?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
