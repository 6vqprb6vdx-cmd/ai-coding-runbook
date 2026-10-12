---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=hi
fetched_at: 2026-10-12T07:17:53.117954+00:00
title: "\u0915\u0902\u092a\u094d\u092f\u0942\u091f\u0930 \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# कंप्यूटर का इस्तेमाल

कंप्यूटर इस्तेमाल करने वाले टूल की मदद से, ब्राउज़र, मोबाइल, और डेस्कटॉप कंट्रोल एजेंट बनाए जा सकते हैं. ये एजेंट, टास्क के साथ इंटरैक्ट करते हैं और उन्हें ऑटोमेट करते हैं. स्क्रीनशॉट का इस्तेमाल करके, मॉडल कंप्यूटर स्क्रीन को "देख" सकता है. साथ ही, माउस क्लिक और कीबोर्ड इनपुट जैसी यूज़र इंटरफ़ेस (यूआई) से जुड़ी कार्रवाइयां करके "काम" कर सकता है. फ़ंक्शन कॉलिंग की तरह ही, आपको क्लाइंट-साइड एक्ज़ीक्यूशन एनवायरमेंट लागू करना होगा, ताकि कंप्यूटर के इस्तेमाल से जुड़ी कार्रवाइयां की जा सकें.

इस्तेमाल किए जा सकने वाले मॉडल की सूची देखने के लिए, [मॉडल के वर्शन](#model-versions) पर जाएं. Gemini 3.x मॉडल में कई बेहतर सुविधाएँ उपलब्ध हैं:

- **एक से ज़्यादा एनवायरमेंट के लिए सहायता:** [ब्राउज़र, मोबाइल, और डेस्कटॉप](#supported-environments) एनवायरमेंट के लिए एजेंट बनाएं.
- **आसानी से की जा सकने वाली कार्रवाइयां:** कार्रवाइयों में एक `intent` फ़ील्ड शामिल होता है. इसमें मॉडल के हर चरण के पीछे की वजह बताई जाती है.
- **कॉन्फ़िगर की जा सकने वाली सुरक्षा नीतियां:** पहले से मौजूद नीति की कैटगरी और ओवरराइड की मदद से, [सुरक्षा से जुड़ी सेटिंग](#safety-policies) को बेहतर बनाएं.
- **प्रॉम्प्ट इंजेक्शन का पता लगाने की सुविधा:** छिपे हुए नुकसान पहुंचाने वाले निर्देशों का पता लगाने के लिए, [स्क्रीनशॉट स्कैन करने की सुविधा](#prompt-injection) के लिए ऑप्ट-इन करें.

कंप्यूटर के इस्तेमाल की सुविधा की मदद से, ऐसे एजेंट बनाए जा सकते हैं जो:

- वेबसाइटों पर बार-बार डेटा डालने या फ़ॉर्म भरने की प्रोसेस को अपने-आप होने की सुविधा का इस्तेमाल करके आसान बनाएं.
- वेब ऐप्लिकेशन और उपयोगकर्ता फ़्लो की ऑटोमेटेड टेस्टिंग करना
- अलग-अलग वेबसाइटों पर रिसर्च करना. जैसे, खरीदारी करने से पहले ई-कॉमर्स साइटों से प्रॉडक्ट की जानकारी, कीमतें, और समीक्षाएं इकट्ठा करना

यहां क्लाइंट को शुरू करने और ब्राउज़र एनवायरमेंट के लिए `computer_use` टूल चालू करके, मॉडल को प्रॉम्प्ट भेजने का एक छोटा उदाहरण दिया गया है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Search for 'Gemini API' on Google.",
    tools=[{"type": "computer_use", "environment": "browser"}]
)

print(interaction)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.8-flash',
  input: "Search for 'Gemini API' on Google.",
  tools: [{ type: "computer_use", environment: "browser" }]
});

console.log(interaction);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Search for 'Gemini API' on Google."))
        .tools(
            Arrays.asList(
                ComputerUse.builder().environment(EnvironmentEnum.BROWSER).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction);
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Search for 'Gemini API' on Google."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumBrowser.ToPointer(),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction)
}
```

## कंप्यूटर के इस्तेमाल की सुविधा कैसे काम करती है

कंप्यूटर के इस्तेमाल वाले मॉडल के साथ एजेंट बनाने के लिए, आपको अपने ऐप्लिकेशन और एपीआई के बीच एक लूप सेट अप करना होगा. यहां बताया गया है कि हर चरण में आपका कोड क्या करेगा:

1. [**मॉडल को अनुरोध भेजना**](#send-request)
   - आपका ऐप्लिकेशन, एपीआई का एक अनुरोध भेजता है. इसमें कंप्यूटर के इस्तेमाल से जुड़ा टूल, आपकी कॉन्फ़िगरेशन सेटिंग (जैसे कि टारगेट एनवायरमेंट), उपयोगकर्ता का प्रॉम्प्ट, और मौजूदा स्क्रीन का स्क्रीनशॉट शामिल होता है.
2. [**मॉडल से जवाब पाना**](#model-response)
   - मॉडल, स्क्रीन और प्रॉम्प्ट का विश्लेषण करता है. इसके बाद, जवाब देता है. इस जवाब में, यूज़र इंटरफ़ेस (यूआई) से जुड़ी कार्रवाई (जैसे कि क्लिक करना, स्क्रोल करना या कीस्ट्रोक) को दिखाने वाला `function_call` शामिल होता है.
   - **Gemini 3.x मॉडल** के लिए, जवाब में `intent` भी शामिल होता है. इसमें यह बताया जाता है कि मॉडल ने वह कार्रवाई क्यों चुनी.
   - जवाब में, `safety_decision` भी शामिल हो सकता है. यह इंटरनल सुरक्षा सिस्टम से मिलता है. इसमें कार्रवाई को सामान्य/अनुमति दी गई, `require_confirmation` (उपयोगकर्ता की अनुमति ज़रूरी है) या ब्लॉक के तौर पर क्लासिफ़ाई किया जाता है.
3. [**मिली हुई कार्रवाई को पूरा करना**](#execute-actions)
   - अगर कार्रवाई की अनुमति है या उपयोगकर्ता इसकी पुष्टि करता है, तो आपका क्लाइंट-साइड कोड `function_call` को पार्स करता है. इसके बाद, सामान्य किए गए कोऑर्डिनेट को आपके व्यूपोर्ट से मैच करने के लिए स्केल करता है. इसके बाद, ऑटोमेशन टूल (जैसे, Playwright) का इस्तेमाल करके, आपके टारगेट एनवायरमेंट में कार्रवाई को पूरा करता है. अगर कार्रवाई ब्लॉक कर दी जाती है, तो आपके क्लाइंट को कार्रवाई रोकनी चाहिए या रुकावट को मैनेज करना चाहिए.
4. [**नए एनवायरमेंट की स्थिति कैप्चर करना**](#capture-state)
   - कार्रवाई पूरी होने के बाद, आपका ऐप्लिकेशन एक नया स्क्रीनशॉट कैप्चर करता है और उसे मॉडल को वापस भेजता है. ऐसा `function_result` में अगले चरण का अनुरोध करने के लिए किया जाता है.

इसके बाद, यह प्रोसेस दूसरे चरण से फिर शुरू होती है. इसमें मॉडल से लगातार अगली कार्रवाई करने के लिए कहा जाता है. यह तब तक जारी रहता है, जब तक टास्क पूरा नहीं हो जाता या उसे बंद नहीं कर दिया जाता.

![कंप्यूटर के इस्तेमाल की खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=hi)

## कंप्यूटर इस्तेमाल करने की सुविधा कैसे लागू करें

कंप्यूटर के इस्तेमाल से जुड़ी जानकारी देने वाले टूल का इस्तेमाल करने से पहले, आपको ये सेट अप करने होंगे:

- **सुरक्षित एक्ज़ीक्यूशन एनवायरमेंट:** अपने एजेंट को सैंडबॉक्स किए गए वीएम या कंटेनर में चलाएं, ताकि उसे अपने होस्ट सिस्टम से अलग किया जा सके और उसके संभावित असर को कम किया जा सके.
  [रेफ़रंस इंप्लीमेंटेशन](https://github.com/google/computer-use-preview/) में, इस्तेमाल के लिए तैयार Docker पर आधारित सैंडबॉक्स शामिल है. इसका इस्तेमाल शुरुआती तौर पर किया जा सकता है.
- **क्लाइंट-साइड ऐक्शन हैंडलर:** क्लाइंट-साइड लॉजिक लागू करें, ताकि कोऑर्डिनेट लागू किए जा सकें, टेक्स्ट टाइप किया जा सके, और स्क्रीनशॉट लिए जा सकें.

यहां दिए गए उदाहरणों में, वेब ब्राउज़र को एक्ज़ीक्यूशन एनवायरमेंट के तौर पर इस्तेमाल किया गया है. साथ ही, क्लाइंट-साइड हैंडलर के तौर पर [Playwright](https://playwright.dev/) का इस्तेमाल किया गया है.

### 0. Playwright को सेट अप करना

सबसे पहले, ज़रूरी पैकेज इंस्टॉल करें:

```
pip install google-genai playwright
playwright install chromium
```

इसके बाद, Playwright ब्राउज़र इंस्टेंस को शुरू करें, ताकि इसका इस्तेमाल किया जा सके:

```
from playwright.sync_api import sync_playwright

# 1. Configure screen dimensions for the target environment
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# 2. Start the Playwright browser
# In production, utilize a sandboxed environment.
playwright = sync_playwright().start()
# Set headless=False to see the actions performed on your screen
browser = playwright.chromium.launch(headless=False)

# 3. Create a context and page with the specified dimensions
context = browser.new_context(
    viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
)
page = context.new_page()

# 4. Navigate to an initial page to start the task
page.goto("https://www.google.com")

# The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
# will be used in the steps below.
```

### 1. मॉडल को अनुरोध भेजना

क्लाइंट लाइब्रेरी शुरू करें और कंप्यूटर के इस्तेमाल से जुड़े टूल को कॉन्फ़िगर करें. ध्यान दें कि अनुरोध करते समय, डिसप्ले साइज़ के बारे में बताना ज़रूरी नहीं है. मॉडल, स्क्रीन की ऊंचाई और चौड़ाई के हिसाब से पिक्सेल कोऑर्डिनेट का अनुमान लगाता है.

### Python

ब्राउज़र एनवायरमेंट को टारगेट करने वाले अनुरोध को कॉन्फ़िगर करने के लिए, `google-genai` Python SDK (वर्शन `2.7.0` या इसके बाद का वर्शन) का इस्तेमाल करें:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
        }
    ]
)

print(interaction)
```

### JavaScript

ब्राउज़र एनवायरमेंट को टारगेट करने वाले अनुरोध को कॉन्फ़िगर करने के लिए, `@google/genai` Node.js SDK का इस्तेमाल करें:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.8-flash',
  input: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
  tools: [
    {
      type: "computer_use",
      environment: "browser",
      enable_prompt_injection_detection: true
    }
  ]
});

