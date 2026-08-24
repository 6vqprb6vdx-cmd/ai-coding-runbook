---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=hi
fetched_at: 2026-08-24T02:18:56.813550+00:00
title: "Gemini \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u0938\u094b\u091a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini के बारे में सोच

[Gemini 3 और 2.5 सीरीज़ के मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi), "थिंकिंग प्रोसेस" का इस्तेमाल करते हैं. इससे, गहराई से विश्लेषण करने और कई चरणों वाली प्लानिंग करने की उनकी क्षमता में काफ़ी सुधार होता है. इसलिए, ये मॉडल कोडिंग, ऐडवांस गणित, और डेटा विश्लेषण जैसे मुश्किल कामों को बेहतर तरीके से कर पाते हैं.

थिंकिंग मॉडल का इस्तेमाल करने पर, Gemini जवाब देने से पहले अंदरूनी तौर पर तर्क करता है. इंटरैक्शन एपीआई, इस वजह को `thought` चरणों के ज़रिए दिखाता है. ये ऐसे चरण होते हैं जो फ़ंक्शन कॉल, उपयोगकर्ता के इनपुट या मॉडल के आउटपुट के साथ-साथ, `thought` ऐरे में क्रम से दिखते हैं.`steps`

हर थॉट स्टेप में दो फ़ील्ड होते हैं:

| फ़ील्ड | ज़रूरी है | ब्यौरा |
| --- | --- | --- |
| `signature` | ✅ हां | मॉडल की इंटरनल रीज़निंग स्टेट का एन्क्रिप्ट (सुरक्षित) किया गया वर्शन. यह हमेशा मौजूद होता है. भले ही, मॉडल कम से कम तर्क दे. |
| `summary` | ❌ नहीं | वजह बताने के लिए, कॉन्टेंट (टेक्स्ट और/या इमेज) की एक सीरीज़. [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=hi) कॉन्फ़िगरेशन के आधार पर, यह फ़ील्ड खाली हो सकता है. ऐसा तब भी हो सकता है, जब मॉडल ने गहराई से विश्लेषण के साथ जवाब न दिया हो या कॉन्टेंट का टाइप अलग हो. उदाहरण के लिए, इमेज के लिए टेक्स्ट वाली खास जानकारी उपलब्ध न हो. |

## सोचने की प्रोसेस के साथ इंटरैक्शन

