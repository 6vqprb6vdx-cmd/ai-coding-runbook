---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=bn
fetched_at: 2026-10-19T05:32:29.486500+00:00
title: "Gemini \u09ad\u09be\u09ac\u099b\u09c7 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Gemini ভাবছে

[Gemini মডেল](https://ai.google.dev/gemini-api/docs/models?hl=bn) একটি
"চিন্তা করার প্রসেস" ব্যবহার করে যা এর রিজনিং ও মাল্টি-স্টেপ
প্ল্যানিংয়ের ক্ষমতাকে উল্লেখযোগ্যভাবে উন্নত করে, যার ফলে কোডিং, উন্নত গণিত ও ডেটা বিশ্লেষণের মতো
জটিল টাস্কের ক্ষেত্রে এটি অত্যন্ত কার্যকর হয়ে ওঠে।

আপনি থিঙ্কিং মডেল ব্যবহার করলে, Gemini উত্তর দেওয়ার আগে ইন্টার্নালি যুক্তি দেয়। Interactions API এই যুক্তি `thought` ধাপের মাধ্যমে দেখায়, এগুলি হল নির্দিষ্ট ধাপ যা `steps` অ্যারেতে ফাংশন কল, ব্যবহারকারীর ইনপুট বা মডেল আউটপুটের পাশাপাশি ক্রমানুসারে দেখানো হয়।

প্রতিটি চিন্তার ধাপে দুটি ফিল্ড থাকে:

| ফিল্ড | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- |
| `signature` | ✅ হ্যাঁ | মডেলের ইন্টার্নাল রিজনিং স্টেট এনক্রিপ্ট করে দেখানো হয়েছে। মডেলটি ন্যূনতম যুক্তি সম্পাদন করলেও সর্বদা উপস্থিত থাকে। |
| `summary` | ❌ না | যুক্তিকে সংক্ষিপ্তসার করে এমন কন্টেন্টের (টেক্সট এবং/অথবা ছবি) একটি অ্যারে। [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=bn) কনফিগারেশনের উপর নির্ভর করে খালি থাকতে পারে, মডেলটি যথেষ্ট যুক্তি দেখিয়েছে কিনা বা কন্টেন্টের ধরন (যেমন, ইমেজ লেটেন্টে টেক্সট সারসংক্ষেপ নাও থাকতে পারে)। |

## Thinking-এর সাথে ইন্টার‍্যাকশন

থিংকিং মডেলের সাথে ইন্টার‍্যাকশন শুরু করা, অন্য যেকোনও ইন্টার‍্যাকশন অনুরোধের মতোই। `model` ফিল্ডে [চিন্তাভাবনা সংক্রান্ত সহায়তা সহ মডেল](#thinking-levels)গুলির মধ্যে একটি নির্দিষ্ট করুন:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Explain the concept of Occam's Razor and provide a simple, everyday example."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
            Input: interactions.NewInteractionsInput("Explain the concept of Occam's Razor and provide a simple, everyday example."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## চিন্তাভাবনার সারসংক্ষেপ

চিন্তার সারসংক্ষেপ মডেলের ইন্টার্নাল রিজনিং প্রসেস সম্পর্কে ইনসাইট প্রদান করে।
ডিফল্ট হিসেবে, শুধু চূড়ান্ত আউটপুটই রিটার্ন করা হয়। আপনি `thinking_summaries`-এর মাধ্যমে
থট সামারি চালু করতে পারবেন:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtStep;
import com.google.genai.gaos.models.interactions.ThoughtSummaryContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the sum of the first 50 prime numbers?"))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ThoughtStep thoughtStep) {
    System.out.println("Thought summary:");
    for (ThoughtSummaryContent contentBlock : thoughtStep.summary().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println(textContent.text().orElse(""));
      }
    }
    System.out.println();
  } else if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println("Answer:");
        System.out.println(textContent.text().orElse(""));
        System.out.println();
      }
    }
  }
}
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
            Input: interactions.NewInteractionsInput("Provide a list of 3 famous physicists and their key contributions"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

এইসব ক্ষেত্রে, একটি থট ব্লকে **সারসংক্ষেপ ছাড়া শুধুমাত্র একটি স্বাক্ষর** থাকতে পারে:

- সহজ অনুরোধ, যেখানে মডেলটি সারসংক্ষেপ তৈরি করার জন্য যথেষ্ট যুক্তি দেয়নি
- `thinking_summaries: "none"`, যেখানে সারসংক্ষেপ স্পষ্টভাবে বন্ধ করা আছে
- ছবির মতো নির্দিষ্ট কিছু থট কন্টেন্টের টেক্সট সারসংক্ষেপ নাও থাকতে পারে

আপনার কোডকে সবসময় এমন থট ব্লক ম্যানেজ করতে হবে যেখানে `summary` খালি বা অনুপস্থিত।

## থিঙ্কিং সহ স্ট্রিমিং

জেনারেট করার সময় ইনক্রিমেন্টাল চিন্তার সারসংক্ষেপ পেতে স্ট্রিমিং ব্যবহার করুন।
Server-Sent Events (SSE) ব্যবহার করে থট ব্লক ডেলিভার করা হয়, যার মধ্যে দুটি আলাদা
ডেল্টা টাইপ থাকে:

| ডেল্টার ধরন | এর মধ্যে আছে | কখন পাঠানো হয়েছে |
| --- | --- | --- |
| `thought_summary` | টেক্সট বা ছবির সারসংক্ষেপ কন্টেন্ট | ক্রমবর্ধমান সারসংক্ষেপ সহ এক বা একাধিক ডেল্টা |
| `thought_signature` | ক্রিপ্টোগ্রাফিক স্বাক্ষর | `step.stop`-এর আগে শেষ ডেল্টা |

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
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

String prompt =
    "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.\n"
        + "Alice does not live in the red house.\n"
        + "Bob does not live in the green house.\n"
        + "Carol does not live in the red or green house.\n"
        + "Which house does each person live in?";

StringBuilder thoughts = new StringBuilder();
StringBuilder answer = new StringBuilder();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta stepDelta) {
      StepDeltaData delta = stepDelta.delta().orElse(null);
      if (delta instanceof ThoughtSummaryDelta thoughtDelta) {
        Content content = thoughtDelta.content().orElse(null);
        if (content instanceof TextContent textContent) {
          if (thoughts.length() == 0) {
            System.out.println("Thinking...");
          }
          String summaryText = textContent.text().orElse("");
          System.out.print("[Thought] " + summaryText);
          thoughts.append(summaryText);
        }
      } else if (delta instanceof TextDelta textDelta) {
        String text = textDelta.text().orElse("");
        if (!text.isEmpty()) {
          if (answer.length() == 0) {
            System.out.println("\nAnswer:");
          }
          System.out.print(text);
          answer.append(text);
        }
      }
    }
  }
}
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
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought summary:\n%s\n\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

