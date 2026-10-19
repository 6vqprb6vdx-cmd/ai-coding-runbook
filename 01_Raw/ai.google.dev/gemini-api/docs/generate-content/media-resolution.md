---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=sq
fetched_at: 2026-10-19T05:39:56.241407+00:00
title: "Rezolucioni i medias \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Rezolucioni i medias

Parametri `media_resolution` kontrollon se si Gemini API përpunon hyrjet e mediave si imazhet, videot, audiot dhe dokumentet PDF duke përcaktuar **numrin maksimal të kodeve** të caktuara për hyrjet e mediave, duke të të lejuar të balancosh cilësinë e përgjigjes me vonesën dhe koston. Ndërsa hyrjet vizuale dhe të dokumenteve e shkallëzojnë alokimin e tokenëve bazuar në cilësimin e rezolucionit, hyrjet e audios tokenizohen me një normë fikse për sekondë në të gjitha nivelet e rezolucionit. Për
cilësimet e ndryshme, vlerat e parazgjedhura dhe mënyrën se si ato korrespondojnë me tokenët, shiko
seksionin [Numrat e tokenëve](#token-counts).

Mund ta konfigurosh rezolucionin e medias në dy mënyra:

- [Për pjesë](#per-part-media-resolution) (modelet Gemini 4 dhe Gemini 3)
- [Në nivel global](#global-media-resolution) për një kërkesë të tërë të `generateContent` (të gjitha modelet multimodale)

## Rezolucioni i medias për çdo pjesë (Gemini 4 dhe Gemini 3)

Gemini 4 dhe Gemini 3 të lejojnë të caktosh rezolucionin e medias për objektet individuale të medias brenda kërkesës sate, duke ofruar optimizim të detajuar të përdorimit të kodeve. Mund të kombinosh nivelet e rezolucionit në një kërkesë të vetme. Për shembull, duke përdorur rezolucion të lartë për një diagram kompleks dhe rezolucion të ulët për një imazh kontekstual. Ky cilësim
mbishkruan çdo konfigurim global për një pjesë specifike. Për cilësimet e parazgjedhura,
shiko seksionin [Numrat e tokenëve](#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-4-argon'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-4-argon';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### QETËSI

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-4-argon"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Rezolucioni global i medias

Mund të caktosh një rezolucion të parazgjedhur për të gjitha pjesët e medias në një kërkesë duke përdorur
`GenerationConfig`. Kjo mbështetet nga të gjitha modelet multimodale. Nëse një kërkesë
përfshin cilësimet globale dhe [cilësimet për çdo pjesë](#per-part-media-resolution), cilësimi për çdo pjesë ka përparësi për atë artikull specifik.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Vlerat e disponueshme të rezolucionit

Gemini API përcakton nivelet e mëposhtme për rezolucionin e medias:

- `MEDIA_RESOLUTION_UNSPECIFIED`: Cilësimi i parazgjedhur. Numri i tokenëve për këtë nivel ndryshon në mënyrë të konsiderueshme midis Gemini 3 dhe modeleve të mëparshme të Gemini.
- `MEDIA_RESOLUTION_LOW`: Numër më i ulët tokenësh, që rezulton në përpunim më të shpejtë
  dhe kosto më të ulët, por me më pak detaje.
- `MEDIA_RESOLUTION_MEDIUM`: Një balancë mes detajeve, kostos dhe vonesës.
- `MEDIA_RESOLUTION_HIGH`: Numër më i lartë i kodeve, që ofron më shumë detaje për të punuar modeli, me koston e rritjes së vonesës dhe kostos.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (vetëm për pjesë): Numri më i lartë i tokenëve, i kërkuar për raste specifike përdorimi si p.sh. [përdorimi i kompjuterit](https://ai.google.dev/gemini-api/docs/computer-use?hl=sq).

Ki parasysh se `MEDIA_RESOLUTION_HIGH` ofron performancën optimale për shumicën e rasteve të përdorimit.

Numri i saktë i tokenëve të gjeneruar për secilin nga këto nivele varet nga **lloji i medias** (imazh, video, audio, PDF) dhe **versioni i modelit**.

## Numri i tokenëve

Tabelat më poshtë përmbledhin numrat e përafërt të tokenëve për çdo
vlerë të `media_resolution` dhe lloj të medias për familje të modelit.

**Modelet e Gemini 3**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Imazh** | **Video** | **Audioja** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (parazgjedhja) | 1120 | 70 | 25 (për sekondë) | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 25 (për sekondë) | 280 + Native Text |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 25 (në sekondë) | 560 + tekst i integruar |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 25 (në sekondë) | 1120 + Native Text |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | Nuk ka | Nuk ka | Nuk ka |

**Modelet Gemini 2.5**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **Imazh** | **Video** | **Audioja** | **PDF (i skanuar)** | **PDF (i integruar)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (parazgjedhja) | 256 + Pan & Scan (~2048) | 256 | 32 (për sekondë) | 256 + OCR | 256 + teksti i integruar |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 32 (për sekondë) | 64 + OCR | 64 + Native Text |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 32 (për sekondë) | 256 + OCR | 256 + Native Text |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 32 (për sekondë) | 256 + OCR | 256 + teksti i integruar |

## Zgjedhja e rezolucionit të duhur

- **Parazgjedhja (`UNSPECIFIED`):** Fillo me parazgjedhjen. Ai është i optimizuar për një balancë të mirë të cilësisë, vonesës dhe kostos për rastet më të zakonshme të përdorimit.
- **`LOW`:** Përdore për skenarë ku kostoja dhe vonesa janë parësore dhe
  detajet e imta janë më pak kritike.
- **`MEDIUM` / `HIGH`:** Rrit rezolucionin kur detyra kërkon
  të kuptuarit e detajeve të ndërlikuara brenda medias. Kjo nevojitet shpesh për
  analizë vizuale komplekse, lexim grafikësh ose të kuptuarit e dokumenteve të dendura.
- **`ULTRA HIGH`** - Ofrohet vetëm për cilësimin për pjesë. Rekomandohet për raste specifike përdorimi, si p.sh. përdorimi i kompjuterit ose kur testimi tregon një përmirësim të qartë në krahasim me `HIGH`.
- **Kontrolli për pjesë (Gemini 4 dhe Gemini 3):** Optimizon përdorimin e kodeve. Për
  shembull, në një kërkesë me disa imazhe, përdor `HIGH` për një diagram kompleks
  dhe `LOW` ose `MEDIUM` për imazhe kontekstuale më të thjeshta.

**Cilësimet e rekomanduara**

Më poshtë listohen cilësimet e rekomanduara të rezolucionit të medias për çdo lloj të mbështetur të medias.

|  |  |  |  |
| --- | --- | --- | --- |
| **Lloji i medias** | **Cilësimi i rekomanduar** | **Maks. i tokenëve** | **Udhëzimet për përdorimin** |
| **Imazhet** | `MEDIA_RESOLUTION_HIGH` | 1120 | Rekomandohet për shumicën e detyrave të analizës së imazheve për të siguruar cilësinë maksimale. |
| **Skedarët PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Optimale për kuptimin e dokumentit; cilësia zakonisht arrin nivelin e ngopjes në `medium`. Rritja në `high` rrallëherë i përmirëson rezultatet e OCR-së për dokumentet standarde. |
| **Video** (e përgjithshme) | `MEDIA_RESOLUTION_LOW` (ose `MEDIA_RESOLUTION_MEDIUM`) | 70 (për kuadër) | **Shënim.** Për videot, cilësimet `low` dhe `medium` trajtohen në mënyrë identike (70 jeto) për të optimizuar përdorimin e kontekstit. Kjo është e mjaftueshme për shumicën e detyrave të njohjes dhe përshkrimit të veprimeve. |
| **Video** (Me shumë tekst) | `MEDIA_RESOLUTION_HIGH` | 280 (për kuadër) | Kërkohet vetëm kur rasti i përdorimit përfshin leximin e tekstit të dendur (OCR) ose detajeve të vogla brenda kuadrove të videos. |
| **Audioja** | `MEDIA_RESOLUTION_UNSPECIFIED` (parazgjedhja) | 25 (për sekondë) për Gemini 3; 32 (për sekondë) për Gemini 2.5 | Audioja tokenizohet me një normë fikse për sekondë në të gjitha cilësimet e mbështetura të rezolucionit (`unspecified`, `low`, `medium` dhe `high`). |

Testo dhe vlerëso gjithmonë ndikimin e cilësimeve të ndryshme të rezolucionit në aplikacionin tënd specifik për të gjetur kompromisin më të mirë midis cilësisë, vonesës dhe kostos.

## Marrëdhënia me modalitetet e përpunimit të videos

`media_resolution` dhe parametrat e përpunimit kontrollojnë aspekte të ndryshme të hyrjes së videos:

- `media_resolution` kontrollon **rezolucionin** e çdo kuadri (numri i kodeve për kuadër).
- `processing` / `media_processing` kontrollon **se cila përmbajtje nga videoja** ngarkohet në kontekst.

Mund t'i caktosh të dyja në të njëjtën hyrje videoje. Për shembull, mund të përdorësh përpunimin agjentik me rezolucion të ulët të medias për të minimizuar përdorimin total të tokenëve për një video të gjatë.

Për detaje mbi modalitetet e përpunimit të videos, shih udhëzuesin [Kuptimi i videos nga agjenti](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=sq#agentic-video-understanding).

## Përmbledhja e përputhshmërisë së versioneve

- `MediaResolution` enum ofrohet për të gjitha modelet që mbështesin hyrjen e medias.
- Numrat e kodeve që lidhen me çdo nivel të numërimit **ndryshojnë** midis modeleve Gemini 4 / Gemini 3 dhe versioneve të mëparshme të Gemini.
- Konfigurimi i `media_resolution` në objekte individuale të `Part` **mbështetet në
  modelet Gemini 4 dhe Gemini 3**.

## Hapat e radhës

- Mëso më shumë rreth aftësive multimodale të Gemini API në udhëzuesit për
  [kuptimin e imazheve](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=sq),
  [kuptimin e videove](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=sq),
  [kuptimin e audios](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=sq) dhe
  [kuptimin e dokumenteve](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=sq).

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
