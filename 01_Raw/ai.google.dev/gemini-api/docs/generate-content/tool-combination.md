---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=hi
fetched_at: 2026-11-02T07:02:52.206530+00:00
title: "\u092a\u0939\u0932\u0947 \u0938\u0947 \u092e\u094c\u091c\u0942\u0926 \u091f\u0942\u0932 \u0914\u0930 \u092b\u093c\u0902\u0915\u094d\u0936\u0928 \u0915\u0949\u0932\u093f\u0902\u0917 \u0915\u094b \u090f\u0915 \u0938\u093e\u0925 \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# पहले से मौजूद टूल और फ़ंक्शन कॉलिंग को एक साथ इस्तेमाल करना

Gemini, एक ही जनरेशन में [बिल्ट-इन टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi), जैसे कि `google_search`, और [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) (इसे *कस्टम टूल* भी कहा जाता है) को एक साथ इस्तेमाल करने की सुविधा देता है. इसके लिए, यह टूल कॉल के कॉन्टेक्स्ट के इतिहास को सुरक्षित रखता है और उसे दिखाता है. पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन से, एजेंट के जटिल वर्कफ़्लो को मैनेज किया जा सकता है. उदाहरण के लिए, मॉडल आपके कारोबार के खास नियम को कॉल करने से पहले, रीयल-टाइम वेब डेटा में खुद को ग्राउंड कर सकता है.

