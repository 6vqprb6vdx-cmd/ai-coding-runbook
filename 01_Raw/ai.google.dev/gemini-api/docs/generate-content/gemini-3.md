---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=sq
fetched_at: 2026-11-02T07:03:23.323347+00:00
title: "Udh\u00ebzuesi i zhvilluesit t\u00eb Gemini 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)

Dërgo komente

# Udhëzuesi i zhvilluesit të Gemini 3

Gemini 3 është familja jonë më inteligjente e modeleve deri më sot, e ndërtuar mbi bazën e arsyetimit të nivelit më të lartë. Ai është krijuar për t'i dhënë jetë çdo ideje duke zotëruar flukset e punës agjentike, kodimin autonom dhe detyrat komplekse me shumë modalitete.
Ky udhëzues mbulon veçoritë kryesore të familjes së modeleve Gemini 3 dhe se si të përfitosh sa më shumë prej tyre.

[Provo "Versionin paraprak" të Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=sq)
[Provo "Versionin paraprak" të Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=sq)
[Provo Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=sq)
[Provo Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=sq)

Eksploro [koleksionin tonë të aplikacioneve të Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=sq) për të parë se si modeli administron arsyetimin e përparuar, kodimin autonom dhe detyrat komplekse multimodale.

Fillo me disa rreshta kodi:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Njihu me serinë Gemini 3

Gemini 3.1 Pro është më i miri për detyra komplekse që kërkojnë njohuri të gjera për botën dhe arsyetim të përparuar nëpër modalitete.

Gemini 3 Flash është modeli ynë më i fundit i serisë 3, me inteligjencë të nivelit Pro me shpejtësinë dhe çmimin e Flash.

Nano Banana Pro (i njohur edhe si Gemini 3 Pro Image) është modeli ynë i gjenerimit të imazheve me cilësinë më të lartë dhe Nano Banana 2 (i njohur edhe si Gemini 3.1 Flash Image) është njëkuivalent me volum të lartë, efikasitet të lartë dhe me çmim më të ulët.

Gemini 3.1 Flash-Lite është modeli ynë i fuqishëm i krijuar për efikasitetin e kostos dhe detyrat me volum të lartë.

| ID-ja e modelit | Dritarja kontekstuale (brenda / jashtë) | Kufiri kohor i njohurive | Çmimi (hyrja / dalja)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Janar 2025 | $0.25 (tekst, imazh, video), $0.50 (audio) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | Janar 2025 | $0.25 (Hyrja e tekstit) / $0.067 (Dalja e imazhit)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Janar 2025 | 2 USD / 12 USD (<200 000 tokenë)   4 USD / 18 USD (>200 000 tokenë) |
| **gemini-3-flash-preview** | 1M / 64k | Janar 2025 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65k / 32k | Janar 2025 | $2 (hyrja e tekstit) / $0,134 (dalja e imazhit)\*\* |

