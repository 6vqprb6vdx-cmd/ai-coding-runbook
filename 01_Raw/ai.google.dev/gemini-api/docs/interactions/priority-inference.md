---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=he
fetched_at: 2026-06-15T06:23:35.416398+00:00
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

# הסקת עדיפות

‫Gemini Priority API הוא רמה של הסקת מסקנות (inference) בתשלום, שמיועדת לעומסי עבודה קריטיים לעסק שדורשים זמן אחזור נמוך ואמינות גבוהה ביותר, במחיר פרימיום. תעבורת נתונים ברמת עדיפות גבוהה מקבלת עדיפות על פני תעבורת נתונים ב-API רגיל וברמת Flex.

הסקת מסקנות לפי עדיפות זמינה בכל נקודות הקצה של Interactions API.

## איך משתמשים בעדיפות

כדי להשתמש ברמת העדיפות Priority, מגדירים את השדה `service_tier` בבקשה לערך `priority`. אם לא מציינים את המסלול בשדה, ברירת המחדל היא המסלול הרגיל.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    print(interaction.output_text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      console.log(interaction.output_text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## איך פועל הסקת העדיפות

ההסקה לפי עדיפות מעבירה בקשות לתורים של מחשוב ברמת קריטיות גבוהה, ומציעה ביצועים מהירים וצפויים לאפליקציות שפונות למשתמשים. המנגנון העיקרי שלו הוא שדרוג לאחור בצד השרת לעיבוד רגיל של תנועה שחורגת מהמגבלות הדינמיות, כדי להבטיח את יציבות האפליקציה במקום לגרום לכשל בבקשה.

| תכונה | עדיפות | רגיל | שרירים של סלע | Batch |
| --- | --- | --- | --- | --- |
| **תמחור** | ‫75% עד 100% יותר מבתוכנית Standard | מחיר מלא | הנחה של 50% | הנחה של 50% |
| **זמן אחזור** | שניות | שניות לדקות | דקות (יעד של 15-1 דקות) | עד 24 שעות |
| **אמינות** | גבוהה (לא ניתן להסרה) | גבוהה / בינונית-גבוהה | ללא התחייבות (ניתן להשמטה) | גבוהה (לתפוקה) |
| **ממשק** | סינכרוני | סינכרוני | סינכרוני | אסינכרוני |

### יתרונות עיקריים

- **זמן אחזור נמוך**: מיועד לזמני תגובה של שנייה אחת עבור כלים אינטראקטיביים של AI שפונים למשתמשים.
- **אמינות גבוהה**: התנועה מטופלת ברמת קריטיות גבוהה ביותר, ואין אפשרות להפחית אותה.
- **הורדה הדרגתית של רמת השירות**: אם יש עליות פתאומיות בתנועה שחורגות מהמגבלות הדינמיות, רמת השירות יורדת אוטומטית לרמה רגילה לצורך עיבוד, במקום שהעיבוד ייכשל. כך נמנעים שיבושים בשירות.
- **הפעלה חלקה**: משתמש באותה שיטת `create` סינכרון כמו בתוכניות הרגילה והגמישה.

### תרחישים לדוגמה

עיבוד בעדיפות גבוהה הוא פתרון אידיאלי לתהליכי עבודה קריטיים לעסק שבהם הביצועים והאמינות הם בעלי חשיבות עליונה.

- **אפליקציות אינטראקטיביות מבוססות-AI**: צ'אטבוטים וטייסים וירטואליים לשירות לקוחות, שבהם המשתמשים משלמים מחיר פרימיום ומצפים לתשובות מהירות ועקביות.
- **מנועי החלטות בזמן אמת**: מערכות שנדרשים בהן תוצאות מהימנות עם זמן אחזור נמוך, כמו תעדוף כרטיסים בשידור חי או זיהוי הונאות.
- **תכונות ללקוחות פרימיום**: מפתחים שצריכים להבטיח יעדים גבוהים יותר למדידת רמת השירות (SLO) ללקוחות משלמים.

### מגבלות קצב

לצריכה בעדיפות יש מגבלות קצב משלה, גם אם הצריכה נספרת במסגרת [מגבלות הקצב הכוללות של תנועה אינטראקטיבית](https://aistudio.google.com/rate-limit?hl=he). מגבלות ברירת המחדל על קצב הבקשות להסקת עדיפות הן **0.3x ממגבלת הקצב הרגילה עבור מודל או רמת שירות**

### לוגיקה של שדרוג לאחור

אם יש עומס ומתרחשת חריגה ממגבלות העדיפות, בקשות שחורגות מהמגבלות **משודרגות אוטומטית בצורה חלקה** לעיבוד רגיל במקום להיכשל עם שגיאה 503 או 429. בקשות ששודרגו לאחור יחויבו בתעריף הרגיל, ולא בתעריף הפרימיום של Priority.

### באחריות הלקוח

- **מעקב אחר תגובות**: מפתחים צריכים לעקוב אחר `x-gemini-service-tier`
  הכותרת בתגובת ה-API כדי לזהות אם הבקשות משודרגות לעיתים קרובות ל`standard`.
- **ניסיונות חוזרים**: לקוחות צריכים להטמיע לוגיקה של ניסיונות חוזרים או השהיה מעריכית לפני ניסיון חוזר (exponential backoff) לשגיאות רגילות, כמו `DEADLINE_EXCEEDED`.

## תמחור

המחיר של הסקת עדיפות גבוה ב-75% עד 100% מהמחיר של [ה-API הרגיל](https://ai.google.dev/gemini-api/docs/pricing?hl=he), והחיוב הוא לפי טוקן.

## מודלים נתמכים

המודלים הבאים תומכים בהסקת מסקנות בעדיפות גבוהה:

| מודל | הסקת עדיפות |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| ‫[Gemini 3.1 Pro (גרסת טרום-השקה)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## המאמרים הבאים

- [הסקת מסקנות גמישה](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=he) לצורך צמצום עלויות.
- [טוקנים](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=he): הסבר על טוקנים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
