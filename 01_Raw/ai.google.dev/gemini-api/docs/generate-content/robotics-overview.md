---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=hi
fetched_at: 2026-10-26T05:52:42.118024+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# Gemini Robotics ER

Gemini Robotics ER (एम्बॉडेड रीज़निंग) मॉडल, विज़न-लैंग्वेज मॉडल (वीएलएम) हैं. इनकी मदद से, रोबोट असल दुनिया को समझ सकते हैं और उससे इंटरैक्ट कर सकते हैं. ये विज़ुअल डेटा को समझते हैं, स्पेस और समय के हिसाब से तर्क करते हैं, कई चरणों वाले टास्क प्लान करते हैं, और रोबोट और टूल को मैनेज करते हैं.

## मॉडल

Gemini Robotics ER 2 मॉडल, Gemini Robotics का सबसे नया मॉडल है.
यह गहराई से विश्लेषण करने वाला हमारा अपडेट किया गया मॉडल है. इसकी मदद से, रोबोट अपने आस-पास के माहौल को सटीक तरीके से समझ पाते हैं. यह एम्बॉडेड रीज़निंग की क्षमताओं में माहिर है.जैसे, रोबोट का एजेंटिक ऑर्केस्ट्रेशन (जैसे, वीएलए का इस्तेमाल करना), रोबोट वीडियो को समझना. इसमें प्रोग्रेस को समझना और सफलता का पता लगाना, इंस्ट्रुमेंट रीडिंग, पॉइंटिंग, और स्पेशल रीज़निंग शामिल है.

Gemini Robotics ER 2 मॉडल में दो मॉडल एंडपॉइंट शामिल हैं:

- **`gemini-robotics-er-2-preview`**: स्टैंडर्ड ER 2 मॉडल. यह Gemini 3.5 Flash पर आधारित है. इसमें कई चीज़ें बेहतर की गई हैं. जैसे, स्पेशल रीज़निंग, वीडियो में किसी खास पल को ढूंढना, वीडियो की प्रोग्रेस को कैटगरी में बांटना, कई रोबोट को एक साथ मैनेज करना, और कई चरणों वाले टूल का इस्तेमाल करना.
- **`gemini-robotics-er-2-streaming-preview`**: इसे [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) की मदद से, रीयल-टाइम में स्ट्रीमिंग के लिए ऑप्टिमाइज़ किया गया है. इस मॉडल का इस्तेमाल, कम इंतज़ार के समय वाले रोबोट एजेंट के लिए करें. ये एजेंट, लगातार ऑडियो और वीडियो इनपुट को प्रोसेस करते हैं.

