---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=hi
fetched_at: 2026-05-11T12:40:33.770104+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini सोच रहा है

[Gemini 3 और 2.5 सीरीज़ के मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi), "थिंकिंग प्रोसेस" का इस्तेमाल करते हैं. इससे, उनकी तर्क करने और कई चरणों वाली प्लानिंग करने की क्षमता बेहतर होती है. इसलिए, ये मॉडल कोडिंग, ऐडवांस गणित, और डेटा विश्लेषण जैसे मुश्किल कामों को बेहतर तरीके से कर पाते हैं.

इस गाइड में, Gemini API का इस्तेमाल करके, Gemini की सोचने-समझने की क्षमताओं का इस्तेमाल करने का तरीका बताया गया है.

## सोच-समझकर कॉन्टेंट जनरेट करना

सोचने वाले मॉडल से अनुरोध करना, कॉन्टेंट जनरेट करने के किसी अन्य अनुरोध की तरह ही होता है. मुख्य अंतर यह है कि `model` फ़ील्ड में, [सोचने की क्षमता वाले मॉडल](#supported-models) में से किसी एक को तय किया जाता है. जैसा कि [टेक्स्ट जनरेट करने](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#text-input) के इस उदाहरण में दिखाया गया है:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3-flash-preview"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## सोच-समझकर तैयार की गई खास जानकारी

सोच के बारे में खास जानकारी, मॉडल की सोच के बारे में खास जानकारी देने वाले वर्शन होते हैं. इनसे मॉडल की सोच के बारे में जानकारी मिलती है. ध्यान दें कि सोचने के लेवल और बजट, मॉडल के रॉ थॉट पर लागू होते हैं. ये थॉट की खास जानकारी पर लागू नहीं होते.

अपने अनुरोध के कॉन्फ़िगरेशन में `includeThoughts` को `true` पर सेट करके, सोच के बारे में खास जानकारी देने वाली सुविधा चालू की जा सकती है. इसके बाद, `response` पैरामीटर के `parts` को दोहराकर और `thought` बूलियन की जांच करके, खास जानकारी को ऐक्सेस किया जा सकता है.

यहां एक उदाहरण दिया गया है, जिसमें यह दिखाया गया है कि स्ट्रीमिंग के बिना, सोच के बारे में खास जानकारी देने वाली सुविधा को कैसे चालू करें और उससे जानकारी कैसे पाएं. इससे जवाब के साथ, सोच के बारे में खास जानकारी देने वाला एक फ़ाइनल जवाब मिलता है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

यहां स्ट्रीमिंग के साथ सोचने की सुविधा का इस्तेमाल करके एक उदाहरण दिया गया है. इससे जवाब जनरेट होने के दौरान, रोलिंग और इंक्रीमेंटल खास जानकारी मिलती है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3-flash-preview",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3-flash-preview"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## सोचने की क्षमता पर कंट्रोल करना

Gemini मॉडल, डिफ़ॉल्ट रूप से डाइनैमिक थिंकिंग का इस्तेमाल करते हैं. वे उपयोगकर्ता के अनुरोध की जटिलता के आधार पर, जवाब देने के लिए ज़रूरी कोशिश को अपने-आप अडजस्ट करते हैं.
हालांकि, अगर आपको लेटेन्सी से जुड़ी कुछ खास पाबंदियां लगानी हैं या मॉडल को सामान्य से ज़्यादा गहराई से सोचने की ज़रूरत है, तो आपके पास पैरामीटर का इस्तेमाल करके, सोचने के तरीके को कंट्रोल करने का विकल्प होता है.

### सूझ-बूझ वाले मॉडल के लेवल (Gemini 3)

`thinkingLevel` पैरामीटर का इस्तेमाल करने का सुझाव Gemini 3 और इसके बाद के मॉडल के लिए दिया जाता है. इससे, तर्क करने के तरीके को कंट्रोल किया जा सकता है.

यहां दी गई टेबल में, हर मॉडल टाइप के लिए `thinkingLevel` सेटिंग के बारे में जानकारी दी गई है:

| सोचने का लेवल | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | ब्यौरा |
| --- | --- | --- | --- | --- |
| **`minimal`** | काम नहीं करता है | काम करता है (डिफ़ॉल्ट) | काम करता है | यह सेटिंग, ज़्यादातर क्वेरी के लिए "सोचने की ज़रूरत नहीं है" सेटिंग से मेल खाती है. मुश्किल कोडिंग टास्क के लिए, मॉडल बहुत कम सोच सकता है. यह चैट या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए, लेटेन्सी को कम करता है. ध्यान दें कि `minimal` इस बात की गारंटी नहीं देता कि सोचने की सुविधा बंद है. |
| **`low`** | काम करता है | काम करता है | काम करता है | इससे इंतज़ार का समय और लागत कम हो जाती है. यह मॉडल, आसान निर्देशों का पालन करने, चैट करने या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए सबसे अच्छा है. |
| **`medium`** | काम करता है | काम करता है | काम करता है | ज़्यादातर कामों के लिए, सोच-समझकर जवाब देता है. |
| **`high`** | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | काम करता है (डाइनैमिक) | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | इससे रीज़निंग की गहराई बढ़ जाती है. मॉडल को पहले (बिना सोचे-समझे) आउटपुट टोकन तक पहुंचने में ज़्यादा समय लग सकता है. हालांकि, आउटपुट ज़्यादा सोच-समझकर दिया जाएगा. |

नीचे दिए गए उदाहरण में, सोचने का लेवल सेट करने का तरीका बताया गया है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Gemini 3.1 Pro के लिए, सोचने की सुविधा बंद नहीं की जा सकती. Gemini 3 Flash और Flash-Lite में भी, 'सोचने की सुविधा' को पूरी तरह से बंद नहीं किया जा सकता. हालांकि, `minimal` सेटिंग का मतलब है कि मॉडल शायद ही सोचे (हालाँकि, यह अब भी सोच सकता है).
अगर आपने सोचने का लेवल नहीं बताया है, तो Gemini, Gemini 3 मॉडल के डिफ़ॉल्ट डाइनैमिक थिंकिंग लेवल, `"high"` का इस्तेमाल करेगा.

Gemini 2.5 सीरीज़ के मॉडल, `thinkingLevel` के साथ काम नहीं करते. इसके बजाय, `thinkingBudget` का इस्तेमाल करें.

### बजट के बारे में सोचना

Gemini 2.5 सीरीज़ के साथ पेश किया गया `thinkingBudget` पैरामीटर, मॉडल को यह बताता है कि तर्क करने के लिए कितने थिंकिंग टोकन का इस्तेमाल करना है.

यहां हर मॉडल टाइप के लिए, `thinkingBudget` कॉन्फ़िगरेशन की जानकारी दी गई है.
`thinkingBudget` को 0 पर सेट करके, सोचने की सुविधा को बंद किया जा सकता है.
`thinkingBudget` को -1 पर सेट करने से, **डाइनैमिक थिंकिंग** चालू हो जाती है. इसका मतलब है कि मॉडल, अनुरोध की जटिलता के आधार पर बजट को अडजस्ट करेगा.

| मॉडल | डिफ़ॉल्ट सेटिंग (बजट सेट नहीं किया गया है) | रेंज | प्रोसेस की जानकारी छिपाएं | डाइनैमिक थिंकिंग की सुविधा चालू करना |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | डाइनैमिक थिंकिंग | `128` से `32768` | लागू नहीं: सोचने की सुविधा बंद नहीं की जा सकती | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 फ़्लैश** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 Flash Preview** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 Flash Lite** | मॉडल को नहीं लगता | `512` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite की झलक** | मॉडल को नहीं लगता | `512` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 की झलक** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 फ़्लैश लाइव नेटिव ऑडियो की झलक (09-2025)** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

प्रॉम्प्ट के हिसाब से, मॉडल टोकन बजट से ज़्यादा या कम टोकन जनरेट कर सकता है.

## सोच के हस्ताक्षर

[थॉट सिग्नेचर को मैन्युअल तरीके से मैनेज करना होगा](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#thought-signatures).

Gemini API स्टेटलेस है. इसलिए, मॉडल हर एपीआई अनुरोध को अलग-अलग तरीके से प्रोसेस करता है. साथ ही, कई बार की बातचीत में, मॉडल के पास पिछले टर्न के कॉन्टेक्स्ट का ऐक्सेस नहीं होता.

कई बार की बातचीत में, सोच के कॉन्टेक्स्ट को बनाए रखने के लिए, Gemini, थॉट सिग्नेचर दिखाता है. ये मॉडल की इंटरनल थॉट प्रोसेस के एन्क्रिप्ट (सुरक्षित) किए गए वर्शन होते हैं.

- **Gemini 2.5 मॉडल**, थिंकिंग की सुविधा चालू होने पर थॉट सिग्नेचर दिखाते हैं. साथ ही, अनुरोध में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#thinking) और खास तौर पर [फ़ंक्शन के बारे में जानकारी](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#step-2) शामिल होनी चाहिए.
- **Gemini 3 मॉडल**, सभी तरह के [पार्ट](https://ai.google.dev/api/caching?hl=hi#Part) के लिए थॉट सिग्नेचर दिखा सकते हैं.
  हमारा सुझाव है कि आपको मिले सभी हस्ताक्षर वापस भेजें. हालांकि, फ़ंक्शन कॉल करने के लिए हस्ताक्षर *ज़रूरी* हैं. ज़्यादा जानने के लिए, [Thought Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi) पेज पढ़ें.

फ़ंक्शन कॉलिंग के साथ-साथ, इस्तेमाल से जुड़ी अन्य पाबंदियों का भी ध्यान रखना चाहिए. जैसे:

- जवाब के अन्य हिस्सों में मॉडल से सिग्नेचर मिलते हैं. उदाहरण के लिए, फ़ंक्शन कॉल करना या टेक्स्ट वाले हिस्से.
  [पूरे जवाब को वापस मॉडल को भेजें](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#step-4). ऐसा अगले टर्न में करें.
- सिग्नेचर वाले हिस्सों को एक साथ न जोड़ें.
- बिना हस्ताक्षर वाले हिस्से को हस्ताक्षर वाले हिस्से के साथ न मिलाएं.

## कीमत

सोचने की सुविधा चालू होने पर, जवाब की कीमत आउटपुट टोकन और सोचने के लिए इस्तेमाल किए गए टोकन के योग के बराबर होती है. `thoughtsTokenCount` फ़ील्ड से, जनरेट किए गए थिंकिंग टोकन की कुल संख्या मिल सकती है.

### Python

```
# ...
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### ऐप पर जाएं

```
// ...
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println("Thoughts tokens:", string(usageMetadata.thoughts_token_count))
fmt.Println("Output tokens:", string(usageMetadata.candidates_token_count))
```

थिंकिंग मॉडल, जवाब की क्वालिटी को बेहतर बनाने के लिए पूरी जानकारी जनरेट करते हैं. इसके बाद, वे [खास जानकारी](#summaries) देते हैं, ताकि यह पता चल सके कि जवाब कैसे जनरेट किया गया. इसलिए, कीमत इस बात पर तय होती है कि खास जानकारी जनरेट करने के लिए, मॉडल को कितने थॉट टोकन जनरेट करने पड़े. भले ही, एपीआई से सिर्फ़ खास जानकारी आउटपुट के तौर पर मिली हो.

[टोकन की गिनती](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) गाइड में, टोकन के बारे में ज़्यादा जानें.

## सबसे सही तरीके

इस सेक्शन में, थिंकिंग मॉडल का असरदार तरीके से इस्तेमाल करने के बारे में कुछ दिशा-निर्देश दिए गए हैं.
हमेशा की तरह, [प्रॉम्प्ट लिखने के बारे में हमारे दिशा-निर्देशों और सबसे सही तरीकों](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi) का पालन करने से आपको सबसे अच्छे नतीजे मिलेंगे.

### डीबग करना और स्टीयर करना

- **जवाब देने के पीछे की वजह की समीक्षा करना**: अगर आपको थिंकिंग मॉडल से अपनी उम्मीद के मुताबिक़ जवाब नहीं मिल रहा है, तो Gemini के जवाब देने के पीछे की वजह की समीक्षा करने से मदद मिल सकती है.
  आपको यह पता चल सकता है कि Gemini ने टास्क को कैसे पूरा किया और नतीजे पर कैसे पहुंचा. साथ ही, इस जानकारी का इस्तेमाल करके, सही नतीजे पाने के लिए किया जा सकता है.
- **जवाब के लिए दिशा-निर्देश देना**: अगर आपको कोई लंबा जवाब चाहिए, तो अपने प्रॉम्प्ट में दिशा-निर्देश दें. इससे मॉडल को [सोचने-समझने](#set-budget) में कम समय लगेगा. इससे आपको अपने जवाब के लिए ज़्यादा टोकन आउटपुट रिज़र्व करने की सुविधा मिलती है.

### टास्क की मुश्किल का लेवल

- **आसान टास्क (सोचने की ज़रूरत नहीं):** ऐसे अनुरोधों के लिए सोचने की ज़रूरत नहीं होती जिनमें जटिल तर्क की ज़रूरत नहीं होती. जैसे, तथ्यों को ढूंढना या उन्हें कैटगरी में बांटना. उदाहरण के लिए:
  - "DeepMind की स्थापना कहाँ हुई थी?"
  - "क्या इस ईमेल में मीटिंग के लिए कहा गया है या सिर्फ़ जानकारी दी गई है?"
- **सामान्य टास्क (डिफ़ॉल्ट/कुछ सोच-विचार):** कई सामान्य अनुरोधों के लिए, चरण-दर-चरण प्रोसेस करने या बेहतर तरीके से समझने की ज़रूरत होती है. Gemini, सोचने की क्षमता का इस्तेमाल इन कामों के लिए कर सकता है:
  - प्रकाश संश्लेषण और बड़े होने की प्रक्रिया के बीच समानताएं बताओ.
  - इलेक्ट्रिक कारों और हाइब्रिड कारों की तुलना करें और उनके बीच अंतर बताएं.
- **मुश्किल टास्क (सोचने की क्षमता सबसे ज़्यादा):** अगर आपको वाकई मुश्किल चुनौतियों का सामना करना है, तो हम आपको सोचने के लिए ज़्यादा बजट सेट करने का सुझाव देते हैं. जैसे, गणित के मुश्किल सवालों को हल करना या कोडिंग के टास्क पूरे करना. इस तरह के टास्क के लिए, मॉडल को अपनी पूरी तर्क क्षमता और प्लानिंग की क्षमताओं का इस्तेमाल करना होता है. जवाब देने से पहले, अक्सर इसमें कई इंटरनल चरण शामिल होते हैं. उदाहरण के लिए:
  - AIME 2025 में समस्या 1 को हल करें: उन सभी पूर्णांक आधारों b > 9 का योग निकालें जिनके लिए 17b, 97b का भाजक है.
  - किसी वेब ऐप्लिकेशन के लिए Python कोड लिखो. यह ऐप्लिकेशन, शेयर बाज़ार के रीयल-टाइम डेटा को विज़ुअलाइज़ करता हो. साथ ही, इसमें उपयोगकर्ता की पुष्टि करने की सुविधा भी शामिल हो. इसे ज़्यादा से ज़्यादा असरदार बनाएँ.

## साथ काम करने वाले मॉडल, टूल, और सुविधाएं

सोचने की क्षमता वाली सुविधाएं, 3 और 2.5 सीरीज़ के सभी मॉडल पर काम करती हैं.
आपको मॉडल की सभी क्षमताओं के बारे में जानकारी, [मॉडल की खास जानकारी](https://ai.google.dev/gemini-api/docs/models?hl=hi) वाले पेज पर मिलेगी.

सोच-समझकर जवाब देने वाले मॉडल, Gemini के सभी टूल और सुविधाओं के साथ काम करते हैं. इससे मॉडल, बाहरी सिस्टम के साथ इंटरैक्ट कर पाते हैं, कोड लागू कर पाते हैं या रीयल-टाइम में जानकारी ऐक्सेस कर पाते हैं. साथ ही, वे अपने तर्क और फ़ाइनल जवाब में नतीजों को शामिल कर पाते हैं.

[सोच-समझकर जवाब देने वाले मॉडल की कुकबुक](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking.ipynb?hl=hi) में, टूल इस्तेमाल करने के उदाहरण देखे जा सकते हैं.

## आगे क्या करना है?

- सोचने की क्षमता से जुड़ी जानकारी, हमारी [OpenAI के साथ काम करने की सुविधा](https://ai.google.dev/gemini-api/docs/openai?hl=hi#thinking) गाइड में उपलब्ध है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-07 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-07 (UTC) को अपडेट किया गया."],[],[]]
