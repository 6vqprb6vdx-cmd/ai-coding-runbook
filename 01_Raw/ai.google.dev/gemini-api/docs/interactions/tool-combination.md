---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=hi
fetched_at: 2026-06-08T15:08:29.438606+00:00
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

# पहले से मौजूद टूल और फ़ंक्शन कॉल करने की सुविधा को एक साथ इस्तेमाल करना

Gemini में, [पहले से मौजूद टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi) (जैसे, `google_search`) और [फ़ंक्शन कॉल करने की सुविधा](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi) (
जिसे *कस्टम टूल* भी कहा जाता है) को एक साथ इस्तेमाल किया जा सकता है. इसके लिए, टूल कॉल के कॉन्टेक्स्ट के इतिहास को सेव और दिखाया जाता है. पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन की मदद से, एजेंटिक वर्कफ़्लो बनाए जा सकते हैं. जैसे, मॉडल, आपकी खास कारोबार की लॉजिक को कॉल करने से पहले, वेब पर मौजूद रीयल-टाइम डेटा के आधार पर जानकारी दे सकता है.

यहां एक उदाहरण दिया गया है, जिसमें `google_search` और कस्टम फ़ंक्शन `getWeather` के साथ, पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन का इस्तेमाल किया गया है:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## यह कैसे काम करता है

Gemini 3 मॉडल, पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन को इस्तेमाल करने के लिए, *टूल कॉन्टेक्स्ट सर्कुलेशन* का इस्तेमाल करते हैं. टूल कॉन्टेक्स्ट सर्कुलेशन की मदद से, पहले से मौजूद टूल के कॉन्टेक्स्ट को सेव और दिखाया जा सकता है. साथ ही, इसे एक ही इंटरैक्शन में कस्टम टूल के साथ शेयर किया जा सकता है.

### टूल के कॉम्बिनेशन की सुविधा चालू करना

