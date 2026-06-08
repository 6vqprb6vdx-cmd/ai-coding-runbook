---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=he
fetched_at: 2026-06-08T14:54:54.266081+00:00
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

# עיגון באמצעות חיפוש Google

עיגון באמצעות חיפוש Google מחבר את מודל Gemini לתוכן אינטרנט בזמן אמת, והוא פועל בכל השפות הזמינות. כך Gemini יכול לספק תשובות מדויקות יותר ולצטט מקורות שאפשר לאמת, גם אם הם פורסמו אחרי תאריך סף הידע שלו.

ההארקה עוזרת לכם ליצור אפליקציות שיכולות:

- **שיפור הדיוק העובדתי:** כדי לצמצם את ההזיות של המודל, התשובות מבוססות על מידע מהעולם האמיתי.
- **גישה למידע בזמן אמת:** מענה לשאלות על אירועים ונושאים עדכניים.
- **לספק ציטוטים:** כדי לבנות את אמון המשתמשים, כדאי להציג את המקורות של הטענות של המודל.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## איך עיגון באמצעות חיפוש Google פועל

כשמפעילים את הכלי `google_search`, המודל מטפל בכל תהליך העבודה של חיפוש, עיבוד וציטוט מידע באופן אוטומטי.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=he)

1. **הנחיית משתמש:** האפליקציה שולחת הנחיית משתמש ל-Gemini API עם הכלי `google_search` מופעל.
2. **ניתוח ההנחיה:** המודל מנתח את ההנחיה וקובע אם חיפוש ב-Google יכול לשפר את התשובה.
3. **חיפוש Google:** אם צריך, המודל יוצר באופן אוטומטי שאילתת חיפוש אחת או יותר ומריץ אותן.
4. **עיבוד תוצאות החיפוש:** המודל מעבד את תוצאות החיפוש, מסנתז את המידע ומנסח תשובה.
5. **תשובה מבוססת:** ה-API מחזיר תשובה סופית וידידותית למשתמש שמבוססת על תוצאות החיפוש. התשובה הזו כוללת את התשובה הטקסטואלית של המודל עם `annotations` מוטבעות שמכילות את הציטוטים, וגם את השלבים `google_search_call` ו-`google_search_result` עם שאילתות החיפוש וההצעות לחיפוש.

## הסבר על תגובת ההארקה

כשמקרקעים תשובה בהצלחה, פלט הטקסט של המודל כולל `annotations` מוטבע ישירות בגוש התוכן של הטקסט. ההערות האלה
כוללות פרטי ציטוט שמקשרים בין חלקים בתשובה לבין המקורות שלהם.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

שדות המפתח בתגובה:

- ‫`google_search_call` : מכיל את החיפוש `queries` שהמודל ביצע.
- ‫`google_search_result` : מכיל את `search_suggestions`, קטע HTML להצגת הצעות לחיפוש בממשק המשתמש. דרישות השימוש המלאות מפורטות [בתנאים ובהגבלות](https://ai.google.dev/gemini-api/terms?hl=he#grounding-with-google-search).
- `text` עם `annotations` : התשובה המסונתזת של המודל עם ציטוטים מוטבעים. כל הערה `url_citation` מקשרת פלח טקסט (מוגדר על ידי `start_index` ו-`end_index`) לכתובת URL של מקור. זהו המפתח ליצירת ציטוטים בתוך הטקסט.

אפשר גם להשתמש בעיגון באמצעות חיפוש Google בשילוב עם [כלי ההקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=he) כדי לעגן את התשובות גם בנתונים ציבוריים באינטרנט וגם בכתובות ה-URL הספציפיות שאתם מספקים.

## שיוך מקורות באמצעות ציטוטים מוטמעים

ממשק ה-API מחזיר הערות `url_citation` משולבות בתוכן של בלוק הטקסט,
כך שאתם יכולים לשלוט באופן מלא באופן שבו המקורות מוצגים בממשק המשתמש.
כל הערה כוללת את התגים `start_index` ו-`end_index` כדי לזהות את החלק בטקסט שהיא מצטטת. כך מחלצים ומציגים אותם.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

הפלט יציג את הטקסט ואחריו את הציטוטים שלו:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## תמחור

כשמשתמשים ב-עיגון באמצעות חיפוש Google עם Gemini 3, הפרויקט מחויב על כל שאילתת חיפוש שהמודל מחליט להריץ. אם המודל מחליט להריץ כמה שאילתות חיפוש כדי לענות על הנחיה אחת (לדוגמה, חיפוש של `"UEFA Euro 2024 winner"` ושל `"Spain vs England Euro 2024 final
score"` באותה קריאה ל-API), זה נחשב כשני שימושים מחויבים בכלי עבור הבקשה הזו. לצורך חיוב, אנחנו מתעלמים משאילתות חיפוש אינטרנט ריקות כשסופרים שאילתות ייחודיות. מודל החיוב הזה רלוונטי רק למודלים של Gemini 3. כשמשתמשים בהארקה של חיפוש עם Gemini 2.5 או מודלים ישנים יותר, החיוב על הפרויקט הוא לפי הנחיה.

למידע מפורט על התמחור, אפשר לעיין ב[דף התמחור של Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מודלים נתמכים

אפשר למצוא את כל היכולות בדף [סקירה כללית של המודל](https://ai.google.dev/gemini-api/docs/models?hl=he).

| מודל | עיגון באמצעות חיפוש Google |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| תצוגה מקדימה של תמונות ב-Gemini 3.1 Flash | ✔️ |
| ‫Gemini 3.1 Pro Preview | ✔️ |
| תצוגה מקדימה של תמונות ב-Gemini 3 Pro | ✔️ |
| ‫Gemini 3 Flash Preview | ✔️ |
| Gemini ‎2.5 Pro | ✔️ |
| Gemini ‎2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini ‎2.0 Flash | ✔️ |

## שילובים נתמכים של כלים

אפשר להשתמש בעיגון באמצעות חיפוש Google בשילוב עם כלים אחרים כמו [הרצת קוד](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=he) ו[הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=he) כדי להפעיל תרחישי שימוש מורכבים יותר.

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו עיגון באמצעות חיפוש Google) עם כלים בהתאמה אישית (קריאה לפונקציה). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=he).

## המאמרים הבאים

- אפשר לקרוא על כלים זמינים אחרים, כמו [הפעלת פונקציות](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=he).
- [כאן](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=he) מוסבר איך להוסיף לתיאור כתובות URL ספציפיות באמצעות הכלי 'הוספת הקשר של כתובת URL'.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