স্ট্রিমিং রেসপন্স Server-Sent Events (SSE) ব্যবহার করে এবং এটি বিভিন্ন ধাপ ও ইভেন্ট নিয়ে গঠিত, যেমন:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

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

## নিয়ন্ত্রণকারী চিন্তাভাবনা

Gemini মডেলগুলি ডিফল্ট হিসেবে ডায়নামিক চিন্তাভাবনা করে, অনুরোধের জটিলতার উপর ভিত্তি করে যুক্তির পরিমাণ অটোমেটিক অ্যাডজাস্ট করে।
আপনি `thinking_level` প্যারামিটার ব্যবহার করে এই আচরণ নিয়ন্ত্রণ করতে পারবেন।

| মডেল | ডিফল্ট থিঙ্কিং | লেভেল কাজ করে |
| --- | --- | --- |
| gemini-4-argon | চালু আছে (মাঝারি) | কম, মাঝারি, বেশি |
| gemini-3.8-flash | চালু আছে (মাঝারি) | কম, মাঝারি, বেশি |
| gemini-3.6-flash | চালু আছে (মাঝারি) | ন্যূনতম, কম, মাঝারি, বেশি |
| gemini-3.5-flash-lite | চালু আছে (মিনিমাল) | ন্যূনতম, কম, মাঝারি, বেশি |
| gemini-3.1-pro-preview | চালু (বেশি) | কম, মাঝারি, বেশি |
| gemini-3.1-flash-lite-image | চালু আছে (মিনিমাল) | মিনিমাল, হাই |
| gemini-3-flash-preview | চালু (বেশি) | ন্যূনতম, কম, মাঝারি, বেশি |
| gemini-3-pro-preview | চালু (বেশি) | কম, বেশি |
| gemini-2.5-pro | চালু আছে | কম, মাঝারি, বেশি |
| gemini-2.5-flash | চালু আছে | কম, মাঝারি, বেশি |
| gemini-2.5-flash-lite | বন্ধ আছে | কম, মাঝারি, বেশি |
| gemini-robotics-er-2-preview | চালু আছে (হাই) | ন্যূনতম, কম, মাঝারি, বেশি |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Provide a list of 3 famous physicists and their key contributions"))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.LOW).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("[Thought Summary] %s\n", textContent.Text)
                }
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### টোকেন সীমা ও `max_output_tokens`

