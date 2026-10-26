---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=bn
fetched_at: 2026-10-26T05:51:00.972682+00:00
title: "\u0995\u09ae\u09cd\u09aa\u09bf\u0989\u099f\u09be\u09b0\u09c7\u09b0 \u09ac\u09cd\u09af\u09ac\u09b9\u09be\u09b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# কম্পিউটারের ব্যবহার

কম্পিউটার ব্যবহার টুল আপনাকে ব্রাউজার, মোবাইল এবং ডেস্কটপ কন্ট্রোল এজেন্ট তৈরি করতে দেয়
যা ইন্টার‍্যাক্ট করে এবং টাস্ক অটোমেট করে। স্ক্রিনশট ব্যবহার করে, মডেলটি একটি কম্পিউটার স্ক্রিন "দেখতে" পারে এবং মাউস ক্লিক এবং কীবোর্ড ইনপুটের মতো নির্দিষ্ট UI অ্যাকশন তৈরি করে "কাজ" করতে পারে। ফাংশন কলিংয়ের মতোই, কম্পিউটার ব্যবহার অ্যাকশন গ্রহণ ও কার্যকর করার জন্য আপনাকে ক্লায়েন্ট-সাইড এক্সিকিউশন এনভায়রনমেন্ট প্রয়োগ করতে হবে।

