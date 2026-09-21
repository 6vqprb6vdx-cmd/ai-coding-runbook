---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=hi
fetched_at: 2026-09-21T05:46:45.120718+00:00
title: "Gemini \u0915\u0947 \u0928\u090f \u092e\u0949\u0921\u0932 \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# Gemini के नए मॉडल का इस्तेमाल करना

[यह पेज](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=hi)

Gemini 3.6 Flash (`gemini-3.6-flash`) और Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) अब सामान्य रूप से उपलब्ध हैं. इनका इस्तेमाल ऐप्लिकेशन बनाने के लिए किया जा सकता है.

- **Gemini 3.6 Flash**: यह मॉडल, 3.5 Flash की तुलना में कम कीमत पर उपलब्ध है. साथ ही, यह एजेंटिक और मल्टीमॉडल वाले मुश्किल कामों को बेहतर तरीके से पूरा करता है. इसके अलावा, यह कम टोकन का इस्तेमाल करता है.
- **Gemini 3.5 Flash-Lite**: यह 3.5 फ़ैमिली का सबसे तेज़ और सबसे कम कीमत वाला मॉडल है. यह ज़्यादा थ्रूपुट के साथ काम करने के लिए, Flash-Lite की पिछली जनरेशन से बेहतर है.

इस गाइड में बताया गया है कि हर मॉडल में नया क्या है, एपीआई में हुए किन बदलावों से आपके कोड पर असर पड़ता है, और माइग्रेट कैसे करें.

### Gemini 3.6 Flash

1. स्किल इंस्टॉल करें:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करें:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. स्किल इंस्टॉल करें:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करें:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## नए मॉडल

| मॉडल | मॉडल आईडी | सोचने-समझने का डिफ़ॉल्ट लेवल | कीमत | ब्यौरा |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | इनपुट टोकन के लिए 1.50 डॉलर/मिलियन और आउटपुट टोकन के लिए 7.50 डॉलर/मिलियन | यह एजेंटिक और मल्टीमॉडल टास्क के लिए, तेज़ी से काम करने के साथ-साथ इंटेलिजेंस का भी इस्तेमाल करता है. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | इनपुट टोकन के लिए 0.30 डॉलर/मिलियन और आउटपुट टोकन के लिए 2.50 डॉलर/मिलियन | यह 3.5 मॉडल, ज़्यादा थ्रूपुट के साथ काम करने के लिए सबसे तेज़ और सबसे कम लागत वाला मॉडल है. |

दोनों मॉडल में, 10 लाख टोकन वाली कॉन्टेक्स्ट विंडो, ज़्यादा से ज़्यादा 64 हज़ार आउटपुट टोकन, सोचने की क्षमता, और [कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) करने की सुविधा के साथ-साथ, बिल्ट-इन टूल का पूरा सुइट उपलब्ध है.

पूरी जानकारी के लिए, मॉडल के पेज देखें:

- [Gemini 3.6 Flash मॉडल पेज](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi)
- [Gemini 3.5 Flash-Lite मॉडल का पेज](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi)

