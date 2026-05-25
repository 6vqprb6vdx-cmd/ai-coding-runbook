---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=he
fetched_at: 2026-05-25T12:59:36.951312+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# רזולוציית המדיה

הפרמטר `media_resolution` קובע איך Gemini API מעבד קלט של מדיה כמו תמונות, סרטונים ומסמכי PDF. הוא מגדיר את **מספר הטוקנים המקסימלי** שמוקצה לקלט של מדיה, וכך מאפשר לכם לאזן בין איכות התגובה לבין זמן האחזור והעלות. בקטע [ספירת טוקנים](#token-counts) מפורטים ערכי ברירת המחדל של הגדרות שונות והטוקנים שמתאימים להן.

יש שתי דרכים להגדיר את רזולוציית המדיה:

- [לכל חלק](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he#per-part-media-resolution) (רק ב-Gemini 3)
- [באופן גלובלי](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he#global-media-resolution) לכל בקשת `generateContent` (כל המודלים המולטי-מודאליים)

## רזולוציית מדיה לכל חלק (Gemini 3 בלבד)

‫Gemini 3 מאפשר לכם להגדיר את רזולוציית המדיה לאובייקטים ספציפיים של מדיה בבקשה, וכך לבצע אופטימיזציה פרטנית של השימוש בטוקנים. אפשר לשלב רמות רזולוציה שונות בבקשה אחת. לדוגמה, שימוש ברזולוציה גבוהה לתרשים מורכב וברזולוציה נמוכה לתמונה פשוטה שמוסיפה הקשר. ההגדרה הזו מחליפה כל הגדרה גלובלית לחלק ספציפי. הגדרות ברירת המחדל מפורטות בקטע [ספירת טוקנים](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
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

model_name = 'gemini-3.1-pro-preview'

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

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

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
    const model_name = 'gemini-3.1-pro-preview';
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

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

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
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## רזולוציה גלובלית של מדיה

אפשר להגדיר רזולוציית ברירת מחדל לכל חלקי המדיה בבקשה באמצעות התג `GenerationConfig`. התכונה הזו נתמכת בכל המודלים מרובי-האופנים. אם בקשה כוללת גם הגדרות גלובליות וגם [הגדרות לכל חלק](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he#per-part-media-resolution), ההגדרה לכל חלק מקבלת עדיפות עבור הפריט הספציפי הזה.

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
    model='gemini-3.5-flash',
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
      model: 'gemini-3.5-flash',
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
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## ערכי הרזולוציה הזמינים

ב-Gemini API מוגדרות רמות הרזולוציה הבאות למדיה:

- ‫`MEDIA_RESOLUTION_UNSPECIFIED`: הגדרת ברירת המחדל. מספר הטוקנים ברמה הזו משתנה באופן משמעותי בין Gemini 3 לבין מודלים קודמים של Gemini.
- ‫`MEDIA_RESOLUTION_LOW`: מספר נמוך יותר של טוקנים, שמוביל לעיבוד מהיר יותר ולעלות נמוכה יותר, אבל עם פחות פרטים.
- ‫`MEDIA_RESOLUTION_MEDIUM`: איזון בין רמת הפירוט, העלות וההשהיה.
- ‫`MEDIA_RESOLUTION_HIGH`: מספר גבוה יותר של טוקנים, שמספק יותר פרטים למודל לעבודה, אבל על חשבון עלייה בחביון ובעלות.
- ‫`MEDIA_RESOLUTION_ULTRA_HIGH` (לכל חלק בלבד): מספר האסימונים הגבוה ביותר, נדרש לתרחישי שימוש ספציפיים כמו [שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he).

שימו לב: `MEDIA_RESOLUTION_HIGH` מספק את הביצועים האופטימליים ברוב תרחישי השימוש.

המספר המדויק של הטוקנים שנוצרים לכל אחת מהרמות האלה תלוי ב**סוג המדיה** (תמונה, סרטון, PDF) וב**גרסת המודל**.

## מספר הטוקנים

בטבלאות הבאות מופיע סיכום של מספר הטוקנים המשוער לכל ערך `media_resolution` ולכל סוג מדיה לכל משפחת מודלים.

**מודלים של Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **תמונה** | **סרטון** | **PDF** |
| ‫`MEDIA_RESOLUTION_UNSPECIFIED` (ברירת מחדל) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | ‫280 + טקסט מותאם |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | ‫560 + טקסט מותאם |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | ‫1120 + טקסט מותאם |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | לא רלוונטי | לא רלוונטי |

**מודלים של Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **תמונה** | **סרטון** | **PDF (נסרק)** | **PDF (Native)** |
| ‫`MEDIA_RESOLUTION_UNSPECIFIED` (ברירת מחדל) | ‫256 + Pan & Scan (~2048) | 256 | ‫256 + OCR | ‫256 + טקסט מותאם |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | ‫64 + OCR | ‫64 + טקסט מותאם |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | ‫256 + OCR | ‫256 + טקסט מותאם |
| `MEDIA_RESOLUTION_HIGH` | ‫256 + Pan & Scan | 256 | ‫256 + OCR | ‫256 + טקסט מותאם |

## בחירת הרזולוציה המתאימה

- **ברירת מחדל (`UNSPECIFIED`):** מתחילים עם ברירת המחדל. הוא מותאם לאיזון טוב בין איכות, זמן אחזור ועלות ברוב התרחישים הנפוצים.
- ‫**`LOW`:** מתאים לתרחישים שבהם העלות והחביון הם בעלי חשיבות עליונה, ופרטים מדויקים פחות קריטיים.
- ‫**`MEDIUM` / `HIGH`:** הגדלת הרזולוציה כשנדרשת הבנה של פרטים מורכבים במדיה. השימוש בתכונה הזו נדרש לרוב לניתוח חזותי מורכב, לקריאת תרשימים או להבנת מסמכים ארוכים.
- ‫**`ULTRA HIGH`** – זמין רק להגדרה לכל חלק. מומלץ לתרחישי שימוש ספציפיים, כמו שימוש במחשב או במקרים שבהם בדיקות מראות שיפור ברור לעומת `HIGH`.
- **שליטה בכל חלק (Gemini 3):** אופטימיזציה של השימוש בטוקנים. לדוגמה, בהנחיה עם כמה תמונות, אפשר להשתמש ב-`HIGH` לתרשים מורכב וב-`LOW` או ב-`MEDIUM` לתמונות פשוטות יותר שנותנות הקשר.

**הגדרות מומלצות**

ברשימה הבאה מפורטות הגדרות הרזולוציה המומלצות לכל סוג מדיה נתמך.

|  |  |  |  |
| --- | --- | --- | --- |
| **סוג המדיה** | **הגדרה מומלצת** | **מספר הטוקנים המקסימלי** | **הנחיות לשימוש** |
| **תמונות** | `MEDIA_RESOLUTION_HIGH` | 1120 | מומלץ לרוב משימות ניתוח התמונות כדי להבטיח איכות מקסימלית. |
| **קובצי PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | אופטימלי להבנת מסמכים; האיכות בדרך כלל מגיעה לרוויה ב-`medium`. הגדלה ל-`high` משפרת לעיתים רחוקות את תוצאות ה-OCR במסמכים רגילים. |
| **סרטון** (כללי) | `MEDIA_RESOLUTION_LOW` (או `MEDIA_RESOLUTION_MEDIUM`) | ‫70 (לכל פריים) | **הערה:** כשמדובר בסרטונים, ההגדרות `low` ו-`medium` מטופלות באופן זהה (70 טוקנים) כדי לייעל את השימוש בהקשר. זה מספיק לרוב המשימות של זיהוי ותיאור פעולות. |
| **סרטון** (עם הרבה טקסט) | `MEDIA_RESOLUTION_HIGH` | ‫280 (לכל פריים) | נדרש רק אם תרחיש השימוש כולל קריאת טקסט צפוף (OCR) או פרטים קטנים בתוך פריים של סרטון. |

חשוב תמיד לבדוק ולהעריך את ההשפעה של הגדרות רזולוציה שונות על האפליקציה הספציפית שלכם, כדי למצוא את האיזון הטוב ביותר בין איכות, זמן אחזור ועלות.

## סיכום תאימות הגרסה

- ה-enum‏ `MediaResolution` זמין לכל המודלים שתומכים בקלט מדיה.
- מספר הטוקנים שמשויך לכל רמת enum **שונה** בין מודלים של Gemini 3 לבין גרסאות קודמות של Gemini.
- ההגדרה `media_resolution` על אובייקטים `Part` ספציפיים **בלעדית למודלים של Gemini 3**.

## השלבים הבאים

- במדריכים בנושא [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he), [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he) ו[הבנת מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he) אפשר לקרוא מידע נוסף על היכולות המולטי-מודאליות של Gemini API.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
