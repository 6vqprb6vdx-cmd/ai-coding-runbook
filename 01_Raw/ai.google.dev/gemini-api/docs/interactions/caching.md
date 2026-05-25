---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=he
fetched_at: 2026-05-25T13:03:15.715378+00:00
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

# שמירה במטמון של הקשר

בתהליך עבודה טיפוסי של AI, יכול להיות שתעבירו את אותם אסימוני קלט שוב ושוב למודל. ‫Gemini API מציע שמירה מרומזת במטמון כדי לשפר את הביצועים ולצמצם את העלויות.

## שמירה מרומזת במטמון

האפשרות 'שמירת נתונים במטמון באופן מרומז' מופעלת כברירת מחדל בכל המודלים של Gemini מגרסה 2.5 ואילך. אם הבקשה שלכם מגיעה למטמון, אנחנו מעבירים לכם באופן אוטומטי את החיסכון בעלויות. לא צריך לעשות שום דבר כדי להפעיל את התכונה הזו. בטבלה הבאה מפורט מספר האסימונים המינימלי של הקלט לכל מודל לצורך שמירת מטמון של ההקשר:

| מודל | מגבלת טוקנים מינימלית |
| --- | --- |
| Gemini 3.5 Flash | 1024 |
| ‫Gemini 3 Pro Preview | 4096 |
| Gemini ‎2.5 Flash | 1024 |
| Gemini ‎2.5 Pro | 4096 |

כדי להגדיל את הסיכוי לפגיעה במטמון משתמע:

- כדאי לנסות להוסיף בתחילת ההנחיה תוכן גדול ונפוץ
- ניסיון לשלוח בקשות עם קידומת דומה בפרק זמן קצר

אפשר לראות את מספר הטוקנים שהיו פגיעות במטמון בשדה `usage_metadata` (Python) או `usageMetadata` (JavaScript) של אובייקט התגובה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
