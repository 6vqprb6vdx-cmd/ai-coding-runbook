---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=hi
fetched_at: 2026-06-08T14:59:00.159414+00:00
title: "Gemini API \u0915\u094d\u0935\u093f\u0915\u0938\u094d\u091f\u093e\u0930\u094d\u091f \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini API क्विकस्टार्ट

इस क्विकस्टार्ट गाइड में, हमारी [लाइब्रेरी](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) इंस्टॉल करने और पहला अनुरोध करने का तरीका बताया गया है. साथ ही, इसमें जवाब स्ट्रीम करने, कई बार बातचीत करने, और स्टैंडर्ड `generateContent` तरीके का इस्तेमाल करके टूल इस्तेमाल करने का तरीका बताया गया है.

## शुरू करने से पहले

Gemini API का इस्तेमाल करने के लिए, आपके पास एक एपीआई पासकोड होना चाहिए. इससे आपके अनुरोधों की पुष्टि की जा सकेगी, सुरक्षा से जुड़ी सीमाओं को लागू किया जा सकेगा, और आपके खाते के इस्तेमाल को ट्रैक किया जा सकेगा.

शुरू करने के लिए, AI Studio पर मुफ़्त में एक प्रोजेक्ट बनाएं:

[Gemini API पासकोड बनाना](https://aistudio.google.com/app/apikey?hl=hi)

## Google GenAI SDK इंस्टॉल करना

### Python

[Python 3.9 या इसके बाद के वर्शन](https://www.python.org/downloads/) का इस्तेमाल करके, [`google-genai` पैकेज](https://pypi.org/project/google-genai/) इंस्टॉल करें. इसके लिए, यहां दी गई [pip कमांड](https://packaging.python.org/en/latest/tutorials/installing-packages/) का इस्तेमाल करें:

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager) का इस्तेमाल करके, [TypeScript और JavaScript के लिए Google Gen AI SDK](https://www.npmjs.com/package/@google/genai) इंस्टॉल करें. इसके लिए, यहां दी गई [npm कमांड](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) का इस्तेमाल करें:

```
npm install @google/genai
```

## टेक्स्ट जनरेट करना

`models.generate_content` तरीके का इस्तेमाल करके, [टेक्स्ट वाला जवाब जनरेट करें](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## जवाब स्ट्रीम करें

डिफ़ॉल्ट रूप से, मॉडल जवाब सिर्फ़ तब देता है, जब जनरेट करने की पूरी प्रोसेस पूरी हो जाती है. तेज़ी से और ज़्यादा इंटरैक्टिव अनुभव पाने के लिए, जवाब जनरेट होने के साथ-साथ, [जवाब के हिस्सों को स्ट्रीम किया जा सकता है](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#stream).

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## एक से ज़्यादा बार बातचीत करने की सुविधा

एक से ज़्यादा बार बातचीत करने की सुविधा के लिए, एसडीके एक स्टेटफ़ुल `chats` हेल्पर उपलब्ध कराते हैं. इससे [एक से ज़्यादा बार बातचीत करने की सुविधा](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#chat) बनाई जा सकती है. यह सुविधा, बातचीत के इतिहास को अपने-आप मैनेज करती है.

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## टूल इस्तेमाल करना

मॉडल की क्षमताओं को बेहतर बनाएं. इसके लिए, [Google Search से मिले नतीजों के आधार पर जवाब जनरेट करें](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), ताकि रीयल-टाइम में वेब कॉन्टेंट ऐक्सेस किया जा सके. मॉडल अपने-आप यह तय करता है कि कब खोजना है, क्वेरी को पूरा करना है, और जवाब जनरेट करना है.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Gemini API में पहले से मौजूद अन्य टूल भी काम करते हैं:

- **[कोड को एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**:
  इस सुविधा की मदद से, मॉडल को गणित की मुश्किल समस्याओं को हल करने के लिए Python कोड लिखने और उसे चलाने की अनुमति मिलती है.
- **[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**: इसकी मदद से, जवाबों को उन वेब पेज यूआरएल के हिसाब से तैयार किया जा सकता है जिन्हें आपने उपलब्ध कराया है.
- **[फ़ाइल खोज](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**: इसकी मदद से, फ़ाइलें अपलोड की जा सकती हैं. साथ ही, सिमैंटिक सर्च का इस्तेमाल करके, उनके कॉन्टेंट में जवाब खोजे जा सकते हैं.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**: इसकी मदद से, जगह की जानकारी के डेटा के आधार पर जवाब पाए जा सकते हैं. साथ ही, जगहों, दिशा-निर्देशों, और मैप को खोजा जा सकता है.
- **[कंप्यूटर का इस्तेमाल करना](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**: इसकी मदद से मॉडल, वर्चुअल कंप्यूटर स्क्रीन, कीबोर्ड, और माउस के साथ इंटरैक्ट करके टास्क पूरे कर सकता है.

## कस्टम फ़ंक्शन कॉल करना

अपने कस्टम टूल और एपीआई से मॉडल कनेक्ट करने के लिए, **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)** का इस्तेमाल करें. मॉडल यह तय करता है कि आपकी फ़ंक्शन को कब कॉल करना है. साथ ही, आपके ऐप्लिकेशन को लागू करने के लिए, जवाब में `functionCall` दिखाता है.

इस उदाहरण में, तापमान का एक मॉक फ़ंक्शन तय किया गया है. साथ ही, यह जांच की गई है कि मॉडल इसे कॉल करना चाहता है या नहीं.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## आगे क्या करना है

अब आपने Gemini API का इस्तेमाल शुरू कर दिया है. ज़्यादा बेहतर ऐप्लिकेशन बनाने के लिए, यहाँ दी गई गाइड पढ़ें:

- [टेक्स्ट जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi)
- [इमेज जनरेट करना](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)
- [इमेज की बारीक़ी से पहचान](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi)
- [सोच रहा है](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)
- [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)
- [Google Search से सटीक जानकारी पाने की सुविधा](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)
- [ज़्यादा कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/long-context?hl=hi)
- [एम्बेडिंग](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया."],[],[]]