কোন কোন মডেলে এই সুবিধা কাজ করে তার তালিকা দেখতে, [মডেলের ভার্সন](#model-versions) দেখুন। Gemini
4 এবং Gemini 3.x মডেল বিভিন্ন উন্নত কার্যকারিতা সাপোর্ট করে:

- **মাল্টি-এনভায়রনমেন্ট সাপোর্ট:** [ব্রাউজার, মোবাইল ও ডেস্কটপ](#supported-environments) এনভায়রনমেন্টের জন্য এজেন্ট তৈরি করুন।
- **ইনটেন্ট সহ স্ট্রিমলাইন করা অ্যাকশন:** অ্যাকশনে একটি `intent` ফিল্ড অন্তর্ভুক্ত থাকে যা প্রতিটি ধাপের পিছনে মডেলের যুক্তি ব্যাখ্যা করে।
- **কনফিগার করা যায় এমন নিরাপত্তা নীতি:** বিল্ট-ইন নীতি বিভাগ ও ওভাররাইডের মাধ্যমে [নিরাপত্তা সংক্রান্ত আচরণ](#safety-policies) ফাইন-টিউন করুন।
- **প্রম্পট ইঞ্জেকশন ডিটেকশন:** লুকানো অ্যাডভারসেরিয়াল নির্দেশাবলী শনাক্ত করতে [স্ক্রিনশট স্ক্যানিং](#prompt-injection) অপ্ট-ইন করুন।

Computer Use-এর মাধ্যমে, আপনি এমন এজেন্ট তৈরি করতে পারবেন যা:

- ওয়েবসাইটে বারবার করতে হয় এমন ডেটা এন্ট্রি বা ফর্ম পূরণ করার কাজ অটোমেট করুন।
- ওয়েব অ্যাপ্লিকেশন ও ইউজার ফ্লোয়ের অটোমেটেড টেস্টিং পারফর্ম করুন
- বিভিন্ন ওয়েবসাইট জুড়ে রিসার্চ করা (যেমন, কেনাকাটার ব্যাপারে সিদ্ধান্ত নিতে ই-কমার্স সাইট থেকে প্রোডাক্টের
  তথ্য, দাম ও রিভিউ সংগ্রহ করা)

ব্রাউজার এনভায়রনমেন্টের জন্য `computer_use` টুল চালু করে ক্লায়েন্ট শুরু করা এবং মডেলে প্রম্পট পাঠানোর একটি সংক্ষিপ্ত উদাহরণ এখানে দেওয়া হল:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

## কম্পিউটার ইউজ কীভাবে কাজ করে

কম্পিউটার ব্যবহার মডেলের সাহায্যে এজেন্ট তৈরি করতে, আপনার অ্যাপ্লিকেশন ও API-এর মধ্যে
একটি কন্টিনিউয়াস লুপ সেট-আপ করতে হবে। প্রতিটি ধাপে আপনার কোড
কী করবে তা এখানে দেওয়া হল:

1. [**মডেলকে অনুরোধ পাঠান**](#send-request)
   - আপনার অ্যাপ্লিকেশন, কম্পিউটার ব্যবহার টুল, আপনার কনফিগারেশন সেটিংস (যেমন টার্গেট এনভায়রনমেন্ট), ব্যবহারকারীর প্রম্পট এবং বর্তমান স্ক্রিনের স্ক্রিনশট সহ একটি API অনুরোধ পাঠায়।
2. [**মডেলের উত্তর পাওয়া**](#model-response)
   - মডেলটি স্ক্রিন ও প্রম্পট বিশ্লেষণ করে এবং একটি উত্তর প্রদান করে
     যার মধ্যে একটি সাজেস্ট করা `function_call` থাকে যা UI অ্যাকশন (যেমন
     ক্লিক, স্ক্রল বা কিস্ট্রোক) দেখায়।
   - **Gemini 4 এবং Gemini 3.x মডেলের** ক্ষেত্রে, উত্তরে একটি
     যুক্তি `intent` অন্তর্ভুক্ত থাকে যা ব্যাখ্যা করে যে মডেলটি কেন সেই অ্যাকশন বেছে নিয়েছে।
   - এছাড়াও, উত্তরে ইন্টার্নাল নিরাপত্তা সিস্টেম থেকে পাওয়া `safety_decision` অন্তর্ভুক্ত থাকতে পারে যা অ্যাকশনকে নিয়মিত/অনুমোদিত,
     `require_confirmation` (ব্যবহারকারীর অনুমোদন প্রয়োজন) বা ব্লক করা হিসেবে শ্রেণীবদ্ধ করে।
3. [**প্রাপ্ত অ্যাকশন এক্সিকিউট করুন**](#execute-actions)
   - অ্যাকশনটি করার অনুমতি থাকলে (অথবা ব্যবহারকারী কনফার্ম করলে), আপনার ক্লায়েন্ট-সাইড
     কোড `function_call` পার্স করে, আপনার ভিউপোর্টের সাথে ম্যাচ করার জন্য নরমালাইজ করা কোঅর্ডিনেট স্কেল করে
     এবং অটোমেশন টুল (যেমন Playwright) ব্যবহার করে আপনার টার্গেট এনভায়রনমেন্টে
     অ্যাকশনটি এক্সিকিউট করে। অ্যাকশন ব্লক করা হলে, আপনার
     ক্লায়েন্টকে এক্সিকিউশন বন্ধ করতে হবে অথবা বাধা সামলাতে হবে।
4. [**নতুন এনভায়রনমেন্ট স্টেট ক্যাপচার করুন**](#capture-state)
   - অ্যাকশনটি সম্পূর্ণ হওয়ার পরে, আপনার অ্যাপ্লিকেশন একটি নতুন স্ক্রিনশট ক্যাপচার করে এবং পরবর্তী ধাপের জন্য অনুরোধ করতে `function_result`-এ মডেলের কাছে ফেরত পাঠায়।

এই প্রসেসটি ধাপ ২ থেকে আবার শুরু হয় এবং টাস্ক সম্পূর্ণ বা বন্ধ না হওয়া পর্যন্ত মডেল থেকে পরবর্তী অ্যাকশন
চাইতে থাকে।

![কম্পিউটার ইউজ ওভারভিউ](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=bn)

## কীভাবে Computer Use প্রয়োগ করতে হয়

কম্পিউটার ব্যবহার টুল দিয়ে তৈরি করার আগে আপনাকে এগুলি সেট-আপ করতে হবে:

- **সুরক্ষিত এক্সিকিউশন এনভায়রনমেন্ট:** আপনার এজেন্টকে স্যান্ডবক্স করা VM বা
  কন্টেনারে চালান যাতে এটি আপনার হোস্ট সিস্টেম থেকে আলাদা থাকে এবং এর সম্ভাব্য প্রভাব সীমিত হয়।
  [রেফারেন্স ইমপ্লিমেন্টেশন](https://github.com/google/computer-use-preview/)
  -এ ব্যবহার করার জন্য প্রস্তুত Docker-ভিত্তিক স্যান্ডবক্স অন্তর্ভুক্ত থাকে যা আপনি শুরুর স্থান হিসেবে ব্যবহার করতে পারেন।
- **ক্লায়েন্ট-সাইড অ্যাকশন হ্যান্ডলার:** কোঅর্ডিনেট, টাইপ টেক্সট ও স্ক্রিনশট নেওয়ার জন্য ক্লায়েন্ট-সাইড লজিক প্রয়োগ করুন।

নিচের উদাহরণে এক্সিকিউশন এনভায়রনমেন্ট হিসেবে ওয়েব ব্রাউজার এবং ক্লায়েন্ট-সাইড হ্যান্ডলার হিসেবে
[Playwright](https://playwright.dev/) ব্যবহার করা হয়েছে।

### ০. Playwright সেট-আপ করা

প্রথমে, প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

```
pip install google-genai playwright
playwright install chromium
```

তারপর, এক্সিকিউশনের জন্য ব্যবহার করতে Playwright ব্রাউজার ইনস্ট্যান্স ইনিশিয়ালাইজ করুন:

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

### ১. মডেলকে অনুরোধ পাঠান

ক্লায়েন্ট লাইব্রেরি শুরু করুন এবং কম্পিউটার ব্যবহার টুল কনফিগার করুন। মনে রাখবেন, অনুরোধ করার সময় ডিসপ্লে সাইজ উল্লেখ করার প্রয়োজন নেই; মডেলটি স্ক্রিনের উচ্চতা ও প্রস্থ অনুযায়ী পিক্সেল কোঅর্ডিনেট অনুমান করে।

### Python

ব্রাউজার এনভায়রনমেন্টকে টার্গেট করে কোনও অনুরোধ কনফিগার করতে `google-genai` Python SDK (ভার্সন `2.7.0` বা তার পরবর্তী) ব্যবহার করুন:

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

### জাভাস্ক্রিপ্ট

ব্রাউজার এনভায়রনমেন্টকে টার্গেট করে অনুরোধ কনফিগার করতে `@google/genai` Node.js SDK ব্যবহার করুন:

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

### খুলুন

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

### বিশ্রাম

অনুরোধ পাঠাতে curl ব্যবহার করুন:

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

### ২. মডেলের উত্তর পান

মডেলের উত্তরে একটি ফাংশন কল সাজেস্ট করা হয়েছে যাতে কোঅর্ডিনেট এবং
অ্যাকশন ব্যাখ্যা করার জন্য একটি কাস্টমাইজ করা রিজনিং ইনটেন্ট রয়েছে:

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

### ৩. প্রাপ্ত অ্যাকশনগুলি কার্যকর করুন

আপনার অ্যাপ্লিকেশনকে অবশ্যই রেসপন্স কোঅর্ডিনেট পার্স করতে হবে, নরমালাইজ করা ১০০০x১০০০ কোঅর্ডিনেট থেকে সেগুলিকে স্কেল করতে হবে এবং অ্যাকশনটি কার্যকর করতে হবে:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### ৪. নতুন পরিবেশের অবস্থা ক্যাপচার করুন

অ্যাকশনগুলি কার্যকর করার পরে, ফাংশন কার্যকর করার ফলাফলটি মডেলে ফেরত পাঠান যাতে এটি পরবর্তী অ্যাকশন তৈরি করতে এই তথ্য ব্যবহার করতে পারে। একাধিক
অ্যাকশন (প্যারালাল কল) এক্সিকিউট করা হলে, ব্যবহারকারীর পরবর্তী টার্নে আপনাকে
প্রতিটির জন্য একটি করে `function_result` পাঠাতে হবে।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

এনভায়রনমেন্ট স্টেট কীভাবে ক্যাপচার ও ফর্ম্যাট করতে হবে তা নির্ধারণ করার পরে, আপনি
এইসব ধাপকে একটি একটানা এক্সিকিউশন লুপে একত্রিত করতে পারবেন।

## এজেন্ট লুপ তৈরি করুন

মাল্টি-স্টেপ ইন্টার‍্যাকশন চালু করতে, [কীভাবে
কম্পিউটার ব্যবহার ফিচার প্রয়োগ করবেন](#implement-computer-use) বিভাগ থেকে চারটি ধাপ একটি লুপে একত্রিত করুন।
টাস্ক সম্পূর্ণ না হওয়া পর্যন্ত এই লুপ অ্যাকশনের জন্য অনুরোধ করতে থাকে এবং ফলাফল মডেলকে
ফিডব্যাক হিসেবে পাঠায়।

প্রতিটি ধাপে মডেলের উত্তর এবং আপনার ফাংশনের উত্তর, দুটিই ইতিহাসে যোগ করে কথোপকথনের ইতিহাস সঠিকভাবে ম্যানেজ করতে ভুলবেন না।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

## কাজ করে এমন এনভায়রনমেন্ট

Gemini 4 এবং Gemini 3.x মডেলগুলি `computer_use` কনফিগারেশনে নির্দিষ্ট করা তিনটি এনভায়রনমেন্টে কাজ করে:

### ব্রাউজার এনভায়রনমেন্ট (`ENVIRONMENT_BROWSER`)

ব্রাউজার টুলের অধীনে উপলভ্য অ্যাকশন:

| কমান্ডের নাম | বিবরণ | আর্গুমেন্ট (ফাংশন কলে) |
| --- | --- | --- |
| **ক্লিক করুন** | স্থানাঙ্কে বাঁদিকের বোতামে ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | স্থানাঙ্কে ডবল ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | স্থানাঙ্কে ট্রিপল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | স্থানাঙ্কে মিডল ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | কোঅর্ডিনেটে ডানদিকের বোতামে ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | কোঅর্ডিনেটে মাউস বোতাম প্রেস করে ধরে রাখে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | স্থানাঙ্কে মাউসের বোতাম রিলিজ করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **সরান** | কার্সরকে নির্দিষ্ট পজিশনে নিয়ে যায়। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | টেক্সট টাইপ করে। | `text`: str `press_enter`: bool (ঐচ্ছিক, ডিফল্ট `false`) `intent`: str |
| **drag\_and\_drop** | শুরুর কোঅর্ডিনেট থেকে শেষের কোঅর্ডিনেট পর্যন্ত কোনও আইটেম টেনে নিয়ে যায়। | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **অপেক্ষা করুন** | নির্দিষ্ট সংখ্যক সেকেন্ডের জন্য এক্সিকিউশন পজ করে। | `seconds`: int (ঐচ্ছিক, ডিফল্ট `1`) `intent`: str |
| **press\_key** | নির্দিষ্ট কী প্রেস করে ছেড়ে দেয়। | `key`: str `intent`: str |
| **key\_down** | নির্দিষ্ট করা 'কী' প্রেস করে ধরে রাখে। | `key`: str `intent`: str |
| **key\_up** | নির্দিষ্ট কী রিলিজ করে। | `key`: str `intent`: str |
| **হটকী** | নির্দিষ্ট 'কী' কম্বিনেশন প্রেস করে। | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | বর্তমান স্ক্রিনের স্ক্রিনশট দেখায়। | `intent`: str |
| **স্ক্রল করা** | পিক্সেল দূরত্ব অনুযায়ী কোনও কোঅর্ডিনেটে উপরে, নিচে, বাঁদিকে বা ডানদিকে স্ক্রল করে। | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, ঐচ্ছিক, ডিফল্ট `300`) `intent`: str |
| **go\_back** | ব্রাউজার ইতিহাসে আগের ওয়েবপেজে নেভিগেট করে ফিরে যায়। | `intent`: str |
| **নেভিগেট করো** | নির্দিষ্ট URL-এ সরাসরি নেভিগেট করে। | `url`: str `intent`: str |
| **go\_forward** | ব্রাউজার ইতিহাসে পরবর্তী ওয়েবপেজে নেভিগেট করে। | `intent`: str |

### মোবাইল এনভায়রনমেন্ট (`ENVIRONMENT_MOBILE`)

Android-এর জন্য অপ্টিমাইজ করা এনভায়রনমেন্ট অ্যাকশন:

| কমান্ডের নাম | বিবরণ | আর্গুমেন্ট (ফাংশন কলে) |
| --- | --- | --- |
| **open\_app** | নাম অনুযায়ী কোনও অ্যাপ্লিকেশন খোলে। | `app_name`: str `intent`: str |
| **ক্লিক করুন** | স্থানাঙ্কে বাঁদিকের বোতামে ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | ডিভাইসে উপলভ্য অ্যাপ্লিকেশনের তালিকা দেখায়, তাদের নাম এবং প্যাকেজের নাম ফিরিয়ে দেয়। | `intent`: str |
| **অপেক্ষা করুন** | নির্দিষ্ট সংখ্যক সেকেন্ডের জন্য এক্সিকিউশন পজ করে। | `seconds`: int (ঐচ্ছিক, ডিফল্ট `1`) `intent`: str |
| **go\_back** | নেভিগেট করে আগের স্ক্রিন বা ওয়েবপেজে ফিরে যান। | `intent`: str |
| **type** | টেক্সট টাইপ করে। | `text`: str `press_enter`: bool (ঐচ্ছিক, ডিফল্ট `false`) `intent`: str |
| **drag\_and\_drop** | শুরুর কোঅর্ডিনেট থেকে শেষের কোঅর্ডিনেট পর্যন্ত কোনও আইটেম টেনে নিয়ে যায়। | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | স্ক্রিনের কোনও কোঅর্ডিনেটে বেশিক্ষণ প্রেস করে রাখে। | `y`: int (0-999) `x`: int (0-999) `seconds`: int (ঐচ্ছিক, ডিফল্ট `2`) `intent`: str |
| **press\_key** | নির্দিষ্ট কী প্রেস করে ছেড়ে দেয়। | `key`: str `intent`: str |
| **take\_screenshot** | বর্তমান স্ক্রিনের স্ক্রিনশট দেখায়। | `intent`: str |

### ডেস্কটপ এনভায়রনমেন্ট (`ENVIRONMENT_DESKTOP`)

ডেস্কটপ এনভায়রনমেন্ট OS-লেভেল কার্সর কমান্ড:

| কমান্ডের নাম | বিবরণ | আর্গুমেন্ট (ফাংশন কলে) |
| --- | --- | --- |
| **ক্লিক করুন** | স্থানাঙ্কে বাঁদিকের বোতামে ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | স্থানাঙ্কে ডবল ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | স্থানাঙ্কে ট্রিপল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | স্থানাঙ্কে মিডল ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | কোঅর্ডিনেটে ডানদিকের বোতামে ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | কোঅর্ডিনেটে মাউস বোতাম প্রেস করে ধরে রাখে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | স্থানাঙ্কে মাউসের বোতাম রিলিজ করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **সরান** | কার্সরকে নির্দিষ্ট পজিশনে নিয়ে যায়। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | টেক্সট টাইপ করে। | `text`: str `press_enter`: bool (ঐচ্ছিক, ডিফল্ট `false`) `intent`: str |
| **drag\_and\_drop** | শুরুর কোঅর্ডিনেট থেকে শেষের কোঅর্ডিনেট পর্যন্ত কোনও আইটেম টেনে নিয়ে যায়। | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **অপেক্ষা করুন** | নির্দিষ্ট সংখ্যক সেকেন্ডের জন্য এক্সিকিউশন পজ করে। | `seconds`: int (ঐচ্ছিক, ডিফল্ট `1`) `intent`: str |
| **press\_key** | নির্দিষ্ট কী প্রেস করে ছেড়ে দেয়। | `key`: str `intent`: str |
| **key\_down** | নির্দিষ্ট করা 'কী' প্রেস করে ধরে রাখে। | `key`: str `intent`: str |
| **key\_up** | নির্দিষ্ট কী রিলিজ করে। | `key`: str `intent`: str |
| **হটকী** | নির্দিষ্ট 'কী' কম্বিনেশন প্রেস করে। | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | বর্তমান স্ক্রিনের স্ক্রিনশট দেখায়। | `intent`: str |
| **স্ক্রল করা** | পিক্সেল দূরত্ব অনুযায়ী কোনও কোঅর্ডিনেটে উপরে, নিচে, বাঁদিকে বা ডানদিকে স্ক্রল করে। | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, ঐচ্ছিক, ডিফল্ট `300`) `intent`: str |

## ব্যবহারকারীর নির্ধারণ করা কাস্টম ফাংশন

আপনি কাস্টম ব্যবহারকারী-নির্ধারিত ফাংশন অন্তর্ভুক্ত করে মডেলের কার্যকারিতা বাড়াতে পারেন। যেমন, হিউম্যান-ইন-দ্য-লুপ (HITL) পরিস্থিতিতে আপনি ডিফল্ট পূর্বনির্ধারিত অ্যাকশন বাদ দিতে এবং কাস্টম অ্যাকশন রেজিস্টার করতে পারেন।

### Python

স্ট্যান্ডার্ড প্রিডিফাইন করা ব্রাউজার অ্যাকশন (যেমন `click`) বাদ দিন এবং কাস্টম `yield_to_user` টুল রেজিস্টার করুন:

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

### জাভাস্ক্রিপ্ট

স্ট্যান্ডার্ড প্রিডিফাইন করা ব্রাউজার অ্যাকশন (যেমন `click`) বাদ দিন এবং কাস্টম `yield_to_user` টুল রেজিস্টার করুন:

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

### খুলুন

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

## থিঙ্কিং লেভেল ম্যানেজ করা

কম্পিউটার ব্যবহারকারী এজেন্টের জন্য, আপনি অ্যাকশনের কোয়ালিটি এবং এক্সিকিউশনের স্পিডের মধ্যে ভারসাম্য বজায় রাখতে বিভিন্ন থিঙ্কিং লেভেল কনফিগার করতে পারেন। স্ট্যান্ডার্ড অটোমেশন টাস্কের ক্ষেত্রে, থিঙ্কিং লেভেল কম হলে সাধারণত ভালো ব্যালেন্স পাওয়া যায়।

## নিরাপত্তা ও সুরক্ষা

### নিরাপত্তা সংক্রান্ত নীতি কনফিগার করা হচ্ছে

Gemini 4 এবং Gemini 3.x মডেলে বিল্ট-ইন নিরাপত্তা পরিষেবার বিভাগ অন্তর্ভুক্ত থাকে যা
ব্যবহারকারীর কনফার্মেশন প্রয়োজন কিনা তা নির্ধারণ করতে সাহায্য করে।

| নিরাপত্তা নীতি বিভাগ | বিবরণ |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | পেমেন্ট, রিটেল চেক-আউট বা নিয়ন্ত্রিত প্রোডাক্টের সাথে জড়িত অ্যাকশনের জন্য কনফার্মেশন ব্লক বা ট্রিগার করে। |
| `SENSITIVE_DATA_MODIFICATION` | অননুমোদিত পরিবর্তন থেকে স্বাস্থ্য, আর্থিক বা সরকারি রেকর্ড সুরক্ষিত রাখে। |
| `COMMUNICATION_TOOL` | এজেন্টকে স্বয়ংক্রিয়ভাবে ইমেল, চ্যাট মেসেজ বা ড্রাফ্ট পাঠানো থেকে বিরত রাখে। |
| `ACCOUNT_CREATION` | এজেন্টকে ওয়েবসাইটে অটোমেটিক নতুন অ্যাকাউন্ট রেজিস্টার করা থেকে আটকায়। |
| `DATA_MODIFICATION` | সামগ্রিক ফাইল সিস্টেমের পরিবর্তন, ডেটা শেয়ারিং এবং স্টোরেজ মুছে ফেলার বিষয়টি নিয়ন্ত্রণ করে। |
| `USER_CONSENT_MANAGEMENT` | কুকি সংক্রান্ত সম্মতি ব্যানার ও গোপনীয়তা প্রম্পটের জন্য ব্যবহারকারীর টেকওভার প্রয়োজন। |
| `LEGAL_TERMS_AND_AGREEMENTS` | মডেলকে নিজে থেকে পরিষেবার শর্তাবলী বা আইনত বাধ্যতামূলক চুক্তিতে সম্মতি জানাতে বাধা দেয়। |

#### নিরাপত্তা ওভাররাইড

আপনি ওভাররাইড পাস করে বেছে নেওয়া নীতি ওভাররাইড করতে পারবেন:

with in some cases.

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### প্রম্পট ইঞ্জেকশন ডিটেকশন

Gemini 3.5 Flash-Lite বা তার পরবর্তী ভার্সনের জন্য কম্পিউটার ব্যবহার, প্রম্পট ইনজেকশন অ্যাটাক শনাক্ত করার জন্য একটি উন্নত নিরাপত্তা
মেকানিজমকে সমর্থন করে। চালু করা হলে, এই ফিচার
চেক করে দেখে যে অন্তর্ভুক্ত স্ক্রিনশটে লুকানো অ্যাডভার্সারিয়াল
নির্দেশ (যেমন, "আগের কমান্ড উপেক্ষা করো") আছে কিনা এবং শনাক্ত করা হলে
এক্সিকিউশন ব্লক করে দেয়।

প্রম্পট ইঞ্জেকশন ডিটেকশন হল একটি অপ্ট-ইন ফিচার। ডিফল্ট হল `false`।

আপনার কম্পিউটার ব্যবহার টুল কনফিগারেশনে কীভাবে প্রম্পট ইঞ্জেকশন ডিটেকশন চালু করবেন তা নিম্নলিখিত উদাহরণ থেকে
জানতে পারবেন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### নিরাপত্তা সংক্রান্ত সিদ্ধান্তে সম্মতি জানান

উত্তরে ফাংশন কল আর্গুমেন্টে `safety_decision` প্যারামিটার অন্তর্ভুক্ত থাকতে পারে:

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

`safety_decision` যদি `require_confirmation` হয়, তাহলে ব্যবহারকারীকে প্রম্পট করুন। ব্যবহারকারী কনফার্ম করলে, `function_result`-এ `safety_acknowledgement` সেট করুন।

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

### নিরাপত্তা সংক্রান্ত পেশাদার পদ্ধতি

কম্পিউটার ব্যবহারের ক্ষেত্রে অনন্য নিরাপত্তা ও অপারেশনাল ঝুঁকি থাকে, কারণ ব্যবহারকারীর হয়ে কাজ করা
মডেল স্ক্রিনে বিশ্বস্ত নয় এমন কন্টেন্টের সম্মুখীন হতে পারে অথবা অ্যাকশন কার্যকর করার সময়
ভুল করতে পারে। ব্যবহারকারীর ডেটা ও সিস্টেম সুরক্ষিত রাখতে নিম্নলিখিত পেশাদার পদ্ধতি
প্রয়োগ করুন:

1. **হিউম্যান-ইন-দ্য-লুপ (HITL):**
   - **ব্যবহারকারীর কনফার্মেশন এনফোর্স করা:** নিরাপত্তা সংক্রান্ত উত্তর
     `require_confirmation` নির্দেশ করলে, ব্যবহারকারীকে অনুমোদনের জন্য প্রম্পট করুন।
   - **কাস্টম নিরাপত্তা নির্দেশাবলী প্রদান করুন:** আপনার নিজস্ব নিরাপত্তা সীমানা নির্ধারণ এবং প্রয়োগ করতে একটি কাস্টম সিস্টেম নির্দেশাবলী প্রয়োগ করুন। যেমন:

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

     ### জাভাস্ক্রিপ্ট

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

### খুলুন

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

1. **নিরাপদ এক্সিকিউশন এনভায়রনমেন্ট:** আপনার এজেন্টের সম্ভাব্য প্রভাব সীমিত করতে, এটি একটি নিরাপদ, স্যান্ডবক্সড
   এনভায়রনমেন্টে চালান। এটি স্যান্ডবক্স করা ভার্চুয়াল
   মেশিন (VM), কন্টেনার (যেমন, Docker) বা সীমিত অনুমতি সহ
   নির্দিষ্ট ব্রাউজার প্রোফাইল হতে পারে। Docker ব্যবহার করে স্যান্ডবক্স সেট-আপ করার নির্দেশিকার জন্য
   [GitHub রেফারেন্স ইমপ্লিমেন্টেশন](https://github.com/google/computer-use-preview/)
   দেখুন।
2. **ইনপুট স্যানিটাইজেশন:** অনিচ্ছাকৃত নির্দেশাবলী বা প্রম্পট ইঞ্জেকশনের ঝুঁকি কমাতে
   প্রম্পটে ব্যবহারকারীর তৈরি করা সব টেক্সট স্যানিটাইজ করুন। এটি সুরক্ষার একটি
   সহায়ক স্তর, তবে এটি নিরাপদ এক্সিকিউশন এনভায়রনমেন্টের
   বিকল্প নয়।
3. **কন্টেন্ট গার্ডরেল:** ব্যবহারকারীর ইনপুট, টুলের ইনপুট ও আউটপুট এবং এজেন্টের উত্তর উপযুক্ত কিনা,
   প্রম্পট ইঞ্জেকশন এবং জেলব্রেক শনাক্তকরণের জন্য গার্ডরেল এবং কন্টেন্ট সুরক্ষা API ব্যবহার করুন।
4. **অনুমোদিত তালিকা এবং ব্লকলিস্ট:** মডেলটি কোথায় নেভিগেট করতে পারে এবং এটি কী করতে পারে তা নিয়ন্ত্রণ করতে ফিল্টারিং মেকানিজম প্রয়োগ করুন। নিষিদ্ধ ওয়েবসাইটের একটি ব্লকলিস্ট একটি ভাল সূচনা পয়েন্ট, যখন আরও সীমাবদ্ধ অনুমোদিত তালিকা আরও বেশি নিরাপদ।
5. **পর্যবেক্ষণ ও লগিং:** ডিবাগিং, অডিটিং ও ঘটনার প্রতিক্রিয়া সংক্রান্ত বিস্তারিত লগ বজায় রাখা। আপনার ক্লায়েন্টকে প্রম্পট, স্ক্রিনশট, মডেলের সাজেস্ট করা অ্যাকশন (`function_call`), নিরাপত্তা সংক্রান্ত উত্তর এবং
   ক্লায়েন্টের মাধ্যমে শেষ পর্যন্ত নেওয়া সব অ্যাকশন লগ করতে হবে।
6. **এনভায়রনমেন্ট ম্যানেজমেন্ট:** GUI এনভায়রনমেন্ট সামঞ্জস্যপূর্ণ কিনা তা নিশ্চিত করুন।
   অপ্রত্যাশিত পপ-আপ, বিজ্ঞপ্তি বা লে-আউটে পরিবর্তন মডেলকে বিভ্রান্ত করতে পারে। সম্ভব হলে, প্রতিটি নতুন টাস্কের জন্য পরিচিত, পরিষ্কার অবস্থা থেকে শুরু করুন।

## মডেল ভার্সন

আপনি নিম্নলিখিত মডেলের সাথে কম্পিউটার ব্যবহার করতে পারবেন:

- [**Gemini 4 Argon**](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=bn) (`gemini-4-argon`): আমাদের সবচেয়ে দক্ষ মডেল, যা জটিল রিজনিং ও এজেন্টিক UI ওয়ার্কফ্লোর জন্য কম্পিউটার ব্যবহার করার সুবিধা দেয়।
- [**Gemini 3.8 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=bn) (`gemini-3.8-flash`): কম্পিউটার ব্যবহারের জন্য সাজেস্ট করা মডেল, এতে উচ্চ-নির্ভুল UI ইন্টার‍্যাকশন এবং নির্ভরযোগ্য টুল কলিংয়ের সুবিধা রয়েছে।
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=bn) (`gemini-3.5-flash-lite`): কম লেটেন্সি ও সাশ্রয়ী মডেল যা কম্পিউটার ব্যবহার
  সমর্থন করে।
- [**Gemini 3 Flash প্রিভিউ**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=bn) (`gemini-3-flash-preview`): কম্পিউটার ব্যবহার
  সমর্থনকারী প্রিভিউ মডেল।

## এর পরে কী করতে হবে

- [Browserbase ডেমো এনভায়রনমেন্টে](http://gemini.browserbase.com) কম্পিউটার ব্যবহার নিয়ে এক্সপেরিমেন্ট করুন।
- উদাহরণ কোডের জন্য [রেফারেন্স প্রয়োগ](https://github.com/google/computer-use-preview) চেক করুন।
- অন্যান্য Gemini API টুল সম্পর্কে জানুন:
  - [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)
  - [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn)

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-22 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-22 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
