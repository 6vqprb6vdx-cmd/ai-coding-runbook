---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he
fetched_at: 2026-05-25T13:01:30.904964+00:00
title: "\u05e2\u05d9\u05d2\u05d5\u05df \u05d1\u05e2\u05d6\u05e8\u05ea \u05de\u05e4\u05d5\u05ea Google \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# עיגון בעזרת מפות Google

עיגון בעזרת מפות Google מחבר בין היכולות הגנרטיביות של Gemini לבין הנתונים העשירים, העובדתיים והעדכניים של מפות Google. התכונה הזו מאפשרת למפתחים לשלב בקלות באפליקציות שלהם פונקציונליות שמתבססת על מיקום. כששאילתת משתמש מכילה הקשר שקשור לנתונים של מפות Google, מודל Gemini משתמש במפות Google כדי לספק תשובות מדויקות מבחינה עובדתית ועדכניות שרלוונטיות למיקום הספציפי או לאזור הכללי שהמשתמש ציין.

- **תשובות מדויקות שמודעות למיקום:** שימוש בנתונים המקיפים והעדכניים של מפות Google לשאילתות ספציפיות מבחינה גיאוגרפית.
- **התאמה אישית משופרת:** התאמת ההמלצות והמידע על סמך המיקומים שהמשתמשים סיפקו.
- **ווידג'טים ומידע לפי הקשר:** טוקנים של הקשר להצגת ווידג'טים אינטראקטיביים של מפות Google לצד תוכן שנוצר.

## שנתחיל?

בדוגמה הזו אפשר לראות איך לשלב את עיגון בעזרת מפות Google באפליקציה כדי לספק תשובות מדויקות לשאילתות של משתמשים, בהתאם למיקום שלהם. ההנחיה מבקשת המלצות מקומיות עם מיקום משתמש אופציונלי, ומאפשרת למודל Gemini להשתמש בנתונים של מפות Google.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: "gemini-3.5-flash",
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

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

## איך עיגון בעזרת מפות Google עובד

עיגון בעזרת מפות Google משלב את Gemini API עם המערכת האקולוגית של Google Geo באמצעות Maps API כמקור לעיגון. כששאילתה של משתמש מכילה הקשר גיאוגרפי, מודל Gemini יכול להפעיל את הכלי Grounding עם מפות Google. לאחר מכן המודל יכול ליצור תשובות שמבוססות על נתונים ממפות Google שרלוונטיים למיקום שצוין.

התהליך כולל בדרך כלל:

1. **שאילתת משתמש:** משתמש שולח שאילתה לאפליקציה שלכם, שיכולה לכלול הקשר גיאוגרפי (לדוגמה, "בתי קפה בקרבתי", "מוזיאונים בסן פרנסיסקו").
2. **הפעלת כלי:** מודל Gemini, שמזהה את הכוונה הגיאוגרפית, מפעיל את הכלי 'עיגון בעזרת מפות Google'. אפשר לספק לכלי הזה את `latitude` ו`longitude` של המשתמש. הכלי הוא כלי לחיפוש טקסטואלי, והוא פועל באופן דומה לחיפוש במפות Google. כלומר, בשאילתות מקומיות ("בסביבה שלי") נעשה שימוש בקואורדינטות, בעוד שבשאילתות ספציפיות או לא מקומיות, סביר להניח שהמיקום המפורש לא ישפיע על התוצאות.
3. **אחזור נתונים:** שירות ה-עיגון בעזרת מפות Google שולח שאילתות למפות Google כדי לקבל מידע רלוונטי (למשל, מקומות, ביקורות, תמונות, כתובות, שעות פתיחה).
4. **יצירה מבוססת-קרקע:** נתוני המפות שאוחזרו משמשים ליצירת התשובה של מודל Gemini, כדי להבטיח דיוק עובדתי ורלוונטיות.
5. **אסימון של תגובה ווידג'ט:** המודל מחזיר תגובה טקסטואלית, שכוללת ציטוטים ממקורות במפות Google. אופציונלית, תגובת ה-API עשויה להכיל גם `google_maps_widget_context_token`, שיאפשר למפתחים להציג בווידג'ט של מפות Google בהקשר המתאים באפליקציה שלהם, כדי ליצור אינטראקציה ויזואלית.