console.log(interaction);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.BROWSER)
                    .enablePromptInjectionDetection(true)
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction);
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                    interactions.EnvironmentEnumBrowser.ToPointer(),
                    EnablePromptInjectionDetection: genai.Ptr(true),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction)
}
```

### REST

अनुरोध भेजने के लिए curl का इस्तेमाल करें:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com",
    "tools": [
      {
        "type": "computer_use",
        "environment": "browser",
        "enable_prompt_injection_detection": true
      }
    ]
  }'
```

### 2. मॉडल का जवाब पाना

मॉडल के जवाब में, कोऑर्डिनेट और कार्रवाई के बारे में बताने वाले तर्क के साथ फ़ंक्शन कॉल का सुझाव दिया गया है:

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
      "arguments": {
        "x": 450,
        "y": 120,
        "intent": "Click the search box to type the destination."
      }
    }
  ]
}
```

### 3. मिली हुई कार्रवाइयों को लागू करना

आपके ऐप्लिकेशन को जवाब के कोऑर्डिनेट पार्स करने होंगे. साथ ही, उन्हें सामान्य किए गए 1000x1000 कोऑर्डिनेट से स्केल करना होगा और कार्रवाई करनी होगी:

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname} (Intent: {args.get('intent', 'N/A')})")

        try:
            if fname == "open_app":
                pass # Handled / already open
            elif fname in ("click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname == "click":
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname == "type":
                actual_x = denormalize_x(args["x"], screen_width) if "x" in args else None
                actual_y = denormalize_y(args["y"], screen_height) if "y" in args else None
                text = args["text"]
                press_enter = args.get("press_enter", False)

                if actual_x is not None and actual_y is not None:
                    page.mouse.click(actual_x, actual_y)
                # Clear field first
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            elif fname == "navigate":
                page.goto(args["url"])
            elif fname == "go_back":
                page.go_back()
            elif fname == "go_forward":
                page.go_forward()
            elif fname == "wait":
                time.sleep(args.get("seconds", 1))
            else:
                print(f"Warning: Custom or unhandled function {fname}")

            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### JavaScript

```
function denormalizeX(x, screenWidth) {
    // Convert normalized x coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((x / 1000) * screenWidth);
}

function denormalizeY(y, screenHeight) {
    // Convert normalized y coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((y / 1000) * screenHeight);
}