- कॉम्बिनेशन के व्यवहार को ट्रिगर करने के लिए, [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi#function-declarations) को उन पहले से मौजूद टूल के साथ शामिल करें जिनका आपको इस्तेमाल करना है, along

### एपीआई, चरण दिखाता है

इंटरैक्शन के जवाब में, एपीआई, पहले से मौजूद टूल कॉल और फ़ंक्शन (कस्टम टूल) कॉल के लिए अलग-अलग चरण दिखाता है:

- **पहले से मौजूद टूल के चरण**: एपीआई इन्हें अपने-आप मैनेज करता है. साथ ही, हर चरण में
  कॉन्टेक्स्ट को सेव रखता है.
- **फ़ंक्शन कॉल के चरण**: एपीआई, आपके
  कस्टम फ़ंक्शन के लिए `function_call` चरण दिखाता है. आपको फ़ंक्शन को लागू करना होता है और उसका नतीजा वापस देना होता है.

### जवाब में मिले चरणों में ज़रूरी फ़ील्ड

जवाब में मिले चरणों में कुछ फ़ील्ड, टूल के कॉन्टेक्स्ट को बनाए रखने और टूल के कॉम्बिनेशन को चालू करने के लिए ज़रूरी होते हैं:

- **`id`**: यह `function_call` और `function_response` चरणों में मौजूद होता है. यह एक यूनीक आइडेंटिफ़ायर होता है, जो किसी कॉल को उसके जवाब से मैप करता है.
- **`signature`**: यह `thought` चरणों के साथ-साथ, Gemini 3 या इसके बाद के मॉडल के लिए, सभी टूल कॉल (जैसे, `function_call`) और नतीजे (जैसे, `function_response`) चरणों में मौजूद होता है. एनक्रिप्ट किया गया यह कॉन्टेक्स्ट, इंटरैक्शन के दौरान **टूल कॉन्टेक्स्ट सर्कुलेशन** की सुविधा चालू करता है.

**इन फ़ील्ड को मैनेज करना:**

- **स्टेटफ़ुल मोड (सुझाया गया)**: `previous_interaction_id` का इस्तेमाल करने पर, सर्वर, `id` और `signature` दोनों फ़ील्ड को अपने-आप हैंडल करता है.
- **स्टेटलेस मोड**: बातचीत के इतिहास को मैन्युअल तरीके से मैनेज करते समय, आपको यह पक्का करना होगा कि पुष्टि करने और कॉन्टेक्स्ट को बनाए रखने के लिए, बाद के अनुरोधों में मॉडल को `id` और `signature` दोनों फ़ील्ड पास किए जाएं. अगर आपने जवाब के पूरे ऑब्जेक्ट को इतिहास में पास किया है, तो आधिकारिक SDK इसे अपने-आप हैंडल करते हैं.

### टूल के हिसाब से डेटा

कुछ पहले से मौजूद टूल, उपयोगकर्ता को दिखने वाले डेटा आर्ग्युमेंट दिखाते हैं. ये आर्ग्युमेंट, टूल के टाइप के हिसाब से अलग-अलग होते हैं.

| टूल | उपयोगकर्ता को दिखने वाले टूल कॉल आर्ग्युमेंट (अगर कोई हो) | उपयोगकर्ता को दिखने वाला टूल रिस्पॉन्स (अगर कोई हो) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URLs to be browsed | `status`: Browse status `retrieved_url`: URLs browsed |
| **file\_search** | कोई नहीं | कोई नहीं |

## टोकन और कीमत

ध्यान दें कि अनुरोधों में, पहले से मौजूद टूल कॉल के हिस्सों को `prompt_token_count` में गिना जाता है. अब ये इंटरमीडिएट टूल चरण दिखते हैं और आपको वापस मिलते हैं. इसलिए, ये बातचीत के इतिहास का हिस्सा होते हैं. यह सिर्फ़
*अनुरोधों* के लिए लागू होता है, *जवाबों* के लिए नहीं.

Google Search टूल, इस नियम का अपवाद है. Google Search, क्वेरी के लेवल पर अपना कीमत मॉडल पहले से ही
लागू करता है. इसलिए, टोकन के लिए दो बार
शुल्क नहीं लिया जाता ([कीमत वाला](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज देखें).

ज़्यादा जानकारी के लिए, [टोकन](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=hi) वाला पेज पढ़ें.

## सीमाएं

- टूल कॉन्टेक्स्ट सर्कुलेशन की सुविधा चालू होने पर, डिफ़ॉल्ट रूप से `validated` मोड का इस्तेमाल किया जाता है. `auto` मोड काम नहीं करता.
- `google_search` जैसे पहले से मौजूद टूल, जगह और मौजूदा समय की जानकारी पर निर्भर करते हैं. इसलिए, अगर आपके `system_instruction` या `function_declaration.description` में, जगह और समय की जानकारी में कोई गड़बड़ी है, तो टूल के कॉम्बिनेशन की सुविधा ठीक से काम नहीं कर सकती.

## इन टूल पर पासकी का इस्तेमाल किया जा सकता है

सर्वर-साइड (पहले से मौजूद) टूल पर, टूल कॉन्टेक्स्ट सर्कुलेशन का स्टैंडर्ड तरीका लागू होता है.
कोड चलाने की सुविधा भी सर्वर-साइड टूल है, लेकिन इसमें कॉन्टेक्स्ट सर्कुलेशन के लिए, पहले से मौजूद अपना समाधान है. कंप्यूटर के इस्तेमाल और फ़ंक्शन कॉल करने की सुविधा, क्लाइंट-साइड टूल हैं. इनमें भी कॉन्टेक्स्ट सर्कुलेशन के लिए, पहले से मौजूद समाधान हैं.

| टूल | निष्पादन की जगह | कॉन्टेक्स्ट सर्कुलेशन की सुविधा |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=hi) | सर्वर-साइड | उपलब्ध |
| [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=hi) | सर्वर-साइड | उपलब्ध |
| [यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=hi) | सर्वर-साइड | उपलब्ध |
| [फ़ाइल सर्च](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=hi) | सर्वर-साइड | उपलब्ध |
| [कोड चलाने की सुविधा](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=hi) | सर्वर-साइड | उपलब्ध (पहले से मौजूद, `code_execution` और `code_execution_result` चरणों का इस्तेमाल करता है) |
| [कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=hi) | क्लाइंट-साइड | उपलब्ध (पहले से मौजूद, `function_call` और `function_response` चरणों का इस्तेमाल करता है) |
| [कस्टम फ़ंक्शन](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi) | क्लाइंट-साइड | उपलब्ध (पहले से मौजूद, `function_call` और `function_response` चरणों का इस्तेमाल करता है) |

## आगे क्या करना है

- Gemini API में, [फ़ंक्शन कॉल करने की सुविधा](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi) के बारे में ज़्यादा जानें.
- इन टूल के बारे में जानें:
  - [Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=hi)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=hi)
  - [यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=hi)
  - [फ़ाइल सर्च](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया."],[],[]]
