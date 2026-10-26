---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=hi
fetched_at: 2026-10-26T05:49:38.006396+00:00
title: "Gemini \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u0938\u094b\u091a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini के बारे में सोच

[Gemini मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi), "सोचने की प्रोसेस" का इस्तेमाल करते हैं. इससे, तर्क करने और कई चरणों में योजना बनाने की उनकी क्षमता में काफ़ी सुधार होता है. इस वजह से, वे कोडिंग, ऐडवांस मैथ, और डेटा विश्लेषण जैसे मुश्किल कामों को बेहतर तरीके से कर पाते हैं.

सूझ-बूझ वाले मॉडल का इस्तेमाल करने पर, Gemini जवाब देने से पहले अंदरूनी तौर पर विश्लेषण करता है. Interactions API, इस गहराई से विश्लेषण को `thought` चरणों के ज़रिए दिखाता है. ये ऐसे चरण होते हैं जो `steps` ऐरे में, फ़ंक्शन कॉल, उपयोगकर्ता के इनपुट या मॉडल आउटपुट के साथ-साथ समय के हिसाब से दिखते हैं.

हर थॉट स्टेप में दो फ़ील्ड होते हैं:

| फ़ील्ड | ज़रूरी है | ब्यौरा |
| --- | --- | --- |
| `signature` | ✅ हां | मॉडल के इंटरनल रीज़निंग स्टेट को एन्क्रिप्ट करके दिखाया गया है. यह हमेशा मौजूद रहता है, भले ही मॉडल कम से कम रीज़निंग करे. |
| `summary` | ❌ नहीं | कॉन्टेंट (टेक्स्ट और/या इमेज) का कलेक्शन, जिसमें वजह बताई गई हो. [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=hi) कॉन्फ़िगरेशन के आधार पर, यह खाली हो सकता है. इससे यह भी तय होता है कि मॉडल ने ज़रूरी तर्क दिए हैं या नहीं. इसके अलावा, कॉन्टेंट टाइप के आधार पर भी यह खाली हो सकता है. उदाहरण के लिए, इमेज लेटेंट में टेक्स्ट की खास जानकारी नहीं हो सकती. |

## सूझ-बूझ वाले मॉडल के साथ इंटरैक्शन