async function executeFunctionCalls(interaction, page, screenWidth, screenHeight) {
    const results = [];
    const functionCalls = interaction.steps.filter(step => step.type === "function_call");

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.arguments;
        console.log(`  -> Executing: ${fname} (Intent: ${args.intent || 'N/A'})`);

        try {
            if (fname === "open_app") {
                // Handled / already open
            } else if (["click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click") {
                    await page.mouse.click(actualX, actualY);
                } else if (fname === "double_click") {
                    await page.mouse.dblclick(actualX, actualY);
                } else if (fname === "right_click") {
                    await page.mouse.click(actualX, actualY, { button: "right" });
                } else if (fname === "middle_click") {
                    await page.mouse.click(actualX, actualY, { button: "middle" });
                } else if (fname === "move") {
                    await page.mouse.move(actualX, actualY);
                }
            } else if (fname === "type") {
                const actualX = args.x !== undefined ? denormalizeX(args.x, screenWidth) : null;
                const actualY = args.y !== undefined ? denormalizeY(args.y, screenHeight) : null;
                const text = args.text;
                const pressEnter = args.press_enter || false;

                if (actualX !== null && actualY !== null) {
                    await page.mouse.click(actualX, actualY);
                }
                // Clear field first
                await page.keyboard.press("Meta+A");
                await page.keyboard.press("Backspace");
                await page.keyboard.type(text);
                if (pressEnter) {
                    await page.keyboard.press("Enter");
                }
            } else if (fname === "navigate") {
                await page.goto(args.url);
            } else if (fname === "go_back") {
                await page.goBack();
            } else if (fname === "go_forward") {
                await page.goForward();
            } else if (fname === "wait") {
                await new Promise(resolve => setTimeout(resolve, (args.seconds || 1) * 1000));
            } else {
                console.log(`Warning: Custom or unhandled function ${fname}`);
            }

            await page.waitForLoadState('load', { timeout: 5000 }).catch(() => {});
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (e) {
            console.log(`Error executing ${fname}: ${e}`);
            actionResult.error = e.message;
        }

        results.push([fname, functionCall.id, actionResult]);
    }

    return results;
}
```

### Java

```
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.Step;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class ActionExecutor {
  int denormalizeX(int x, int screenWidth) {
    return (int) (x / 1000.0 * screenWidth);
  }

  int denormalizeY(int y, int screenHeight) {
    return (int) (y / 1000.0 * screenHeight);
  }

  List<Map<String, Object>> executeFunctionCalls(
      Interaction interaction, int screenWidth, int screenHeight) {
    List<Map<String, Object>> results = new ArrayList<>();

    for (Step step : interaction.steps().orElse(Collections.emptyList())) {
      if (step instanceof FunctionCallStep) {
        FunctionCallStep functionCall = (FunctionCallStep) step;
        String fname = functionCall.name().orElse("");
        Map<String, Object> args = functionCall.arguments().orElse(Collections.emptyMap());
        Map<String, Object> actionResult = new HashMap<>();

        System.out.println(
            "  -> Executing: " + fname + " (Intent: " + args.getOrDefault("intent", "N/A") + ")");

        try {
          if (fname.equals("click")) {
            int actualX = denormalizeX(((Number) args.get("x")).intValue(), screenWidth);
            int actualY = denormalizeY(((Number) args.get("y")).intValue(), screenHeight);
            // Perform mouse click at (actualX, actualY) using your browser automation library
          } else if (fname.equals("type")) {
            String text = (String) args.get("text");
            // Type text into active element using your browser automation library
          } else if (fname.equals("navigate")) {
            String url = (String) args.get("url");
            // Navigate browser to url
          }
        } catch (Exception e) {
          actionResult.put("error", e.getMessage());
        }

        Map<String, Object> entry = new HashMap<>();
        entry.put("name", fname);
        entry.put("callId", functionCall.id().orElse(""));
        entry.put("result", actionResult);
        results.add(entry);
      }
    }
    return results;
  }
}
```

### ऐप पर जाएं

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func denormalizeX(x, screenWidth int) int {
    return int(float64(x) / 1000.0 * float64(screenWidth))
}

func denormalizeY(y, screenHeight int) int {
    return int(float64(y) / 1000.0 * float64(screenHeight))
}

func executeFunctionCalls(interaction *interactions.Interaction, screenWidth, screenHeight int) []map[string]any {
    var results []map[string]any

    for _, step := range interaction.Steps {
        if functionCall := step.FunctionCallStep; functionCall != nil {
            fname := functionCall.Name
            args := functionCall.Arguments
            actionResult := map[string]any{}

            intent := args["intent"]
            if intent == nil {
                intent = "N/A"
            }
            fmt.Printf("  -> Executing: %s (Intent: %v)\n", fname, intent)

            switch fname {
            case "click":
                xVal, _ := args["x"].(float64)
                yVal, _ := args["y"].(float64)
                actualX := denormalizeX(int(xVal), screenWidth)
                actualY := denormalizeY(int(yVal), screenHeight)
                _ = actualX
                _ = actualY
                // Perform mouse click at (actualX, actualY) using your browser automation library
            case "type":
                text, _ := args["text"].(string)
                _ = text
                // Type text into active element using your browser automation library
            case "navigate":
                url, _ := args["url"].(string)
                _ = url
                // Navigate browser to url
            }

            results = append(results, map[string]any{
                "name":   fname,
                "callId": functionCall.ID,
                "result": actionResult,
            })
        }
    }
    return results
}

func main() {
    // Example helper usage with an Interaction response
}
```

### 4. नए एनवायरमेंट की स्थिति कैप्चर करना

कार्रवाइयां पूरी करने के बाद, फ़ंक्शन के नतीजे को मॉडल को वापस भेजें, ताकि वह इस जानकारी का इस्तेमाल करके अगली कार्रवाई जनरेट कर सके. अगर एक साथ कई कार्रवाइयां (पैरलल कॉल) की गई हैं, तो आपको उपयोगकर्ता के अगले टर्न में हर कार्रवाई के लिए `function_result` भेजना होगा.

### Python

```
import json
import base64

def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

### JavaScript

```
async function getFunctionResponses(page, results) {
    const screenshotBuffer = await page.screenshot({ type: 'png' });
    const screenshotBase64 = screenshotBuffer.toString('base64');
    const currentUrl = page.url();
    const functionResponses = [];

    for (const [name, callId, result] of results) {
        functionResponses.push({
            type: "function_result",
            name: name,
            call_id: callId,
            result: [
                {
                    type: "text",
                    text: JSON.stringify({ url: currentUrl, ...result })
                },
                {
                    type: "image",
                    data: screenshotBase64,
                    mime_type: "image/png"
                }
            ]
        });
    }
    return functionResponses;
}
```

### Java

```
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;
import java.util.Map;

