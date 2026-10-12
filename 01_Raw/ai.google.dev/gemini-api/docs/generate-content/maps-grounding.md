---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=sq
fetched_at: 2026-10-12T06:48:21.943200+00:00
title: "Argumentimi me Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash është tani në dispozicion. [Provojeni](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=sq) .

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Argumentimi me Google Maps

Argumentimi me Google Maps lidh aftësitë gjeneruese të Gemini me të dhënat e pasura, faktike dhe të përditësuara të Google Maps. Kjo veçori u mundëson zhvilluesve të integrojnë me lehtësi funksionalitetin e bazuar te vendndodhja në aplikacionet e tyre. Kur një pyetje e përdoruesit ka një kontekst në lidhje me të dhënat e Maps, modeli i Gemini përdor Google Maps për të ofruar përgjigje të sakta dhe të përditësuara që janë të përshtatshme për vendndodhjen e specifikuar të përdoruesit ose zonën e përgjithshme.

- **Përgjigje të sakta që njohin vendndodhjen:** Përfito nga të dhënat e gjera dhe aktuale të Google Maps për pyetje specifike gjeografike.
- **Personalizim i përmirësuar:** Personalizo rekomandimet dhe informacionet bazuar në vendndodhjet e dhëna nga përdoruesit.

## Fillo

Ky shembull demonstron se si të integrosh Grounding me Google Maps në aplikacionin tënd për të ofruar përgjigje të sakta dhe të ndërgjegjshme për vendndodhjen për pyetjet e përdoruesve. Kërkesa kërkon rekomandime lokale me një vendndodhje opsionale të përdoruesit, duke bërë të mundur që modeli i Gemini të përdorë të dhënat e Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### QETËSI

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Si funksionon argumentimi me Google Maps

"Argumentimi me Google Maps" integron Gemini API me ekosistemin e Google Geo duke përdorur Maps API si burim argumentimi. Kur kërkesa e një përdoruesi përfshin kontekst gjeografik, modeli i Gemini mund të aktivizojë veglën e "Argumentimit me Google Maps". Më pas, modeli mund të gjenerojë përgjigje të bazuara në të dhënat e Google Maps që janë të përshtatshme për vendndodhjen e dhënë.

Procesi zakonisht përfshin:

1. **Kërkesa e përdoruesit:** Një përdorues dërgon një kërkesë në aplikacionin tënd, ndoshta duke përfshirë kontekstin gjeografik (p.sh. "kafene në afërsi", "muze në San-Francisko").
2. **Aktivizimi i veglës:** Modeli i Gemini, duke njohur qëllimin gjeografik, aktivizon veglën "Argumentimi me Google Maps". Kjo vegël mund të ofrohet në mënyrë opsionale me `latitude` dhe `longitude` të përdoruesit. Vegla është një vegël kërkimi me tekst dhe funksionon në mënyrë të ngjashme me kërkimin në Maps, në atë që kërkesat lokale ("pranë meje") do të përdorin koordinatat, ndërsa kërkesat specifike ose jolokale ka të ngjarë që të mos ndikohen nga vendndodhja e qartë.
3. **Marrja e të dhënave:** Shërbimi i "Kërkimit në terren" me Google Maps kërkon në Google Maps për informacione përkatëse (p.sh. vende, komente, fotografi, adresa, orare hapjeje).
4. **Gjenerimi i bazuar në të dhëna:** Të dhënat e marra nga Maps përdoren për të informuar përgjigjen e modelit Gemini, duke siguruar saktësinë faktike dhe përshtatshmërinë.
5. **Përgjigjja:** Modeli kthen një përgjigje me tekst, e cila
   përfshin citime për burimet e Google Maps.

## Pse dhe kur të përdorësh "Argumentimin me Google Maps"

"Vendosja në tokë" me Google Maps është ideale për aplikacionet që kërkojnë informacione të sakta, të përditësuara dhe specifike për vendndodhjen. Ai përmirëson përvojën e përdoruesit duke ofruar përmbajtje të personalizuara dhe të përshtatshme të mbështetura nga baza e gjerë e të dhënave e Google Maps me mbi 250 milionë vende në mbarë botën.

Duhet të përdorësh "Argumentimin me Google Maps" kur aplikacioni yt ka nevojë që:

- Të japësh përgjigje të plota dhe të sakta për pyetjet specifike për vendndodhjen gjeografike.
- Krijo planifikues udhëtimi dhe udhëzues lokalë nëpërmjet bisedës.
- Rekomando pika interesi bazuar në vendndodhje dhe preferencat e përdoruesit, si p.sh. restorante ose dyqane.
- Krijo përvoja të ndërgjegjshme për vendndodhjen për shërbimet sociale, të shitjes me pakicë ose të dërgesave të ushqimeve.

