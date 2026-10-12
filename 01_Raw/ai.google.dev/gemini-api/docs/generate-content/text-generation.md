---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=sq
fetched_at: 2026-10-12T06:47:43.256717+00:00
title: "Gjenerimi i tekstit \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash është tani në dispozicion. [Provojeni](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=sq) .

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Gjenerimi i tekstit

Gemini API mund të gjenerojë dalje me tekst nga hyrjet me tekst, imazhe, video dhe audio.

Këtu është një shembull bazë:

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

## Po mendon me Gemini

Modelet e Gemini shpesh kanë të aktivizuar si parazgjedhje ["arsyetimin"](https://ai.google.dev/gemini-api/docs/thinking?hl=sq), i cili e lejon modelin të arsyetojë para se t'i përgjigjet një kërkese.

Çdo model mbështet konfigurime të ndryshme të të menduarit, gjë që të jep kontroll mbi koston, vonesën dhe inteligjencën. Për më shumë detaje, shiko
[udhëzuesin e të menduarit](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=sq#set-budget).

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

## Udhëzimet e sistemit dhe konfigurimet e tjera

Mund të udhëzosh sjelljen e modeleve të Gemini me udhëzimet e sistemit. Për ta bërë këtë, kalo një objekt [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerationConfig)

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

Objekti [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerationConfig)
të lejon gjithashtu të zëvendësosh parametrat e parazgjedhur të gjenerimit, si p.sh.
[`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerationConfig).

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

Referoju [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerationConfig)
në referencën tonë të API-së për një listë të plotë të parametrave të konfigurueshëm dhe
përshkrimet e tyre.

## Hyrjet multimodale

API-ja e Gemini mbështet hyrjet multimodale, duke të të lejuar që të kombinosh tekstin me skedarët e mediave. Shembulli i mëposhtëm demonstron dhënien e një imazhi:

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

Për metoda alternative për të ofruar imazhe dhe për përpunim më të avancuar të imazheve,
shiko [udhëzuesin tonë për kuptimin e imazheve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq).
API-ja mbështet gjithashtu hyrjet dhe të kuptuarit e [dokumenteve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq),
[videove](https://ai.google.dev/gemini-api/docs/video-understanding?hl=sq) dhe
[audios](https://ai.google.dev/gemini-api/docs/audio?hl=sq).

## Përgjigjet e transmetuara

Si parazgjedhje, modeli kthen një përgjigje vetëm pasi të ketë përfunduar i gjithë procesi i gjenerimit.

Për ndërveprime më të rrjedhshme, përdor transmetimin për të marrë
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerateContentResponse)
shembuj në mënyrë shtesë ndërsa gjenerohen.

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

## Bisedat me shumë kthesa (biseda)

SDK-të tona ofrojnë funksionalitetin për të mbledhur disa raunde kërkesash dhe përgjigjesh në një bisedë, duke të të dhënë një mënyrë të lehtë për të mbajtur nën kontroll historikun e bisedës.

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

Transmetimi mund të përdoret gjithashtu për biseda me shumë kthesa.

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

### Go

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

### QETËSI

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

### Skripti i aplikacioneve

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

## Këshilla për kërkesat

Konsulto [udhëzuesin tonë për hartimin e kërkesave](https://ai.google.dev/gemini/docs/prompting-strategies?hl=sq) për sugjerime për të përfituar sa më shumë nga Gemini.

## Çfarë ka më pas

- Provo [Gemini në Google AI Studio](https://aistudio.google.com?hl=sq).
- Eksperimento me [daljet e strukturuara](https://ai.google.dev/gemini-api/docs/structured-output?hl=sq) për përgjigje të ngjashme me JSON.
- Eksploro aftësitë e Gemini për të kuptuar [imazhet](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq),
  [videot](https://ai.google.dev/gemini-api/docs/video-understanding?hl=sq), [audion](https://ai.google.dev/gemini-api/docs/audio?hl=sq)
  dhe [dokumentet](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq).
- Mëso rreth
  [strategjive të kërkesave për skedarë](https://ai.google.dev/gemini-api/docs/files?hl=sq#prompt-guide) multimodalë.

## Gjenerimi i përmbajtjes

Kjo është pika përfundimtare qendrore për dërgimin e kërkesave te modeli. Ka dy pika fundore për gjenerimin e përmbajtjeve. Ndryshimi kryesor është mënyra se si e merr përgjigjen:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=sq#method:-models.generatecontent)
  (REST)**:
  Merr një kërkesë dhe ofron një përgjigje të vetme pasi modeli ka përfunduar gjenerimin e tij të plotë.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=sq#method:-models.streamgeneratecontent)
  (SSE)**: Merr të njëjtën kërkesë, por modeli transmeton përsëri pjesë të përgjigjes ndërsa ato gjenerohen. Kjo ofron një përvojë më të mirë për përdoruesit për aplikacionet interaktive pasi të lejon të shfaqësh menjëherë rezultate të pjesshme.

### Struktura e trupit të kërkesës

[Trupi i kërkesës](https://ai.google.dev/api/generate-content?hl=sq#request-body) është një objekt JSON që është
**identik** për modalitetet standard dhe të transmetimit dhe është ndërtuar nga disa objekte
themelore:

- Objekti [`Content`](https://ai.google.dev/api/caching?hl=sq#Content): Përfaqëson një kthesë të vetme në një bisedë.
- Objekti [`Part`](https://ai.google.dev/api/caching?hl=sq#Part): Një pjesë e të dhënave brenda një kthese të `Content`
  (si teksti ose një imazh).
- `inline_data` ([`Blob`](https://ai.google.dev/api/caching?hl=sq#Blob)): Një kontejner për bajtet e medias së papërpunuar
  dhe llojin e tyre MIME.

Në nivelin më të lartë, trupi i kërkesës përmban një objekt `contents`, i cili është një listë e objekteve `Content`, secili prej të cilëve përfaqëson radhët në bisedë. Në shumicën e rasteve, për gjenerimin bazë të tekstit, do të kesh një objekt të vetëm `Content`, por nëse dëshiron të mbash historikun e bisedave, mund të përdorësh disa objekte `Content`.

Më poshtë tregohet një trup tipik i kërkesës `generateContent`:

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

### Struktura e trupit të përgjigjes

[Trupi i përgjigjes](https://ai.google.dev/api/generate-content?hl=sq#response-body) është i ngjashëm për të dyja modalitetet e transmetimit dhe standarde, përveç sa më poshtë:

- Modaliteti standard: Trupi i përgjigjes përmban një shembull të
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerateContentResponse).
- Modaliteti i transmetimit: Trupi i përgjigjes përmban një transmetim të
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerateContentResponse)
  rasteve.

Në nivel të lartë, trupi i përgjigjes përmban një objekt `candidates`, i cili është një listë e objekteve `Candidate`. Objekti `Candidate` përfshin një objekt `Content`
që ka përgjigjen e gjeneruar të kthyer nga modeli.

## Shembuj të REST API

### Kërkesë multimodale (tekst dhe imazh)

Për të ofruar tekst dhe një imazh në një kërkesë, vargu `parts` duhet të përmbajë dy objekte `Part`: një për tekstin dhe një për imazhin `inline_data`.

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

### Bisedat me shumë kthesa (biseda)

Për të ndërtuar një bisedë me shumë kthesa, ti përcakton një grup `contents` me shumë objekte `Content`. API-ja do ta përdorë të gjithë këtë historik si kontekst
për përgjigjen e radhës. `role` për çdo objekt `Content` duhet të alternohet
midis `user` dhe `model`.

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

### Pikat kryesore

- `Content` është zarfi: Është kontejneri i nivelit të lartë për një kthesë të mesazhit, pavarësisht nëse është nga përdoruesi apo modeli.
- `Part` mundëson modalitetin e shumëfishtë: Përdor disa objekte të `Part` brenda një objekti të vetëm të `Content` për të kombinuar lloje të ndryshme të dhënash (tekst, imazh, URI videoje etj.).
- Zgjidh metodën tënde të të dhënave:
  - Për media të vogla të integruara drejtpërdrejt (si shumica e imazheve), përdor një `Part` me
    `inline_data`.
  - Për skedarë më të mëdhenj ose skedarë që dëshiron të ripërdorësh nëpër kërkesa, përdor File API për të ngarkuar skedarin dhe referoju atij me një pjesë `file_data`.
- Menaxho historikun e bisedave: Për aplikacionet e bisedës që përdorin API-në REST, krijo
  masivin `contents` duke shtuar objekte `Content` për çdo radhë,
  duke alternuar rolet e `"user"` dhe `"model"`. Nëse po përdor një SDK, referoju dokumentacionit të SDK-së për mënyrën e rekomanduar për të menaxhuar historikun e bisedave.

## Shembuj të përgjigjeve

Shembujt e mëposhtëm tregojnë se si këta komponentë bashkohen për lloje të ndryshme kërkesash.

### Përgjigje vetëm me tekst

Një përgjigje e parazgjedhur me tekst përbëhet nga një matricë `candidates` me një ose më shumë objekte `content` që përmbajnë përgjigjen e modelit.

Më poshtë është një shembull i një përgjigjeje **standarde**:

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

Në vijim është një seri përgjigjesh **me transmetim**. Çdo përgjigje përmban një
`responseId` që i lidh të gjitha përgjigjet së bashku:

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

## API-ja e drejtpërdrejtë (BidiGenerateContent) WebSockets API

Live API ofron një API me gjendje të bazuar në WebSocket për transmetim në dy drejtime për të mundësuar raste përdorimi të transmetimit në kohë reale. Mund të rishikosh
[udhëzuesin e API-së së transmetimit të drejtpërdrejtë](https://ai.google.dev/gemini-api/docs/live?hl=sq) dhe [referencën e API-së së transmetimit të drejtpërdrejtë](https://ai.google.dev/api/live?hl=sq)
për më shumë detaje.

## Modelet e specializuara

Përveç familjes së modeleve të Gemini, Gemini API ofron pika fundore për modele të specializuara si [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=sq),
[Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=sq) dhe
[modelet e integrimit](https://ai.google.dev/gemini-api/docs/embeddings?hl=sq). Mund t'i shikosh këta udhëzues te seksioni "Modelet".

## API-të e platformës

Pjesa tjetër e pikave fundore aktivizojnë aftësi shtesë për t'u përdorur me pikat fundore kryesore të përshkruara deri tani. Shiko temat
[Modaliteti i grupeve](https://ai.google.dev/gemini-api/docs/batch-mode?hl=sq) dhe
[API-ja e skedarëve](https://ai.google.dev/gemini-api/docs/files?hl=sq) në seksionin "Udhëzuesit" për të mësuar më shumë.

## Çfarë ka më pas

Nëse sapo ke filluar, shiko udhëzuesit e mëposhtëm, të cilët do të të ndihmojnë të kuptosh modelin e programimit të Gemini API:

- [Udhëzuesi i fillimit për Gemini API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Udhëzuesi për modelin e Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=sq)

Mund të dëshirosh gjithashtu të shikosh udhëzuesit e aftësive, të cilët prezantojnë veçori të ndryshme të Gemini API dhe ofrojnë shembuj kodesh:

- [Gjenerimi i tekstit](https://ai.google.dev/gemini-api/docs/text-generation?hl=sq)
- [Ruajtja në memorien specifike e kontekstit](https://ai.google.dev/gemini-api/docs/caching?hl=sq)
- [Integrimet](https://ai.google.dev/gemini-api/docs/embeddings?hl=sq)

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-09 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-09 UTC."],[],[]]