class StateCapturer {
  List<Step> getFunctionResponses(
      byte[] screenshotBytes, String currentUrl, List<Map<String, Object>> results) {
    List<Step> functionResponses = new ArrayList<>();
    String base64Screenshot = Base64.getEncoder().encodeToString(screenshotBytes);

    for (Map<String, Object> entry : results) {
      String name = (String) entry.get("name");
      String callId = (String) entry.get("callId");
      String jsonResult = String.format("{\"url\": \"%s\"}", currentUrl);

      FunctionResultStep responseStep =
          FunctionResultStep.builder()
              .name(name)
              .callId(callId)
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(
                          TextContent.builder().text(jsonResult).build(),
                          ImageContent.builder()
                              .data(base64Screenshot)
                              .mimeType(ImageContentMimeType.IMAGE_PNG)
                              .build())))
              .build();
      functionResponses.add(responseStep);
    }
    return functionResponses;
  }
}
```

### ऐप पर जाएं

```
package main

import (
    "encoding/base64"
    "fmt"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func getFunctionResponses(screenshotBytes []byte, currentURL string, results []map[string]any) []interactions.Step {
    var functionResponses []interactions.Step
    base64Screenshot := base64.StdEncoding.EncodeToString(screenshotBytes)

    for _, entry := range results {
        name, _ := entry["name"].(string)
        callID, _ := entry["callId"].(string)
        jsonResult := fmt.Sprintf(`{"url": "%s"}`, currentURL)

        responseStep := interactions.NewStep(interactions.FunctionResultStep{
            Name:   genai.Ptr(name),
            CallID: callID,
            Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                interactions.NewFunctionResultSubcontent(interactions.TextContent{
                    Text: jsonResult,
                }),
                interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Screenshot),
                    MimeType: interactions.ImageContentMimeType("image/png").ToPointer(),
                }),
            }),
        })
        functionResponses = append(functionResponses, responseStep)
    }
    return functionResponses
}

func main() {
    // Example helper usage to build FunctionResultStep responses
}
```

यह तय करने के बाद कि एनवायरमेंट की स्थिति को कैसे कैप्चर और फ़ॉर्मैट करना है, इन सभी चरणों को लगातार चलने वाले एक्ज़ीक्यूशन लूप में शामिल किया जा सकता है.

## एजेंट लूप बनाना

कई चरणों वाले इंटरैक्शन की सुविधा चालू करने के लिए, [कंप्यूटर के इस्तेमाल को लागू करने का तरीका](#implement-computer-use) सेक्शन में दिए गए चार चरणों को एक लूप में जोड़ें.
टास्क पूरा होने तक, यह लूप कार्रवाई का अनुरोध करता रहता है और मॉडल को नतीजे वापस भेजता रहता है.

बातचीत के इतिहास को सही तरीके से मैनेज करना न भूलें. इसके लिए, हर चरण में मॉडल के जवाब और फ़ंक्शन के जवाब, दोनों को इतिहास में जोड़ें.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-3.8-flash',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-3.8-flash',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser",
                "enable_prompt_injection_detection": True
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

### JavaScript

```
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Constants for screen dimensions
const SCREEN_WIDTH = 1440;
const SCREEN_HEIGHT = 900;

console.log("Initializing browser...");
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
    viewport: { width: SCREEN_WIDTH, height: SCREEN_HEIGHT }
});
const page = await context.newPage();

// Define helper functions. Copy/paste from steps 3 and 4:
// function denormalizeX(...)
// function denormalizeY(...)
// async function executeFunctionCalls(...)
// async function getFunctionResponses(...)