"Bazimi" me Google Maps shkëlqen në rastet e përdorimit ku afërsia dhe të dhënat aktuale faktike janë kritike, si p.sh. për të gjetur "kafenenë më të mirë në afërsi" ose për të marrë udhëzime.

## Metodat dhe parametrat e API-së

"Argumentimi me Google Maps" ekspozohet nëpërmjet Gemini API si një veglë brenda metodës [`generateContent`](https://ai.google.dev/api/generate-content?hl=sq). Ti aktivizon dhe konfiguron
Grounding me Google Maps duke përfshirë një objekt
[`googleMaps`](https://ai.google.dev/api/caching?hl=sq#GoogleMaps) në parametrin `tools` të kërkesës sate.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Përveç kësaj, vegla mbështet kalimin e vendndodhjes kontekstuale si `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Kuptimi i përgjigjes së bazuar

Kur një përgjigje bazohet me sukses në të dhënat e Google Maps, përgjigjja
përfshin një fushë [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=sq#GroundingMetadata).
Këto të dhëna të strukturuara janë thelbësore për verifikimin e pretendimeve dhe krijimin e një përvoje të pasur citimi në aplikacionin tënd, si dhe për përmbushjen e kërkesave për përdorimin e shërbimit.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API kthen informacionet e mëposhtme me
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=sq#GroundingMetadata):

- `groundingChunks`: Vargu i objekteve që përmbajnë burimet e `maps` (`uri`,
  `placeId` dhe `title`).
- `groundingSupports`: Vargu i pjesëve për të lidhur tekstin e përgjigjes së modelit me burimet në `groundingChunks`. Çdo pjesë lidh një shtrirje teksti (të përcaktuar nga
  `startIndex` dhe `endIndex`) me një ose më shumë `groundingChunkIndices`. Ky është çelësi për të ndërtuar citime të ndërfutura.

Për një fragment kodi që tregon se si të paraqiten citimet e integruara në tekst, shiko [shembullin](https://ai.google.dev/gemini-api/docs/google-search?hl=sq#attributing_sources_with_inline_citations) në dokumentet e "Themelimit me 'Kërko në Google'".

## Rastet e përdorimit

Argumentimi me Google Maps mbështet një sërë rastesh përdorimi që kanë parasysh vendndodhjen. Shembujt e mëposhtëm demonstrojnë se si kërkesa dhe parametra të ndryshëm mund të shfrytëzojnë "Bazimin" me Google Maps. Informacionet në "Rezultatet e bazuara në vendndodhje" të Google Maps mund të ndryshojnë nga kushtet aktuale.

### Trajtimi i pyetjeve specifike për vendin

Bëj pyetje të detajuara për një vend specifik për të marrë përgjigje bazuar në komentet e përdoruesve të Google dhe të dhëna të tjera të Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### QETËSI

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Ofrimi i personalizimit bazuar në vendndodhje

Merr rekomandime të personalizuara për preferencat e një përdoruesi dhe një zonë specifike gjeografike.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### QETËSI

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Ndihmon për planifikimin e itinerarit

Gjenero plane shumëditore me udhëzime dhe informacione për
lokacione të ndryshme, të përsosura për aplikacionet e udhëtimeve.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### QETËSI

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Kërkesat për përdorimin e shërbimit

Ky seksion përshkruan kërkesat për përdorimin e shërbimit për "Argumentimin me Google
Maps".

### Informo përdoruesin për përdorimin e burimeve të Google Maps

Me çdo rezultat të bazuar në Google Maps, do të marrësh burimet në `groundingChunks` që mbështesin çdo përgjigje. Metadatat e mëposhtme kthehen gjithashtu:

- uri i burimit
- titulli
- ID-ja

Kur paraqet rezultate nga "Argumentimi me Google Maps", duhet të specifikosh burimet përkatëse të Google Maps dhe të informosh përdoruesit e tu për sa më poshtë:

- Burimet e Google Maps duhet të ndjekin menjëherë përmbajtjen e gjeneruar që mbështesin burimet. Kjo përmbajtje e gjeneruar referohet gjithashtu si rezultat i bazuar në terren i Google Maps.
- Burimet e Google Maps duhet të jenë të shikueshme brenda një ndërveprimi të përdoruesit.

### Shfaq burimet e Google Maps me lidhjet e Google Maps

Për çdo burim në `groundingChunks` dhe në
`grounding_chunks.maps.placeAnswerSources.reviewSnippets`, duhet të gjenerohet një pamje paraprake e lidhjes sipas këtyre kërkesave:

- Atribuo çdo burim te Google Maps duke ndjekur [udhëzimet e atribuimit](#maps-attribution-guidelines) të tekstit të Google Maps.
- Shfaq titullin e burimit të dhënë në përgjigje.
- Lidhja për te burimi duke përdorur `uri` ose `googleMapsUri` nga përgjigjja.

Këto imazhe tregojnë kërkesat minimale për shfaqjen e burimeve dhe lidhjeve të Google
Maps.

![Kërkesa me përgjigjen që shfaq burimet](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=sq)

Mund ta palosësh pamjen e burimeve.

![Kërkesa me përgjigjen dhe burimet u palosën](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=sq)

Opsionale: Përmirëso pamjen paraprake të lidhjes me përmbajtje shtesë, si p.sh.:

- Një [favicon i Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=sq)
  futet para atribuimit me tekst të Google Maps.
- Një fotografi nga URL-ja e burimit (`og:image`).

Për më shumë informacione rreth disa prej ofruesve të të dhënave të Google Maps dhe kushteve të tyre të licencës, shiko [njoftimet ligjore të Google Maps dhe Google Earth](https://www.google.com/help/legalnotices_maps/?hl=sq).

### Udhëzimet për atribuimin me tekst të Google Maps

Kur u atribuon burime Google Maps në tekst, ndiq këto udhëzime:

- Mos e modifiko tekstin Google Maps në asnjë mënyrë:
  - Mos e ndrysho kapitalizimin e Google Maps.
  - Mos e mbështill Google Maps në disa rreshta.
  - Mos e lokalizo Google Maps në një gjuhë tjetër.
  - Parandalo përkthimin e Google Maps nga shfletuesit duke përdorur atributin translate="no" të HTML.
- Stilizo tekstin e Google Maps siç përshkruhet në tabelën e mëposhtme:

| Prona | Stili |
| --- | --- |
| `Font family` | Roboto. Ngarkimi i fontit është opsional. |
| `Fallback font family` | Çdo font sans serif i trupit të tekstit që përdoret tashmë në produktin tënd ose "Sans-Serif" për të aktivizuar fontin e parazgjedhur të sistemit |
| `Font style` | Normale |
| `Font weight` | 400 |
| `Font color` | E bardhë, e zezë (#1F1F1F) ose gri (#5E5E5E). Mbaj kontrast të arritshëm (4,5:1) me sfondin. |
| `Font size` | - Madhësia minimale e fontit: 12sp - Madhësia maksimale e fontit: 16 sp - Për të mësuar rreth sp, shiko "Njësitë e madhësisë së fontit" në [uebsajtin e Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Normale |

#### Shembull i CSS-së

Kodi i mëposhtëm CSS e paraqet Google Maps me stilin e duhur tipografik dhe ngjyrën në një sfond të bardhë ose të lehtë.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### ID-ja e vendit dhe ID-ja e komentit

Të dhënat e Google Maps përfshijnë ID-në e vendit dhe ID-në e komenteve. Mund të ruash në memorien specifike, të ruash dhe të eksportosh të dhënat e mëposhtme të përgjigjes:

- `placeId`
- `reviewId`

Kufizimet kundër ruajtjes në memorien specifike te "Kushtet e 'Argumentimit me Google Maps'" nuk zbatohen.

### Aktiviteti dhe territori i ndaluar

"Qëndrimi në tokë" me Google Maps ka kufizime shtesë për përmbajtje dhe aktivitete të caktuara për të ruajtur një platformë të sigurt dhe të besueshme. Përveç kufizimeve të përdorimit në [Kushtet](https://ai.google.dev/gemini-api/terms?hl=sq#grounding-with-google-maps):

- Nuk do ta përdorësh Grounding me Google Maps për aktivitete me rrezik të lartë, duke përfshirë shërbimet e reagimit ndaj urgjencave.
- Nuk do ta shpërndash apo tregtosh aplikacionin tënd që ofron "Argumentimin me Google Maps" në një territor të ndaluar. Për më shumë informacione, shiko
  [Territoret e ndaluara të Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=sq).
  Lista e Territoreve të Ndaluara mund të përditësohet herë pas here.

## Praktikat më të mira

- **Jep vendndodhjen e përdoruesit:** Për përgjigjet më të përshtatshme dhe të personalizuara,
  përfshi gjithmonë `user_location` (gjerësinë dhe gjatësinë gjeografike) në konfigurimin e `googleMapsGrounding` kur dihet vendndodhja e përdoruesit.
- **Informo përdoruesit fundorë:** Informo në mënyrë të qartë përdoruesit fundorë që të dhënat e Google Maps po përdoren për t'iu përgjigjur pyetjeve të tyre, sidomos kur vegla është e aktivizuar.
- **Monitoro vonesën:** Për aplikacionet bisedore, sigurohu që vonesa P95
  për përgjigjet e bazuara në njohuri të mbetet brenda pragjeve të pranueshme për të
  ruajtur një përvojë të qetë të përdoruesit.
- **Çaktivizoje kur nuk është e nevojshme:** Argumentimi me Google Maps është joaktiv si parazgjedhje. Aktivizoje atë (`"tools": [{"googleMaps": {}}]`) vetëm kur një kërkesë ka një kontekst të qartë gjeografik, për të optimizuar performancën dhe koston.

## Kufizimet

- **Fushëveprimi gjeografik:** "Argumentimi me Google Maps" ofrohet në nivel global
- **Mbështetja e modelit:** Shiko seksionin [Modelet e mbështetura](#supported-models).
- **Hyrjet/daljet multimodale:** "Bazimi" me Google Maps nuk mbështet aktualisht hyrjet ose daljet multimodale përveç tekstit.
- **Gjendja e parazgjedhur:** Vegla "Argumentimi me Google Maps" është joaktive si parazgjedhje.
  Duhet ta aktivizosh në mënyrë të qartë në kërkesat e tua të API-së.

## Çmimet dhe kufijtë e normës

Çmimi i "Argumentimit me Google Maps" ndryshon në varësi të gjeneratës së modelit:

- **Gemini 3 dhe modelet më të reja:** Projekti yt faturohet për çdo kërkesë kërkimi që modeli vendos të ekzekutojë, me 5000 kërkesa falas në muaj të ndara në të gjitha modelet Gemini 3 dhe më të reja dhe më pas **14 USD për 1000 kërkesa kërkimi**. Një kërkesë e vetme kërkimi (kërkesa jote e API-së për modelin) mund të rezultojë në ekzekutimin e disa kërkesave kërkimi nga modeli për të gjetur informacionet e nevojshme. Secila nga këto kërkesa llogaritet si një përdorim i faturueshëm i veglës.
- **Gemini 2.5 dhe modelet më të vjetra:** Projekti yt faturohet për çdo kërkesë kërkimi
  (25 USD për 1000 kërkesa të bazuara në kontekst). Një kërkesë faturohet vetëm nëse kërkesa
  kthehet me sukses me të paktën një rezultat të bazuar në Google Maps, pavarësisht
  se sa kërkesa individuale kërkimi ka kryer modeli në mënyrë të brendshme për të marrë
  atë rezultat.

Kuota për argumentimin me Google Maps përputhet zakonisht me kufijtë e normës së modelit bazë të Gemini. Për informacion të detajuar për çmimet, shiko [faqen e çmimeve të Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=sq).

## Modelet e mbështetura

Modelet e mëposhtme mbështesin "Argumentimin me Google Maps":

| Modeli | Argumentimi me Google Maps |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=sq) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=sq) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=sq) | ✔️ |
| [Versioni paraprak i Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=sq) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=sq) | ✔️ |
| [Pamja paraprake e Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=sq) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=sq) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=sq) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=sq) | ✔️ |

## Kombinimet e mbështetura të veglave

Mund të përdorësh "Argumentimin me Google Maps" me veglat e tjera të integruara, si p.sh.
[Argumentimi me "Kërko në Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq) (mbështetet në
Gemini 3.5 Flash-Lite dhe modelet e mëvonshme) për të mundësuar raste përdorimi më kompleks.
Modelet e Gemini 3
mbështesin gjithashtu kombinimin e këtyre veglave të integruara me vegla të personalizuara (thirrja e funksioneve). Mëso më shumë në faqen e
[kombinimeve të veglave](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq).

## Çfarë ka më pas

- Provo [Argumentimin me "Kërko në Google" në "Librin e gatimeve" të Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=sq).
- Mëso rreth [veglave të tjera të disponueshme](https://ai.google.dev/gemini-api/docs/tools?hl=sq).
- Për të mësuar më shumë rreth praktikave më të mira të IA-së së përgjegjshme dhe filtrave të sigurisë të Gemini API, shiko [udhëzuesin e cilësimeve të sigurisë](https://ai.google.dev/gemini-api/docs/safety-settings?hl=sq).

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-09 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-09 UTC."],[],[]]
