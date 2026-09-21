---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=hi
fetched_at: 2026-09-21T05:43:47.998888+00:00
title: "\u091f\u0947\u0915\u094d\u0938\u094d\u091f \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# टेक्स्ट जनरेट करना

Gemini API, टेक्स्ट, इमेज, वीडियो, और ऑडियो इनपुट से टेक्स्ट आउटपुट जनरेट कर सकता है.

यहां एक सामान्य उदाहरण दिया गया है:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How does AI work?"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "How does AI work?",
  });
  console.log(response.text);
}

await main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Explain how AI works in a few words"),
      nil,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithTextInput {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "How does AI work?", null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'How AI does work?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## Gemini के साथ मिलकर सोचना

Gemini मॉडल में, ["सोचना"](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) मोड डिफ़ॉल्ट रूप से चालू होता है. इससे मॉडल को किसी अनुरोध का जवाब देने से पहले, उस पर विचार करने का समय मिलता है.

हर मॉडल, अलग-अलग थिंकिंग कॉन्फ़िगरेशन के साथ काम करता है. इससे आपको लागत, लेटेन्सी, और इंटेलिजेंस पर कंट्रोल मिलता है. ज़्यादा जानकारी के लिए, [सोचने की गाइड](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#set-budget) देखें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How does AI work?",
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
    model: "gemini-3.8-flash",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    }
  });
  console.log(response.text);
}

await main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("How does AI work?"),
      &genai.GenerateContentConfig{
        ThinkingConfig: &genai.ThinkingConfig{
            ThinkingLevel: &thinkingLevelVal,
        },
      }
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.ThinkingConfig;
import com.google.genai.types.ThinkingLevel;

public class GenerateContentWithThinkingConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config =
        GenerateContentConfig.builder()
            .thinkingConfig(ThinkingConfig.builder().thinkingLevel(new ThinkingLevel("low")))
            .build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "How does AI work?", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
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

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'How AI does work?' },
        ],
      },
    ],
    generationConfig: {
      thinkingConfig: {
        thinkingLevel: 'low'
      }
    }
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## सिस्टम के निर्देश और अन्य कॉन्फ़िगरेशन

