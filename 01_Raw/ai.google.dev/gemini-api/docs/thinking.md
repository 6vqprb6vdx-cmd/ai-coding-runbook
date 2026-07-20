---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=he
fetched_at: 2026-07-20T04:45:25.281096+00:00
title: "\u05d7\u05e9\u05d9\u05d1\u05d4 \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# חשיבה של Gemini

[למודלים מסדרות Gemini 3 ו-2.5](https://ai.google.dev/gemini-api/docs/models?hl=he) יש 'תהליך חשיבה' שמשפר באופן משמעותי את יכולות החשיבה הרציונלית והתכנון הרב-שלבי שלהם. כך הם יעילים מאוד במשימות מורכבות כמו כתיבת קוד, מתמטיקה מתקדמת וניתוח נתונים.

כשמשתמשים במודל חשיבה, Gemini מנתח את ההנחיה באופן פנימי לפני שהוא משיב. ה-API של האינטראקציות חושף את ההסבר הזה באמצעות `thought` שלבים ייעודיים שמופיעים בסדר כרונולוגי לצד קריאות לפונקציות, קלט משתמש או פלט של מודל במערך `steps`.

כל שלב מחשבה מכיל שני שדות:

| שדה | חובה? | תיאור |
| --- | --- | --- |
| `signature` | ‫✅ כן | ייצוג מוצפן של מצב הנימוק הפנימי של המודל. תמיד מוצג, גם כשהמודל מבצע נימוק מינימלי. |
| `summary` | ❌ לא | מערך של תוכן (טקסט ו/או תמונות) שמסכם את הנימוקים. יכול להיות שיהיה ריק, בהתאם להגדרות של [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=he), אם המודל לא ביצע מספיק חשיבה רציונלית או בהתאם לסוג התוכן (לדוגמה, יכול להיות שלא יהיו סיכומי טקסט לתמונות לטנטיות). |

## אינטראקציות עם תכונת ההעמקה

התחלת אינטראקציה עם מודל חשיבה דומה לכל בקשת אינטראקציה אחרת. בשדה `model`, מציינים אחד מ[המודלים עם תמיכה בחשיבה](#thinking-levels):

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## סיכומי חשיבה

סיכומי מחשבות מספקים תובנות לגבי תהליך הנימוק הפנימי של המודל.
כברירת מחדל, מוחזר רק הפלט הסופי. אפשר להפעיל סיכומי מחשבות באמצעות `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

בלוק מחשבה יכול להכיל **רק חתימה ללא סיכום** במקרים הבאים:

- בקשות פשוטות, שבהן המודל לא נימק מספיק כדי ליצור סיכום
- `thinking_summaries: "none"`, במקרים שבהם הסיכומים מושבתים באופן מפורש
- יכול להיות שלסוגים מסוימים של תוכן מחשבות, כמו תמונות, לא יהיו סיכומי טקסט

הקוד צריך תמיד לטפל בבלוקים של מחשבות שבהם `summary` ריק או לא קיים.

## סטרימינג עם חשיבה

אפשר להשתמש בסטרימינג כדי לקבל סיכומים מצטברים של המחשבות במהלך היצירה.
בלוקי מחשבה מועברים באמצעות אירועים שנשלחים מהשרת (SSE) עם שני סוגים שונים של דלתא:

| סוג הדלתא | מכיל | מתי נשלח |
| --- | --- | --- |
| `thought_summary` | תוכן סיכום של טקסט או תמונה | דלתא אחת או יותר עם סיכום מצטבר |
| `thought_signature` | החתימה הקריפטוגרפית | הדלתא האחרונה לפני `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

התגובה בסטרימינג משתמשת באירועים שנשלחים מהשרת (SSE) ומורכבת משלבים ומאירועים, לדוגמה:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## שליטה בחשיבה

מודלים של Gemini חושבים באופן דינמי כברירת מחדל, ומתאימים באופן אוטומטי את כמות המאמץ שמושקע בהסקה על סמך מורכבות הבקשה. אפשר לשלוט בהתנהגות הזו באמצעות הפרמטר `thinking_level`.

| מודל | חשיבה כברירת מחדל | רמות נתמכות |
| --- | --- | --- |
| gemini-3.1-pro-preview | מופעל (גבוהה) | נמוך, בינוני, גבוה |
| gemini-3.1-flash-lite-image | מופעל (מינימלי) | מינימלי, גבוה |
| gemini-3-flash-preview | מופעל (גבוהה) | מינימלי, נמוך, בינוני, גבוה |
| gemini-3-pro-preview | מופעל (גבוהה) | נמוך, גבוה |
| gemini-3.5-flash | מופעל (בינוני) | מינימלי, נמוך, בינוני, גבוה |
| gemini-2.5-pro | מופעל | נמוך, בינוני, גבוה |
| gemini-2.5-flash | מופעל | נמוך, בינוני, גבוה |
| gemini-2.5-flash-lite | מושבת | נמוך, בינוני, גבוה |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## חתימות של מחשבות

חתימות מחשבה הן ייצוגים מוצפנים של ההיגיון הפנימי של המודל. הם נדרשים לשמור על רצף של נימוקים לאורך אינטראקציות עוקבות.

ממשק Interactions API מפשט את הטיפול בחתימות מחשבה בהשוואה ל-`generateContent` API.

### מצב עם שמירת מצב (מומלץ)

כברירת מחדל, כשמשתמשים ב-Interactions API במצב stateful (על ידי הגדרת `store: true` והעברת `previous_interaction_id` בתורות הבאות), השרת מנהל באופן אוטומטי את מצב השיחה, כולל כל בלוקי המחשבה והחתימות. במצב הזה, לא צריך לעשות שום דבר לגבי חתימות. הם מטופלים באופן מלא בצד השרת.

### מצב חסר סטטוס

אם אתם מנהלים את מצב השיחה בעצמכם (מצב בלי שמירת מצב) ומעבירים את ההיסטוריה המלאה של הקלט והפלט בכל בקשה:

- **חובה** לשלוח מחדש את כל הבלוקים של `thought` בדיוק כמו שהם התקבלו מהמודל.
- **חשוב** לא להסיר או לשנות את בלוקי המחשבה מההיסטוריה, כי הם מכילים את החתימות שנדרשות כדי שהמודל ימשיך את הנימוק שלו.
- כשמחליפים מודלים במהלך סשן, עדיין צריך לשלוח מחדש את בלוקי המחשבה של המודל הקודם. הקצה העורפי מנהל את התאימות.

## תמחור

כשהחשיבה מופעלת, התמחור של התשובה הוא סכום הטוקנים של הפלט והטוקנים של החשיבה. אפשר לקבל את המספר הכולל של טוקנים של חשיבה שנוצרו מהשדה `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

מודלים של חשיבה יוצרים מחשבות מלאות כדי לשפר את האיכות של התשובה הסופית, ואז יוצרים [סיכומים](#summaries) כדי לספק תובנות לגבי תהליך החשיבה. התמחור מבוסס על כל הטוקנים של המחשבה שהמודל צריך ליצור, למרות שרק הסיכום מופק מה-API.

מידע נוסף על טוקנים זמין במדריך [ספירת טוקנים](https://ai.google.dev/gemini-api/docs/tokens?hl=he).

## שיטות מומלצות

כדי להשתמש במודלים של חשיבה בצורה יעילה, כדאי לפעול לפי ההנחיות הבאות.

- **בדיקת ההיגיון**: ניתוח סיכומי המחשבות כדי להבין את הכשלים ולשפר את ההנחיות.
- **שליטה בתקציב החשיבה**: אפשר להנחות את המודל לחשוב פחות כדי ליצור פלט ארוך ולחסוך בטוקנים.
- **משימות פשוטות**: שימוש במינימום חשיבה או בחשיבה ברמה נמוכה כדי לאחזר עובדות או לבצע סיווג (לדוגמה, "איפה הוקמה DeepMind?").
- **משימות מורכבות**: השתמשו בחשיבה רגילה כדי להשוות בין מושגים או להסיק מסקנות יצירתיות (למשל, השוואה בין רכבים חשמליים לרכבים היברידיים).
- **משימות מורכבות**: כדי לכתוב קוד מתקדם, לפתור בעיות מתמטיות או לתכנן תוכניות מרובות שלבים (למשל, לפתור בעיות מתמטיות של AIME), כדאי להשתמש בחשיבה מקסימלית.

## המאמרים הבאים

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he): תשובות טקסט בסיסיות
- [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he): התחברות לכלי
- [מדריך Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=he): תכונות ספציפיות למודל

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-06 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-06 (שעון UTC)."],[],[]]