शुल्क के बारे में पूरी जानकारी के लिए, [कीमत तय करने से जुड़ा पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

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

- **टोकन और टर्न में कमी:** यह Gemini 3.5 की तुलना में, कम तर्कों, बातचीत के टर्न, और टूल कॉल के साथ कई चरणों वाले वर्कफ़्लो को पूरा करता है. इससे एक्ज़ीक्यूशन लूप स्पाइरलिंग भी कम हो जाती है.
- **बेहतर कोड जनरेशन:** यह सुविधा, इस्तेमाल के लिए तैयार बेहतर क्वालिटी वाला कोड जनरेट करती है. इसमें अनचाहे बदलाव कम होते हैं और डीबग करने के लिए कम लूप होते हैं.
- **निर्देशों का बेहतर तरीके से पालन करना**: गड़बड़ी की जानकारी देने वाले टास्क के दौरान, फ़ाइल में अनचाहे बदलावों को कम करता है.
- **मल्टीमॉडल और स्पेशल गहराई से विश्लेषण की बेहतर सुविधा:** चार्ट को समझने, विज़ुअल ब्लूप्रिंट को बदलने, और कई एलिमेंट वाले वेब लेआउट जनरेट करने की बेहतर सुविधा.
- **प्रोग्राम के हिसाब से पहले से की गई जांच:** Gemini 3.5 Flash की तुलना में, यह मॉडल बदलाव करने से पहले ज़्यादा बार डाइग्नोस्टिक कोड स्क्रिप्ट चलाता है. इससे मुश्किल टास्क को ज़्यादा सटीक तरीके से पूरा किया जा सकता है. हालांकि, इससे सामान्य फ़्रंटएंड के काम में कुछ और एक्सप्लोरेटरी चरण जोड़े जा सकते हैं.
- **कंप्यूटर पर इस्तेमाल करने की सुविधा:** एजेंटिक यूज़र इंटरफ़ेस (यूआई) ऑटोमेशन के लिए, नेटिव टूल के तौर पर काम करता है.
- **यूज़र इंटरफ़ेस (यूआई) स्टाइलिंग की प्राथमिकता**: यह फ़ंक्शनल कोड बेहतर तरीके से बना सकता है. हालांकि, मैन्युअल तरीके से आकलन करने वालों ने विज़ुअल लेआउट और स्टाइलिंग के लिए, पहले के मॉडल को प्राथमिकता दी. डिजाइन से जुड़े दिशा-निर्देशों के बारे में साफ़ तौर पर जानकारी देकर, इस समस्या को कम किया जा सकता है.
- **सोच-समझकर जवाब देने का डिफ़ॉल्ट लेवल (मीडियम):** यह Gemini 3.5 Flash के `medium` सोच-समझकर जवाब देने के डिफ़ॉल्ट लेवल का इस्तेमाल करता है.
- **कम कीमत**: आउटपुट टोकन की कम लागत (3.5 फ़्लैश के लिए 9.00 डॉलर/मिलियन के मुकाबले 7.50 डॉलर/मिलियन). इनपुट टोकन के लिए, 10 लाख टोकन का शुल्क 150 रुपये ही रहेगा.

## Gemini 3.5 Flash-Lite में नया क्या है

- **टास्क पूरा होने में कम समय लगता है:** ज़्यादा डेटा पार्स करने और दस्तावेज़ निकालने के लिए, 3.5 फ़ैमिली में सबसे ज़्यादा थ्रूपुट.
- **गहराई से विश्लेषण और टेक्स्ट, इमेज वग़ैरह को प्रोसेस करने वाले मॉडल की परफ़ॉर्मेंस को बेहतर बनाया गया है:** Gemini 2.5 Flash से डेटा दूसरी जगह भेजने का बेहतर विकल्प. साथ ही, गहराई से विश्लेषण वाले टास्क में ज़्यादा स्कोर. जैसे, HLE (18.0% बनाम 11.0%) और टेक्स्ट, इमेज वग़ैरह को प्रोसेस करने वाले मॉडल के बेंचमार्क. जैसे, CharXIV (74.5% बनाम 63.7%).
- **सब-एजेंट ऑर्केस्ट्रेशन और टूल की भरोसेमंदता:** इससे कोड को लागू करने, खोजने, और एमसीपी वर्कफ़्लो के लिए टूल को लागू करने की भरोसेमंदता बेहतर होती है. ऑटोनॉमस प्लानिंग और सब-एजेंट के मुश्किल टास्क के लिए, सोचने के लेवल को बढ़ाएं.
- **दस्तावेज़ को बेहतर तरीके से समझना:** इससे दस्तावेज़ को पार्स करने और स्ट्रक्चर्ड डेटा निकालने की सुविधा को ज़्यादा सटीक बनाया जा सकता है. दस्तावेज़ की जटिलता के आधार पर, कम और ज़्यादा सोच-विचार करके जवाब देने की सुविधा को आज़माएं.
- **इंटरैक्टिव वेब कोडिंग और टेबल के फ़ॉर्मैट में मौजूद डेटा को प्रोसेस करना:** यह मॉडल, फ़्रंटएंड JavaScript और टेबल के फ़ॉर्मैट में मौजूद डेटा को प्रोसेस करने के लिए बेहतरीन है. यह हल्के कोड एक्ज़ीक्यूशन के ज़रिए प्लान करता है.
- **चैटबॉट और पर्सोना की पहचान बनाए रखना:** Gemini 3.1 Flash-Lite की तुलना में, यह मॉडल कई बार दिए गए निर्देशों को बेहतर तरीके से समझता है और पर्सोना की पहचान बनाए रखता है.
- **कंप्यूटर पर इस्तेमाल करने की सुविधा:** एजेंटिक यूज़र इंटरफ़ेस (यूआई) ऑटोमेशन के लिए, नेटिव टूल के तौर पर काम करता है.

## सही Flash या Flash-Lite मॉडल चुनना

इस टेबल का इस्तेमाल करके, अपने वर्कलोड के लिए सही मॉडल और माइग्रेशन पाथ चुनें.

दोनों मॉडल के लिए, अब काम न करने वाले सैंपलिंग पैरामीटर (`temperature`, `top_p`, `top_k`) और पहले से भरे गए मॉडल टर्न हटाने होंगे. ज़्यादा जानकारी के लिए, [एपीआई में हुए बदलाव](#api-changes-and-parameter-updates) देखें.

| मॉडल | इस्तेमाल के मुख्य उदाहरण | माइग्रेशन के लिए सुझाया गया टारगेट |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | कोड जनरेशन, स्पेशल/टेक्स्ट, इमेज वग़ैरह को प्रोसेस करने वाला मॉडल गहराई से विश्लेषण, कई चरणों वाले एजेंटिक वर्कफ़्लो | **Gemini 3.5 Flash**, **Gemini 3 Flash (प्रीव्यू)** या **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | ऑटोनॉमस सब-एजेंट एक्ज़ीक्यूशन, ज़्यादा डेटा का विश्लेषण और दस्तावेज़ एक्सट्रैक्शन, स्ट्रक्चर्ड JSON पार्सिंग | **Gemini 3.1 Flash-Lite** या **Gemini 2.5 Flash** |

## Antigravity एजेंट को अपडेट किया गया

Gemini 3.6 Flash की बेहतर परफ़ॉर्मेंस की वजह से, अब यह Gemini Managed Agents में [Antigravity एजेंट](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=hi) के लिए डिफ़ॉल्ट मॉडल है. एपीआई पर नया फ़ील्ड सेट करके इसे बदला जा सकता है.

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

## एपीआई में हुए बदलाव और पैरामीटर से जुड़े अपडेट

Gemini 3.6 Flash और Gemini 3.5 Flash-Lite से शुरू करके, एपीआई में हुए ये बदलाव इन मॉडल और Gemini के आने वाले सभी मॉडल पर लागू होंगे.

- **सैंपलिंग पैरामीटर अब काम नहीं करते**: `temperature`, `top_p`, और `top_k` अब काम नहीं करते. एपीआई इन पैरामीटर को अनदेखा करता है और आने वाले समय में मॉडल जनरेशन में गड़बड़ी दिखाता है.
- **मॉडल के जवाब में पहले से भरी गई जानकारी की पुष्टि करना**: मॉडल के जवाब में पहले से भरी गई जानकारी की पुष्टि करने की सुविधा अब काम नहीं करती. अगर अनुरोध में मौजूद आखिरी टर्न `model` टर्न है, तो एपीआई `400` गड़बड़ी दिखाता है.

यहां एपीआई में हुए हर बदलाव के बारे में पूरी जानकारी और कोड सैंपल दिए गए हैं.

### 1. सैंपलिंग पैरामीटर के इस्तेमाल पर रोक (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p`, और `top_k` को बंद कर दिया गया है और इन्हें अनदेखा किया जाता है. आने वाले समय में मॉडल जनरेशन के लिए, इन पैरामीटर को उपलब्ध कराने पर एचटीटीपी 400 गड़बड़ी दिखेगी. **सभी अनुरोधों से इन पैरामीटर को हटाएं.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

जवाब को ज़्यादा सटीक बनाने के लिए, अपने इस्तेमाल के उदाहरण के हिसाब से साफ़ तौर पर नियम तय करके सिस्टम के लिए निर्देश तय करें.

### 2. पहले से भरे गए मॉडल के जवाब की पुष्टि करना

एपीआई के ऐसे अनुरोधों को अनुमति नहीं दी जाती है जिनमें मॉडल की भूमिका के लिए कोई जवाब नहीं दिया गया है. ऐसे अनुरोधों के जवाब में, **एचटीटीपी 400 गड़बड़ी** का मैसेज दिखता है.

#### ⚠️ इस्तेमाल करने से बचें

लेगसी `generateContent` या रॉ REST पेलोड में, मॉडल की भूमिका वाले टर्न के साथ खत्म होने वाले अनुरोधों को अब अनुमति नहीं है:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ माइग्रेशन का सुझाव दिया गया

अगर आपके ऐप्लिकेशन ने पहले मॉडल के जवाब में, प्रस्तावनाओं को हटाने या JSON फ़ॉर्मैट को लागू करने के लिए, पहले से जानकारी भरी थी, तो इसके बजाय `system_instruction` या [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) का इस्तेमाल करें.

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## माइग्रेशन की चेकलिस्ट

### Gemini 3.6 Flash

1. स्किल इंस्टॉल करें:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करें:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. स्किल इंस्टॉल करें:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. स्किल लागू करें:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### gemini-3.6-flash पर माइग्रेट करना

- **मॉडल आईडी अपडेट करें:** अपने टारगेट मॉडल स्ट्रिंग को `gemini-3.6-flash` में बदलें.
- **सैमलिंग के पुराने पैरामीटर हटाएं:**
  - जनरेशन कॉन्फ़िगरेशन से `temperature`, `top_p`, और `top_k` हटाएं.
  - `thinking_budget` को स्ट्रिंग enum `thinking_level` से बदलें. इसे `"medium"` या `"high"` पर सेट करें.
  - `candidate_count` को हटाएं. यह सुविधा Gemini 3.x में काम नहीं करती.
- **टर्न की पुष्टि करने से जुड़े नियमों को लागू करें:**
  - पहले से भरे गए मॉडल के जवाबों को हटाना.
  - पक्का करें कि उपयोगकर्ता के आखिरी टर्न में कुछ टेक्स्ट मौजूद हो.
- **फ़ंक्शन कॉल की ऑडिटिंग:**
  - पक्का करें कि सभी `FunctionResponse` ऑब्जेक्ट में `call_id` और `name` शामिल हों.
  - जवाब के पेलोड में मल्टीमॉडल ऐसेट रखें.
  - इनलाइन निर्देशों को `\\n\\n` का इस्तेमाल करके फ़ॉर्मैट करें.
  - अगर आपको टूल से पहले के टेक्स्ट से जुड़ी `Malformed_Function_Call` गड़बड़ियां दिखती हैं, तो [टूल से पहले के टेक्स्ट की ज़रूरी शर्तों को पूरा करने के तरीके](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=hi#workarounds-for-pre-tool-text-requirements) देखें.
- **Gemini 3.x की बुनियादी ज़रूरी शर्तें:** एसडीके अपडेट और थॉट सिग्नेचर को सुरक्षित रखने के लिए, [Gemini 3.5 पर माइग्रेट करने से पहले की जाने वाली कार्रवाइयों की सूची](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=hi#migration) देखें.

### gemini-3.5-flash-lite पर माइग्रेट करना

- **मॉडल आईडी अपडेट करें:** अपने टारगेट मॉडल स्ट्रिंग को `gemini-3.5-flash-lite` में बदलें.
- **सोच-विचार करने के लेवल को कॉन्फ़िगर करना:**
  - ज़्यादा डेटा निकालने, रूट करने या क्लासिफ़ाई करने के लिए: ज़्यादा थ्रूपुट पाने के लिए, `thinking_level` को `"minimal"` (डिफ़ॉल्ट) पर छोड़ दें.
  - टूल कॉल, कोड एक्ज़ीक्यूशन या कई चरणों में तर्क करने की सुविधा वाले ऑटोनॉमस सब-एजेंट के लिए: `thinking_level` को `"medium"` या `"high"` पर सेट करें, ताकि टूल को समय से पहले बंद होने से रोका जा सके.
- **बंद किए गए पैरामीटर हटाएं और फ़ंक्शन कॉल करने की सुविधा की पुष्टि करें:** [3.6 Flash वाले नियम लागू करें](#migrate-to-gemini-3-6-flash).
- **Gemini 3.x के लिए ज़रूरी शर्तें:** [Gemini 3.5 पर माइग्रेट करने से जुड़ी चेकलिस्ट](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=hi#migration) देखें.

## अगले चरण

- [मॉडल की खास जानकारी](https://ai.google.dev/gemini-api/docs/models?hl=hi) में जाकर, एपीआई की खास बातें देखें.
- [Interactions API की गाइड](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) में, एक से ज़्यादा एजेंट को मैनेज करने की सुविधा के बारे में जानें.
- [Google AI Studio](https://aistudio.google.com/?hl=hi) में प्रॉम्प्ट को टेस्ट करें और उन्हें बेहतर बनाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया."],[],[]]