[`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=bn#request-body) জেনারেশন
প্যারামিটার, কোনও উত্তর সর্বাধিক কতগুলি টোকেন জেনারেট করতে পারবে তা সেট করে, এর মধ্যে
থট টোকেনও অন্তর্ভুক্ত।

সেট করা হলে, এই প্যারামিটারটি ইনফ্রাস্ট্রাকচার দ্বারা প্রয়োগ করা একটি হার্ড কাটঅফ হিসাবে কাজ করে
মডেল কীভাবে তার থিঙ্কিং বাজেট বরাদ্দ করে তা পরিবর্তন না করেই
(`thinking_level`)।

রিজনিং করার সময় মডেল এই সীমায় পৌঁছে গেলে, এটি
`"incomplete"` স্ট্যাটাস সহ জেনারেট করা বন্ধ করে দেয় এবং ট্রাঙ্কেট করা বা খালি আউটপুট রিটার্ন করে (যদিও জেনারেট করা যেকোনও থিঙ্কিং টোকেনের জন্য
বিলিং করা হয়)। উত্তর ট্রাঙ্কেট না করে খরচ বা লেটেন্সি কমাতে, ছোট `max_output_tokens` সেট করার পরিবর্তে `thinking_level` (`low` বা `medium`)
কমান।

Gemini 4 মডেলের (`gemini-4-argon`) জন্য, নিম্নলিখিত কনটেক্সট ও আউটপুট সীমা মনে রাখবেন:

- **শেয়ার করা 1M কন্টেক্সট উইন্ডো:** ইনপুট, থিঙ্কিং ও আউটপুট টোকেন একটি 1M-টোকেন কন্টেক্সট উইন্ডো (`1,048,576` টোকেন) শেয়ার করে। আপনার ইনপুট টোকেন এবং `max_output_tokens`-এর যোগফল 1,048,576 টোকেনের বেশি হলে, API অটোমেটিক আউটপুট সীমা কন্টেক্সট উইন্ডোর বাকি স্পেসে (`1,048,576` থেকে আপনার ইনপুট টোকেন বিয়োগ করে) সীমাবদ্ধ করে দেয়।
- **ডিফল্ট সিঙ্ক্রোনাস আউটপুট ক্যাপ (64K):** যখন `background=False` (স্ট্রিমিং এবং নন-স্ট্রিমিং অনুরোধের জন্য), ডিফল্ট এবং সর্বাধিক `max_output_tokens` ক্যাপ হল `65,536` টোকেন। `background=False` সহ `max_output_tokens > 65536` সেট করলে `400` সমস্যা হয়।
- **লং ডিকোড (সর্বাধিক ১ মিলিয়ন টোকেন):** Gemini 4-কে `65,536` টোকেনের (সর্বাধিক `1,048,576` টোকেন) বাইরে রিজনিং ও জেনারেট করার অনুমতি দিতে, `background=True` সেট করুন এবং `max_output_tokens`-কে `65,536`-এর থেকে বেশি হিসেবে কনফিগার করুন। বিবরণের জন্য [লং ডিকোড](https://ai.google.dev/gemini-api/docs/long-decode?hl=bn) দেখুন।

## থট সিগনেচার

থট সিগনেচার হল মডেলের ইন্টার্নাল যুক্তির এনক্রিপ্টেড উপস্থাপনা। মাল্টি-টার্ন ইন্টার‍্যাকশন জুড়ে রিজনিংয়ের ধারাবাহিকতা বজায় রাখার জন্য এগুলি প্রয়োজন।

Interactions API, `generateContent` API-এর চেয়ে অনেক সহজে থট সিগনেচার ম্যানেজ করে।

### স্টেটফুল মোড (সাজেস্ট করা হয়েছে)

ডিফল্ট হিসেবে, আপনি যখন স্টেটফুল মোডে Interactions API ব্যবহার করেন (`store: true` সেট করে এবং পরবর্তী টার্নে `previous_interaction_id` পাস করে), তখন সার্ভার অটোমেটিক কথোপকথনের স্টেট ম্যানেজ করে, যার মধ্যে সব থট ব্লক ও সিগনেচার অন্তর্ভুক্ত থাকে। এই মোডে, আপনাকে স্বাক্ষর সংক্রান্ত কোনও কিছু করতে হবে না। এগুলি সম্পূর্ণভাবে সার্ভার সাইডে ম্যানেজ করা হয়।

### স্টেটলেস মোড

আপনি যদি নিজে কথোপকথনের স্টেট ম্যানেজ করেন (স্টেটলেস মোড) এবং প্রতিটি অনুরোধে ইনপুট ও আউটপুটের সম্পূর্ণ ইতিহাস পাস করেন:

- মডেল থেকে যেভাবে `thought` ব্লক পেয়েছেন, আপনাকে **অবশ্যই** ঠিক সেইভাবেই সেগুলি আবার পাঠাতে হবে।
- ইতিহাস থেকে আপনার চিন্তাভাবনার ব্লক সরানো বা পরিবর্তন করা **উচিত নয়**, কারণ এতে মডেলের যুক্তি চালিয়ে যাওয়ার জন্য প্রয়োজনীয় স্বাক্ষর থাকে।
- একটি সেশনের মধ্যে মডেল পরিবর্তন করার সময়, আপনাকে আগের মডেলের থট ব্লক আবার পাঠাতে হবে। ব্যাকএন্ড কম্প্যাটিবিলিটি ম্যানেজ করে।

## দাম

থিঙ্কিং চালু করা থাকলে, রেসপন্সের দাম হল আউটপুট টোকেন এবং থিঙ্কিং টোকেনের
যোগফল। আপনি `total_thought_tokens` ফিল্ড থেকে জেনারেট করা থিঙ্কিং টোকেনের মোট সংখ্যা
পেতে পারেন।

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### জাভাস্ক্রিপ্ট

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain the concept of Occam's Razor."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.usage().isPresent()) {
  Usage usage = interaction.usage().get();
  System.out.println("Thoughts tokens: " + usage.totalThoughtTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
}
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

    // Turn 1: Execute a reasoning + tool use interaction
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Compare the GDP growth of Japan and Germany in 2025."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Pass PreviousInteractionID so thought signatures are automatically preserved
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-pro"),
            PreviousInteractionID: turn1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Now summarize that comparison in a 3-row markdown table."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

থিঙ্কিং মডেল চূড়ান্ত উত্তরের কোয়ালিটি উন্নত করতে সম্পূর্ণ চিন্তাভাবনা জেনারেট করে এবং তারপর চিন্তাভাবনার প্রসেস সম্পর্কে ইনসাইট প্রদান করতে [সারসংক্ষেপ](#summaries) আউটপুট করে। API থেকে শুধুমাত্র সারসংক্ষেপ আউটপুট হিসেবে পাওয়া গেলেও, মডেলের সম্পূর্ণ থট টোকেন জেনারেট করার উপর ভিত্তি করে দাম নির্ধারণ করা হয়।

[টোকেন গণনা](https://ai.google.dev/gemini-api/docs/tokens?hl=bn) সংক্রান্ত নির্দেশিকা থেকে টোকেন সম্পর্কে আরও জানতে পারবেন।

## পেশাদার পদ্ধতি

এইসব নির্দেশিকা অনুসরণ করে থিঙ্কিং মডেল দক্ষতার সাথে ব্যবহার করুন।

- **রিজনিং পর্যালোচনা করা**: ব্যর্থতা বুঝতে এবং প্রম্পট উন্নত করতে থট সামারি বিশ্লেষণ করুন।
- **থিংকিং বাজেট নিয়ন্ত্রণ করা**: টোকেন বাঁচাতে, দীর্ঘ আউটপুটের জন্য মডেলকে কম ভাবতে প্রম্পট করুন।
- **সহজ টাস্ক**: তথ্য উদ্ধার বা শ্রেণীবিন্যাসের জন্য ন্যূনতম বা কম চিন্তাভাবনা ব্যবহার করুন (যেমন, "DeepMind কোথায় প্রতিষ্ঠিত হয়েছিল?")।
- **মাঝারি টাস্ক**: ধারণা তুলনা করা বা ক্রিয়েটিভ রিজনিংয়ের (যেমন, ইলেকট্রিক ও হাইব্রিড গাড়ির তুলনা করা) জন্য ডিফল্ট থিঙ্কিং ব্যবহার করো।
- **জটিল টাস্ক**: উন্নত কোডিং, অঙ্ক বা মাল্টি-স্টেপ প্ল্যানিংয়ের জন্য সর্বোচ্চ থিঙ্কিং ব্যবহার করুন (যেমন, AIME অঙ্কের সমস্যার সমাধান করা)।

## এর পরে কী করতে হবে

- [টেক্সট তৈরি করা](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn): প্রাথমিক টেক্সট উত্তর
- [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn): টুলের সাথে কানেক্ট করুন
- [Gemini 4 গাইড](https://ai.google.dev/gemini-api/docs/latest-model?hl=bn): Gemini 4-এ নতুন কী কী আছে
- [Gemini 3 গাইড](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=bn): মডেল-নির্দিষ্ট
  ফিচার

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-14 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-14 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