सिस्टम के निर्देशों की मदद से, Gemini मॉडल के व्यवहार को कंट्रोल किया जा सकता है. ऐसा करने के लिए,
[`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerationConfig) ऑब्जेक्ट पास करें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko."),
    contents="Hello there"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Hello there",
    config: {
      systemInstruction: "You are a cat. Your name is Neko.",
    },
  });
  console.log(response.text);
}

await main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  config := &genai.GenerateContentConfig{
      SystemInstruction: genai.NewContentFromText("You are a cat. Your name is Neko.", genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Hello there"),
      config,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

public class GenerateContentWithSystemInstruction {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config =
        GenerateContentConfig.builder()
            .systemInstruction(
                Content.fromParts(Part.fromText("You are a cat. Your name is Neko.")))
            .build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "Hello there", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "system_instruction": {
      "parts": [
        {
          "text": "You are a cat. Your name is Neko."
        }
      ]
    },
    "contents": [
      {
        "parts": [
          {
            "text": "Hello there"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const systemInstruction = {
    parts: [{
      text: 'You are a cat. Your name is Neko.'
    }]
  };

  const payload = {
    systemInstruction,
    contents: [
      {
        parts: [
          { text: 'Hello there' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

[`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerationConfig) ऑब्जेक्ट की मदद से, जनरेशन के डिफ़ॉल्ट पैरामीटर भी बदले जा सकते हैं. जैसे, [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerationConfig).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        max_output_tokens=1000
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works",
    config: {
      maxOutputTokens: 1000,
    },
  });
  console.log(response.text);
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
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  config := &genai.GenerateContentConfig{
    MaxOutputTokens:   1000,
    ResponseMIMEType:  "application/json",
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    genai.Text("What is the average size of a swallow?"),
    config,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config = GenerateContentConfig.builder().maxOutputTokens(1000).build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "Explain how AI works", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works"
          }
        ]
      }
    ],
    "generationConfig": {
      "stopSequences": [
        "Title"
      ],
      "maxOutputTokens": 1000
    }
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const generationConfig = {
    maxOutputTokens: 1000,
    responseFormat: { text: { mimeType: "text/plain" } },
  };

  const payload = {
    generationConfig,
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

कॉन्फ़िगर किए जा सकने वाले पैरामीटर और उनके ब्यौरे की पूरी सूची देखने के लिए, हमारे एपीआई रेफ़रंस में [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerationConfig) देखें.

## मल्टीमोडल इनपुट

Gemini API में, टेक्स्ट, इमेज, वीडियो, और ऑडियो, सभी तरह के इनपुट इस्तेमाल किए जा सकते हैं. इससे आपको टेक्स्ट के साथ-साथ मीडिया फ़ाइलें भी इस्तेमाल करने की सुविधा मिलती है. यहां दी गई इमेज में, इमेज उपलब्ध कराने का तरीका दिखाया गया है:

### Python

```
from PIL import Image
from google import genai

client = genai.Client()

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[image, "Tell me about this instrument"]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const image = await ai.files.upload({
    file: "/path/to/organ.png",
  });
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: [
      createUserContent([
        "Tell me about this instrument",
        createPartFromUri(image.uri, image.mimeType),
      ]),
    ],
  });
  console.log(response.text);
}

await main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  imagePath := "/path/to/organ.jpg"
  imgData, _ := os.ReadFile(imagePath)

  parts := []*genai.Part{
      genai.NewPartFromText("Tell me about this instrument"),
      &genai.Part{
          InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imgData,
          },
      },
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

public class GenerateContentWithMultiModalInputs {
  public static void main(String[] args) {

    Client client = new Client();

    Content content =
      Content.fromParts(
          Part.fromText("Tell me about this instrument"),
          Part.fromUri("/path/to/organ.jpg", "image/jpeg"));

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", content, null);

    System.out.println(response.text());
  }
}
```

### REST

```
# Use a temporary file to hold the base64 encoded image data
TEMP_B64=$(mktemp)
trap 'rm -f "$TEMP_B64"' EXIT
base64 $B64FLAGS $IMG_PATH > "$TEMP_B64"

# Use a temporary file to hold the JSON payload
TEMP_JSON=$(mktemp)
trap 'rm -f "$TEMP_JSON"' EXIT

cat > "$TEMP_JSON" << EOF
{
  "contents": [
    {
      "parts": [
        {
          "text": "Tell me about this instrument"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "$(cat "$TEMP_B64")"
          }
        }
      ]
    }
  ]
}
EOF

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d "@$TEMP_JSON"
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const imageUrl = 'https://example.com/image.jpg';
  const image = getImageData(imageUrl);
  const payload = {
    contents: [
      {
        parts: [
          { image },
          { text: 'Tell me about this instrument' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}

function getImageData(url) {
  const blob = UrlFetchApp.fetch(url).getBlob();

  return {
    mimeType: blob.getContentType(),
    data: Utilities.base64Encode(blob.getBytes())
  };
}
```

इमेज उपलब्ध कराने के अन्य तरीकों और इमेज प्रोसेसिंग के ज़्यादा बेहतर तरीके के बारे में जानने के लिए, [इमेज समझने से जुड़ी हमारी गाइड](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi) देखें.
यह एपीआई, [दस्तावेज़](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi), [वीडियो](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi), और [ऑडियो](https://ai.google.dev/gemini-api/docs/audio?hl=hi) इनपुट को भी समझ सकता है.

## जवाब स्ट्रीम करना

डिफ़ॉल्ट रूप से, मॉडल जवाब सिर्फ़ तब देता है, जब जनरेट करने की पूरी प्रोसेस पूरी हो जाती है.

बेहतर इंटरैक्शन के लिए, स्ट्रीमिंग का इस्तेमाल करें. इससे जनरेट होने वाले [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerateContentResponse) इंस्टेंस, आपको धीरे-धीरे मिलते रहेंगे.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works",
  });

  for await (const chunk of response) {
    console.log(chunk.text);
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
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  stream := client.Models.GenerateContentStream(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Write a story about a magic backpack."),
      nil,
  )

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentStream {
  public static void main(String[] args) {

    Client client = new Client();

    ResponseStream<GenerateContentResponse> responseStream =
      client.models.generateContentStream(
          "gemini-3.8-flash", "Write a story about a magic backpack.", null);

    for (GenerateContentResponse res : responseStream) {
      System.out.print(res.text());
    }

    // To save resources and avoid connection leaks, it is recommended to close the response
    // stream after consumption (or using try block to get the response stream).
    responseStream.close();
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## सिलसिलेवार बातचीत (चैट)

हमारे SDK, चैट में कई राउंड के प्रॉम्प्ट और जवाब इकट्ठा करने की सुविधा देते हैं. इससे आपको बातचीत के इतिहास को आसानी से ट्रैक करने में मदद मिलती है.

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.8-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.8-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const response1 = await chat.sendMessage({
    message: "I have 2 dogs in my house.",
  });
  console.log("Chat response 1:", response1.text);

  const response2 = await chat.sendMessage({
    message: "How many paws are in my house?",
  });
  console.log("Chat response 2:", response2.text);
}

await main();
```

### ऐप पर जाएं

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  history := []*genai.Content{
      genai.NewContentFromText("Hi nice to meet you! I have 2 dogs in my house.", genai.RoleUser),
      genai.NewContentFromText("Great to meet you. What would you like to know?", genai.RoleModel),
  }

  chat, _ := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
  res, _ := chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})

  if len(res.Candidates) > 0 {
      fmt.Println(res.Candidates[0].Content.Parts[0].Text)
  }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversation {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.8-flash");

    GenerateContentResponse response =
        chatSession.sendMessage("I have 2 dogs in my house.");
    System.out.println("First response: " + response.text());

    response = chatSession.sendMessage("How many paws are in my house?");
    System.out.println("Second response: " + response.text());

    // Get the history of the chat session.
    // Passing 'true' to getHistory() returns the curated history, which excludes
    // empty or invalid parts.
    // Passing 'false' here would return the comprehensive history, including
    // empty or invalid parts.
    ImmutableList<Content> history = chatSession.getHistory(true);
    System.out.println("History: " + history);
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Great to meet you. What would you like to know?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "I have two dogs in my house. How many paws are in my house?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        role: 'user',
        parts: [
          { text: 'Hello' },
        ],
      },
      {
        role: 'model',
        parts: [
          { text: 'Great to meet you. What would you like to know?' },
        ],
      },
      {
        role: 'user',
        parts: [
          { text: 'I have two dogs in my house. How many paws are in my house?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

स्ट्रीमिंग का इस्तेमाल, सिलसिलेवार बातचीत के लिए भी किया जा सकता है.

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.8-flash")

response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")

response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")

for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.8-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const stream1 = await chat.sendMessageStream({
    message: "I have 2 dogs in my house.",
  });
  for await (const chunk of stream1) {
    console.log(chunk.text);
    console.log("_".repeat(80));
  }

  const stream2 = await chat.sendMessageStream({
    message: "How many paws are in my house?",
  });
  for await (const chunk of stream2) {
    console.log(chunk.text);
    console.log("_".repeat(80));
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
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  history := []*genai.Content{
      genai.NewContentFromText("Hi nice to meet you! I have 2 dogs in my house.", genai.RoleUser),
      genai.NewContentFromText("Great to meet you. What would you like to know?", genai.RoleModel),
  }

  chat, _ := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
  stream := chat.SendMessageStream(ctx, genai.Part{Text: "How many paws are in my house?"})

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversationWithStreaming {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.8-flash");

    ResponseStream<GenerateContentResponse> responseStream =
        chatSession.sendMessageStream("I have 2 dogs in my house.", null);

    for (GenerateContentResponse response : responseStream) {
      System.out.print(response.text());
    }

    responseStream = chatSession.sendMessageStream("How many paws are in my house?", null);

    for (GenerateContentResponse response : responseStream) {
      System.out.print(response.text());
    }

    // Get the history of the chat session. History is added after the stream
    // is consumed and includes the aggregated response from the stream.
    System.out.println("History: " + chatSession.getHistory(false));
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent?alt=sse \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Great to meet you. What would you like to know?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "I have two dogs in my house. How many paws are in my house?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        role: 'user',
        parts: [
          { text: 'Hello' },
        ],
      },
      {
        role: 'model',
        parts: [
          { text: 'Great to meet you. What would you like to know?' },
        ],
      },
      {
        role: 'user',
        parts: [
          { text: 'I have two dogs in my house. How many paws are in my house?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## प्रॉम्प्ट लिखने से जुड़ी सलाह

Gemini का ज़्यादा से ज़्यादा फ़ायदा पाने के लिए, हमारी [प्रॉम्प्ट इंजीनियरिंग गाइड](https://ai.google.dev/gemini/docs/prompting-strategies?hl=hi) देखें.

## आगे क्या करना है

- [Google AI Studio में Gemini](https://aistudio.google.com?hl=hi) को आज़माएं.
- JSON जैसे जवाबों के लिए, [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) की सुविधा आज़माएं.
- Gemini की [इमेज](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi), [वीडियो](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi), [ऑडियो](https://ai.google.dev/gemini-api/docs/audio?hl=hi), और [दस्तावेज़](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi) को समझने की क्षमताओं के बारे में जानें.
- मल्टीमॉडल [फ़ाइल प्रॉम्प्ट करने की रणनीतियों](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide) के बारे में जानें.

## कॉन्टेंट जनरेट करना

यह मॉडल को प्रॉम्प्ट भेजने के लिए मुख्य एंडपॉइंट है. कॉन्टेंट जनरेट करने के लिए, दो एंडपॉइंट उपलब्ध हैं. इनमें मुख्य अंतर यह है कि आपको जवाब कैसे मिलता है:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=hi#method:-models.generatecontent)
  (REST)**:
  यह अनुरोध स्वीकार करता है और मॉडल के जवाब जनरेट करने के बाद, एक जवाब देता है.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=hi#method:-models.streamgeneratecontent)
  (एसएसई)**: इसे ठीक वही अनुरोध मिलता है, लेकिन मॉडल जवाब के हिस्सों को जनरेट होने के साथ-साथ स्ट्रीम करता है. इससे इंटरैक्टिव ऐप्लिकेशन के लिए, उपयोगकर्ताओं को बेहतर अनुभव मिलता है. ऐसा इसलिए, क्योंकि इससे आपको तुरंत कुछ नतीजे दिखाने की सुविधा मिलती है.

### अनुरोध के मुख्य हिस्से का स्ट्रक्चर

[अनुरोध का मुख्य हिस्सा](https://ai.google.dev/api/generate-content?hl=hi#request-body) एक JSON ऑब्जेक्ट है. यह स्टैंडर्ड और स्ट्रीमिंग, दोनों मोड के लिए **एक जैसा** होता है. इसे कुछ मुख्य ऑब्जेक्ट से बनाया जाता है:

- [`Content`](https://ai.google.dev/api/caching?hl=hi#Content) ऑब्जेक्ट: यह बातचीत के एक टर्न को दिखाता है.
- [`Part`](https://ai.google.dev/api/caching?hl=hi#Part) ऑब्जेक्ट: `Content` टर्न में मौजूद डेटा का कोई हिस्सा (जैसे, टेक्स्ट या इमेज).
- `inline_data` ([`Blob`](https://ai.google.dev/api/caching?hl=hi#Blob)): यह रॉ मीडिया बाइट और उनके एमआईएमई टाइप के लिए एक कंटेनर होता है.

सबसे ऊपर के लेवल पर, अनुरोध के मुख्य हिस्से में एक `contents` ऑब्जेक्ट होता है. यह `Content` ऑब्जेक्ट की सूची होती है. हर ऑब्जेक्ट, बातचीत के टर्न को दिखाता है. ज़्यादातर मामलों में, बुनियादी टेक्स्ट जनरेट करने के लिए आपके पास एक `Content` ऑब्जेक्ट होगा. हालांकि, अगर आपको बातचीत का इतिहास बनाए रखना है, तो एक से ज़्यादा `Content` ऑब्जेक्ट इस्तेमाल किए जा सकते हैं.

यहां `generateContent` अनुरोध के मुख्य हिस्से का एक सामान्य उदाहरण दिया गया है:

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
          "role": "user",
          "parts": [
              // A list of Part objects goes here
          ]
      },
      {
          "role": "model",
          "parts": [
              // A list of Part objects goes here
          ]
      }
    ]
  }'
```

### जवाब के मुख्य भाग का स्ट्रक्चर

स्ट्रीमिंग और स्टैंडर्ड, दोनों मोड के लिए [जवाब का मुख्य हिस्सा](https://ai.google.dev/api/generate-content?hl=hi#response-body) एक जैसा होता है. हालांकि, इनमें ये अंतर होते हैं:

- स्टैंडर्ड मोड: जवाब के मुख्य हिस्से में [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerateContentResponse) का एक इंस्टेंस होता है.
- स्ट्रीमिंग मोड: जवाब के मुख्य हिस्से में, [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=hi#v1beta.GenerateContentResponse) इंस्टेंस की स्ट्रीम होती है.

जवाब के मुख्य हिस्से में एक `candidates` ऑब्जेक्ट होता है. यह `Candidate` ऑब्जेक्ट की सूची होती है. `Candidate` ऑब्जेक्ट में एक `Content` ऑब्जेक्ट होता है. इसमें मॉडल से मिला जनरेट किया गया जवाब होता है.

## REST API के उदाहरण

### मल्टीमॉडल प्रॉम्प्ट (टेक्स्ट और इमेज)

प्रॉम्प्ट में टेक्स्ट और इमेज, दोनों शामिल करने के लिए, `parts` ऐरे में दो `Part` ऑब्जेक्ट होने चाहिए: एक टेक्स्ट के लिए और दूसरा इमेज `inline_data` के लिए.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{
    "parts":[
        {
            "inline_data": {
            "mime_type":"image/jpeg",
            "data": "/9j/4AAQSkZJRgABAQ... (base64-encoded image)"
            }
        },
        {"text": "What is in this picture?"},
      ]
    }]
  }'
```

### सिलसिलेवार बातचीत (चैट)

कई टर्न वाली बातचीत बनाने के लिए, `contents` ऐरे को कई `Content` ऑब्जेक्ट के साथ तय करें. एपीआई, इस पूरे इतिहास का इस्तेमाल अगले जवाब के लिए कॉन्टेक्स्ट के तौर पर करेगा. हर `Content` ऑब्जेक्ट के लिए `role`, `user` और `model` के बीच बदलता रहना चाहिए.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          { "text": "Hello." }
        ]
      },
      {
        "role": "model",
        "parts": [
          { "text": "Hello! How can I help you today?" }
        ]
      },
      {
        "role": "user",
        "parts": [
          { "text": "Please write a four-line poem about the ocean." }
        ]
      }
    ]
  }'
```

### ज़रूरी बातें

- `Content` एनवलप है: यह मैसेज टर्न के लिए टॉप-लेवल कंटेनर होता है. यह उपयोगकर्ता या मॉडल, किसी का भी हो सकता है.
- `Part` मल्टीमॉडल की सुविधा चालू करता है: अलग-अलग तरह के डेटा (टेक्स्ट, इमेज, वीडियो यूआरआई वगैरह) को एक साथ इस्तेमाल करने के लिए, एक ही `Content` ऑब्जेक्ट में कई `Part` ऑब्जेक्ट का इस्तेमाल करें.
- डेटा ट्रांसफ़र करने का तरीका चुनें:
  - सीधे तौर पर एम्बेड किए गए छोटे मीडिया (जैसे कि ज़्यादातर इमेज) के लिए, `Part` के साथ `inline_data` का इस्तेमाल करें.
  - बड़ी फ़ाइलों या उन फ़ाइलों के लिए जिन्हें आपको कई अनुरोधों में फिर से इस्तेमाल करना है, फ़ाइल अपलोड करने के लिए File API का इस्तेमाल करें. साथ ही, इसे `file_data` पार्ट के साथ रेफ़रंस करें.
- बातचीत के इतिहास को मैनेज करना: REST API का इस्तेमाल करने वाले चैट ऐप्लिकेशन के लिए, `contents` ऐरे बनाएं. इसके लिए, हर टर्न के लिए `Content` ऑब्जेक्ट जोड़ें. साथ ही, `"user"` और `"model"` भूमिकाओं के बीच बारी-बारी से बदलाव करें. अगर एसडीके का इस्तेमाल किया जा रहा है, तो बातचीत के इतिहास को मैनेज करने के सुझाए गए तरीके के लिए, एसडीके के दस्तावेज़ देखें.

## जवाब के उदाहरण

यहां दिए गए उदाहरणों में दिखाया गया है कि अलग-अलग तरह के अनुरोधों के लिए, ये कॉम्पोनेंट एक साथ कैसे काम करते हैं.

### सिर्फ़ टेक्स्ट वाला जवाब

डिफ़ॉल्ट टेक्स्ट रिस्पॉन्स में, एक `candidates` ऐरे होता है. इसमें एक या उससे ज़्यादा `content` ऑब्जेक्ट होते हैं. इनमें मॉडल का जवाब शामिल होता है.

यहां **स्टैंडर्ड** जवाब का एक उदाहरण दिया गया है:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "At its core, Artificial Intelligence works by learning from vast amounts of data ..."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 1
    }
  ],
}
```

यहां **स्ट्रीमिंग** के ज़रिए दिए गए जवाबों की सीरीज़ दी गई है. हर जवाब में एक `responseId` होता है, जिसमें पूरे जवाब की जानकारी होती है:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "The image displays"
          }
        ],
        "role": "model"
      },
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  },
  "modelVersion": "gemini-3.8-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}

...

{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": " the following materials:\n\n*   **Wood:** The accordion and the violin are primarily"
          }
        ],
        "role": "model"
      },
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  }
  "modelVersion": "gemini-3.8-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}
```