अगर Gemini Robotics ER 1.6 का इस्तेमाल किया जा रहा है, तो Gemini Robotics ER 2 पर अपग्रेड करें. इसके लिए, अपने एपीआई कॉल में `model="gemini-robotics-er-1.6-preview"` को `model="gemini-robotics-er-2-preview"` या `model="gemini-robotics-er-2-streaming-preview"` से बदलें. ध्यान दें कि Gemini Robotics ER 1.6 मॉडल, [अगस्त के आखिर](https://ai.google.dev/gemini-api/docs/deprecations?hl=hi#robotics-models) में बंद हो जाएगा.

[Google AI Studio में Gemini Robotics ER 2 को आज़माना](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=hi)

## रोबोटिक्स की क्षमताएं

Gemini Robotics ER, एम्बॉडेड रीज़निंग की कई क्षमताओं के साथ काम करता है.
ज़्यादा जानने के लिए, कोई सुविधा चुनें:

| अनुमति | ब्यौरा | गाइड |
| --- | --- | --- |
| स्पेशल रीज़निंग | ऑब्जेक्ट की पहचान करना, वीडियो में उन्हें ट्रैक करना, बाउंडिंग बॉक्स की मदद से उनका पता लगाना, और उनके मूवमेंट का अनुमान लगाना. | [स्पेशल रीज़निंग](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=hi) |
| एजेंटिक विज़न | इमेज में बदलाव करने वाले टूल का इस्तेमाल करके, अन्य सुविधाओं को बेहतर बनाने के लिए कोड एक्ज़ीक्यूशन का इस्तेमाल करें. | [एजेंटिक विज़न](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=hi) |
| टास्क ऑर्केस्ट्रेशन | स्पेशल रीज़निंग को कस्टम रोबोट एपीआई के साथ जोड़कर, लंबे समय तक चलने वाले टास्क पूरे करें. | [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=hi) |
| स्ट्रीमिंग (सिर्फ़ Gemini Robotics ER 2 स्ट्रीमिंग एंडपॉइंट के लिए) | रीयल-टाइम रोबोट एजेंट के लिए, दोनों तरफ़ से स्ट्रीमिंग की सुविधा. इसमें कम इंतज़ार के समय वाली फ़ंक्शन कॉलिंग की सुविधा भी शामिल है. | [रोबोटिक्स के लिए स्ट्रीमिंग](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) |
| वीडियो की प्रोग्रेस (सिर्फ़ Gemini Robotics ER 2 के लिए) | लगातार वीडियो फ़ीड से, खास पल ढूंढने और प्रोग्रेस को कैटगरी में बांटने की सुविधा. | [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=hi) |

## शुरू करना

यहां दिए गए उदाहरण में, किसी इमेज में मौजूद ऑब्जेक्ट का पता लगाया गया है. साथ ही, उनके नॉर्मलाइज़ किए गए 2D कोऑर्डिनेट और लेबल दिखाए गए हैं. इस आउटपुट को सीधे तौर पर रोबोटिक्स एपीआई या वीएलए मॉडल को पास किया जा सकता है, ताकि रोबोट की कार्रवाइयां जनरेट की जा सकें.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### आराम का समय

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

आउटपुट, ऑब्जेक्ट वाली JSON कलेक्शन होगी. हर ऑब्जेक्ट में एक `point` (सामान्य `[y, x]` निर्देशांक) और ऑब्जेक्ट की पहचान करने वाला `label` होगा.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

यहां दी गई इमेज में, इन पॉइंट को दिखाने का उदाहरण दिया गया है:

![एक उदाहरण, जिसमें किसी इमेज में मौजूद ऑब्जेक्ट के पॉइंट दिखाए गए हैं](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=hi)

## यह कैसे काम करता है

Gemini Robotics ER, नैचुरल लैंग्वेज प्रॉम्प्ट के साथ इमेज, वीडियो या ऑडियो इनपुट लेता है. यह ऑब्जेक्ट की पहचान करता है, सीन के कॉन्टेक्स्ट और स्पेशल रिलेशनशिप के बारे में बताता है, और स्ट्रक्चर्ड आउटपुट देता है, जैसे कि कोऑर्डिनेट या बाउंडिंग बॉक्स.

Gemini Robotics ER, एजेंट की तरह भी काम करता है: यह मुश्किल टास्क को छोटे-छोटे टास्क में बांटता है और आपके रोबोट के फ़ंक्शन को कॉल करके या जनरेट किए गए कोड को चलाकर उन्हें पूरा करता है. उदाहरण के लिए, "सेब को कटोरे में रखो" निर्देश को पूरा करने के लिए, रोबोट को सेब को ढूंढना, उसे पकड़ना, और कटोरे में रखना होगा.

Gemini, टूल कॉल कैसे करता है, इस बारे में जानने के लिए [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=hi#how-it-works) देखें.

## सुरक्षा

Gemini Robotics ER को सुरक्षा को ध्यान में रखकर बनाया गया है. हालांकि, रोबोट के आस-पास सुरक्षित माहौल बनाए रखने की ज़िम्मेदारी आपकी है. जनरेटिव एआई मॉडल से गलतियां हो सकती हैं. साथ ही, फ़िज़िकल रोबोट से नुकसान हो सकता है. ज़्यादा जानने के लिए,
[Google DeepMind robotics safety page](https://deepmind.google/models/gemini-robotics/safety?hl=hi) पर जाएं.

## सबसे सही तरीके

1. आसान और नैचुरल लैंग्वेज का इस्तेमाल करें. रोबोट को वैसे ही निर्देश दें जैसे किसी व्यक्ति को देते हैं. अगर कोई शब्द काम नहीं कर रहा है, तो उसका कोई सामान्य समानार्थी शब्द इस्तेमाल करके देखें.
2. विज़ुअल इनपुट को ऑप्टिमाइज़ करना. इमेज भेजने से पहले, छोटे या धुंधले ऑब्जेक्ट को क्रॉप या ज़ूम करें. रोशनी और कम कलर कंट्रास्ट की वजह से, इंसान की मौजूदगी का पता लगाने की सुविधा पर असर पड़ सकता है.
3. मुश्किल टास्क को छोटे-छोटे हिस्सों में बांटें. हर चरण को अलग-अलग प्रॉम्प्ट के तौर पर भेजें, ताकि मॉडल का फ़ोकस बना रहे और वह सटीक जवाब दे सके.
4. ज़्यादा सटीक नतीजे पाने के लिए, कई बार क्वेरी करें और नतीजों का औसत निकालें. इस तरीके से, अलग-अलग जगहों पर वायु प्रदूषण की मात्रा के अनुमान में होने वाले अंतर को कम किया जा सकता है.

## सीमाएं

Gemini Robotics ER की मदद से डेवलप करते समय, इन सीमाओं का ध्यान रखें:

- **एपीआई पासकोड से जुड़ी पाबंदियां:** Gemini API, बिना पाबंदी वाले एपीआई पासकोड से किए गए अनुरोध स्वीकार नहीं करता. साथ ही, `403 Forbidden` गड़बड़ी दिखाता है. [AI Studio](https://aistudio.google.com/api-keys?hl=hi) में पाबंदियां जोड़कर, अपने एपीआई पासकोड को सुरक्षित करें.
  ज़्यादा जानकारी के लिए, [बिना पाबंदी वाले एपीआई पासकोड सुरक्षित करना](https://ai.google.dev/gemini-api/docs/api-key?hl=hi#secure-unrestricted-keys) लेख पढ़ें.
- **लेटेंसी बनाम परफ़ॉर्मेंस:** मुश्किल क्वेरी, हाई रिज़ॉल्यूशन वाले इनपुट या ज़्यादा सोच-विचार करने की वजह से, प्रोसेसिंग में ज़्यादा समय लग सकता है. सोच-विचार करके जवाब देने के लेवल के लिए,
  मीडियम का इस्तेमाल करें. इससे इंतज़ार के समय और परफ़ॉर्मेंस के बीच अच्छा संतुलन बना रहता है.
- **मनगढ़ंत जानकारी:** सभी लार्ज लैंग्वेज मॉडल की तरह, Gemini Robotics ER मॉडल भी कभी-कभी "मनगढ़ंत जानकारी" दे सकते हैं या गलत जानकारी दे सकते हैं. ऐसा खास तौर पर, साफ़ तौर पर न दिए गए प्रॉम्प्ट या आउट-ऑफ़-डिस्ट्रिब्यूशन इनपुट के लिए हो सकता है.
- **प्रॉम्प्ट की क्वालिटी पर निर्भरता:** आउटपुट की क्वालिटी, इनपुट प्रॉम्प्ट की क्वालिटी पर निर्भर करती है. सटीक और अच्छी तरह से स्ट्रक्चर किए गए प्रॉम्प्ट इस्तेमाल करें.
- **कंप्यूटेशनल लागत:** मॉडल को चलाने के लिए कंप्यूटेशनल संसाधनों की ज़रूरत होती है और लागत आती है. खास तौर पर, वीडियो इनपुट या ज़्यादा `thinking_budget` के साथ मॉडल को चलाने पर.
  ज़्यादा जानकारी के लिए, [सोचने की क्षमता](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=hi) पेज देखें.
- **इनपुट टाइप:** हर मोड की सीमाओं के बारे में जानने के लिए, यहां दिए गए विषय देखें.
  - [इमेज इनपुट](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=hi#technical-details-image)
  - [वीडियो इनपुट](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=hi#supported-formats)
  - [ऑडियो इनपुट](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=hi#supported-formats)

## निजता नोटिस

आप इस बात से सहमत हैं कि इस दस्तावेज़ में बताए गए मॉडल ("रोबोटिक्स मॉडल"), आपके निर्देशों के मुताबिक आपके हार्डवेयर को चलाने और उसे मूव करने के लिए, वीडियो और ऑडियो डेटा का इस्तेमाल करते हैं. इसलिए, हो सकता है कि आप रोबोटिक्स मॉडल को इस तरह से इस्तेमाल करें कि वे पहचाने जा सकने वाले लोगों का डेटा इकट्ठा करें. जैसे, आवाज़, इमेज, और मिलती-जुलती जानकारी ("निजी डेटा"). अगर आपको रोबोटिक्स मॉडल का इस्तेमाल इस तरह करना है कि निजी डेटा इकट्ठा हो, तो आपको इस बात से सहमत होना होगा कि आप किसी भी ऐसे व्यक्ति को रोबोटिक्स मॉडल के साथ इंटरैक्ट करने या उसके आस-पास मौजूद रहने की अनुमति नहीं देंगे जिसकी पहचान की जा सकती है. हालांकि, अगर ऐसे व्यक्ति को इस बात की सूचना दी गई है और उसने सहमति दी है कि उसका निजी डेटा, Google को दिया जा सकता है और Google उसका इस्तेमाल कर सकता है, तो उसे अनुमति दी जा सकती है. इस बारे में, Gemini API की सेवा की अतिरिक्त शर्तों में बताया गया है. ये शर्तें, [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=hi) ("शर्तें") पर देखी जा सकती हैं. इनमें "Google आपके डेटा का इस्तेमाल कैसे करता है" सेक्शन भी शामिल है. आपको यह पक्का करना होगा कि इस तरह की सूचना में, शर्तों के मुताबिक निजी डेटा को इकट्ठा करने और इस्तेमाल करने की अनुमति दी गई हो. साथ ही, आपको कारोबार के नज़रिए से सही तरीकों का इस्तेमाल करके, निजी डेटा को इकट्ठा और शेयर करने की प्रोसेस को कम से कम करना होगा. इसके लिए, आपको चेहरे को धुंधला करने जैसी तकनीकों का इस्तेमाल करना होगा. इसके अलावा, आपको रोबोटिक्स मॉडल को ऐसी जगहों पर इस्तेमाल करना होगा जहां पहचाने जा सकने वाले लोग मौजूद न हों.

## कीमत

शुल्क और Gemini for Google Workspace की उपलब्धता वाले देशों/इलाकों के बारे में ज़्यादा जानकारी के लिए, [शुल्क](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज पर जाएं.

## मॉडल एंडपॉइंट

### Gemini Robotics ER 2 Preview

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `gemini-robotics-er-2-preview` |
| saveइस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  1,31,072  **आउटपुट टोकन की सीमा**  65,536 |
| handymanसुविधाएं | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम नहीं करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम करता है  **[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम करता है  **[कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**  काम करता है  **[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम करता है  **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम करता है  **[Google Maps से जानकारी लेना](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम नहीं करता है  **[भरोसेमंद स्रोतों से जानकारी लें](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम करता है  **[प्रोसेस जारी है](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम करता है  **[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम करता है |
| speedकॉन्टेंट देखने के विकल्प | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम करता है  **[Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता का अनुमान](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - झलक देखें: `gemini-robotics-er-2-preview` |
| calendar\_monthनया अपडेट | जुलाई 2026 |
| id\_cardमॉडल कार्ड | [मॉडल कार्ड](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=hi) |

### Gemini Robotics ER 2 स्ट्रीमिंग की झलक

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `gemini-robotics-er-2-streaming-preview` |
| saveइस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  1,31,072  **आउटपुट टोकन की सीमा**  65,536 |
| handymanसुविधाएं | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम नहीं करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम नहीं करता है  **[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम नहीं करता है  **[कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**  काम नहीं करता है  **[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम नहीं करता है  **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम करता है  **[Google Maps से जानकारी लेना](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम नहीं करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम करता है  **[भरोसेमंद स्रोतों से जानकारी लें](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम नहीं करता है  **[प्रोसेस जारी है](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम करता है  **[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम नहीं करता है |
| speedकॉन्टेंट देखने के विकल्प | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम नहीं करता है  **[Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता का अनुमान](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - झलक देखें: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthनया अपडेट | जुलाई 2026 |
| id\_cardमॉडल कार्ड | [मॉडल कार्ड](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=hi) |

### Gemini Robotics ER 1.6 Preview

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `gemini-robotics-er-1.6-preview` |
| saveइस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  1,31,072  **आउटपुट टोकन की सीमा**  65,536 |
| handymanसुविधाएं | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम नहीं करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम करता है  **[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम करता है  **[कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**  काम करता है  **[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम करता है  **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम करता है  **[Google Maps से जानकारी लेना](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम नहीं करता है  **[भरोसेमंद स्रोतों से जानकारी लें](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम करता है  **[प्रोसेस जारी है](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम करता है  **[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम करता है |
| speedकॉन्टेंट देखने के विकल्प | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम करता है  **[Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता का अनुमान](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - शट डाउन करें: `gemini-robotics-er-1.6-preview` |
| calendar\_monthनया अपडेट | दिसंबर 2025 |
| cognition\_2जानकारी न मिलना | जनवरी 2025 |

## आगे क्या करना है

- [स्पेशल रीज़निंग](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=hi) — पॉइंट करना, ट्रैक करना, बाउंडिंग बॉक्स, ट्रैजेक्टरी.
- [एजेंटिक एआई की सुविधाएं](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=hi) — कोड एक्ज़ीक्यूशन, इंस्ट्रुमेंट रीडिंग, इमेज एनोटेशन.
- [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=hi) — कस्टम रोबोट एपीआई की मदद से, लंबे समय तक चलने वाले टास्क.
- [स्ट्रीमिंग के साथ रोबोटिक्स](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) — रीयल-टाइम में दोनों तरफ़ से स्ट्रीमिंग (सिर्फ़ Gemini Robotics ER 2 के लिए).
- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=hi) — किसी खास पल को ढूंढना और प्रोग्रेस को कैटगरी में बांटना (सिर्फ़ Gemini Robotics ER 2 के लिए).
- [Google DeepMind robotics safety](https://deepmind.google/models/gemini-robotics/safety?hl=hi) — मॉडल फ़ैमिली के पीछे की सुरक्षा रिसर्च.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-21 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-21 (UTC) को अपडेट किया गया."],[],[]]
