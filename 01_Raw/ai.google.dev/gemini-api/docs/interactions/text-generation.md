---
source_url: https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=hi
fetched_at: 2026-06-01T19:35:30.360254+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# टेक्स्ट जनरेट करने की सुविधा

Gemini API, टेक्स्ट, इमेज, वीडियो, और ऑडियो इनपुट से टेक्स्ट आउटपुट जनरेट कर सकता है.

यहां एक सामान्य उदाहरण दिया गया है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?"
  }'
```

Google GenAI SDK, मॉडल के जवाब को ऐक्सेस करने के लिए, लौटाए गए `Interaction` ऑब्जेक्ट पर सीधे तौर पर सुविधाजनक प्रॉपर्टी उपलब्ध कराता है.

सबसे आम हेल्पर **`interaction.output_text`** (स्ट्रिंग) है. यह मॉडल के जवाब में मौजूद, टेक्स्ट के आखिरी ब्लॉक दिखाता है. अगर जवाब को एक के बाद एक कई `TextContent` ब्लॉक में बांटा जाता है, तो यह उन्हें अपने-आप जोड़ देता है.
ध्यान दें कि `.output_text` में, टेक्स्ट के पहले वाले ब्लॉक शामिल नहीं होते. इन्हें, टेक्स्ट के अलावा अन्य कॉन्टेंट (जैसे, विचार, इमेज, ऑडियो या टूल कॉल) से अलग किया जाता है. जटिल या इंटरलीव्ड मल्टीमोडल जवाबों के लिए, इसके बजाय आपको `steps` पर मैन्युअल तरीके से इटरेट करना होगा. अन्य मीडिया की सुविधाजनक प्रॉपर्टी के बारे में ज़्यादा जानने के लिए, [इंटरैक्शन की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions?hl=hi#convenience-properties) देखें.

## Gemini की मदद से सोच-समझकर जवाब देना

Gemini मॉडल में अक्सर ["थिंकिंग"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi)
की सुविधा डिफ़ॉल्ट रूप से चालू होती है. इससे मॉडल, किसी अनुरोध का जवाब देने से पहले, सोच-समझकर जवाब दे पाता है.

हर मॉडल, अलग-अलग थिंकिंग कॉन्फ़िगरेशन के साथ काम करता है. इससे आपको लागत, इंतज़ार का समय, और इंटेलिजेंस पर कंट्रोल मिलता है. ज़्यादा जानकारी के लिए, [थिंकिंग गाइड](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi#set-budget) देखें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## सिस्टम के निर्देश और अन्य कॉन्फ़िगरेशन

सिस्टम के निर्देशों की मदद से, Gemini मॉडल के व्यवहार को गाइड किया जा सकता है. मॉडल के व्यवहार को कॉन्फ़िगर करने के लिए, `system_instruction` पैरामीटर पास करें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

`generation_config` पैरामीटर का इस्तेमाल करके, जनरेशन के डिफ़ॉल्ट पैरामीटर भी बदले जा सकते हैं. जैसे, तापमान.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

कॉन्फ़िगर किए जा सकने वाले पैरामीटर और उनके
ब्यौरे की पूरी सूची देखने के लिए, [Interactions API का रेफ़रंस](https://ai.google.dev/api/interactions-api?hl=hi)देखें.

## मल्टीमोडल इनपुट

Gemini API, मल्टीमोडल इनपुट के साथ काम करता है. इससे टेक्स्ट को मीडिया फ़ाइलों के साथ जोड़ा जा सकता है. यहां दिया गया उदाहरण, इमेज उपलब्ध कराने का तरीका दिखाता है:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

इमेज उपलब्ध कराने के अन्य तरीकों और इमेज को बेहतर तरीके से प्रोसेस करने के बारे में जानने के लिए,
हमारी [इमेज को समझने की गाइड](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=hi) देखें.
एपीआई, [दस्तावेज़](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=hi), [वीडियो](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=hi), और
[ऑडियो](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=hi) इनपुट के साथ-साथ, उन्हें समझने की सुविधा भी देता है.

## जवाब स्ट्रीम करना

डिफ़ॉल्ट रूप से, मॉडल जनरेशन की पूरी प्रोसेस पूरी होने के बाद ही जवाब देता है.

बेहतर इंटरैक्शन के लिए, स्ट्रीम करने की सुविधा का इस्तेमाल करें. इससे जवाब के चंक जनरेट होने पर उन्हें मैनेज किया जा सकता है. इवेंट टाइप,
टूल के साथ स्ट्रीम करने की सुविधा, थिंकिंग, एजेंट, और इमेज जनरेशन के बारे में पूरी जानकारी पाने के लिए, स्ट्रीम करने की सुविधा से जुड़े इंटरैक्शन की खास [गाइड](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=hi)
देखें.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## कई राउंड वाली बातचीत

Interactions API, `previous_interaction_id` का इस्तेमाल करके, इंटरैक्शन को एक साथ जोड़कर कई राउंड वाली बातचीत की सुविधा देता है. हर राउंड एक अलग इंटरैक्शन होता है. एपीआई, बातचीत के इतिहास को अपने-आप मैनेज करता है.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

कई राउंड वाली बातचीत के लिए, स्ट्रीम करने की सुविधा का भी इस्तेमाल किया जा सकता है. इसके लिए, `previous_interaction_id` को स्ट्रीम करने के तरीकों के साथ जोड़ें.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
    stream: true,
  });
  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## स्टेटलेस बातचीत

डिफ़ॉल्ट रूप से, Interactions API, `previous_interaction_id` का इस्तेमाल करने पर, बातचीत की स्थिति को सर्वर-साइड पर मैनेज करता है. हालांकि, क्लाइंट साइड पर बातचीत के इतिहास को खुद मैनेज करके, स्टेटलेस मोड में भी काम किया जा सकता है.

स्टेटलेस मोड का इस्तेमाल करने के लिए: 1. सर्वर-साइड स्टोरेज से ऑप्ट आउट करने के लिए, अपने अनुरोध में `store=false` सेट करें.
2. क्लाइंट साइड पर, बातचीत के इतिहास को **स्टेप** की एक कलेक्शन के तौर पर बनाए रखें.
3. इसके बाद के अनुरोधों में, इकट्ठा किए गए चरणों को `input` फ़ील्ड में पास करें. साथ ही, अपने नए राउंड को `user_input` स्टेप के तौर पर जोड़ें.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "I have 2 dogs in my house." }]
    }
  ];

  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  history.push(...interaction1.steps);

  history.push({
    type: "user_input",
    content: [{ type: "text", text: "How many paws are in my house?" }]
  });

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## प्रॉम्प्ट के बारे में सलाह

Gemini का ज़्यादा से ज़्यादा फ़ायदा पाने के सुझाव पाने के लिए, प्रॉम्प्ट इंजीनियरिंग की हमारी [गाइड](https://ai.google.dev/gemini/docs/prompting-strategies?hl=hi) देखें.

## आगे क्या करना है

- Google AI Studio में [Gemini आज़माएं](https://aistudio.google.com?hl=hi).
- JSON जैसे जवाबों के लिए,
  [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=hi) के साथ
  एक्सपेरिमेंट करें.
- [[[[इमेज, वीडियो, ऑडियो, और दस्तावेज़ को समझने की Gemini की क्षमताओं के बारे में जानें.](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=hi)](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=hi)](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=hi)](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=hi)
- मल्टीमोडल
  [फ़ाइल प्रॉम्प्ट करने की रणनीतियों](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi#prompt-guide) के बारे में जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-28 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-28 (UTC) को अपडेट किया गया."],[],[]]