try {
    // Go to initial page
    await page.goto("https://ai.google.dev/gemini-api/docs");

    // Take initial screenshot
    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    // First interaction
    let interaction = await ai.interactions.create({
        model: 'gemini-3.8-flash',
        input: [
            { type: 'text', text: USER_PROMPT },
            { type: 'image', data: initialScreenshotBase64, mime_type: 'image/png' }
        ],
        tools: [{
            type: 'computer_use',
            environment: 'browser',
            enable_prompt_injection_detection: true
        }]
    });

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);

        const hasFunctionCalls = interaction.steps.some(step => step.type === "function_call");
        if (!hasFunctionCalls) {
            const textResponses = [];
            for (const step of interaction.steps) {
                if (step.type === "model_output") {
                    for (const contentBlock of step.content || []) {
                        if (contentBlock.type === "text") {
                            textResponses.push(contentBlock.text);
                        }
                    }
                }
            }
            console.log("Agent finished:", textResponses.join(" "));
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        // Continue conversation with function responses
        interaction = await ai.interactions.create({
            model: 'gemini-3.8-flash',
            previous_interaction_id: interaction.id,
            input: functionResponses,
            tools: [{
                type: 'computer_use',
                environment: 'browser',
                enable_prompt_injection_detection: true
            }]
        });
    }
} finally {
    // Cleanup
    console.log("\nClosing browser...");
    await browser.close();
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.List;

Client client = new Client();

// Constants for screen dimensions
int screenWidth = 1440;
int screenHeight = 900;

// Capture initial screenshot from browser driver (e.g. Playwright)
byte[] initialScreenshot = new byte[0];
String base64Screenshot = Base64.getEncoder().encodeToString(initialScreenshot);
String userPrompt = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
System.out.println("Goal: " + userPrompt);

ComputerUse computerUseTool =
    ComputerUse.builder()
        .environment(EnvironmentEnum.BROWSER)
        .enablePromptInjectionDetection(true)
        .build();

CreateModelInteraction initialParams =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text(userPrompt).build(),
                    ImageContent.builder()
                        .data(base64Screenshot)
                        .mimeType(ImageContentMimeType.IMAGE_PNG)
                        .build())))
        .tools(Arrays.asList(computerUseTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(initialParams)).interaction().get();

int turnLimit = 5;
for (int i = 0; i < turnLimit; i++) {
  System.out.println("\n--- Turn " + (i + 1) + " ---");

  boolean hasFunctionCalls =
      interaction.steps().orElse(Collections.emptyList()).stream()
          .anyMatch(step -> step instanceof FunctionCallStep);

  if (!hasFunctionCalls) {
    StringBuilder textResponse = new StringBuilder();
    for (Step step : interaction.steps().orElse(Collections.emptyList())) {
      if (step instanceof ModelOutputStep) {
        for (Content contentBlock :
            ((ModelOutputStep) step).content().orElse(Collections.emptyList())) {
          if (contentBlock instanceof TextContent) {
            textResponse.append(((TextContent) contentBlock).text().orElse("")).append(" ");
          }
        }
      }
    }
    System.out.println("Agent finished: " + textResponse.toString().trim());
    break;
  }

  System.out.println("Executing actions and capturing state...");
  // Execute function calls against browser driver and capture List<Step> functionResponses
  List<Step> functionResponses = new ArrayList<>();

  CreateModelInteraction nextParams =
      CreateModelInteraction.builder()
          .model("gemini-3.8-flash")
          .previousInteractionId(interaction.id().get())
          .input(InteractionsInput.ofStep(functionResponses))
          .tools(Arrays.asList(computerUseTool))
          .build();

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(nextParams)).interaction().get();
}
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Constants for screen dimensions
    screenWidth := 1440
    screenHeight := 900
    _ = screenWidth
    _ = screenHeight

    // Capture initial screenshot from browser driver (e.g. Playwright)
    initialScreenshot := []byte{}
    base64Screenshot := base64.StdEncoding.EncodeToString(initialScreenshot)
    userPrompt := "Go to ai.google.dev/gemini-api/docs and search for pricing."
    fmt.Println("Goal:", userPrompt)

    computerUseTool := interactions.NewTool(interactions.ComputerUse{
        Environment:                    interactions.EnvironmentEnumBrowser.ToPointer(),
        EnablePromptInjectionDetection: genai.Ptr(true),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: userPrompt}),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Screenshot),
                    MimeType: interactions.ImageContentMimeType("image/png").ToPointer(),
                }),
            }),
            Tools: []interactions.Tool{computerUseTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction

    turnLimit := 5
    for i := 0; i < turnLimit; i++ {
        fmt.Printf("\n--- Turn %d ---\n", i+1)

        hasFunctionCalls := false
        for _, step := range interaction.Steps {
            if step.FunctionCallStep != nil {
                hasFunctionCalls = true
                break
            }
        }

        if !hasFunctionCalls {
            var parts []string
            for _, step := range interaction.Steps {
                if outStep := step.ModelOutputStep; outStep != nil {
                    for _, contentBlock := range outStep.Content {
                        if textContent := contentBlock.TextContent; textContent != nil {
                            parts = append(parts, textContent.GetText())
                        }
                    }
                }
            }
            fmt.Println("Agent finished:", strings.TrimSpace(strings.Join(parts, " ")))
            break
        }

        fmt.Println("Executing actions and capturing state...")
        // Execute function calls against browser driver and capture []interactions.Step functionResponses
        var functionResponses []interactions.Step

        nextRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:                 interactions.Model("gemini-3.8-flash"),
                PreviousInteractionID: interaction.ID,
                Input:                 interactions.NewInteractionsInput(functionResponses),
                Tools:                 []interactions.Tool{computerUseTool},
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = nextRes.Interaction
    }
}
```

## इन प्लैटफ़ॉर्म पर काम करता है

Gemini 3.x मॉडल, `computer_use`कॉन्फ़िगरेशन में बताए गए तीन एनवायरमेंट के साथ काम करते हैं:

### ब्राउज़र एनवायरमेंट (`ENVIRONMENT_BROWSER`)

ब्राउज़र टूल में ये कार्रवाइयां उपलब्ध हैं:

| कमांड का नाम | ब्यौरा | आर्ग्युमेंट (फ़ंक्शन कॉल में) |
| --- | --- | --- |
| **click** | इस विकल्प का इस्तेमाल करने पर, चुने गए निर्देशांक पर बाईं ओर क्लिक किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | निर्देशांक पर दो बार क्लिक करता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | निर्देशांक पर तीन बार क्लिक करें. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | मिडिल क्लिक, निर्देशांक पर होता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | इस कमांड से, दिए गए कोऑर्डिनेट पर राइट क्लिक किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | इस कुकी का इस्तेमाल, दिए गए कोऑर्डिनेट पर माउस बटन को दबाकर रखने के लिए किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | इस तरीके का इस्तेमाल, दिए गए निर्देशांक पर माउस बटन को छोड़ने के लिए किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | इस निर्देश से कर्सर को बताई गई जगह पर ले जाया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | टेक्स्ट टाइप करता है. | `text`: str `press_enter`: bool (ज़रूरी नहीं, डिफ़ॉल्ट `false`) `intent`: str |
| **drag\_and\_drop** | यह कमांड, किसी आइटम को शुरुआती निर्देशांक से आखिरी निर्देशांक तक खींचकर ले जाती है. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | यह फ़ंक्शन, तय की गई संख्या के हिसाब से कुछ सेकंड के लिए एक्ज़ीक्यूशन को रोकता है. | `seconds`: int (ज़रूरी नहीं, डिफ़ॉल्ट `1`) `intent`: str |
| **press\_key** | यह कमांड, बताई गई कुंजी को दबाती है और छोड़ती है. | `key`: str `intent`: str |
| **key\_down** | यह कमांड, तय की गई कुंजी को दबाकर रखती है. | `key`: str `intent`: str |
| **key\_up** | यह फ़ंक्शन, बताई गई कुंजी को छोड़ता है. | `key`: str `intent`: str |
| **हॉटकी** | यह कमांड, तय किए गए बटन के कॉम्बिनेशन को दबाती है. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | यह मौजूदा स्क्रीन का स्क्रीनशॉट दिखाता है. | `intent`: str |
| **scroll** | यह किसी पिक्सल की दूरी पर मौजूद कोऑर्डिनेट पर, ऊपर, नीचे, बाएं या दाएं स्क्रोल करता है. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Optional, default `300`) `intent`: str |
| **go\_back** | यह कुकी, ब्राउज़र के इतिहास में पिछले वेबपेज पर वापस ले जाती है. | `intent`: str |
| **navigate** | यह सीधे तौर पर किसी यूआरएल पर ले जाता है. | `url`: str `intent`: str |
| **go\_forward** | यह कुकी, ब्राउज़र के इतिहास में अगले वेबपेज पर ले जाती है. | `intent`: str |

### मोबाइल एनवायरमेंट (`ENVIRONMENT_MOBILE`)

Android के लिए ऑप्टिमाइज़ की गई एनवायरमेंट ऐक्शन:

| कमांड का नाम | ब्यौरा | आर्ग्युमेंट (फ़ंक्शन कॉल में) |
| --- | --- | --- |
| **open\_app** | इस कमांड से, ऐप्लिकेशन को उसके नाम से खोला जाता है. | `app_name`: str `intent`: str |
| **click** | इस विकल्प का इस्तेमाल करने पर, चुने गए निर्देशांक पर बाईं ओर क्लिक किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | यह डिवाइस पर उपलब्ध ऐप्लिकेशन की सूची दिखाता है. साथ ही, उनके नाम और पैकेज के नाम दिखाता है. | `intent`: str |
| **wait** | यह फ़ंक्शन, तय की गई संख्या के हिसाब से कुछ सेकंड के लिए एक्ज़ीक्यूशन को रोकता है. | `seconds`: int (ज़रूरी नहीं, डिफ़ॉल्ट `1`) `intent`: str |
| **go\_back** | यह बटन, पिछली स्क्रीन या वेबपेज पर वापस ले जाता है. | `intent`: str |
| **type** | टेक्स्ट टाइप करता है. | `text`: str `press_enter`: bool (ज़रूरी नहीं, डिफ़ॉल्ट `false`) `intent`: str |
| **drag\_and\_drop** | यह कमांड, किसी आइटम को शुरुआती निर्देशांक से आखिरी निर्देशांक तक खींचकर ले जाती है. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | स्क्रीन पर किसी जगह को दबाकर रखता है. | `y`: int (0-999) `x`: int (0-999) `seconds`: int (वैकल्पिक, डिफ़ॉल्ट `2`) `intent`: str |
| **press\_key** | यह कमांड, बताई गई कुंजी को दबाती है और छोड़ती है. | `key`: str `intent`: str |
| **take\_screenshot** | यह मौजूदा स्क्रीन का स्क्रीनशॉट दिखाता है. | `intent`: str |

### डेस्कटॉप एनवायरमेंट (`ENVIRONMENT_DESKTOP`)

डेस्कटॉप एनवायरमेंट के लिए, ओएस-लेवल पर कर्सर को कंट्रोल करने के निर्देश:

| कमांड का नाम | ब्यौरा | आर्ग्युमेंट (फ़ंक्शन कॉल में) |
| --- | --- | --- |
| **click** | इस विकल्प का इस्तेमाल करने पर, चुने गए निर्देशांक पर बाईं ओर क्लिक किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | निर्देशांक पर दो बार क्लिक करता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | निर्देशांक पर तीन बार क्लिक करें. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | मिडिल क्लिक, निर्देशांक पर होता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | इस कमांड से, दिए गए कोऑर्डिनेट पर राइट क्लिक किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | इस कुकी का इस्तेमाल, दिए गए कोऑर्डिनेट पर माउस बटन को दबाकर रखने के लिए किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | इस तरीके का इस्तेमाल, दिए गए निर्देशांक पर माउस बटन को छोड़ने के लिए किया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | इस निर्देश से कर्सर को बताई गई जगह पर ले जाया जाता है. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | टेक्स्ट टाइप करता है. | `text`: str `press_enter`: bool (ज़रूरी नहीं, डिफ़ॉल्ट `false`) `intent`: str |
| **drag\_and\_drop** | यह कमांड, किसी आइटम को शुरुआती निर्देशांक से आखिरी निर्देशांक तक खींचकर ले जाती है. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | यह फ़ंक्शन, तय की गई संख्या के हिसाब से कुछ सेकंड के लिए एक्ज़ीक्यूशन को रोकता है. | `seconds`: int (ज़रूरी नहीं, डिफ़ॉल्ट `1`) `intent`: str |
| **press\_key** | यह कमांड, बताई गई कुंजी को दबाती है और छोड़ती है. | `key`: str `intent`: str |
| **key\_down** | यह कमांड, तय की गई कुंजी को दबाकर रखती है. | `key`: str `intent`: str |
| **key\_up** | यह फ़ंक्शन, बताई गई कुंजी को छोड़ता है. | `key`: str `intent`: str |
| **हॉटकी** | यह कमांड, तय किए गए बटन के कॉम्बिनेशन को दबाती है. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | यह मौजूदा स्क्रीन का स्क्रीनशॉट दिखाता है. | `intent`: str |
| **scroll** | यह किसी पिक्सल की दूरी पर मौजूद कोऑर्डिनेट पर, ऊपर, नीचे, बाएं या दाएं स्क्रोल करता है. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Optional, default `300`) `intent`: str |

## उपयोगकर्ता के तय किए गए कस्टम फ़ंक्शन

उपयोगकर्ता के तय किए गए कस्टम फ़ंक्शन शामिल करके, मॉडल की सुविधाओं को बढ़ाया जा सकता है. उदाहरण के लिए, ह्यूमन-इन-द-लूप (एचआईटीएल) के मामलों में, पहले से तय की गई डिफ़ॉल्ट कार्रवाइयों को बाहर रखा जा सकता है और कस्टम कार्रवाइयों को रजिस्टर किया जा सकता है.

### Python

पहले से तय की गई स्टैंडर्ड ब्राउज़र कार्रवाइयों (जैसे कि `click`) को बाहर रखें और कस्टम `yield_to_user` टूल रजिस्टर करें:

```
from google import genai

