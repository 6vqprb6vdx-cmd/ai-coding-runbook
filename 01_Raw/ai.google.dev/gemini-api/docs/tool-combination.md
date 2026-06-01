---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi
fetched_at: 2026-06-01T19:45:32.402413+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# पहले से मौजूद टूल और फ़ंक्शन कॉलिंग को एक साथ इस्तेमाल करना

Gemini, [पहले से मौजूद टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi) (जैसे, `google_search`) और [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) (*कस्टम टूल* भी कहा जाता है) को एक साथ इस्तेमाल करने की अनुमति देता है. इसके लिए, टूल कॉल के कॉन्टेक्स्ट के इतिहास को सेव किया जाता है और उसे दिखाया जाता है. पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन की मदद से, एजेंटिक वर्कफ़्लो को आसानी से पूरा किया जा सकता है. उदाहरण के लिए, मॉडल आपकी खास कारोबारी लॉजिक को कॉल करने से पहले, वेब पर मौजूद रीयल-टाइम डेटा को आधार बना सकता है.

यहां एक उदाहरण दिया गया है, जिसमें `google_search` और कस्टम फ़ंक्शन `getWeather` के साथ, पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन का इस्तेमाल किया गया है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.getGenerativeModel({
        model: "gemini-3.5-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.5-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## यह कैसे काम करता है

Gemini 3 मॉडल, पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन को इस्तेमाल करने के लिए, *टूल कॉन्टेक्स्ट सर्कुलेशन* का इस्तेमाल करते हैं. टूल कॉन्टेक्स्ट सर्कुलेशन की मदद से, पहले से मौजूद टूल के कॉन्टेक्स्ट को सेव किया जा सकता है और उसे दिखाया जा सकता है. साथ ही, इसे एक ही कॉल में, एक से दूसरी बारी में कस्टम टूल के साथ शेयर किया जा सकता है.

### टूल कॉम्बिनेशन की सुविधा चालू करना

- टूल कॉन्टेक्स्ट सर्कुलेशन की सुविधा चालू करने के लिए, आपको `include_server_side_tool_invocations` फ़्लैग को `true` पर सेट करना होगा.
- कॉम्बिनेशन के व्यवहार को ट्रिगर करने के लिए, [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#function-declarations) को उन
  पहले से मौजूद टूल के साथ शामिल करें जिनका इस्तेमाल आपको करना है.
  - अगर आपने `function_declarations` को शामिल नहीं किया है, तब भी फ़्लैग सेट होने पर, टूल कॉन्टेक्स्ट सर्कुलेशन, शामिल किए गए पहले से मौजूद टूल पर काम करेगा.

### एपीआई, इन हिस्सों को दिखाता है

एक ही जवाब में, एपीआई, पहले से मौजूद टूल कॉल के लिए `toolCall` और `toolResponse` के हिस्से दिखाता है. फ़ंक्शन (कस्टम टूल) कॉल के लिए, एपीआई, `functionCall` कॉल का हिस्सा दिखाता है. इसके जवाब में, उपयोगकर्ता अगली बारी में `functionResponse` का हिस्सा देता है.

- `toolCall` और `toolResponse`: एपीआई, इन हिस्सों को इसलिए दिखाता है, ताकि यह पता चल सके कि सर्वर साइड पर कौनसे टूल चलाए गए हैं और उनके नतीजे क्या हैं. इससे अगली बारी में, कॉन्टेक्स्ट को सेव किया जा सकता है.
- `functionCall` और `functionResponse`: एपीआई, फ़ंक्शन कॉल को उपयोगकर्ता को भेजता है, ताकि वह इसे भर सके. इसके बाद, उपयोगकर्ता, नतीजे को फ़ंक्शन रिस्पॉन्स में वापस भेजता है. ये हिस्से, Gemini API में सभी [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) के लिए स्टैंडर्ड हैं. ये सिर्फ़ टूल कॉम्बिनेशन की सुविधा के लिए यूनीक नहीं हैं.
- ([सिर्फ़ कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) टूल)
  `executableCode` और `codeExecutionResult`:
  कोड एक्ज़ीक्यूशन टूल का इस्तेमाल करते समय, एपीआई, `functionCall` और
  `functionResponse` के बजाय, `executableCode` (मॉडल से जनरेट किया गया कोड,
  जिसे एक्ज़ीक्यूट किया जाना है) और `codeExecutionResult` (एक्ज़ीक्यूटेबल कोड का
  नतीजा) दिखाता है.

कॉन्टेक्स्ट को बनाए रखने और टूल
कॉम्बिनेशन की सुविधा चालू करने के लिए, आपको हर बारी में मॉडल को सभी हिस्से वापस भेजने होंगे. इनमें शामिल सभी [फ़ील्ड](#critical-fields) भी शामिल होने चाहिए जो उनमें
हैं.

### दिखाए गए हिस्सों में ज़रूरी फ़ील्ड

एपीआई से दिखाए गए कुछ [हिस्सों](#api-returns-parts) में, `id`,
`tool_type`, और `thought_signature` फ़ील्ड शामिल होंगे. ये फ़ील्ड, टूल कॉन्टेक्स्ट को बनाए रखने के लिए ज़रूरी हैं. इसलिए, ये टूल कॉम्बिनेशन के लिए भी ज़रूरी हैं. आपको अपने अगले अनुरोधों में, *जवाब में दिए गए* सभी हिस्से वापस भेजने होंगे.

- `id`: यह एक यूनीक आइडेंटिफ़ायर है, जो किसी कॉल को उसके जवाब से मैप करता है. `id` , **सभी फ़ंक्शन कॉल के जवाबों पर सेट होता है** . भले ही, टूल कॉन्टेक्स्ट सर्कुलेशन की सुविधा चालू हो या न हो.
  *आपको फ़ंक्शन रिस्पॉन्स में वही `id` देना होगा
  जो एपीआई, फ़ंक्शन कॉल में देता है.* पहले से मौजूद टूल, टूल कॉल और टूल रिस्पॉन्स के बीच `id` को अपने-आप शेयर करते हैं.
  - यह टूल से जुड़े सभी हिस्सों में मौजूद होता है: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: इससे पता चलता है कि कौनसा टूल इस्तेमाल किया जा रहा है. जैसे, पहले से मौजूद टूल का नाम (उदाहरण के लिए, `URL_CONTEXT`) या फ़ंक्शन का नाम (उदाहरण के लिए, `getWeather`).
  - यह `toolCall` और `toolResponse` के हिस्सों में मौजूद होता है.
- `thought_signature`: यह **एपीआई से दिखाए गए हर हिस्से** में एम्बेड किया गया, असल में एनक्रिप्ट किया गया कॉन्टेक्स्ट होता है. थॉट सिग्नेचर के बिना, कॉन्टेक्स्ट को फिर से नहीं बनाया जा सकता. अगर आपने हर बारी में सभी हिस्सों के लिए थॉट सिग्नेचर नहीं दिखाए, तो मॉडल में गड़बड़ी होगी.
  - यह *सभी* हिस्सों में मौजूद होता है.

### टूल के हिसाब से डेटा

कुछ पहले से मौजूद टूल, उपयोगकर्ता को दिखने वाले डेटा आर्ग्युमेंट दिखाते हैं. ये आर्ग्युमेंट, टूल के टाइप के हिसाब से अलग-अलग होते हैं.

| टूल | उपयोगकर्ता को दिखने वाले टूल कॉल आर्ग्युमेंट (अगर कोई हो) | उपयोगकर्ता को दिखने वाला टूल रिस्पॉन्स (अगर कोई हो) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` वे यूआरएल जिन्हें ब्राउज़ किया जाना है | `urls_metadata` `retrieved_url`: ब्राउज़ किए गए यूआरएल `url_retrieval_status`: ब्राउज़ करने की स्थिति |
| **FILE\_SEARCH** | कोई नहीं | कोई नहीं |

## टूल कॉम्बिनेशन के अनुरोध की संरचना का उदाहरण

अनुरोध की इस संरचना में, प्रॉम्प्ट की संरचना दिखाई गई है: "अमेरिका का सबसे उत्तरी शहर कौनसा है? वहां आज कैसा मौसम है?". इसमें तीन टूल को एक साथ इस्तेमाल किया गया है: Gemini के पहले से मौजूद टूल `google_search` और `code_execution`, और एक कस्टम फ़ंक्शन `get_weather`.

```
{
  "model": "models/gemini-3.5-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## टोकन और कीमत

ध्यान दें कि अनुरोधों में `toolCall` और `toolResponse` के हिस्सों को `prompt_token_count` में गिना जाता है. इंटरमीडिएट टूल के ये चरण अब दिखते हैं और आपको दिखाए जाते हैं. इसलिए, ये बातचीत के इतिहास का हिस्सा होते हैं. यह सिर्फ़
*अनुरोधों* के लिए लागू होता है, *जवाबों* के लिए नहीं.

Google Search टूल, इस नियम का अपवाद है. Google Search, क्वेरी के लेवल पर अपना कीमत मॉडल पहले से ही
लागू करता है. इसलिए, टोकन के लिए दो बार
शुल्क नहीं लिया जाता ([कीमत वाला](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज देखें).

ज़्यादा जानकारी के लिए, [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) वाला पेज पढ़ें.

## सीमाएं

- `include_server_side_tool_invocations` फ़्लैग चालू होने पर, डिफ़ॉल्ट रूप से `VALIDATED` मोड का इस्तेमाल करें. `AUTO` मोड काम नहीं करता
- `google_search` जैसे पहले से मौजूद टूल, जगह और मौजूदा समय की जानकारी पर निर्भर करते हैं. इसलिए, अगर आपके `system_instruction` या `function_declaration.description` में जगह और समय की जानकारी में कोई अंतर है, तो टूल कॉम्बिनेशन की सुविधा शायद ठीक से काम न करे.

## काम करने वाले टूल

सर्वर-साइड (पहले से मौजूद) टूल पर, टूल कॉन्टेक्स्ट सर्कुलेशन का स्टैंडर्ड तरीका लागू होता है.
कोड एक्ज़ीक्यूशन भी एक सर्वर-साइड टूल है, लेकिन इसमें कॉन्टेक्स्ट सर्कुलेशन के लिए पहले से मौजूद अपना समाधान है. कंप्यूटर का इस्तेमाल और फ़ंक्शन कॉलिंग, क्लाइंट-साइड टूल हैं. इनमें भी कॉन्टेक्स्ट सर्कुलेशन के लिए पहले से मौजूद समाधान हैं.

| टूल | एक्ज़ीक्यूशन साइड | कॉन्टेक्स्ट सर्कुलेशन की सुविधा |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) | सर्वर-साइड | काम करता है |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi) | सर्वर-साइड | काम करता है |
| [यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) | सर्वर-साइड | काम करता है |
| [फ़ाइल खोजें](https://ai.google.dev/gemini-api/docs/file-search?hl=hi) | सर्वर-साइड | काम करता है |
| [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) | सर्वर-साइड | काम करता है (पहले से मौजूद, `executableCode` और `codeExecutionResult` के हिस्सों का इस्तेमाल करता है) |
| [कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) | क्लाइंट-साइड | काम करता है (पहले से मौजूद, `functionCall` और `functionResponse` के हिस्सों का इस्तेमाल करता है) |
| [कस्टम फ़ंक्शन](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) | क्लाइंट-साइड | काम करता है (पहले से मौजूद, `functionCall` और `functionResponse` के हिस्सों का इस्तेमाल करता है) |

## आगे क्या करना है

- Gemini API में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) के बारे में ज़्यादा जानें.
- काम करने वाले टूल के बारे में जानें:
  - [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)
  - [यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)
  - [फ़ाइल खोजें](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-29 (UTC) को अपडेट किया गया."],[],[]]
