---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=he
fetched_at: 2026-07-06T05:13:19.359322+00:00
title: "\u05e8\u05d6\u05d5\u05dc\u05d5\u05e6\u05d9\u05d9\u05ea \u05d4\u05de\u05d3\u05d9\u05d4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# רזולוציית המדיה

הפרמטר `media_resolution` קובע איך Gemini API מעבד קלט של מדיה כמו תמונות, סרטונים ומסמכי PDF. הוא מגדיר את **מספר הטוקנים המקסימלי** שמוקצה לקלט של מדיה, וכך מאפשר לכם לאזן בין איכות התגובה לבין זמן האחזור והעלות. בקטע [ספירת אסימונים](#token-counts) מפורטים ערכי ברירת המחדל של הגדרות שונות והאסימונים שמתאימים להן.

אתם יכולים להגדיר את רזולוציית המדיה לאובייקטים ספציפיים של מדיה (פריטי תוכן) בבקשה (רק ב-Gemini 3).

## רזולוציית מדיה לכל פריט תוכן (Gemini 3 בלבד)

‫Gemini 3 מאפשר לכם להגדיר רזולוציית מדיה לאובייקטים ספציפיים של מדיה בבקשה, וכך לבצע אופטימיזציה פרטנית של השימוש בטוקנים. אפשר לשלב רמות רזולוציה שונות בבקשה אחת. לדוגמה, שימוש ברזולוציה גבוהה לתרשים מורכב וברזולוציה נמוכה לתמונה פשוטה שמוסיפה הקשר.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## ערכי הרזולוציה הזמינים

ב-Gemini API מוגדרות הרמות הבאות של רזולוציית מדיה:

- ‫`unspecified`: הגדרת ברירת המחדל. מספר הטוקנים ברמה הזו משתנה באופן משמעותי בין Gemini 3 לבין מודלים קודמים של Gemini.
- ‫`low`: מספר אסימונים נמוך יותר, שמוביל לעיבוד מהיר יותר ולעלות נמוכה יותר, אבל עם פחות פרטים.
- ‫`medium`: איזון בין רמת הפירוט, העלות וההשהיה.
- ‫`high`: מספר גבוה יותר של טוקנים, שמספק למודל יותר פרטים לעבודה, אבל על חשבון עלות גבוהה יותר וזמן אחזור ארוך יותר.
- ‫`ultra_high` (לכל פריט תוכן בלבד): מספר האסימונים הגבוה ביותר, נדרש לתרחישי שימוש ספציפיים כמו [שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he).

חשוב לזכור שההגדרה `high` מספקת את הביצועים האופטימליים ברוב תרחישי השימוש.

המספר המדויק של הטוקנים שנוצרו לכל אחת מהרמות האלה תלוי ב**סוג המדיה** (תמונה, סרטון, PDF) וב**גרסת המודל**.

## מספר הטוקנים

בטבלאות הבאות מפורטות ספירות האסימונים המשוערות לכל ערך של `media_resolution` ולכל סוג מדיה לכל משפחת מודלים.

**מודלים של Gemini 3**

| MediaResolution | תמונה | וידאו | PDF |
| --- | --- | --- | --- |
| ‫`unspecified` (ברירת מחדל) | 1120 | 70 | 560 |
| `low` | 280 | 70 | ‫280 + טקסט מותאם |
| `medium` | 560 | 70 | ‫560 + טקסט מותאם |
| `high` | 1120 | 280 | ‫1120 + טקסט מותאם |
| `ultra_high` | 2240 | לא רלוונטי | לא רלוונטי |

## בחירת הרזולוציה המתאימה

- **ברירת מחדל (`unspecified`):** מתחילים עם ברירת המחדל. הוא מותאם לאיזון טוב בין איכות, זמן אחזור ועלות ברוב תרחישי השימוש הנפוצים.
- ‫**`low`:** מתאים לתרחישים שבהם העלות והחביון הם בעלי חשיבות עליונה, ופרטים מדויקים פחות קריטיים.
- ‫**`medium` / `high`:** הגדלת הרזולוציה כשנדרשת הבנה של פרטים מורכבים במדיה. היכולת הזו נדרשת לעיתים קרובות לניתוח חזותי מורכב, לקריאת תרשימים או להבנת מסמכים עמוסים במידע.
- ‫**`ultra_high`** – זמין רק להגדרה של כל פריט תוכן. מומלץ לתרחישי שימוש ספציפיים, כמו שימוש במחשב, או במקרים שבהם בדיקות מראות שיפור ברור לעומת `high`.
- **שליטה בכל פריט תוכן (Gemini 3):** אופטימיזציה של השימוש בטוקנים. לדוגמה, בהנחיה עם כמה תמונות, אפשר להשתמש ב-`high` לתרשים מורכב וב-`low` או ב-`medium` לתמונות פשוטות יותר עם הקשר.

**הגדרות מומלצות**

ברשימה הבאה מפורטות הגדרות הרזולוציה המומלצות של המדיה לכל סוג מדיה נתמך.

| סוג מדיה | הגדרה מומלצת | מספר מקסימלי של טוקנים | הנחיות לשימוש |
| --- | --- | --- | --- |
| **תמונות** | `high` | 1120 | מומלץ לרוב משימות ניתוח התמונות כדי להבטיח איכות מקסימלית. |
| **קובצי PDF** | `medium` | 560 | אופטימלי להבנת מסמכים. האיכות מגיעה בדרך כלל לנקודת רוויה ב-`medium`. הגדלה ל-`high` משפרת לעיתים רחוקות את תוצאות ה-OCR במסמכים רגילים. |
| **סרטון** (כללי) | `low` (או `medium`) | ‫70 (לכל פריים) | **הערה:** כשמדובר בסרטונים, ההגדרות `low` ו-`medium` מטופלות באופן זהה (70 טוקנים) כדי לייעל את השימוש בהקשר. זה מספיק לרוב המשימות של זיהוי פעולות ותיאור שלהן. |
| **סרטון** (הרבה טקסט) | `high` | ‫280 (לכל פריים) | נדרש רק אם תרחיש השימוש כולל קריאת טקסט צפוף (OCR) או פרטים קטנים בתוך פריים של סרטון. |

חשוב תמיד לבדוק ולהעריך את ההשפעה של הגדרות רזולוציה שונות על האפליקציה, כדי למצוא את האיזון הטוב ביותר בין איכות, זמן אחזור ועלות.

## סיכום תאימות הגרסה

- הגדרת `resolution` בפריטי תוכן ספציפיים **זמינה רק במודלים של Gemini 3**.

## השלבים הבאים

- במדריכים בנושא [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he), [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he) ו[הבנת מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he) אפשר לקרוא מידע נוסף על היכולות המולטי-מודאליות של Gemini API.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-22 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-22 (שעון UTC)."],[],[]]