*\* Çmimi është për 1 milion tokenë, përveçse nëse shënohet ndryshe.*
*\*\* Çmimi i imazhit varion sipas rezolucionit. Shiko [faqen e çmimeve](https://ai.google.dev/gemini-api/docs/pricing?hl=sq) për detaje.*

Për kufijtë e detajuar, çmimet dhe informacionet shtesë, shiko
[faqen e modeleve](https://ai.google.dev/gemini-api/docs/models/gemini?hl=sq).

## Veçori të reja të API-së në Gemini 3

Gemini 3 prezanton parametra të rinj të projektuar për t'u dhënë zhvilluesve më shumë kontroll mbi vonesën, koston dhe besnikërinë e modaliteteve të ndryshme.

### Niveli i arsyetimit

Modelet e serisë Gemini 3 përdorin si parazgjedhje të menduarit dinamik për të arsyetuar nëpërmjet kërkesave. Mund të përdorësh parametrin `thinking_level`, i cili kontrollon thellësinë
**maksimale** të procesit të arsyetimit të brendshëm të modelit para se të prodhojë një përgjigje. Gemini 3 i trajton këto nivele si lejime relative për të menduarit
në vend të garancive të rrepta për tokenat.

Nëse `thinking_level` nuk specifikohet, Gemini 3 do të kalojë si parazgjedhje te `high`. Për përgjigje më të shpejta me më pak vonesë kur nuk kërkohet arsyetim kompleks, mund ta kufizosh nivelin e të menduarit të modelit në `low`.

| Niveli i arsyetimit | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Përshkrimi |
| --- | --- | --- | --- | --- |
| **`minimal`** | Nuk mbështetet | Mbështetur (Parazgjedhja) | Mbështetur | Përputhet me cilësimin "pa mendim" për shumicën e kërkesave. Modeli mund të mendojë shumë pak për detyra komplekse të kodimit. Minimizon vonesën për aplikacionet e bisedës ose me kapacitet të lartë. Ki parasysh se `minimal` nuk garanton që të menduarit është joaktiv. |
| **`low`** | Mbështetur | Mbështetur | Mbështetur | Minimizon vonesën dhe koston. Më i miri për ndjekjen e thjeshtë të udhëzimeve, bisedën ose aplikacionet me kapacitet të lartë. |
| **`medium`** | Mbështetur | Mbështetur | Mbështetur | Arsyetim i balancuar për shumicën e detyrave. |
| **`high`** | Mbështetur (Parazgjedhja, dinamike) | Mbështetur (Dinamike) | Mbështetur (Parazgjedhja, dinamike) | Maksimizon thellësinë e arsyetimit. Modelit mund t'i duhet shumë më tepër kohë për të arritur një shenjë të parë dalëse (jo të menduar), por dalja do të jetë më e arsyetuar me kujdes. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Rezolucioni i medias

Gemini 3 prezanton kontrollin e detajuar mbi përpunimin multimodal të imazheve duke përdorur parametrin `media_resolution`. Rezolucionet më të larta përmirësojnë aftësinë e modelit për të lexuar tekstet e imëta ose për të identifikuar detajet e vogla, por rritin përdorimin e kodeve dhe vonesën.
Parametri `media_resolution` përcakton **numrin maksimal të kodeve
të caktuara për imazh hyrës ose kuadër video.**

Tani mund ta caktosh rezolucionin në `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` ose `media_resolution_ultra_high` për çdo pjesë individuale të medias ose në nivel global (nëpërmjet `generation_config`, globali nuk ofrohet për rezolucionin ultra të lartë). Nëse nuk specifikohet, modeli përdor parazgjedhjet optimale bazuar në llojin e medias.

**Cilësimet e rekomanduara**

| Lloji i medias | Cilësimi i rekomanduar | Maks. i tokenëve | Udhëzimet për përdorimin |
| --- | --- | --- | --- |
| **Imazhet** | `media_resolution_high` | 1120 | Rekomandohet për shumicën e detyrave të analizës së imazheve për të siguruar cilësinë maksimale. |
| **Skedarët PDF** | `media_resolution_medium` | 560 | Optimale për të kuptuar dokumentin; cilësia zakonisht arrin maksimumin në `medium`. Rritja në `high` rrallëherë i përmirëson rezultatet e OCR-së për dokumentet standarde. |
| **Video** (e përgjithshme) | `media_resolution_low` (ose `media_resolution_medium`) | 70 (për kuadër) | **Shënim:** Për video, cilësimet `low` dhe `medium` trajtohen në mënyrë identike (70 kode) për të optimizuar përdorimin e kontekstit. Kjo është e mjaftueshme për shumicën e detyrave të njohjes dhe përshkrimit të veprimeve. |
| **Video** (Me shumë tekst) | `media_resolution_high` | 280 (për kuadër) | Kërkohet vetëm kur rasti i përdorimit përfshin leximin e tekstit të dendur (OCR) ose detaje të vogla brenda kuadrove të videos. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Temperatura

Për të gjithë modelet e Gemini 3, ne rekomandojmë shumë që ta mbash parametrin e temperaturës në vlerën e tij të parazgjedhur prej `1.0`.

Ndërkohë që modelet e mëparshme përfitonin shpesh nga rregullimi i temperaturës për të kontrolluar<0x0Akreativitetin kundrejt determinizmit, aftësitë arsyetuese të Gemini 3 janë optimizuar<0x0Apër cilësimin e parazgjedhur. Ndryshimi i temperaturës (vendosja e saj nën 1,0) mund të çojë në sjellje të papritura, si p.sh. përsëritje ose performancë të degraduar, veçanërisht në detyra komplekse matematikore ose arsyetimi.

### Nënshkrimet e mendimeve

Gemini 3 përdor [Nënshkrimet e mendimeve](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=sq) për të
mbajtur kontekstin e arsyetimit nëpër thirrjet e API-së. Këto nënshkrime janë përfaqësime të enkriptuara
të procesit të brendshëm të të menduarit të modelit. Për t'u siguruar që modeli të ruajë aftësitë e tij arsyetuese, duhet t'i kthesh këto nënshkrime te modeli në kërkesën tënde pikërisht ashtu siç janë marrë:

- **Thirrja e funksionit (e rreptë):** API-ja zbaton verifikimin e rreptë për "Radhën aktuale". Nënshkrimet që mungojnë do të rezultojnë në një gabim 400.
- **Tekst/bisedë:** Vërtetimi nuk zbatohet në mënyrë strikte, por heqja e nënshkrimeve do të ulë cilësinë e arsyetimit dhe përgjigjeve të modelit.
- **Gjenerimi/modifikimi i imazheve (i rreptë)**: API-ja zbaton një verifikim të rreptë për të gjitha pjesët e modelit, duke përfshirë `thoughtSignature`. Nënshkrimet që mungojnë do të rezultojnë në një gabim 400.

#### Thirrja e funksionit (verifikim i rreptë)

Kur Gemini gjeneron një `functionCall`, ai mbështetet te `thoughtSignature` për të
përpunuar saktë rezultatin e veglës në radhën tjetër. "Radha aktuale"
përfshin të gjithë hapat e modelit (`functionCall`) dhe përdoruesit (`functionResponse`) që kanë ndodhur që nga mesazhi i fundit standard i **Përdoruesit** `text`.

- **Thirrje e vetme funksioni:** Pjesa `functionCall` përmban një nënshkrim. Duhet ta kthesh atë.
- **Thirrjet e funksioneve paralele:** Vetëm pjesa e parë `functionCall` në listë do të përmbajë nënshkrimin. Duhet t'i kthesh pjesët në të njëjtën renditje siç i ke marrë.
- **Me shumë hapa (vijues):** Nëse modeli thërret një veglë, merr një rezultat dhe thërret *një* veglë tjetër (brenda të njëjtit radhë), **të dyja** thirrjet e funksionit kanë nënshkrime. Duhet të kthesh **të gjitha** nënshkrimet e grumbulluara në historik.

#### Teksti dhe transmetimi

Për bisedën standarde ose gjenerimin e tekstit, prania e një nënshkrimi nuk garantohet.

- **Jo transmetim**: Pjesa përfundimtare e përmbajtjes e përgjigjes mund të përmbajë një
  `thoughtSignature`, megjithëse nuk është gjithmonë e pranishme. Nëse njëra kthehet, duhet ta dërgosh përsëri për të ruajtur performancën më të mirë.
- **Transmetimi**: Nëse gjenerohet një nënshkrim, ai mund të mbërrijë në një pjesë përfundimtare
  që përmban një pjesë teksti bosh. Sigurohu që analizuesi i transmetimit të kontrollojë për nënshkrime edhe nëse fusha e tekstit është bosh.

#### Gjenerimi dhe modifikimi i imazheve

Për `gemini-3-pro-image-preview` dhe `gemini-3.1-flash-image-preview`, nënshkrimet me mendime janë kritike për modifikimin bisedor. Kur i kërkon modelit të modifikojë një imazh, ai mbështetet te `thoughtSignature` nga radha e mëparshme për të kuptuar kompozimin dhe logjikën e imazhit origjinal.

- **Modifikimi:** Nënshkrimet garantohen në pjesën e parë pas mendimeve të përgjigjes (`text` ose `inlineData`) dhe në çdo pjesë pasuese `inlineData`. Duhet t'i kthesh të gjitha këto nënshkrime për të shmangur gabimet.

#### Shembuj të kodeve

#### Thirrja e funksionit me shumë hapa (vijuese)

Përdoruesi bën një pyetje që kërkon dy hapa të veçantë (Kontrollo fluturimin -> Rezervo taksi) në një radhë.   
  
**Hapi 1: Modeli thërret veglën e fluturimeve.**  
Modeli kthen një nënshkrim `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Hapi 2: Përdoruesi dërgon rezultatin e fluturimit**  
Ne duhet të dërgojmë përsëri `<Sig_A>` për të ruajtur rrjedhën e mendimit të modelit.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Hapi 3: Modeli telefonon "Veglën e taksive"**  
Modeli mban mend vonesën e fluturimit nëpërmjet `<Sig_A>` dhe tani vendos të rezervojë një taksi. Gjeneron një nënshkrim *të ri* `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Hapi 4: Përdoruesi dërgon rezultatin e taksisë**  
Për të përfunduar radhën, duhet të dërgosh përsëri të gjithë zinxhirin: `<Sig_A>` DHE `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Thirrja paralele e funksionit

Përdoruesi pyet: "Kontrollo motin në Paris dhe Londër." Modeli kthen dy thirrje funksioni në një përgjigje.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Teksti/arsyetimi kontekstual (pa verifikim)

Përdoruesi bën një pyetje që kërkon arsyetim në kontekst pa mjete të jashtme. Edhe pse nuk është verifikuar në mënyrë strikte, përfshirja e nënshkrimit e ndihmon modelin të ruajë zinxhirin e arsyetimit për pyetjet vijuese.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Gjenerimi dhe modifikimi i imazheve

Për gjenerimin e imazheve, nënshkrimet verifikohen në mënyrë rigoroze. Ato shfaqen në **pjesën e parë** (tekst ose imazh) dhe në **të gjitha pjesët e imazheve pasuese**. Të gjitha duhet të kthehen në radhën tjetër.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Migrimi nga modele të tjera

Nëse po transferon një gjurmë bisede nga një model tjetër (p.sh. Gemini
2.5) ose po injekton një thirrje funksioni të personalizuar që nuk është gjeneruar nga Gemini 3,
nuk do të kesh një nënshkrim të vlefshëm.

Për të anashkaluar verifikimin e rreptë në këto skenarë specifikë, mbush fushën me këtë varg specifik të rremë: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Daljet e strukturuara me veglat

Modelet e Gemini 3 të lejojnë të kombinosh [Daljet e strukturuara](https://ai.google.dev/gemini-api/docs/structured-output?hl=sq) me veglat e integruara, duke përfshirë
[Bazimin me "Kërko në Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq), [Kontekstin e URL-së](https://ai.google.dev/gemini-api/docs/url-context?hl=sq), [Ekzekutimin e kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq) dhe [Thirrjen e funksioneve](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
      "responseFormat": {
        "text": {
          "mimeType": "APPLICATION_JSON",
          "schema": {
            "type": "object",
            "properties": {
              "winner": {"type": "string", "description": "The name of the winner."},
              "final_match_score": {"type": "string", "description": "The final score."},
              "scorers": {
                "type": "array",
                "items": {"type": "string"},
                "description": "The name of the scorer."
              }
            },
            "required": ["winner", "final_match_score", "scorers"]
          }
        }
      }
    }
  }'
```

### Gjenerimi i imazhit

"Imazhi i Gemini 3.1 Flash" dhe "Imazhi i Gemini 3 Pro" të lejojnë të gjenerosh dhe modifikosh imazhe nga kërkesat me tekst. Ai përdor arsyetimin për të "menduar" nëpërmjet një kërkese dhe mund të marrë të dhëna në kohë reale, si p.sh. parashikimet e motit ose grafikët e aksioneve, para se të përdorë bazën e ["Kërko në Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq) përpara se të gjenerojë imazhe me besnikëri të lartë.

**Aftësi të reja dhe të përmirësuara:**

- **Paraqitja e tekstit dhe 4K:** Gjenero tekst dhe diagrame të qarta dhe të lexueshme me rezolucione deri në 2K dhe 4K.
- **Gjenerimi i bazuar në të dhëna:** Përdor veglën `google_search` për të verifikuar faktet dhe për të gjeneruar imazhe bazuar në informacionet e botës reale. Bazimi me Google *Image*
  Search ofrohet për Gemini 3.1 Flash Image.
- **Modifikimi bisedor:** Modifikimi i imazheve me disa hapa thjesht duke kërkuar për ndryshime (p.sh. "Bëje sfondin një perëndim dielli"). Ky fluks pune mbështetet te
  **Nënshkrimet e mendimeve** për të ruajtur kontekstin vizual mes radhëve.

Për detaje të plota mbi raportet e pamjes, flukset e punës të modifikimit dhe opsionet e konfigurimit, shiko [Udhëzuesin e "Gjenerimit të imazheve"](https://ai.google.dev/gemini-api/docs/image-generation?hl=sq).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="4K",
        ),
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      imageConfig: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
      "imageConfig": {
        "aspectRatio": "16:9",
        "imageSize": "4K"
      }
    }
  }'
```

**Shembull përgjigjeje**

![Moti në Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=sq)

### Ekzekutimi i kodit me imazhe

Gemini 3 Flash mund ta trajtojë shikimin si një hetim aktiv, jo vetëm si një vështrim statik. Duke kombinuar arsyetimin me [ekzekutimin e kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq), modeli formulon një plan dhe më pas shkruan dhe ekzekuton kodin në Python për të zmadhuar, prerë, shënuar ose manipuluar imazhet në një mënyrë tjetër hap pas hapi për të bazuar vizualisht përgjigjet e tij.

**Rastet e përdorimit:**

- **Zmadho dhe inspekto:** Modeli zbulon në mënyrë të nënkuptuar kur detajet janë shumë të vogla (p.sh. leximi i një matësi në distancë ose i një numri serial) dhe shkruan kod për të prerë dhe riekzaminuar zonën në rezolucion më të lartë.
- **Matematika vizuale dhe grafikët:** Modeli mund të ekzekutojë llogaritje me shumë hapa duke përdorur kodin (p.sh. duke mbledhur artikujt e rreshtave në një faturë ose duke gjeneruar një grafik të Matplotlib nga të dhënat e nxjerra).
- **Shënimi i imazhit:** Modeli mund të vizatojë shigjeta, kuti kufizuese ose shënime të tjera drejtpërdrejt mbi imazhe për t'u përgjigjur pyetjeve hapësinore si "Ku duhet të shkojë ky artikull?".

Për të aktivizuar të menduarit vizual, konfiguro [Ekzekutimin e kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq) si një vegël. Modeli do të përdorë automatikisht kodin për të manipuluar imazhet kur të jetë e nevojshme.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### QETËSI

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Për më shumë detaje mbi ekzekutimin e kodit me imazhe, shiko [Ekzekutimin e kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq#images).

### Përgjigjet e funksionit multimodal

[Thirrja e funksioneve multimodale](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq#multimodal)
u lejon përdoruesve të kenë përgjigje të funksioneve që përmbajnë
objekte multimodale, duke lejuar përdorimin e përmirësuar të aftësive të thirrjes së funksioneve të modelit. Thirrja standarde e funksionit mbështet vetëm përgjigjet e funksionit të bazuara në tekst:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### QETËSI

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Kombino veglat e integruara dhe telefonatat e funksioneve

Gemini 3 lejon përdorimin e veglave të integruara (si p.sh. "Kërko në Google", konteksti i URL-së dhe [më shumë](https://ai.google.dev/gemini-api/docs/tools?hl=sq)) dhe veglave të personalizuara të [thirrjes së funksioneve](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) në të njëjtën thirrje të API-së, duke lejuar flukse pune më komplekse. Mëso më shumë në faqen e [kombinimeve të veglave](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq).

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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
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
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## Po migron nga Gemini 2.5

Gemini 3 është familja jonë më e aftë e modeleve deri më sot dhe ofron një përmirësim gradual në krahasim me Gemini 2.5. Kur migron, merr parasysh sa më poshtë:

- **Arsyetimi:** Nëse ke përdorur më parë inxhinieri të ndërlikuar të kërkesave (si p.sh. zinxhiri i mendimit) për të detyruar Gemini 2.5 të arsyetojë, provo Gemini 3 me
  `thinking_level: "high"` dhe kërkesa të thjeshtuara.
- **Cilësimet e temperaturës:** Nëse kodi yt ekzistues e cakton në mënyrë të qartë temperaturën
  (sidomos në vlera të ulëta për dalje deterministe), ne rekomandojmë që ta heqësh këtë parametër
  dhe të përdorësh vlerën e parazgjedhur 1,0 të Gemini 3 për të shmangur problemet e mundshme me përsëritjen
  ose degradimin e performancës në detyra komplekse.
- **Kuptimi i dokumenteve dhe PDF-ve:**
  Nëse je mbështetur në sjellje specifike për analizimin e dokumenteve të dendura, testo cilësimin e ri të `media_resolution_high` për të siguruar saktësinë e vazhdueshme.
- **Konsumimi i tokenit:** Migrimi në parazgjedhjet e Gemini 3 mund të **rritë** përdorimin e tokenit
  për skedarët PDF, por mund të **ulë** përdorimin e tokenit për videot. Nëse kërkesat tani e tejkalojnë dritaren e kontekstit për shkak të rezolucioneve të parazgjedhura më të larta, ne rekomandojmë zvogëlimin e rezolucionit të medias.
- **Segmentimi i imazheve:** Aftësitë e segmentimit të imazheve (që kthejnë maska në nivel pikseli për objektet) nuk mbështeten në Gemini 3 Pro ose Gemini 3 Flash. Për ngarkesat e punës që kërkojnë segmentimin origjinal të imazheve, ne rekomandojmë që të vazhdosh të përdorësh Gemini 2.5 Flash me modalitetin e të menduarit të çaktivizuar.
- **Përdorimi në kompjuter:** Gemini 3 Pro dhe Gemini 3 Flash mbështesin [Përdorimin në kompjuter](https://ai.google.dev/gemini-api/docs/computer-use?hl=sq). Ndryshe nga seria 2.5, nuk ke nevojë të përdorësh një model të veçantë për t'u qasur te veglat e përdorimit të kompjuterit.
- **Mbështetja e veglave**: [Kombinimi i veglave të integruara me thirrjen e funksioneve](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq) tani mbështetet për modelet Gemini 3. [Bazimi i Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=sq) mbështetet gjithashtu tani për modelet e Gemini 3.
- **Numri i kandidatëve**: Modelet Gemini 3 nuk e mbështesin `candidateCount > 1`.
  Caktimi i këtij parametri në një vlerë më të madhe se `1` do të kthejë një gabim 400.

## Përputhshmëria me OpenAI

Për përdoruesit që përdorin [shtresën e përputhshmërisë me OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=sq), parametrat standardë (`reasoning_effort` të OpenAI) mapohen automatikisht në
ekuivalentët e Gemini (`thinking_level`).

## Praktikat më të mira për nxitjen

Gemini 3 është një model arsyetimi, i cili ndryshon mënyrën se si duhet të japësh kërkesat.

- **Udhëzime të sakta:** Bëhu i përmbledhur në kërkesat e tua të hyrjes. Gemini 3 përgjigjet më mirë ndaj udhëzimeve të drejtpërdrejta dhe të qarta. Ajo mund të analizojë në mënyrë të tepruar teknikat e detyrave të detajuara ose tepër komplekse që përdoren për modelet më të vjetra.
- **Detajimi i daljes:** Si parazgjedhje, Gemini 3 është më pak i detajuar dhe preferon të japë përgjigje të drejtpërdrejta dhe efikase. Nëse rasti yt i përdorimit kërkon një personazh më bisedor ose "bisedues", duhet ta drejtosh në mënyrë të qartë modelin në kërkesë (p.sh. "Shpjegoje këtë si një asistent miqësor dhe bisedues").
- **Menaxhimi i kontekstit:** Kur punon me grupe të mëdha të dhënash (p.sh. libra të tërë, baza kodesh ose video të gjata), vendos udhëzimet ose pyetjet e tua specifike në fund të kërkesës, pas kontekstit të të dhënave. Ankoro arsyetimin e modelit te të dhënat e dhëna duke e nisur pyetjen tënde me një frazë si "Bazuar në informacionet e mësipërme...".

Mëso më shumë rreth strategjive të projektimit të kërkesave në [udhëzuesin e inxhinierisë së kërkesave](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=sq).

## Pyetjet e shpeshta

1. **Cili është kufiri i njohurive për Gemini 3?** Modelet e Gemini 3 kanë një kufi njohurish në janar 2025. Për informacione më të fundit, përdor veglën e
   [Argumentimit me "Kërko"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq).
2. **Cilat janë kufijtë e dritares kontekstuale?** Modelet e Gemini 3 mbështesin një dritare kontekstuale hyrëse me 1 milion tokenë dhe deri në 64 000 tokenë dalje.
3. **A ka një nivel falas për Gemini 3?** Gemini 3 Flash
   `gemini-3-flash-preview` dhe 3.1 Flash-Lite `gemini-3.1-flash-lite` kanë
   nivele falas në Gemini API. Mund t'i provosh Gemini 3.1 Pro dhe 3 Flash falas në Google AI Studio, por nuk ofrohet nivel falas për `gemini-3.1-pro-preview` në Gemini API.
4. **A do të funksionojë përsëri kodi im i vjetër i `thinking_budget`?** Po, `thinking_budget` mbështetet akoma për përputhshmëri me versionet e mëparshme, por ne rekomandojmë migrimin te `thinking_level` për performancë më të parashikueshme. Mos i përdor të dyja në të njëjtën kërkesë.
5. **A e mbështet Gemini 3 Batch API?** Po, Gemini 3 mbështet
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=sq).
6. **A mbështetet "Ruajtja në memorien specifike"?** Po, [Ruajtja në memorien specifike e kontekstit](https://ai.google.dev/gemini-api/docs/caching?hl=sq) mbështetet për Gemini 3.
7. **Cilat vegla mbështeten në Gemini 3?** Gemini 3 mbështet ["Kërko në Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq), [Argumentimin me Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=sq), [Kërkimin në skedarë](https://ai.google.dev/gemini-api/docs/file-search?hl=sq),
   [Ekzekutimin e kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq) dhe [Kontekstin e URL-së](https://ai.google.dev/gemini-api/docs/url-context?hl=sq). Ai mbështet gjithashtu [Thirrjen standarde të funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) për veglat e tua të personalizuara dhe në [kombinim me veglat e integruara](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq).
8. **Çfarë është `gemini-3.1-pro-preview-customtools`?** Nëse po përdor `gemini-3.1-pro-preview` dhe modeli i shpërfill veglat e personalizuara në favor të komandave bash, provo modelin `gemini-3.1-pro-preview-customtools` më mirë. Më shumë informacione [këtu](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=sq#gemini-31-pro-preview-customtools).

## Hapat e radhës

- Fillo me [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=sq#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Kontrollo udhëzuesin e posaçëm të Cookbook për [nivelet e të menduarit](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=sq#gemini3) dhe se si të migrosh nga buxheti i të menduarit te nivelet e të menduarit.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-19 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-19 UTC."],[],[]]