सोचने वाले मॉडल के साथ इंटरैक्शन शुरू करना, इंटरैक्शन के किसी अन्य अनुरोध की तरह ही होता है. `model` फ़ील्ड में, [सोचने की क्षमता वाले मॉडल](#thinking-levels) में से किसी एक मॉडल का नाम डालें:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## सोच-समझकर तैयार की गई खास जानकारी

सोच के बारे में जानकारी देने वाले जवाबों से, मॉडल की इंटरनल प्रोसेस के बारे में अहम जानकारी मिलती है.
डिफ़ॉल्ट रूप से, सिर्फ़ फ़ाइनल आउटपुट दिखता है. `thinking_summaries` की मदद से, सोच के बारे में खास जानकारी देने वाली सुविधा चालू की जा सकती है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

इन मामलों में, किसी थॉट ब्लॉक में **सिर्फ़ हस्ताक्षर हो सकता है और कोई खास जानकारी नहीं** हो सकती:

- आसान अनुरोध, जिनमें मॉडल ने खास जानकारी जनरेट करने के लिए, सही वजह नहीं बताई
- `thinking_summaries: "none"`, जहां खास जानकारी देने की सुविधा साफ़ तौर पर बंद की गई है
- ऐसा हो सकता है कि कुछ तरह के थॉट कॉन्टेंट, जैसे कि इमेज के लिए टेक्स्ट समरी उपलब्ध न हो

आपके कोड को हमेशा ऐसे थॉट ब्लॉक मैनेज करने चाहिए जिनमें `summary` खाली हो या मौजूद न हो.

## सोच-विचार करके जवाब देने के साथ स्ट्रीमिंग

जनरेट करने के दौरान, सोच के बारे में ज़्यादा जानकारी पाने के लिए स्ट्रीमिंग का इस्तेमाल करें.
Server-Sent Events (SSE) का इस्तेमाल करके, थॉट ब्लॉक डिलीवर किए जाते हैं. इनमें दो अलग-अलग डेल्टा टाइप होते हैं:

| डेल्टा टाइप | इसमें शामिल है | भेजे जाने का समय |
| --- | --- | --- |
| `thought_summary` | टेक्स्ट या इमेज के तौर पर जवाब देने वाला कॉन्टेंट | इंक्रीमेंटल समरी के साथ एक या उससे ज़्यादा डेल्टा |
| `thought_signature` | क्रिप्टोग्राफ़िक हस्ताक्षर | `step.stop` से पहले का आखिरी डेल्टा |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

स्ट्रीमिंग रिस्पॉन्स, Server-Sent Events (एसएसई) का इस्तेमाल करता है. इसमें चरण और इवेंट शामिल होते हैं. उदाहरण के लिए:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## सोचने की प्रोसेस को कंट्रोल करना

Gemini मॉडल, डिफ़ॉल्ट रूप से डाइनैमिक थिंकिंग का इस्तेमाल करते हैं. वे अनुरोध की जटिलता के आधार पर, जवाब देने के लिए ज़रूरी कोशिश को अपने-आप अडजस्ट करते हैं. `thinking_level` पैरामीटर का इस्तेमाल करके, इस व्यवहार को कंट्रोल किया जा सकता है.

| मॉडल | डिफ़ॉल्ट थिंकिंग | इन लेवल पर काम करता है |
| --- | --- | --- |
| gemini-3.6-flash | चालू है (मीडियम) | कम, थोड़ा, सामान्य, ज़्यादा |
| gemini-3.5-flash-lite | चालू है (मिनिमल) | कम, थोड़ा, सामान्य, ज़्यादा |
| gemini-3.1-pro-preview | चालू है (ज़्यादा) | कम, सामान्य, ज़्यादा |
| gemini-3.1-flash-lite-image | चालू है (मिनिमल) | मिनिमल, हाई |
| gemini-3-flash-preview | चालू है (ज़्यादा) | कम, थोड़ा, सामान्य, ज़्यादा |
| gemini-3-pro-preview | चालू है (ज़्यादा) | कम, ज़्यादा |
| gemini-3.5-flash | चालू है (मीडियम) | कम, थोड़ा, सामान्य, ज़्यादा |
| gemini-2.5-pro | चालू | कम, सामान्य, ज़्यादा |
| gemini-2.5-flash | चालू | कम, सामान्य, ज़्यादा |
| gemini-2.5-flash-lite | बंद है | कम, सामान्य, ज़्यादा |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## सोच-समझकर किए गए हस्ताक्षर

थॉट सिग्नेचर, मॉडल की इंटरनल रीज़निंग के एन्क्रिप्ट किए गए वर्शन होते हैं. उन्हें बार-बार किए जाने वाले इंटरैक्शन में, जवाब देने के लिए एक ही तर्क का इस्तेमाल करना होता है.

Interactions API की मदद से, थॉट सिग्नेचर को `generateContent` API की तुलना में ज़्यादा आसानी से मैनेज किया जा सकता है.

### स्टेटफ़ुल मोड (सुझाया गया)

डिफ़ॉल्ट रूप से, स्टेटफ़ुल मोड में Interactions API का इस्तेमाल करने पर (`store: true` सेट करके और बाद के टर्न में `previous_interaction_id` पास करके), सर्वर बातचीत की स्थिति को अपने-आप मैनेज करता है. इसमें सभी थॉट ब्लॉक और सिग्नेचर शामिल होते हैं. इस मोड में, आपको हस्ताक्षर के बारे में कुछ भी करने की ज़रूरत नहीं है. इन्हें पूरी तरह से सर्वर साइड पर मैनेज किया जाता है.

### स्टेटलेस मोड

अगर बातचीत की स्थिति को खुद मैनेज किया जा रहा है (स्टेटलेस मोड) और हर अनुरोध में इनपुट और आउटपुट का पूरा इतिहास पास किया जा रहा है, तो:

- आपको सभी `thought` ब्लॉक को ठीक उसी तरह से फिर से भेजना होगा जिस तरह से वे मॉडल से मिले थे. ऐसा करना **ज़रूरी है**.
- आपको इतिहास से थॉट ब्लॉक हटाने या उनमें बदलाव करने की **अनुमति नहीं है**. ऐसा इसलिए, क्योंकि इनमें ऐसे सिग्नेचर होते हैं जिनकी मदद से मॉडल, जवाब देने के लिए तर्क देना जारी रख सकता है.
- किसी सेशन में मॉडल बदलते समय, आपको पिछले मॉडल के थॉट ब्लॉक फिर से भेजने चाहिए. बैकएंड, कंपैटिबिलिटी को मैनेज करता है.

## कीमत

सोचने की सुविधा चालू होने पर, जवाब की कीमत आउटपुट टोकन और सोचने के लिए इस्तेमाल किए गए टोकन के योग के बराबर होती है. `total_thought_tokens` फ़ील्ड से, जनरेट किए गए थिंकिंग टोकन की कुल संख्या पाई जा सकती है.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

सोचने वाले मॉडल, जवाब की क्वालिटी को बेहतर बनाने के लिए पूरी जानकारी जनरेट करते हैं. इसके बाद, वे [खास जानकारी](#summaries) देते हैं, ताकि यह पता चल सके कि जवाब कैसे जनरेट किया गया. कीमत, मॉडल को जनरेट करने के लिए ज़रूरी सभी थॉट टोकन के आधार पर तय की जाती है. भले ही, एपीआई से सिर्फ़ खास जानकारी आउटपुट की गई हो.

[टोकन की गिनती](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) गाइड में, टोकन के बारे में ज़्यादा जानें.

## सबसे सही तरीके

इन दिशा-निर्देशों का पालन करके, थिंकिंग मॉडल का असरदार तरीके से इस्तेमाल करें.

- **गहराई से विश्लेषण देखें**: जवाब के बारे में जानकारी देने वाले सारांश का विश्लेषण करें, ताकि आपको यह पता चल सके कि जवाब क्यों नहीं मिला. साथ ही, प्रॉम्प्ट को बेहतर बनाया जा सके.
- **सोचने के लिए बजट कंट्रोल करना**: टोकन बचाने के लिए, मॉडल को लंबे जवाबों के लिए कम सोचने का निर्देश दें.
- **आसान टास्क**: तथ्यों को खोजने या उन्हें कैटगरी में बांटने के लिए, कम से कम या सामान्य सोच का इस्तेमाल करना (जैसे, "DeepMind की स्थापना कहां हुई थी?").
- **मॉडरेट टास्क**: कॉन्सेप्ट की तुलना करने या क्रिएटिव तरीके से तर्क देने के लिए, डिफ़ॉल्ट थिंकिंग का इस्तेमाल करें. उदाहरण के लिए, इलेक्ट्रिक और हाइब्रिड कारों की तुलना करें.
- **जटिल टास्क**: ऐडवांस कोडिंग, गणित या कई चरणों वाली प्लानिंग के लिए, ज़्यादा से ज़्यादा सोच-विचार करना (उदाहरण के लिए, एआईएमई गणित की समस्याओं को हल करना).

## आगे क्या करना है

- [टेक्स्ट जनरेशन](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi): टेक्स्ट में बुनियादी जवाब
- [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi): टूल से कनेक्ट करना
- [Gemini 3 की गाइड](https://ai.google.dev/gemini-api/docs/gemini-3?hl=hi): मॉडल के हिसाब से सुविधाएं

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