यहां एक उदाहरण दिया गया है, जिसमें `google_search` और कस्टम फ़ंक्शन `getWeather` की मदद से, बिल्ट-इन और कस्टम टूल के कॉम्बिनेशन को चालू किया गया है:

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
    model="gemini-3.8-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather],  # Custom tool
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
    model="gemini-3.8-flash",
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
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const response1 = await client.models.generateContent({
        model: "gemini-3.8-flash",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

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

    const response2 = await client.models.generateContent({
        model: "gemini-3.8-flash",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response2.candidates[0].content.parts) {
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

    model := client.GenerativeModel("gemini-3.8-flash")
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

### आराम का समय

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

Gemini 3 मॉडल, *टूल के कॉन्टेक्स्ट को शेयर करने की सुविधा* का इस्तेमाल करते हैं. इससे, पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन को चालू किया जा सकता है. टूल कॉन्टेक्स्ट सर्कुलेशन की मदद से, पहले से मौजूद टूल के कॉन्टेक्स्ट को सुरक्षित रखा जा सकता है और उसे एक्सपोज़ किया जा सकता है. साथ ही, उसे एक ही कॉल में कस्टम टूल के साथ शेयर किया जा सकता है.

### टूल कॉम्बिनेशन की सुविधा चालू करना

- टूल के कॉन्टेक्स्ट को शेयर करने की सुविधा चालू करने के लिए, आपको `include_server_side_tool_invocations` फ़्लैग को `true` पर सेट करना होगा.
- कॉम्बिनेशन के व्यवहार को ट्रिगर करने के लिए, [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#function-declarations) के साथ-साथ उन बिल्ट-इन टूल को शामिल करें जिनका आपको इस्तेमाल करना है.
  - अगर आपने `function_declarations` को शामिल नहीं किया है, तो भी टूल के कॉन्टेक्स्ट का सर्कुलेशन, पहले से मौजूद टूल पर काम करेगा. ऐसा तब तक होगा, जब तक फ़्लैग सेट रहेगा.

### एपीआई से मिलने वाले पार्ट

एपीआई, पहले से मौजूद टूल कॉल के लिए, एक ही जवाब में `toolCall` और `toolResponse` हिस्से दिखाता है. फ़ंक्शन (कस्टम टूल) कॉल के लिए, एपीआई `functionCall` कॉल पार्ट दिखाता है. इसके बाद, उपयोगकर्ता अगली बारी में `functionResponse` पार्ट उपलब्ध कराता है.

- `toolCall` और `toolResponse`: एपीआई इन हिस्सों को इसलिए दिखाता है, ताकि यह पता चल सके कि सर्वर साइड पर कौनसे टूल इस्तेमाल किए गए हैं. साथ ही, अगले टर्न के लिए उनके नतीजे भी दिखाए जा सकें.
- `functionCall` और `functionResponse`: एपीआई, फ़ंक्शन कॉल को उपयोगकर्ता को भेजता है, ताकि वह इसे भर सके. इसके बाद, उपयोगकर्ता फ़ंक्शन के जवाब में नतीजे वापस भेजता है. ये हिस्से, Gemini API में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) के सभी स्टैंडर्ड फ़ंक्शन के लिए होते हैं. ये टूल कॉम्बिनेशन की सुविधा के लिए खास नहीं होते.
- (सिर्फ़ [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) टूल के लिए)
  `executableCode` और `codeExecutionResult`:
  कोड एक्ज़ीक्यूशन टूल का इस्तेमाल करने पर, एपीआई `functionCall` और `functionResponse` के बजाय, `executableCode` (मॉडल से जनरेट किया गया कोड, जिसे एक्ज़ीक्यूट किया जाना है) और `codeExecutionResult` (एक्ज़ीक्यूटेबल कोड का नतीजा) दिखाता है.

आपको हर बारी में, सभी हिस्सों को मॉडल में वापस भेजना होगा. इनमें वे सभी [फ़ील्ड](#critical-fields) भी शामिल हैं जिनमें वे मौजूद हैं. इससे कॉन्टेक्स्ट को बनाए रखने और टूल के कॉम्बिनेशन को चालू करने में मदद मिलती है.

### वापस किए गए पुर्ज़ों में मौजूद अहम फ़ील्ड

[एपीआई से मिले कुछ हिस्सों](#api-returns-parts) में `id`, `tool_type`, और `thought_signature` फ़ील्ड शामिल होंगे. इन फ़ील्ड से, टूल के कॉन्टेक्स्ट को बनाए रखने में मदद मिलती है. इसलिए, ये फ़ील्ड टूल के कॉम्बिनेशन के लिए भी ज़रूरी हैं. आपको अपने अगले अनुरोधों में, *जवाब में दिए गए* सभी हिस्सों को वापस भेजना होगा.

- `id`: एक यूनीक आइडेंटिफ़ायर, जो किसी कॉल को उसके जवाब से मैप करता है. `id` को **सभी फ़ंक्शन कॉल के जवाबों पर सेट किया जाता है**. इससे कोई फ़र्क़ नहीं पड़ता कि टूल के कॉन्टेक्स्ट को सर्कुलेट किया गया है या नहीं.
  आपको फ़ंक्शन के रिस्पॉन्स में वही `id` देना *होगा* जो एपीआई, फ़ंक्शन कॉल में देता है. पहले से मौजूद टूल, टूल कॉल और टूल रिस्पॉन्स के बीच `id` को अपने-आप शेयर करते हैं.
  - टूल से जुड़े सभी हिस्सों में मौजूद है: `toolCall`, `toolResponse`,
    `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: इससे इस्तेमाल किए जा रहे टूल की पहचान होती है. यह बिल्ट-इन टूल (जैसे, `URL_CONTEXT`) या फ़ंक्शन (जैसे, `getWeather`) का नाम होता है.
  - `toolCall` और `toolResponse` सेक्शन में मौजूद है.
- `thought_signature`: यह एन्क्रिप्ट (सुरक्षित) किया गया कॉन्टेक्स्ट है. इसे **एपीआई से मिले हर हिस्से** में एम्बेड किया जाता है. थॉट सिग्नेचर के बिना कॉन्टेक्स्ट को फिर से नहीं बनाया जा सकता. अगर हर टर्न में सभी हिस्सों के लिए थॉट सिग्नेचर नहीं दिए जाते हैं, तो मॉडल में गड़बड़ी होगी.
  - यह *सभी* हिस्सों में मौजूद है.

### टूल के हिसाब से डेटा

पहले से मौजूद कुछ टूल, उपयोगकर्ता को दिखने वाले डेटा आर्ग्युमेंट दिखाते हैं. ये आर्ग्युमेंट, टूल के टाइप के हिसाब से होते हैं.

| टूल | उपयोगकर्ता को दिखने वाले टूल कॉल आर्ग्युमेंट (अगर कोई है) | उपयोगकर्ता को दिखने वाला टूल का जवाब (अगर कोई है) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` ब्राउज़ किए जाने वाले यूआरएल | `url_metadata` `retrieved_url`: ब्राउज़ किए गए यूआरएल `url_retrieval_status`: ब्राउज़ करने की स्थिति |
| **FILE\_SEARCH** | कोई नहीं | कोई नहीं |

## टूल के कॉम्बिनेशन के अनुरोध के स्ट्रक्चर का उदाहरण

नीचे दिए गए अनुरोध के स्ट्रक्चर में, प्रॉम्प्ट के अनुरोध का स्ट्रक्चर दिखाया गया है: "अमेरिका का सबसे उत्तरी शहर कौनसा है? आज वहां मौसम कैसा है?". इसमें तीन टूल शामिल हैं: Gemini के बिल्ट-इन टूल `google_search`
और `code_execution`, और कस्टम फ़ंक्शन `get_weather`.

```
{
  "model": "models/gemini-3.8-flash",
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

ध्यान दें कि अनुरोधों में `toolCall` और `toolResponse` हिस्सों को `prompt_token_count` में गिना जाता है. टूल के इस्तेमाल से जुड़े ये इंटरमीडिएट चरण अब आपको दिखते हैं और आपको वापस भेजे जाते हैं. इसलिए, ये बातचीत के इतिहास का हिस्सा होते हैं. यह सिर्फ़ *अनुरोधों* के लिए है, *जवाबों* के लिए नहीं.

Google Search टूल पर यह नियम लागू नहीं होता. Google Search, क्वेरी के लेवल पर पहले से ही अपना प्राइसिंग मॉडल लागू करता है. इसलिए, टोकन के लिए दो बार शुल्क नहीं लिया जाता. [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज देखें.

ज़्यादा जानकारी के लिए, [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) पेज पढ़ें.

## सीमाएं

- `include_server_side_tool_invocations` फ़्लैग चालू होने पर, डिफ़ॉल्ट रूप से `VALIDATED` मोड चालू होता है. `AUTO` मोड मौजूद नहीं है
- `google_search` जैसे पहले से मौजूद टूल, जगह और मौजूदा समय की जानकारी पर निर्भर करते हैं. इसलिए, अगर आपके `system_instruction` या `function_declaration.description` में जगह और समय की जानकारी अलग-अलग है, तो टूल कॉम्बिनेशन की सुविधा ठीक से काम नहीं करेगी.

## इस्तेमाल किए जा सकने वाले टूल

सर्वर-साइड (पहले से मौजूद) टूल पर, टूल के कॉन्टेक्स्ट को सर्कुलेट करने की स्टैंडर्ड प्रोसेस लागू होती है.
कोड एक्ज़ीक्यूशन भी सर्वर-साइड टूल है. हालांकि, इसमें कॉन्टेक्स्ट सर्कुलेशन के लिए पहले से मौजूद समाधान होता है. कंप्यूटर का इस्तेमाल और फ़ंक्शन कॉलिंग, क्लाइंट-साइड टूल हैं. इनमें कॉन्टेक्स्ट को शेयर करने के लिए, पहले से मौजूद समाधान भी होते हैं.

| टूल | एक्ज़ीक्यूशन साइड | कॉन्टेक्स्ट सर्कुलेशन सपोर्ट |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) | सर्वर-साइड | समर्थित |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi) | सर्वर-साइड | समर्थित |
| [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) | सर्वर-साइड | समर्थित |
| [फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi) | सर्वर-साइड | समर्थित |
| [कोड चलाने की सुविधा](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) | सर्वर-साइड | समर्थित (पहले से मौजूद, `executableCode` और `codeExecutionResult` का इस्तेमाल करता है) |
| [कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) | क्लाइंट-साइड | समर्थित (पहले से मौजूद, `functionCall` और `functionResponse` का इस्तेमाल करता है) |
| [कस्टम फ़ंक्शन](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) | क्लाइंट-साइड | इस्तेमाल किया जा सकता है (पहले से मौजूद है, `functionCall` और `functionResponse` हिस्सों का इस्तेमाल करता है) |

## आगे क्या करना है

- Gemini API में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) के बारे में ज़्यादा जानें.
- इन टूल के साथ काम करने की सुविधा उपलब्ध है:
  - [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)
  - [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)
  - [फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