## למה ומתי כדאי להשתמש בעיגון בעזרת מפות Google

עיגון בעזרת מפות Google מתאים במיוחד לאפליקציות שנדרש בהן מידע מדויק, עדכני וספציפי למיקום. הוא משפר את חוויית המשתמש באמצעות תוכן רלוונטי ומותאם אישית שמבוסס על מסד הנתונים הנרחב של מפות Google, שכולל יותר מ-250 מיליון מקומות ברחבי העולם.

כדאי להשתמש בעיגון בעזרת מפות Google כשהאפליקציה צריכה:

- חשוב לענות על השאלות שקשורות למיקום גיאוגרפי בצורה מלאה ומדויקת.
- פיתוח כלים לשיחות לתכנון טיולים ומדריכים מקומיים.
- המלצה על נקודות עניין על סמך מיקום והעדפות משתמש, כמו מסעדות או חנויות.
- ליצור חוויות מבוססות-מיקום לשירותים חברתיים, קמעונאיים או למשלוחי אוכל.

עיגון בעזרת מפות Google מצטיין בתרחישי שימוש שבהם נתונים עובדתיים עדכניים וקירבה הם קריטיים, כמו חיפוש של "בית הקפה הכי טוב בסביבה שלי" או קבלת הוראות הגעה.

## שיטות ופרמטרים של API