client = genai.Client()

yield_to_user_tool = {
    "type": "function",
    "name": "yield_to_user",
    "description": "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    "parameters": {
        "type": "object",
        "properties": {
            "reason": {
                "type": "string",
                "description": "The reason why the agent is yielding control to the human."
            }
        },
        "required": ["reason"]
    }
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Click the submit button. If you need a second factor authentication code, ask me.",
    tools=[
        {
            "type": "computer_use",
            "environment": "mobile",
            "excluded_predefined_functions": ["click"]
        },
        yield_to_user_tool
    ]
)
```

### JavaScript

पहले से तय की गई स्टैंडर्ड ब्राउज़र कार्रवाइयों (जैसे कि `click`) को बाहर रखें और कस्टम `yield_to_user` टूल रजिस्टर करें:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const yieldToUserTool = {
    type: "function",
    name: "yield_to_user",
    description: "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters: {
        type: "object",
        properties: {
            reason: {
                type: "string",
                description: "The reason why the agent is yielding control to the human."
            }
        },
        required: ["reason"]
    }
};

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Click the submit button. If you need a second factor authentication code, ask me.",
    tools: [
        {
            type: "computer_use",
            environment: "mobile",
            excluded_predefined_functions: ["click"]
        },
        yieldToUserTool
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> reasonProp = new HashMap<>();
reasonProp.put("type", "string");
reasonProp.put("description", "The reason why the agent is yielding control to the human.");

Map<String, Object> properties = new HashMap<>();
properties.put("reason", reasonProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Collections.singletonList("reason"));

Function yieldToUserTool =
    Function.builder()
        .name("yield_to_user")
        .description(
            "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "Click the submit button. If you need a second factor authentication code, ask me."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.MOBILE)
                    .excludedPredefinedFunctions(Arrays.asList("click"))
                    .build(),
                yieldToUserTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    yieldToUserTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("yield_to_user"),
        Description: genai.Ptr("Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "reason": map[string]any{
                    "type":        "string",
                    "description": "The reason why the agent is yielding control to the human.",
                },
            },
            "required": []string{"reason"},
        },
    })

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Click the submit button. If you need a second factor authentication code, ask me."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                 interactions.EnvironmentEnumMobile.ToPointer(),
                    ExcludedPredefinedFunctions: []string{"click"},
                }),
                yieldToUserTool,
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

## सूझ-बूझ वाले मॉडल के लेवल मैनेज करना

कंप्यूटर का इस्तेमाल करने वाले एजेंट के लिए, सोचने के अलग-अलग लेवल कॉन्फ़िगर किए जा सकते हैं. इससे कार्रवाई की क्वालिटी और उसे पूरा करने की स्पीड के बीच सही तालमेल बना रहता है. आम तौर पर, स्टैंडर्ड ऑटोमेशन टास्क के लिए, थिंकिंग लेवल कम होने पर बेहतर बैलेंस मिलता है.

## सुरक्षा

### सुरक्षा नीतियां कॉन्फ़िगर करना

Gemini 3.x मॉडल में, सुरक्षा सेवा की कैटगरी पहले से मौजूद होती हैं. इनसे यह तय करने में मदद मिलती है कि उपयोगकर्ता की पुष्टि करना ज़रूरी है या नहीं.

| सुरक्षा से जुड़ी नीति की कैटगरी | ब्यौरा |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | यह कुकी, पेमेंट, खुदरा चेकआउट या बिक्री पर कानूनी नियंत्रण वाले सामान से जुड़ी कार्रवाइयों को ब्लॉक करती है या उनकी पुष्टि करती है. |
| `SENSITIVE_DATA_MODIFICATION` | यह स्वास्थ्य, वित्तीय या सरकारी रिकॉर्ड में बिना अनुमति के बदलाव किए जाने से बचाता है. |
| `COMMUNICATION_TOOL` | इस सेटिंग से, एजेंट को अपने-आप ईमेल, चैट मैसेज या ड्राफ़्ट भेजने से रोका जाता है. |
| `ACCOUNT_CREATION` | इस कुकी से, एजेंट को वेबसाइटों पर नए खाते अपने-आप रजिस्टर करने से रोका जाता है. |
| `DATA_MODIFICATION` | यह फ़ाइल सिस्टम में होने वाले सभी बदलावों, डेटा शेयर करने, और स्टोरेज मिटाने की प्रोसेस को कंट्रोल करता है. |
| `USER_CONSENT_MANAGEMENT` | इसके लिए, कुकी के लिए सहमति वाले बैनर और निजता से जुड़े प्रॉम्प्ट के लिए, उपयोगकर्ता के कंट्रोल की ज़रूरत होती है. |
| `LEGAL_TERMS_AND_AGREEMENTS` | यह मॉडल को, सेवा की शर्तों या कानूनी रूप से बाध्यकारी अनुबंधों को अपने-आप स्वीकार करने से रोकता है. |

#### सुरक्षा से जुड़ी सेटिंग को अनदेखा करना

नीचे दिए गए तरीके से, कुछ नीतियों को बदला जा सकता है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Clean up the local folder by archiving old logs.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "disabled_safety_policies": [
                "data_modification"
            ]
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Clean up the local folder by archiving old logs.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            disabled_safety_policies: [
                "data_modification"
            ]
        }
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DisabledSafetyPolicy;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Clean up the local folder by archiving old logs."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.DESKTOP)
                    .disabledSafetyPolicies(
                        Arrays.asList(DisabledSafetyPolicy.DATA_MODIFICATION))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Clean up the local folder by archiving old logs."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumDesktop.ToPointer(),
                    DisabledSafetyPolicies: []interactions.DisabledSafetyPolicy{
                        interactions.DisabledSafetyPolicyDataModification,
                    },
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### प्रॉम्प्ट इंजेक्शन का पता लगाने की सुविधा

Gemini 3.5 Flash-Lite या इसके बाद के वर्शन के लिए, कंप्यूटर के इस्तेमाल से प्रॉम्प्ट इंजेक्शन के हमलों का पता लगाने में मदद मिलती है. इस सुविधा के चालू होने पर, यह जांच की जाती है कि शामिल किए गए स्क्रीनशॉट में, नुकसान पहुंचाने वाले छिपे हुए निर्देश तो नहीं हैं. उदाहरण के लिए, "पिछली कमांड को अनदेखा करें". अगर ऐसे निर्देश मिलते हैं, तो उन्हें लागू होने से रोक दिया जाता है.

प्रॉम्प्ट इंजेक्शन का पता लगाने की सुविधा, एक ऐसी सुविधा है जिसके लिए ऑप्ट-इन किया जा सकता है. डिफ़ॉल्ट वैल्यू `false` है.

यहां दिए गए उदाहरणों में, कंप्यूटर के इस्तेमाल से जुड़े टूल के कॉन्फ़िगरेशन में, प्रॉम्प्ट इंजेक्शन का पता लगाने की सुविधा चालू करने का तरीका बताया गया है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Search for flight deals and summarize top results.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "enable_prompt_injection_detection": True,
        }
    ],
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Search for flight deals and summarize top results.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            enablePromptInjectionDetection: true,
        }
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Search for flight deals and summarize top results."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.DESKTOP)
                    .enablePromptInjectionDetection(true)
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Search for flight deals and summarize top results."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                    interactions.EnvironmentEnumDesktop.ToPointer(),
                    EnablePromptInjectionDetection: genai.Ptr(true),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### cURL

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions?key=${GEMINI_API_KEY}" \
-H 'Content-Type: application/json' \
-d '{
  "model": "gemini-3.8-flash",
  "input": "Search for flight deals and summarize top results.",
  "tools": [
    {
      "type": "computer_use",
      "environment": "desktop",
      "enable_prompt_injection_detection": true
    }
  ]
}'
```

