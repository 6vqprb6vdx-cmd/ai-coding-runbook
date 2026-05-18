---
source_url: https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=he
fetched_at: 2026-05-18T12:59:02.337680+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ‫Gemini חושב

[למודלים מסדרות Gemini 3 ו-2.5](https://ai.google.dev/gemini-api/docs/models?hl=he) יש תהליך חשיבה שמשפר באופן משמעותי את יכולות החשיבה הרציונלית והתכנון הרב-שלבי שלהם. כך הם יעילים מאוד במשימות מורכבות כמו כתיבת קוד, מתמטיקה מתקדמת וניתוח נתונים.

כשמשתמשים במודל חשיבה, Gemini מסיק מסקנות באופן פנימי לפני שהוא משיב. ה-API של האינטראקציות חושף את ההסבר הזה באמצעות `thought` שלבים ייעודיים שמופיעים בסדר כרונולוגי לצד קריאות לפונקציות, קלט משתמש או פלט של מודל במערך `steps`.

כל שלב מחשבה מכיל שני שדות:

| שדה | חובה? | תיאור |
| --- | --- | --- |
| `signature` | ‫✅ כן | ייצוג מוצפן של מצב החשיבה הרציונלית הפנימית של המודל. תמיד מוצג, גם כשהמודל מבצע נימוק מינימלי. |
| `summary` | ❌ לא | מערך של תוכן (טקסט ו/או תמונות) שמסכם את הנימוקים. יכול להיות שיהיה ריק, בהתאם להגדרות של [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=he), אם המודל ביצע מספיק חשיבה רציונלית או בהתאם לסוג התוכן (לדוגמה, יכול להיות שלא יהיו סיכומי טקסט לתמונות לטנטיות). |

## אינטראקציות עם תכונת ההעמקה

התחלת אינטראקציה עם מודל חשיבה דומה לכל בקשת אינטראקציה אחרת. בשדה `model`, מציינים אחד מ[המודלים עם תמיכה בחשיבה](#thinking-levels):

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

אתם יכולים להפעיל סטרימינג של אינטראקציות של חשיבה כדי לקבל סיכומים מצטברים של מחשבות וחתימות במהלך היצירה. במדריך [הזרמת אינטראקציות](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=he#streaming-with-thinking) אפשר לקרוא על סוגי אירועים, סוגי דלתא ודוגמאות קוד.

## סיכומי מחשבות

סיכומי מחשבות מספקים תובנות לגבי תהליך הנימוק הפנימי של המודל.
כברירת מחדל, מוחזר רק הפלט הסופי. אפשר להפעיל סיכומי מחשבות באמצעות `thinking_summaries`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

בלוק מחשבה יכול להכיל **רק חתימה ללא סיכום** במקרים הבאים:

- בקשות פשוטות, שבהן המודל לא נימק מספיק כדי ליצור סיכום
- `thinking_summaries: "none"`, במקרים שבהם הסיכומים מושבתים באופן מפורש
- יכול להיות שלסוגים מסוימים של תוכן מחשבות, כמו תמונות, לא יהיו סיכומים של טקסט

הקוד צריך תמיד לטפל בבלוקים של מחשבות שבהם `summary` ריק או לא קיים.

## שליטה בחשיבה

מודלים של Gemini חושבים באופן דינמי כברירת מחדל, ומתאימים אוטומטית את כמות המאמץ הנדרש להסקה על סמך מורכבות הבקשה. אפשר לשלוט בהתנהגות הזו באמצעות הפרמטר `thinking_level`.

| מודל | חשיבה כברירת מחדל | רמות נתמכות |
| --- | --- | --- |
| gemini-3.1-pro-preview | מופעל (גבוהה) | נמוך, בינוני, גבוה |
| gemini-3-flash-preview | מופעל (גבוהה) | מינימלי, נמוך, בינוני, גבוה |
| gemini-3-pro-preview | מופעל (גבוהה) | נמוך, גבוה |
| ‫gemini-2.5-pro | מופעל | נמוך, בינוני, גבוה |
| gemini-2.5-flash | מופעל | נמוך, בינוני, גבוה |
| gemini-2.5-flash-lite | מושבת | נמוך, בינוני, גבוה |

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## חתימות של תהליכי חשיבה

חתימות מחשבה הן ייצוגים מוצפנים של ההיגיון הפנימי של המודל. הם נדרשים לשמור על רצף של נימוקים לאורך אינטראקציות עוקבות.

ממשק Interactions API מפשט את הטיפול בחתימות מחשבה בהשוואה ל-`generateContent` API.

### מצב עם שמירת מצב (מומלץ)

כברירת מחדל, כשמשתמשים ב-Interactions API במצב stateful (על ידי הגדרת `store: true` והעברת `previous_interaction_id` בתורות הבאות), השרת מנהל באופן אוטומטי את מצב השיחה, כולל כל בלוקי המחשבה והחתימות. במצב הזה, לא צריך לעשות שום דבר לגבי חתימות. הם מטופלים באופן מלא בצד השרת.

### מצב בלי שמירת מצב

אם אתם מנהלים את מצב השיחה בעצמכם (מצב בלי שמירת מצב) ומעבירים את ההיסטוריה המלאה של הקלט והפלט בכל בקשה:

- **חובה** לשלוח מחדש את כל הבלוקים של `thought` בדיוק כפי שהם התקבלו מהמודל.
- **חשוב** לא להסיר או לשנות את בלוקי המחשבה מההיסטוריה, כי הם מכילים את החתימות שנדרשות כדי שהמודל ימשיך את החשיבה הרציונלית שלו.
- כשמחליפים מודלים במהלך סשן, עדיין צריך לשלוח מחדש את בלוקי המחשבה של המודל הקודם. הקצה העורפי מנהל את התאימות.

## תמחור

כשהתכונה 'חשיבה' מופעלת, התמחור של התגובה הוא סכום האסימונים של הפלט והאסימונים של החשיבה. אפשר לקבל את המספר הכולל של טוקנים של חשיבה שנוצרו מהשדה `total_thought_tokens`.

### Python

```
# This will only work for SDK newer than 2.0.0
# ...
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// ...
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

מודלים של חשיבה יוצרים מחשבות מלאות כדי לשפר את האיכות של התשובה הסופית, ואז יוצרים [סיכומים](#summaries) כדי לספק תובנות לגבי תהליך החשיבה. התמחור מבוסס על מספר הטוקנים המלא שהמודל צריך ליצור, למרות שרק הסיכום מופק מה-API.

מידע נוסף על טוקנים זמין במדריך [ספירת טוקנים](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=he).

## שיטות מומלצות

כדי להשתמש במודלים של חשיבה בצורה יעילה, כדאי לפעול לפי ההנחיות הבאות.

- **בדיקת חשיבה רציונלית**: ניתוח סיכומי המחשבות כדי להבין את הכשלים ולשפר את ההנחיות.
- **שליטה בתקציב החשיבה**: אפשר להנחות את המודל לחשוב פחות כדי לחסוך בטוקנים כשמבקשים פלט ארוך.
- **משימות פשוטות**: השתמשו ב-Gemini כדי לאחזר עובדות או לסווג (למשל, "איפה הוקמה DeepMind?").
- **משימות מתונות**: השתמשו בחשיבה שמוגדרת כברירת מחדל כדי להשוות בין מושגים או לבצע נימוקים יצירתיים (למשל, השוואה בין מכוניות חשמליות למכוניות היברידיות).
- **משימות מורכבות**: שימוש ביכולת חשיבה מקסימלית לתכנות מתקדם, למתמטיקה או לתכנון רב-שלבי (למשל, פתרון בעיות מתמטיות של AIME).

## המאמרים הבאים

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=he): תשובות טקסט בסיסיות
- [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=he): התחברות לכלי עזר
- [מדריך Gemini 3](https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=he): תכונות ספציפיות למודל

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-16 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-16 (שעון UTC)."],[],[]]
