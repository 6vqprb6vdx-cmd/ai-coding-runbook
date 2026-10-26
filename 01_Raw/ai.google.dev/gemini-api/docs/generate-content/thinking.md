---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=sq
fetched_at: 2026-10-26T05:40:21.509561+00:00
title: "Gemini po mendon \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Gemini po mendon

[Modelet e Gemini](https://ai.google.dev/gemini-api/docs/models?hl=sq) përdorin një "proces të brendshëm të të menduarit" që përmirëson ndjeshëm aftësitë e tyre të arsyetimit dhe planifikimit me shumë hapa, duke i bërë ato shumë efikase për detyra komplekse si kodimi, matematika e përparuar dhe analiza e të dhënave.

Ky udhëzues të tregon se si të punosh me aftësitë e të menduarit të Gemini duke përdorur Gemini API.

## Po gjenerohet përmbajtja me arsyetimin

Nisja e një kërkese me një model arsyetues është e ngjashme me çdo kërkesë tjetër për gjenerim përmbajtjesh. Dallimi kryesor qëndron në specifikimin e një prej
[modeleve me mbështetje për të menduarit](#tools) në fushën `model`, siç tregohet në shembullin e mëposhtëm të
[gjenerimit të tekstit](https://ai.google.dev/gemini-api/docs/text-generation?hl=sq):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

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
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
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
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Përmbledhjet e mendimeve

Përmbledhjet e mendimeve janë versione të përmbledhura të mendimeve të papërpunuara të modelit dhe ofrojnë njohuri për procesin e arsyetimit të brendshëm të modelit. Ki parasysh se nivelet e të menduarit dhe buxhetet zbatohen për mendimet e papërpunuara të modelit dhe jo për përmbledhjet e mendimeve.

Mund t'i aktivizosh përmbledhjet e mendimeve duke caktuar `includeThoughts` në `true` në konfigurimin e kërkesës sate. Më pas mund të qasesh te përmbledhja duke përsëritur nëpërmjet parametrit `response` `parts` dhe duke kontrolluar vlerën boolean `thought`.

Këtu është një shembull që demonstron se si të aktivizosh dhe të marrësh përmbledhjet e mendimeve
pa transmetim, i cili kthen një përmbledhje të vetme përfundimtare të mendimeve me
përgjigjen:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Go

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
  model := "gemini-3.8-flash"
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

Dhe këtu është një shembull duke përdorur "të menduarit me transmetim", i cili kthen përmbledhje të vazhdueshme dhe të shtuara gjatë gjenerimit:

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Go

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
  model := "gemini-3.8-flash"

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

## Kontrollimi i arsyetimit

Modelet e Gemini angazhohen në mendim dinamik si parazgjedhje, duke rregulluar automatikisht sasinë e përpjekjes për arsyetimin bazuar në kompleksitetin e kërkesës së përdoruesit.
Megjithatë, nëse ke kufizime specifike të vonesës ose kërkon që modeli të angazhohet në arsyetim më të thellë se zakonisht, mund të përdorësh si opsion parametrat për të kontrolluar sjelljen e të menduarit.

### Nivelet e arsyetimit (Gemini 4 dhe Gemini 3)

Parametri `thinkingLevel`, i kërkuar për modelet Gemini 4 dhe i rekomanduar për modelet Gemini 3, të lejon të kontrollosh sjelljen e arsyetimit. Gemini 4 (`gemini-4-argon`) mbështet `low`, `medium` (parazgjedhur) dhe `high`.

Tabela e mëposhtme jep detaje për cilësimet e `thinkingLevel` për çdo lloj modeli:

| Niveli i arsyetimit | Gemini 3.8 Flash | Gemini 3.6 Flash | Gemini 4 Argon | Gemini 3.5 dhe 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Gemini Robotics ER 2 | Përshkrimi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Nuk mbështetet (gabim) | Mbështetur | Nuk mbështetet (gabim) | Mbështetur (Parazgjedhja) | Mbështetur (Parazgjedhja) | Mbështetur | Mbështetet | Përputhet me cilësimin "pa arsyetim" për shumicën e kërkesave. Ki parasysh se `minimal` nuk garanton që mendimi është i çaktivizuar, pasi modeli mund të arsyetojë në mënyrë shumë minimale për detyrat komplekse. |
| **`low`** | Mbështetet | Mbështetur | Mbështetur | Mbështetur | Nuk mbështetet | Mbështetet | Mbështetur | Minimizon vonesën dhe koston. |
| **`medium`** | Mbështetur (Parazgjedhja) | Mbështetet (parazgjedhje) | Mbështetur (Parazgjedhja) | Mbështetur | Nuk mbështetet | Mbështetet | Mbështetet | Arsyetim i balancuar për shumicën e detyrave. |
| **`high`** | Mbështetur (Dinamike) | Mbështetet (Dinamike) | Mbështetet (Dinamike) | Mbështetet (Dinamike) | Mbështetet (Dinamike) | Mbështetet (parazgjedhje, dinamike) | Mbështetet (parazgjedhje, dinamike) | Maksimizon thellësinë e arsyetimit. Modelit mund t'i duhet shumë më tepër kohë për të arritur një shenjë të parë dalëse (jo të menduar), por dalja do të jetë më e arsyetuar me kujdes. |

Shembulli i mëposhtëm tregon se si të caktosh nivelin e arsyetimit.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Go

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
  model := "gemini-3.8-flash"
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

Nuk mund ta çaktivizosh arsyetimin për Gemini 4 Argon. Gemini 3 Flash dhe Flash-Lite
gjithashtu nuk mbështesin çaktivizimin e plotë të arsyetimit.
Nëse nuk specifikon një nivel arsyetimi, Gemini do të përdorë nivelin e parazgjedhur të arsyetimit të modelit (p.sh. `"medium"` për Gemini 4 Argon, Gemini 3.8 Flash dhe Gemini 3.6 Flash).

Modelet e serisë Gemini 2.5 nuk e mbështesin `thinkingLevel`; përdor `thinkingBudget` në vend të kësaj.

### Kufijtë e kodeve dhe `max_output_tokens`

Parametri i gjenerimit [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=sq#v1beta.GenerationConfig)
cakton numrin maksimal të token-ëve që mund të gjenerojë një përgjigje,
duke përfshirë token-ët e mendimit.

Kur caktohet, ky parametër vepron si një kufi i prerë i zbatuar nga infrastruktura
pa ndryshuar mënyrën se si modeli e cakton buxhetin e tij të arsyetimit
(`thinking_level`).

Nëse modeli e arrin këtë kufi gjatë arsyetimit, ai ndalon së gjeneruari me
`finish_reason: MAX_TOKENS` dhe kthen një dalje të shkurtuar ose bosh (ndërkohë që vazhdon të faturojë për çdo kod të gjeneruar të të menduarit). Për të reduktuar koston ose vonesën pa i shkurtuar përgjigjet, ul `thinking_level` (`low` ose `medium`) në vend që të caktosh një `max_output_tokens` të vogël.

Për modelet e Gemini 4 (`gemini-4-argon`), ki parasysh kufijtë e mëposhtëm të kontekstit dhe nxjerrjes:

- **Dritare kontekstuale e ndarë me 1 milion kode:** Tokenët e hyrjes, të të menduarit dhe të daljes ndajnë një dritare të vetme kontekstuale me 1 milion kode (`1,048,576` tokenë). Nëse tokenët e hyrjes plus `max_output_tokens` tejkalojnë 1 048 576 tokenë, API-ja kufizon automatikisht kufirin e daljes në hapësirën e mbetur në dritaren kontekstuale (`1,048,576` minus tokenët e hyrjes).
- **Kufijtë e daljes për kërkesë (64 K për transmetim / 32 K për jo transmetim) dhe dekodimi i gjatë (deri në 1 milion tokenë):** Një kërkesë e vetme transmetimi (`streamGenerateContent`) kthen deri në `65,536` tokenë dhe një kërkesë e vetme jo transmetimi (`generateContent`) kthen deri në `32,768` tokenë. Për të gjeneruar përtej kufirit për kërkesë (deri në `1,048,576` tokena minus hyrjen tënde), cakto `max_output_tokens` mbi kufirin. SDK-të më të fundit të GenAI të Google vazhdojnë nëpër hapa automatikisht si parazgjedhje (`automatic_continuation=True`) ose mund të ekzekutosh një cikël klienti duke përdorur `continuation_token` që kthehet kur një hap ndalon me `finish_reason: "CONTINUATION"`. Shiko [Dekodimin e gjatë](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=sq) për shembuj të kodit.

### Buxhetet e arsyetimit

Parametri `thinkingBudget`, i prezantuar me serinë Gemini 2.5, e udhëzon
modelin për numrin specifik të tokenave të arsyetimit që do të përdoren për arsyetimin.

Më poshtë janë detajet e konfigurimit të `thinkingBudget` për çdo lloj modeli.
Mund ta çaktivizosh arsyetimin duke e caktuar `thinkingBudget` në 0.
Caktimi i `thinkingBudget` në -1 aktivizon **mendimin dinamik**, që do të thotë se modeli do ta rregullojë buxhetin bazuar në kompleksitetin e kërkesës.

| Modeli | Cilësimi i parazgjedhur (Buxheti i të menduarit nuk është caktuar) | Intervali | Çaktivizo arsyetimin | Aktivizo arsyetimin dinamik |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Mendimi dinamik | `128` - `32768` | N/A: Arsyetimi nuk mund të çaktivizohet | `thinkingBudget = -1` (parazgjedhja) |
| **2.5 Flash** | Mendimi dinamik | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (parazgjedhja) |
| **2.5 Flash Preview** | Mendimi dinamik | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (parazgjedhja) |
| **2.5 Flash Lite** | Modeli nuk mendon | `512` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Modeli nuk mendon | `512` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Versioni paraprak** | Mendimi dinamik | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (parazgjedhja) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Mendimi dinamik | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (parazgjedhja) |

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

### Go

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

Në varësi të kërkesës, modeli mund të tejkalojë ose të mos arrijë buxhetin e tokenëve.

## Nënshkrimet e mendimeve

Gemini API është pa gjendje, kështu që modeli e trajton çdo kërkesë të API-së në mënyrë të pavarur dhe nuk ka qasje në kontekstin e mendimit nga hapat e mëparshëm në ndërveprimet me disa hapa.

Për të bërë të mundur ruajtjen e kontekstit të mendimit në ndërveprimet me disa hapa,
Gemini kthen nënshkrimet e mendimit, të cilat janë paraqitje të enkriptuara të
procesit të brendshëm të mendimit të modelit.

- **Modelet Gemini 2.5** kthejnë nënshkrime të mendimeve kur është aktivizuar të menduarit dhe
  kërkesa përfshin [thirrjen e funksioneve](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq#thinking),
  në mënyrë specifike [deklaratat e funksioneve](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq#step-2).
- **Modelet Gemini 4 dhe Gemini 3** mund të kthejnë nënshkrime të mendimeve për të gjitha llojet e [pjesëve](https://ai.google.dev/api/caching?hl=sq#Part). Ne rekomandojmë që t'i kalosh gjithmonë të gjitha nënshkrimet
  siç i ke marrë, por kjo është *e detyrueshme* për nënshkrimet e thirrjeve të funksioneve. Lexo
  faqen
  [Nënshkrimet e mendimeve](https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=sq)
  për të mësuar më shumë.

Kufizime të tjera të përdorimit që duhet të merren parasysh me thirrjen e funksionit përfshijnë:

- Nënshkrimet kthehen nga modeli brenda pjesëve të tjera në përgjigje,
  për shembull pjesët e thirrjes së funksionit ose të tekstit.
  [Kthe të gjithë përgjigjen](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq#step-4)
  me të gjitha pjesët mbrapsht te modeli në radhët vijuese.
- Mos i bashko pjesët me nënshkrimet së bashku.
- Mos bashko një pjesë me nënshkrim me një pjesë tjetër pa nënshkrim.

## Çmimet

Kur arsyetimi është i aktivizuar, çmimi i përgjigjes është shuma e token-ave të daljes dhe token-ave të arsyetimit. Mund të marrësh numrin total të kodeve të gjeneruara të mendimit nga fusha `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Modelet e "Arsyetuesit" gjenerojnë mendime të plota për të përmirësuar cilësinë e përgjigjes përfundimtare dhe më pas nxjerrin [përmbledhje](#summaries) për të ofruar njohuri për procesin e të menduarit. Pra, çmimi bazohet në xhetonët e plotë të mendimit që modeli duhet të gjenerojë për të krijuar një përmbledhje, pavarësisht se vetëm përmbledhja nxirret nga API-ja.

Mund të mësosh më shumë rreth tokenëve në udhëzuesin për [Numërimin e tokenëve](https://ai.google.dev/gemini-api/docs/tokens?hl=sq).

## Praktikat më të mira

Ky seksion përfshin disa udhëzime për përdorimin e modeleve arsyetuese në mënyrë efikase.
Si gjithmonë, ndjekja e
[udhëzimeve dhe praktikave tona më të mira për kërkesat](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=sq)
do të të japë rezultatet më të mira.

### Korrigjimi i gabimeve dhe drejtimi

- **Rishiko arsyetimin**: Kur nuk merr përgjigjen e pritshme nga modelet e të menduarit, mund të të ndihmojë të analizosh me kujdes përmbledhjet e të menduarit të Gemini.
  Mund të shikosh se si e ka ndarë detyrën dhe si ka arritur në përfundimin e saj dhe t'i përdorësh ato informacione për të korrigjuar drejt rezultateve të duhura.
- **Jep udhëzime për arsyetimin**: Nëse po pret një rezultat veçanërisht të gjatë, mund të të duhet të japësh udhëzime në kërkesën tënde për të kufizuar [sasinë e arsyetimit](#set-budget) që përdor modeli. Kjo të lejon të rezervosh më shumë
  nga rezultati i xhetonit për përgjigjen tënde.

### Kompleksiteti i detyrës

- **Detyrat e lehta (Arsyetimi mund të jetë JOAKTIV):** Për kërkesat e thjeshta ku nuk kërkohet arsyetim kompleks, si p.sh. marrja e fakteve ose klasifikimi, arsyetimi nuk kërkohet. Disa shembuj janë:
  - "Ku është themeluar DeepMind?"
  - "A po kërkon ky email një takim apo thjesht po jep informacione?"
- **Detyrat e mesme (parazgjedhja/pak arsyetim):** Shumë kërkesa të zakonshme përfitojnë nga një<0x0Anivel i përpunimit hap pas hapi ose nga një kuptim më i thellë. Gemini mund të përdorë në mënyrë fleksibël aftësinë e të menduarit për detyra të tilla si:
  - Bëj analogjinë e fotosintezës dhe rritjes.
  - Krahaso makinat elektrike dhe makinat hibride.
- **Detyrat e vështira (kapaciteti maksimal i arsyetimit):** Për sfidat vërtet komplekse,
  si p.sh. zgjidhja e problemeve komplekse matematikore ose detyrat e kodimit, ne rekomandojmë të caktosh
  një buxhet të lartë arsyetimi. Këto lloje detyrash kërkojnë që modeli të përdorë aftësitë e tij të plota të arsyetimit dhe planifikimit, duke përfshirë shpesh shumë hapa të brendshëm para se të japë një përgjigje. Disa shembuj janë:
  - Zgjidh problemin 1 në AIME 2025: Gjej shumën e të gjitha bazave të numrave të plotë b > 9 për të cilat 17b është një pjesëtues i 97b.
  - Shkruaj kodin në Python për një aplikacion uebi që vizualizon të dhënat e tregut të aksioneve në kohë reale, duke përfshirë vërtetimin e përdoruesit. Bëje sa më efikas të jetë e mundur.

## Modelet, veglat dhe aftësitë e mbështetura

Veçoritë e arsyetimit mbështeten në të gjitha modelet e serive 4, 3 dhe 2.5.
Mund t'i gjesh të gjitha aftësitë e modelit në faqen e
[përmbledhjes së modelit](https://ai.google.dev/gemini-api/docs/models?hl=sq).

Modelet arsyetuese funksionojnë me të gjitha veglat dhe aftësitë e Gemini. Kjo i lejon modelet të ndërveprojnë me sistemet e jashtme, të ekzekutojnë kodin ose të qasen në informacione në kohë reale, duke i përfshirë rezultatet në arsyetimin dhe përgjigjen e tyre përfundimtare.

Mund të provosh shembuj të përdorimit të veglave me modelet arsyetuese në [Libri i gatimit i arsyetimit][Colab].

## Çfarë ka më pas?

- Mbulimi i arsyetimit ofrohet në udhëzuesin tonë për
  [Përputhshmërinë me OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=sq#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-14 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-14 UTC."],[],[]]