עיגון בעזרת מפות Google נחשף דרך Gemini API ככלי בשיטה [`generateContent`](https://ai.google.dev/api/generate-content?hl=he). כדי להפעיל ולהגדיר את עיגון בעזרת מפות Google, צריך לכלול אובייקט [`googleMaps`](https://ai.google.dev/api/caching?hl=he#GoogleMaps) בפרמטר `tools` של הבקשה.

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

בנוסף, הכלי [`googleMaps`](https://ai.google.dev/api/caching?hl=he#GoogleMaps) יכול לקבל פרמטר בוליאני `enableWidget`, שמשמש כדי לקבוע אם השדה [`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=he#GroundingMetadata) יוחזר בתשובה. אפשר להשתמש בערך הזה כדי להציג [ווידג'ט הקשרי של מקומות](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=he).

### JSON

```
{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
}
```

בנוסף, הכלי תומך בהעברת המיקום ההקשרי כ-`toolConfig`.

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

### הסבר על תגובת ההארקה

אם התשובה מבוססת על נתונים ממפות Google, היא תכלול את השדה [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=he#GroundingMetadata).
הנתונים המובנים האלה חיוניים לאימות ההצהרות וליצירת חוויית ציטוט עשירה באפליקציה, וגם לעמידה בדרישות השימוש בשירות.

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
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
```

‫Gemini API מחזיר את המידע הבא עם [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=he#GroundingMetadata):

- ‫`groundingChunks`: מערך של אובייקטים שמכילים את מקורות `maps` (`uri`,‏ `placeId` ו-`title`).
- ‫`groundingSupports`: מערך של נתחי טקסט לחיבור טקסט התגובה של המודל למקורות ב-`groundingChunks`. כל מקטע מקשר בין טווח טקסט (מוגדר על ידי `startIndex` ו-`endIndex`) לבין `groundingChunkIndices` אחד או יותר. זהו המפתח ליצירת ציטוטים בגוף הטקסט.
- ‫`googleMapsWidgetContextToken`: אסימון טקסט שאפשר להשתמש בו כדי להציג [ווידג'ט של מקומות בהקשר](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=he).

לדוגמה של קטע קוד שמראה איך לרנדר ציטוטים מוטבעים בטקסט, ראו [את הדוגמה](https://ai.google.dev/gemini-api/docs/google-search?hl=he#attributing_sources_with_inline_citations) במסמכי ההסבר על עיגון באמצעות חיפוש Google.

### הצגת הווידג'ט ההקשרי של מפות Google

כדי להשתמש ב-`googleMapsWidgetContextToken` שמוחזר, צריך [לטעון את Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=he).

## תרחישים לדוגמה

עיגון בעזרת מפות Google תומך במגוון תרחישים לדוגמה שמתבססים על מיקום. בדוגמאות הבאות מוסבר איך אפשר להשתמש בהנחיות ובפרמטרים שונים כדי להסתמך על נתונים ממפות Google. המידע בתוצאות המבוססות על נתונים במפות Google עשוי להיות שונה מהמצב בפועל.

### איך עונים על שאלות ספציפיות לגבי מקום

אתם יכולים לשאול שאלות מפורטות על מקום ספציפי ולקבל תשובות שמבוססות על ביקורות של משתמשים ב-Google ועל נתונים אחרים במפות Google.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: 'gemini-3.5-flash',
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

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

### התאמה אישית על סמך מיקום

לקבל המלצות שמותאמות להעדפות של משתמש ולאזור גיאוגרפי ספציפי.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: 'gemini-3.5-flash',
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

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

### עזרה בתכנון מסלול

יצירת תוכניות לכמה ימים עם הוראות הגעה ומידע על מיקומים שונים, מושלם לאפליקציות נסיעות.

בדוגמה הזו, `googleMapsWidgetContextToken` התבקש על ידי הפעלת הווידג'ט בכלי של מפות Google. כשהאפשרות הזו מופעלת, אפשר להשתמש בטוקן שמוחזר
כדי לעבד ווידג'ט הקשרי של מקומות באמצעות `<gmp-places-contextual> component`
מ-Google Maps JavaScript API.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
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

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {enableWidget: true}}],
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

    if (groundingMetadata.googleMapsWidgetContextToken) {
      console.log('-'.repeat(40));
      document.body.insertAdjacentHTML('beforeend', `<gmp-place-contextual context-token="${groundingMetadata.googleMapsWidgetContextToken}`"></gmp-place-contextual>`);
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {"enableWidget":"true"}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

כשמעבדים את הווידג'ט, הוא נראה בערך כך:

![דוגמה לווידג&#39;ט של מפות אחרי רינדור](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=he)

## דרישות לשימוש בשירות

בקטע הזה מתוארות דרישות השימוש בשירות Grounding with Google Maps.

### לעדכן את המשתמש לגבי השימוש במקורות של מפות Google

בכל תוצאה מבוססת-מקור במפות Google, תקבלו מקורות ב-`groundingChunks` שתומכים בכל תשובה. מוחזרים גם המטא-נתונים הבאים:

- ‫URI במקור
- title
- מזהה

כשמציגים תוצאות של עיגון בעזרת מפות Google, צריך לציין את המקורות המשויכים במפות Google ולעדכן את המשתמשים לגבי הדברים הבאים:

- המקורות של מפות Google צריכים להופיע מיד אחרי התוכן שנוצר ושנתמך על ידי המקורות. התוכן שנוצר נקרא גם תוצאה מבוססת-קרקע ב-Google Maps.
- מקורות המידע במפות Google צריכים להיות גלויים באינטראקציה אחת של המשתמש.

### הצגת מקורות של מפות Google עם קישורים למפות Google

לכל מקור ב-`groundingChunks` וב-`grounding_chunks.maps.placeAnswerSources.reviewSnippets`, צריך ליצור תצוגה מקדימה של הקישור בהתאם לדרישות הבאות:

- צריך לשייך כל מקור למפות Google בהתאם [להנחיות לשיוך טקסט במפות Google](#maps-attribution-guidelines).
- הצגת כותרת המקור שצוינה בתשובה.
- מקשרים למקור באמצעות הסמל `uri` או `googleMapsUri` שמופיע בתשובה.

בתמונות האלה מוצגות הדרישות המינימליות להצגת המקורות והקישורים למפות Google.

![הנחיה עם תשובה שכוללת מקורות](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=he)

אפשר לכווץ את תצוגת המקורות.

![הנחיה עם תשובה ומקורות במצב מכווץ](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=he)

אופציונלי: אפשר להוסיף לתצוגה המקדימה של הקישור תוכן נוסף, כמו:

- [סמל האתר של מפות Google](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=he)
  מופיע לפני טקסט הקרדיט של מפות Google.
- תמונה מכתובת ה-URL של המקור (`og:image`).

מידע נוסף על חלק מספקי הנתונים של מפות Google ועל תנאי הרישיון שלהם מופיע [בהודעות המשפטיות של מפות Google ו-Google Earth](https://www.google.com/help/legalnotices_maps/?hl=he).

### הנחיות לציון מקור במפות Google

כשמציינים את המקורות במפות Google בטקסט, צריך לפעול לפי ההנחיות הבאות:

- אל תשנו את הטקסט 'מפות Google' בשום צורה:
  - אל תשנו את האותיות הרישיות של מפות Google.
  - אל תפצלו את כתובת מפות Google לכמה שורות.
  - אסור להתאים את מפות Google לשוק המקומי בשפה אחרת.
  - כדי למנוע מדפדפנים לתרגם את מפות Google, משתמשים בתכונת ה-HTML‏ translate="no".
- מעצבים את הטקסט במפות Google כמו שמתואר בטבלה הבאה:

| נכס | סגנון |
| --- | --- |
| `Font family` | Roboto. טעינת הגופן היא אופציונלית. |
| `Fallback font family` | כל גופן sans serif שמשמש כבר במוצר או 'Sans-Serif' כדי להפעיל את גופן המערכת שמוגדר כברירת מחדל |
| `Font style` | רגיל |
| `Font weight` | 400 |
| `Font color` | לבן, שחור (#1F1F1F) או אפור (#5E5E5E). שומרים על ניגודיות נגישה (4.5:1) ביחס לרקע. |
| `Font size` | - גודל גופן מינימלי: 12sp - גודל גופן מקסימלי: ‎16sp - מידע על sp זמין במאמר בנושא יחידות של גודל גופן ב[אתר Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | רגיל |

#### דוגמה ל-CSS

קוד ה-CSS הבא מעבד את מפות Google עם סגנון הטיפוגרפיה והצבע המתאימים על רקע לבן או בהיר.

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

### טוקן הקשר, מזהה המקום ומזהה הביקורת

הנתונים של מפות Google כוללים אסימון הקשר, מזהה מקום ומזהה ביקורת. יכול להיות שתשמרו במטמון, תאחסנו ותייצאו את נתוני התשובות הבאים:

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

המגבלות נגד שמירה במטמון בתנאים של עיגון בעזרת מפות Google לא חלות.

### פעילות אסורה ואזור אסור

כדי לשמור על הבטיחות והאמינות של פלטפורמת מפות Google, יש הגבלות נוספות על תוכן ופעילויות מסוימים ב-Grounding עם מפות Google. בנוסף להגבלות השימוש שמפורטות ב[תנאים](https://ai.google.dev/gemini-api/terms?hl=he#grounding-with-google-maps):

- לא תשתמשו ב-עיגון בעזרת מפות Google לפעילויות בסיכון גבוה, כולל שירותי תגובה למקרי חירום.
- לא תפיצו או תשווקו את האפליקציה שלכם שמציעה Grounding עם מפות Google בשטח אסור. מידע נוסף זמין במאמר בנושא [אזורים אסורים ב-Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=he).
  רשימת הטריטוריות האסורות עשויה להתעדכן מעת לעת.

## שיטות מומלצות

- **ציון מיקום המשתמש:** כדי לקבל תשובות רלוונטיות ומותאמות אישית, צריך תמיד לכלול את `user_location` (קו רוחב וקו אורך) בהגדרה של `googleMapsGrounding` כשמיקום המשתמש ידוע.
- **הצגת הווידג'ט ההקשרי של מפות Google:** הווידג'ט ההקשרי מוצג באמצעות טוקן ההקשר, `googleMapsWidgetContextToken`, שמוחזר בתגובה של Gemini API ויכול לשמש להצגת תוכן חזותי ממפות Google. מידע נוסף על הווידג'ט ההקשרי זמין במאמר [עיגון בעזרת מפות Google](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=he) במדריך למפתחים של Google.
- **ליידע את משתמשי הקצה:** חשוב ליידע את משתמשי הקצה בצורה ברורה שהנתונים של מפות Google משמשים למענה על השאילתות שלהם, במיוחד כשהכלי מופעל.
- **מעקב אחרי זמן האחזור:** באפליקציות שיש בהן ממשק שיחה, חשוב לוודא שזמן האחזור של תגובות מעוגנות (P95) נשאר בתוך סף קביל כדי לשמור על חוויית משתמש חלקה.
- **השבתה כשלא צריך:** עיגון בעזרת מפות Google מושבת כברירת מחדל. כדי לשפר את הביצועים ולהוזיל עלויות, מפעילים את האפשרות הזו (`"tools": [{"googleMaps": {}}]`) רק כששאילתה כוללת הקשר גיאוגרפי ברור.

## מגבלות

- **היקף גיאוגרפי:** עיגון בעזרת מפות Google זמין בכל העולם
- **תמיכה בדגמים:** מידע מופיע בקטע [דגמים נתמכים](#supported-models).
- **קלט/פלט מולטימודאלי:** בשלב הזה, עיגון בעזרת מפות Google לא תומך בקלט או בפלט מולטימודאליים מעבר לטקסט ולרכיבי widget של מפות הקשריות.
- **מצב ברירת מחדל:** הכלי 'עיגון בעזרת מפות Google' מושבת כברירת מחדל.
  צריך להפעיל אותו באופן מפורש בבקשות ל-API.

## תמחור ומגבלות על קצב יצירת הבקשות

התמחור של עיגון בעזרת מפות Google מבוסס על שאילתות. התעריף הנוכחי הוא
**‫25$‎ ל-1,000 הנחיות עם עיגון**. בתוכנית ללא תשלום יש גם עד 500 בקשות ביום. בקשה נספרת רק במסגרת המכסה אם ההנחיה מחזירה בהצלחה לפחות תוצאה אחת מבוססת-קרקע של מפות Google (כלומר, תוצאות שמכילות לפחות מקור אחד של מפות Google). אם נשלחות כמה שאילתות אל מפות Google מבקשה אחת, הן נספרות כבקשה אחת לצורך חישוב מגבלת הקצב.

מידע מפורט על התמחור זמין ב[דף התמחור של Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מודלים נתמכים

המודלים הבאים תומכים בעיגון בעזרת מפות Google:

| מודל | עיגון בעזרת מפות Google |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| ‫[Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |
| ‫[Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=he) | ✔️ |

## שילובים נתמכים של כלים

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו Grounding עם מפות Google) עם כלים מותאמים אישית (קריאה לפונקציה). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

## המאמרים הבאים

- כדאי לנסות את [המתכון לעיגון באמצעות חיפוש Google ב-Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=he).
- [מידע על כלים נוספים](https://ai.google.dev/gemini-api/docs/tools?hl=he)
- כדי לקבל מידע נוסף על שיטות מומלצות לאתיקה של בינה מלאכותית ועל מסנני הבטיחות של Gemini API, אפשר לעיין [במדריך להגדרות הבטיחות](https://ai.google.dev/gemini-api/docs/safety-settings?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