### सुरक्षा से जुड़े फ़ैसले को स्वीकार करना

जवाब में, फ़ंक्शन कॉल के तर्कों में `safety_decision` पैरामीटर शामिल हो सकता है:

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "Must check check-box",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

अगर `safety_decision`, `require_confirmation` है, तो असली उपयोगकर्ता को प्रॉम्प्ट करें. अगर उपयोगकर्ता पुष्टि करता है, तो `function_result` में `safety_acknowledgement` को सेट करें.

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.arguments:
    decision = get_safety_confirmation(function_call.arguments['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### सुरक्षा के सबसे सही तरीके

कंप्यूटर का इस्तेमाल करने पर, सुरक्षा और ऑपरेशन से जुड़े जोखिम हो सकते हैं. ऐसा इसलिए, क्योंकि उपयोगकर्ता की ओर से कार्रवाई करने वाले मॉडल को स्क्रीन पर ऐसा कॉन्टेंट मिल सकता है जिस पर भरोसा नहीं किया जा सकता. इसके अलावा, कार्रवाई करते समय उससे गड़बड़ियां भी हो सकती हैं. लोगों के डेटा और सिस्टम को सुरक्षित रखने के लिए, यहां दिए गए सबसे सही तरीके अपनाएं:

1. **ह्यूमन-इन-द-लूप (एचआईटीएल):**
   - **उपयोगकर्ता से पुष्टि कराना:** अगर सुरक्षा से जुड़े जवाब में `require_confirmation` दिखता है, तो उपयोगकर्ता से मंज़ूरी लेने के लिए कहें.
   - **सुरक्षा से जुड़े कस्टम निर्देश दें:** सुरक्षा से जुड़ी अपनी सीमाएं तय करने और उन्हें लागू करने के लिए, सिस्टम के लिए कस्टम निर्देश लागू करें. उदाहरण के लिए:

     ### Python

     ```
     from google import genai

     client = genai.Client()

     system_instruction = """
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     """

     interaction = client.interactions.create(
         model="gemini-3.8-flash",
         system_instruction=system_instruction,
         input="Prepare a draft but do not send.",
         tools=[{
             "type": "computer_use",
             "environment": "browser"
         }]
     )
     ```

     ### JavaScript

     ```
     import { GoogleGenAI } from '@google/genai';

     const ai = new GoogleGenAI();

     const systemInstruction = `
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for \`USER_CONFIRMATION\`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     `;

     const interaction = await ai.interactions.create({
         model: "gemini-3.8-flash",
         system_instruction: systemInstruction,
         input: "Prepare a draft but do not send.",
         tools: [{
             type: "computer_use",
             environment: "browser"
         }]
     });
     ```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String systemInstruction =
    "## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**\n\n"
        + "This is your first and most important check. If the next required action falls "
        + "into any of the following categories, you MUST stop immediately, and seek the "
        + "user's explicit permission.\n\n"
        + "## **RULE 2: Default Behavior (ACTUATE)**\n\n"
        + "If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`, "
        + "your default behavior is to **Actuate**.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .systemInstruction(systemInstruction)
        .input(InteractionsInput.of("Prepare a draft but do not send."))
        .tools(
            Arrays.asList(
                ComputerUse.builder().environment(EnvironmentEnum.BROWSER).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    systemInstruction := "## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**\n\n" +
        "This is your first and most important check. If the next required action falls " +
        "into any of the following categories, you MUST stop immediately, and seek the " +
        "user's explicit permission.\n\n" +
        "## **RULE 2: Default Behavior (ACTUATE)**\n\n" +
        "If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`, " +
        "your default behavior is to **Actuate**."

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:             interactions.Model("gemini-3.8-flash"),
            SystemInstruction: genai.Ptr(systemInstruction),
            Input:             interactions.NewInteractionsInput("Prepare a draft but do not send."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumBrowser.ToPointer(),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

1. **सुरक्षित एक्ज़ीक्यूशन एनवायरमेंट:** अपने एजेंट को सुरक्षित और सैंडबॉक्स वाले एनवायरमेंट में चलाएं, ताकि उसके संभावित असर को सीमित किया जा सके. यह सैंडबॉक्स की गई वर्चुअल मशीन (वीएम), कंटेनर (जैसे, Docker) या सीमित अनुमतियों वाली ब्राउज़र प्रोफ़ाइल हो सकती है. Docker का इस्तेमाल करके सैंडबॉक्स सेट अप करने के बारे में दिशा-निर्देश पाने के लिए, [GitHub का रेफ़रंस इंप्लीमेंटेशन](https://github.com/google/computer-use-preview/) देखें.
2. **इनपुट सैनिटाइज़ेशन:** प्रॉम्प्ट में मौजूद, उपयोगकर्ता के जनरेट किए गए सभी टेक्स्ट को सैनिटाइज़ करें. इससे अनचाहे निर्देशों या प्रॉम्प्ट इंजेक्शन के जोखिम को कम किया जा सकता है. यह सुरक्षा की एक मददगार लेयर है. हालांकि, यह सुरक्षित एक्ज़ीक्यूशन एनवायरमेंट का विकल्प नहीं है.
3. **कॉन्टेंट से जुड़े दिशा-निर्देश:** दिशा-निर्देशों और Content Safety API का इस्तेमाल करके, यह पता लगाएं कि उपयोगकर्ता के इनपुट, टूल के इनपुट और आउटपुट, और एजेंट के जवाब सही हैं या नहीं. साथ ही, यह भी पता लगाएं कि प्रॉम्प्ट इंजेक्शन और जेलब्रेक का पता लगाया गया है या नहीं.
4. **अनुमति वाली और बिना अनुमति वाली सूचियां:** फ़िल्टर करने के तरीके लागू करें, ताकि यह कंट्रोल किया जा सके कि मॉडल किन वेबसाइटों पर जा सकता है और क्या-क्या कर सकता है. प्रतिबंधित वेबसाइटों की बिना अनुमति वाली सूची से शुरुआत करना एक अच्छा विकल्प है. हालांकि, अनुमति वाली सूची को ज़्यादा पाबंदियों के साथ लागू करना ज़्यादा सुरक्षित होता है.
5. **जांचने की क्षमता और लॉगिंग:** डीबग करने, ऑडिट करने, और समस्या हल करने के लिए, लॉग की पूरी जानकारी बनाए रखें. आपके क्लाइंट को प्रॉम्प्ट, स्क्रीनशॉट, मॉडल की सुझाई गई कार्रवाइयां (`function_call`), सुरक्षा से जुड़े जवाब, और क्लाइंट की ओर से की गई सभी कार्रवाइयों को लॉग करना चाहिए.
6. **एनवायरमेंट मैनेजमेंट:** पक्का करें कि जीयूआई एनवायरमेंट एक जैसा हो.
   अनचाहे पॉप-अप, सूचनाएं या लेआउट में बदलाव होने से, मॉडल को समझने में मुश्किल हो सकती है. अगर हो सके, तो हर नए टास्क के लिए, जानी-पहचानी और साफ़-सुथरी स्थिति से शुरुआत करें.

## मॉडल के वर्शन

कंप्यूटर के इस्तेमाल की सुविधा, इन मॉडल के साथ इस्तेमाल की जा सकती है:

- [**Gemini 3.8 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) (`gemini-3.8-flash`): कंप्यूटर पर इस्तेमाल करने के लिए सुझाया गया मॉडल. इसमें यूज़र इंटरफ़ेस (यूआई) के साथ ज़्यादा सटीक इंटरैक्शन और टूल को भरोसेमंद तरीके से कॉल करने की सुविधा मिलती है.
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) (`gemini-3.5-flash-lite`): यह कम समय में जवाब देने वाला और किफ़ायती मॉडल है. इसका इस्तेमाल कंप्यूटर पर किया जा सकता है.
- [**Gemini 3 Flash की झलक**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) (`gemini-3-flash-preview`): कंप्यूटर पर इस्तेमाल किए जा सकने वाले मॉडल की झलक.

## आगे क्या करना है

- [Browserbase के डेमो एनवायरमेंट](http://gemini.browserbase.com) में, कंप्यूटर के इस्तेमाल से जुड़े एक्सपेरिमेंट करें.
- उदाहरण के लिए, [रेफ़रंस के तौर पर लागू किया गया कोड](https://github.com/google/computer-use-preview) देखें.
- Gemini API के अन्य टूल के बारे में जानें:
  - [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)
  - [Google Search से सटीक जानकारी पाने की सुविधा](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-09 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-09 (UTC) को अपडेट किया गया."],[],[]]