सोचने वाले मॉडल के साथ इंटरैक्शन शुरू करने का तरीका, किसी अन्य इंटरैक्शन अनुरोध की तरह ही होता है. `model` फ़ील्ड में, [रीज़निंग की सुविधा वाले मॉडल](#thinking-levels) में से किसी एक को चुनें:

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

### JavaScript

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

### आराम का समय

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## सूझ-बूझ से बनाई गई खास जानकारी

सोच-विचार की खास जानकारी से, मॉडल के तर्क करने की अंदरूनी प्रोसेस के बारे में अहम जानकारी मिलती है.
डिफ़ॉल्ट रूप से, सिर्फ़ फ़ाइनल आउटपुट दिखता है. `thinking_summaries` की मदद से, जवाब के बारे में जानकारी देने वाली सुविधा चालू की जा सकती है:

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

### JavaScript

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

### आराम का समय

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

इन मामलों में, किसी थॉट ब्लॉक में **सिर्फ़ हस्ताक्षर हो सकता है और कोई खास जानकारी नहीं**:

- आसान अनुरोध, जिनमें मॉडल ने खास जानकारी जनरेट करने के लिए, ज़रूरत के मुताबिक तर्क नहीं दिया
- `thinking_summaries: "none"`, जहां खास जानकारी देने की सुविधा को साफ़ तौर पर बंद किया गया है
- ऐसा हो सकता है कि कुछ खास तरह के कॉन्टेंट, जैसे कि इमेज के लिए टेक्स्ट वाली खास जानकारी उपलब्ध न हो

आपके कोड को हमेशा उन थॉट ब्लॉक को मैनेज करना चाहिए जिनमें `summary` खाली है या मौजूद नहीं है.

## रीज़निंग के साथ स्ट्रीमिंग

जनरेट करने के दौरान, सोच की खास जानकारी को धीरे-धीरे पाने के लिए स्ट्रीमिंग का इस्तेमाल करें.
Server-Sent Events (SSE) का इस्तेमाल करके, थॉट ब्लॉक डिलीवर किए जाते हैं. इनमें दो अलग-अलग डेल्टा टाइप होते हैं:

| डेल्टा टाइप | इसमें शामिल है | भेजे जाने का समय |
| --- | --- | --- |
| `thought_summary` | टेक्स्ट या इमेज की खास जानकारी वाला कॉन्टेंट | इंक्रीमेंटल समरी के साथ एक या उससे ज़्यादा डेल्टा |
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

### आराम का समय

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

स्ट्रीमिंग रिस्पॉन्स में, Server-Sent Events (SSE) का इस्तेमाल किया जाता है. इसमें चरण और इवेंट शामिल होते हैं. उदाहरण के लिए:

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

## सोच-विचार करने की प्रोसेस को कंट्रोल करना

Gemini मॉडल, डिफ़ॉल्ट रूप से डाइनैमिक तरीके से सोचते हैं. ये अनुरोध की जटिलता के आधार पर, रीज़निंग की क्षमता को अपने-आप अडजस्ट कर लेते हैं. `thinking_level` पैरामीटर का इस्तेमाल करके, इस व्यवहार को कंट्रोल किया जा सकता है.

| मॉडल | सोच-विचार करके जवाब देने का डिफ़ॉल्ट लेवल | इन लेवल पर काम करता है |
| --- | --- | --- |
| gemini-4-argon | चालू है (मीडियम) | कम, मध्यम, ज़्यादा |
| gemini-3.8-flash | चालू है (मीडियम) | कम, सामान्य, ज़्यादा |
| gemini-3.6-flash | चालू है (मीडियम) | बहुत कम, कम, मीडियम, ज़्यादा |
| gemini-3.5-flash-lite | चालू है (मिनिमल) | बहुत कम, कम, मीडियम, ज़्यादा |
| gemini-3.1-pro-preview | चालू है (ज़्यादा) | कम, सामान्य, ज़्यादा |
| gemini-3.1-flash-lite-image | चालू है (कम से कम) | कम, ज़्यादा |
| gemini-3-flash-preview | चालू है (ज़्यादा) | बहुत कम, कम, सामान्य, ज़्यादा |
| gemini-3-pro-preview | चालू है (ज़्यादा) | कम, ज़्यादा |
| gemini-2.5-pro | चालू | कम, मध्यम, ज़्यादा |
| gemini-2.5-flash | चालू | कम, सामान्य, ज़्यादा |
| gemini-2.5-flash-lite | बंद है | कम, मध्यम, ज़्यादा |
| gemini-robotics-er-2-preview | चालू है (ज़्यादा) | बहुत कम, कम, सामान्य, ज़्यादा |

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

### JavaScript

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

### आराम का समय

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

### टोकन की सीमाएं और `max_output_tokens`

[`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=hi#request-body) जनरेशन पैरामीटर, किसी जवाब में जनरेट किए जा सकने वाले टोकन की ज़्यादा से ज़्यादा संख्या सेट करता है. इसमें थॉट टोकन भी शामिल हैं.

सेट किए जाने पर, यह पैरामीटर इंफ़्रास्ट्रक्चर की ओर से लागू किए गए हार्ड कटऑफ़ के तौर पर काम करता है. इससे मॉडल के थिंकिंग बजट (`thinking_level`) को तय करने के तरीके में कोई बदलाव नहीं होता.

अगर मॉडल, जवाब देने के दौरान इस सीमा तक पहुंच जाता है, तो वह `"incomplete"` स्टेटस के साथ जवाब जनरेट करना बंद कर देता है. साथ ही, छोटा किया गया या खाली आउटपुट दिखाता है. हालाँकि, इस दौरान जनरेट किए गए किसी भी थिंकिंग टोकन के लिए बिलिंग जारी रहती है. जवाबों को छोटा किए बिना लागत या इंतज़ार का समय कम करने के लिए, `max_output_tokens` की वैल्यू को कम करने के बजाय, `thinking_level` (`low` या `medium`) की वैल्यू को कम करें.

Gemini 4 के मॉडल (`gemini-4-argon`) के लिए, कॉन्टेक्स्ट और आउटपुट की इन सीमाओं को ध्यान में रखें:

- **10 लाख टोकन वाली कॉन्टेक्स्ट विंडो:** इनपुट, सोचने, और आउटपुट के लिए इस्तेमाल किए जाने वाले टोकन, 10 लाख टोकन वाली एक ही कॉन्टेक्स्ट विंडो (`1,048,576` टोकन) शेयर करते हैं. अगर आपके इनपुट टोकन और `max_output_tokens` की संख्या 10,48,576 टोकन से ज़्यादा हो जाती है, तो एपीआई अपने-आप आउटपुट की सीमा को कॉन्टेक्स्ट विंडो में बची हुई जगह (`1,048,576` में से आपके इनपुट टोकन घटाने के बाद बची जगह) तक सीमित कर देता है.
- **डिफ़ॉल्ट सिंक्रोनस आउटपुट कैप (64K):** जब `background=False` (स्ट्रीमिंग और नॉन-स्ट्रीमिंग, दोनों अनुरोधों के लिए), डिफ़ॉल्ट और ज़्यादा से ज़्यादा `max_output_tokens` कैप `65,536` टोकन होता है. `max_output_tokens > 65536` को `background=False` पर सेट करने से, `400` गड़बड़ी का मैसेज दिखता है.
- **लॉन्ग डिकोड (ज़्यादा से ज़्यादा 10 लाख टोकन):** Gemini 4 को `65,536` से ज़्यादा टोकन (ज़्यादा से ज़्यादा `1,048,576` टोकन) जनरेट करने और रीज़निंग करने की अनुमति देने के लिए, `background=True` को सेट करें और `max_output_tokens` को `65,536` से ज़्यादा पर कॉन्फ़िगर करें. ज़्यादा जानकारी के लिए, [लॉन्ग डिकोड](https://ai.google.dev/gemini-api/docs/long-decode?hl=hi) देखें.

## सोच के आधार पर हस्ताक्षर

थॉट सिग्नेचर, मॉडल की इंटरनल रीज़निंग के एन्क्रिप्ट किए गए वर्शन होते हैं. उन्हें बार-बार किए जाने वाले इंटरैक्शन में, जवाब देने के लिए एक ही तर्क का इस्तेमाल करना होता है.

Interactions API की मदद से, थॉट सिग्नेचर को मैनेज करना `generateContent` API के मुकाबले ज़्यादा आसान हो जाता है.

### स्टेटफ़ुल मोड (सुझाया गया)

डिफ़ॉल्ट रूप से, स्टेटफ़ुल मोड में Interactions API का इस्तेमाल करने पर, सर्वर बातचीत की स्थिति को अपने-आप मैनेज करता है. इसके लिए, आपको `store: true` सेट करना होगा और इसके बाद के टर्न में `previous_interaction_id` पास करना होगा. बातचीत की स्थिति में, सभी थॉट ब्लॉक और सिग्नेचर शामिल होते हैं. इस मोड में, आपको हस्ताक्षर के बारे में कुछ भी करने की ज़रूरत नहीं है. इन्हें पूरी तरह से सर्वर साइड पर मैनेज किया जाता है.

### स्टेटलेस मोड

अगर बातचीत की स्थिति को खुद मैनेज किया जा रहा है (स्टेटलेस मोड) और हर अनुरोध में इनपुट और आउटपुट का पूरा इतिहास पास किया जा रहा है, तो:

- आपको सभी `thought` ब्लॉक, ठीक उसी तरह से फिर से भेजने **होंगे** जिस तरह से वे मॉडल से मिले थे.
- आपको इतिहास से थॉट ब्लॉक **नहीं** हटाने चाहिए या उनमें बदलाव नहीं करना चाहिए, क्योंकि इनमें ऐसे सिग्नेचर होते हैं जिनकी ज़रूरत मॉडल को जवाब देने के लिए होती है.
- किसी सेशन के दौरान मॉडल स्विच करने पर, आपको पिछले मॉडल के थॉट ब्लॉक फिर से भेजने चाहिए. बैकएंड, साथ काम करने की सुविधा को मैनेज करता है.

## कीमत

सोचने की सुविधा चालू होने पर, जवाब की कीमत आउटपुट टोकन और सोचने वाले टोकन के योग के बराबर होती है. `total_thought_tokens` फ़ील्ड से, जनरेट किए गए थिंकिंग टोकन की कुल संख्या पाई जा सकती है.

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

सूझ-बूझ वाले मॉडल, फ़ाइनल जवाब की क्वालिटी को बेहतर बनाने के लिए पूरी जानकारी जनरेट करते हैं. इसके बाद, वे [खास जानकारी](#summaries) आउटपुट करते हैं, ताकि जवाब जनरेट करने की प्रोसेस के बारे में अहम जानकारी दी जा सके. कीमत, उन सभी थॉट टोकन के आधार पर तय की जाती है जिन्हें मॉडल को जनरेट करना होता है. भले ही, एपीआई से सिर्फ़ खास जानकारी आउटपुट के तौर पर मिलती हो.

[टोकन की गिनती](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) गाइड में, टोकन के बारे में ज़्यादा जानें.

## सबसे सही तरीके

इन दिशा-निर्देशों का पालन करके, थिंकिंग मॉडल का असरदार तरीके से इस्तेमाल करें.

- **रीज़निंग की समीक्षा करना**: गड़बड़ियों को समझने और प्रॉम्प्ट को बेहतर बनाने के लिए, सोच-विचार की खास जानकारी का विश्लेषण करें.
- **सोचने के लिए बजट कंट्रोल करना**: टोकन बचाने के लिए, मॉडल को लंबे आउटपुट के लिए कम सोचने का निर्देश दें.
- **आसान टास्क**: तथ्यों को खोजने या उन्हें कैटगरी में बांटने के लिए, कम से कम या कम सोच-विचार का इस्तेमाल करें. जैसे, "DeepMind की स्थापना कहां हुई थी?".
- **सामान्य टास्क**: कॉन्सेप्ट की तुलना करने या क्रिएटिव रीज़निंग के लिए, डिफ़ॉल्ट थिंकिंग मोड का इस्तेमाल करें. जैसे, इलेक्ट्रिक और हाइब्रिड कारों की तुलना करना.
- **मुश्किल टास्क**: ऐडवांस कोडिंग, गणित या कई चरणों वाली प्लानिंग के लिए, ज़्यादा से ज़्यादा सूझ-बूझ वाले मॉडल का इस्तेमाल करें. जैसे, एआईएमई के गणित के सवाल हल करना.

## आगे क्या करना है

- [टेक्स्ट जनरेशन](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi): सामान्य टेक्स्ट वाले जवाब
- [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi): टूल से कनेक्ट करना
- [Gemini 4 guide](https://ai.google.dev/gemini-api/docs/latest-model?hl=hi): Gemini 4 में नया क्या है
- [Gemini 3 guide](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=hi): Model-specific
  features

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-14 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-14 (UTC) को अपडेट किया गया."],[],[]]