## Live API (BidiGenerateContent) WebSockets API

Live API, स्टेटफ़ुल WebSocket पर आधारित एपीआई उपलब्ध कराता है. इससे दोनों दिशाओं में स्ट्रीमिंग की जा सकती है, ताकि रीयल-टाइम स्ट्रीमिंग के इस्तेमाल के उदाहरणों को चालू किया जा सके. ज़्यादा जानकारी के लिए, [Live API की गाइड](https://ai.google.dev/gemini-api/docs/live?hl=hi) और [Live API के बारे में जानकारी](https://ai.google.dev/api/live?hl=hi) देखें.

## खास मॉडल

Gemini API, Gemini के मॉडल के अलावा, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi), [Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi), और [embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) मॉडल जैसे खास मॉडल के लिए एंडपॉइंट उपलब्ध कराता है. मॉडल सेक्शन में जाकर, इन गाइड को देखा जा सकता है.

## प्लैटफ़ॉर्म एपीआई

बाकी एंडपॉइंट, अब तक बताए गए मुख्य एंडपॉइंट के साथ इस्तेमाल करने के लिए अतिरिक्त सुविधाएं चालू करते हैं. ज़्यादा जानने के लिए, गाइड सेक्शन में जाकर [बैच मोड](https://ai.google.dev/gemini-api/docs/batch-mode?hl=hi) और [File API](https://ai.google.dev/gemini-api/docs/files?hl=hi) के बारे में पढ़ें.

## आगे क्या करना है

अगर आपको Gemini API के बारे में ज़्यादा जानकारी नहीं है, तो यहाँ दी गई गाइड पढ़ें. इनसे आपको Gemini API के प्रोग्रामिंग मॉडल को समझने में मदद मिलेगी:

- [Gemini API का इस्तेमाल शुरू करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Gemini मॉडल गाइड](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi)

आपको Gemini API की सुविधाओं के बारे में बताने वाली गाइड भी देखनी चाहिए. इनमें Gemini API की अलग-अलग सुविधाओं के बारे में बताया गया है. साथ ही, कोड के उदाहरण भी दिए गए हैं:

- [टेक्स्ट जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi)
- [कॉन्टेक्स्ट के लिए कैश मेमोरी की सुविधा](https://ai.google.dev/gemini-api/docs/caching?hl=hi)
- [एम्बेडिंग](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया."],[],[]]
