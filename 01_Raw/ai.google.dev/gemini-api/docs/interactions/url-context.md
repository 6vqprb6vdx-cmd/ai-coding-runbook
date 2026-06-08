---
source_url: https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=he
fetched_at: 2026-06-08T14:59:06.481262+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ההקשר של כתובת ה-URL

הכלי 'הקשר של כתובת URL' מאפשר לכם לספק למודלים הקשר נוסף בצורה של כתובות URL. אם תכללו כתובות URL בבקשה, המודל יוכל לגשת לתוכן מהדפים האלה (כל עוד כתובת ה-URL לא שייכת לסוג שמופיע [בקטע המגבלות](#limitations)) כדי לשפר את התשובה שלו.

הכלי 'הקשר של כתובת URL' שימושי למשימות כמו:

- **חילוץ נתונים**: שליפת מידע ספציפי כמו מחירים, שמות או ממצאים מרכזיים מכמה כתובות URL.
- **השוואת מסמכים**: ניתוח של כמה דוחות, מאמרים או קובצי PDF כדי לזהות הבדלים ולעקוב אחרי מגמות.
- **סינתזה ויצירת תוכן**: שילוב מידע מכמה כתובות URL של מקורות כדי ליצור סיכומים מדויקים, פוסטים בבלוג או דוחות.
- **ניתוח קוד ומסמכים**: אפשר להפנות למאגר GitHub או למסמכים טכניים כדי לקבל הסבר על קוד, ליצור הוראות הגדרה או לקבל תשובות לשאלות.

בדוגמה הבאה אפשר לראות איך משווים בין שני מתכונים מאתרים שונים.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## איך זה עובד

הכלי 'הקשר כתובת ה-URL' משתמש בתהליך אחזור דו-שלבי כדי לאזן בין מהירות, עלות וגישה לנתונים עדכניים. כשמספקים כתובת URL, הכלי מנסה קודם לשלוף את התוכן ממטמון אינדקס פנימי. הוא פועל כמטמון שעבר אופטימיזציה גבוהה. אם כתובת URL לא זמינה באינדקס (למשל, אם מדובר בדף חדש מאוד), הכלי יחזור אוטומטית לאחזור של הגרסה הפעילה.
הכלי ניגש ישירות לכתובת ה-URL כדי לאחזר את התוכן שלה בזמן אמת.

## שילוב עם כלים אחרים

אפשר לשלב את הכלי להקשר של כתובת URL עם כלים אחרים כדי ליצור תהליכי עבודה יעילים יותר.

[מודלים של Gemini 3](#supported-models) תומכים בשילוב של כלים מובנים (כמו הקשר של כתובת URL) עם כלים מותאמים אישית (הפעלת פונקציות). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=he).

### עיגון בנתונים באמצעות חיפוש

אם מפעילים גם את ההגדרה 'הקשר של כתובת ה-URL' וגם את ההגדרה [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he), המודל יכול להשתמש ביכולות החיפוש שלו כדי למצוא מידע רלוונטי באינטרנט, ואז להשתמש בכלי 'הקשר של כתובת ה-URL' כדי לקבל הבנה מעמיקה יותר של הדפים שהוא מוצא. הגישה הזו יעילה במיוחד להנחיות שדורשות חיפוש רחב וניתוח מעמיק של דפים ספציפיים.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## הסבר על התשובה

כשהמודל משתמש בכלי ההקשר של כתובת ה-URL, תשובת הטקסט שלו כוללת הערות מוטבעות
`url_citation` בבלוק התוכן של הטקסט. כל הערה מקשרת קטע של טקסט התשובה (באמצעות `start_index` ו-`end_index`) לכתובת ה-URL של המקור שממנו הוא נלקח. זו הדרך העיקרית להצגת ציטוטים באפליקציה שלכם. [בדוגמה הראשית שלמעלה](#get-started) מוסבר איך לחלץ אותם.

התגובה כוללת גם שלב `url_context_result` עם מטא-נתונים לגבי כל ניסיון לאחזור כתובת URL (סטטוס, כתובת URL שאוחזרה). האפשרות הזו שימושית בעיקר לניפוי באגים.

### בדיקות אבטחה

המערכת מבצעת בדיקה של כתובות ה-URL כדי לוודא שהן עומדות בתקני הבטיחות. אם כתובת URL נכשלת בבדיקה הזו, בשלב `url_context_result` המתאים יוצג `status` עם הערך `"unsafe"`.

### ספירת הטוקנים

התוכן שאוחזר מכתובות ה-URL שציינתם בהנחיה נספר כחלק מאסימוני הקלט. אפשר לראות את מספר האסימונים באובייקט `usage` של האינטראקציה. לדוגמה:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

המחיר לכל טוקן תלוי במודל שבו משתמשים. פרטים נוספים זמינים בדף [התמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מודלים נתמכים

| מודל | ההקשר של כתובת ה-URL |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| ‫[Gemini 3.1 Pro (גרסת טרום-השקה)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## שיטות מומלצות

- **צריך לספק כתובות URL ספציפיות**: כדי לקבל את התוצאות הטובות ביותר, צריך לספק כתובות URL ישירות לתוכן שרוצים שהמודל ינתח. המודל יאחזר תוכן רק מכתובות ה-URL שתספקו, ולא מקישורים מוטמעים.
- **בודקים את הנגישות**: מוודאים שכתובות ה-URL שציינתם לא מובילות לדפים שנדרשת בהם התחברות או שהם נמצאים מאחורי חומת תשלום.
- **שימוש בכתובת ה-URL המלאה**: צריך לציין את כתובת ה-URL המלאה, כולל הפרוטוקול (למשל, https://www.google.com ולא רק google.com).

## מגבלות

- מגבלת בקשות: הכלי יכול לעבד עד 20 כתובות URL לכל בקשה.
- גודל התוכן של כתובת URL: הגודל המקסימלי של תוכן שאוחזר מכתובת URL יחידה הוא 34MB.
- נגישות לכולם: כתובות ה-URL צריכות להיות נגישות לכולם באינטרנט.
  אין תמיכה בכתובות localhost (לדוגמה, localhost,‏ 127.0.0.1), ברשתות פרטיות ובשירותי מנהור (לדוגמה, ngrok,‏ pinggy).
- ‫Gemini API בלבד: הקשר של כתובת ה-URL זמין רק ב-Gemini API, ולא דרך Gemini Enterprise Agent Platform.

### סוגי תוכן נתמכים ולא נתמכים

הכלי יכול לחלץ תוכן מכתובות URL עם סוגי התוכן הבאים:

- טקסט (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- תמונה (image/png, ‏ image/jpeg, ‏ image/bmp, ‏ image/webp)
- ‫PDF (application/pdf)

סוגי התוכן הבאים **לא** נתמכים:

- תוכן שזמין רק לאחר תשלום
- סרטונים ב-YouTube (במאמר בנושא [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=he#youtube) מוסבר איך לעבד כתובות URL של סרטונים ב-YouTube)
- קבצים ב-Google Workspace, כמו מסמכים או גיליונות אלקטרוניים של Google
- קובצי וידאו ואודיו

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
