---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=he
fetched_at: 2026-07-20T04:45:32.384275+00:00
title: "\u05e1\u05e7\u05d9\u05e8\u05d4 \u05db\u05dc\u05dc\u05d9\u05ea \u05e9\u05dc \u05d4\u05e1\u05d5\u05db\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# סקירה כללית של הסוכנים

סוכנים מנוהלים ב-Gemini API מספקים לכם מסגרת סוכנים שניתנת להגדרה. קריאה אחת ל-API מספקת ארגז חול של Linux שבו הסוכן מסיק מסקנות, מריץ קוד, מנהל קבצים וגולש באינטרנט באופן אוטונומי.

[rocket\_launch

מדריך למתחילים

איך מתקשרים לסוכן, משדרים תשובות ויוצרים סוכן בהתאמה אישית](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he)
[smart\_toy

Antigravity Agent

יכולות, כלים, קלט מולטימודאלי ותמחור של הסוכן שמוגדר כברירת מחדל.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he)
[experiment

סוכנים ב-AI Studio

סביבת משחקים ויזואלית ליצירת אב טיפוס של סוכנים בלי לכתוב קוד.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=he)

## סוכנים מנוהלים זמינים

- **[סוכן Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he)**: סוכן מנוהל לשימוש כללי שמבוסס על Gemini 3.5 Flash. מריץ קוד, מנהל קבצים ומבצע חיפושים באינטרנט בתוך ארגז חול מאובטח של Linux שמארחת Google. אתם יכולים להוסיף לו הוראות, מיומנויות ונתונים משלכם כדי [ליצור סוכן בהתאמה אישית](https://ai.google.dev/gemini-api/docs/custom-agents?hl=he).
- ‫**[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he)**: סוכן מחקר אוטונומי שתכנן, מבצע ומסכם משימות מחקר מרובות שלבים לתרחישי שימוש כמו ניתוח שוק, בדיקת נאותות וסקירת ספרות.

## אבטחה ושיטות מומלצות

כל סוכן פועל בסביבת ארגז חול שמבודדת ברמת מערכת ההפעלה.
כברירת מחדל, לארגז החול יש גישה בלתי מוגבלת לרשת יוצאת. אתם יכולים להגביל או להשבית את הגישה לרשת באמצעות רשימת היתרים.

### גישה לרשת

כברירת מחדל, לסביבות יש גישה בלתי מוגבלת לרשת יוצאת. אפשר להשתמש ב`network` רשימת היתרים כדי להגביל את התנועה היוצאת לדומיינים ספציפיים או לדפוסי wildcard. פרטים על ההגדרה מופיעים במאמרים [רשימת כתובות IP ברשת שאפשר לגשת אליהן](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=he#network_allow_list) (AI Studio) או [כללי רשת](https://ai.google.dev/gemini-api/docs/custom-agents?hl=he#with_network_rules) (API).

### כלים חיצוניים וממשקי API

כדי להרחיב את היכולות של הסוכן, אפשר לקשר אליו כלים חיצוניים וממשקי API. מומלץ להשתמש רק בכלים ממקורות מהימנים ולהגדיר את ההרשאות להיקף המינימלי הנדרש. אפשר להחדיר את פרטי הכניסה בצורה מאובטחת באמצעות שינויים בכותרות של שרת proxy ליציאה, והם אף פעם לא נחשפים בתוך ארגז החול. הסוכן יכול להשתמש בכל פרטי כניסה שיש לו גישה אליהם, לכן כדאי לספק רק פרטי כניסה שאתם מוכנים להעניק להם גישה מלאה.

- משתמשים בחשבונות שירות או במפתחות API עם הרשאות מינימליות.
- עדיף להשתמש בטוקנים קצרי טווח במקום במפתחות ארוכי טווח.
- חשוב לספק פרטי כניסה רק אם אתם מוכנים להעניק את ההיקף המלא של ההרשאות.
- עדכון של פרטי הכניסה לפי לוח זמנים קבוע.

פרטים על הגדרת שינויים בכותרות מופיעים במאמר בנושא [אישורים](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he#credentials).

### פיקוח אנושי

תמיד כדאי לאמת את הפלט (קוד שנוצר, טרנספורמציות של נתונים, שינויים בהגדרות) לפני הפריסה, במיוחד במשימות שמשנות נתונים או יוצרות אינטראקציה עם מערכות חיצוניות.

## תמחור

סוכנים מנוהלים משתמשים ב[מודל של תשלום לפי שימוש](https://ai.google.dev/gemini-api/docs/pricing?hl=he#pricing-for-agents) שמבוסס על טוקנים של מודל Gemini ועל שימוש בכלי. אינטראקציה אחת יכולה להפעיל כמה לולאות של ניתוח, ובדרך כלל היא צורכת 100,000 עד 3 מיליון טוקנים. החישוב של הסביבה **לא מחויב** במהלך תקופת התצוגה המקדימה. [כאן](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he#availability-and-pricing) אפשר לראות פירוט של העלויות לכל משימה. סוכנים מנוהלים זמינים גם בתוכנית בחינם, עם מכסת שימוש ומגבלת קצב בחינם.

## מגבלות

| מגבלה | תיאור |
| --- | --- |
| **משך החיים של הסביבה** | סביבות נמחקות סופית אחרי 7 ימים של חוסר פעילות. |
| **VM Spin-down** | מכונות וירטואליות מושבתות אחרי פרק זמן קצר של חוסר פעילות כדי לחסוך במשאבים. הבקשה הבאה משחזרת את המצב (עם הפעלה במצב התחלתי). |
| **תוכנות שהותקנו מראש** | סביבה מבוססת-Ubuntu עם Python 3.12 ו-Node.js 22. מידע נוסף על תמונת הבסיס של הסביבה זמין במאמר בנושא [תוכנות שהותקנו מראש](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he#pre-installed-software). |
| **מספר הנציגים המקסימלי** | אפשר לנהל עד 1,000 סוכנים. |

## מסגרות של סוכנים

אפשר גם ליצור סוכנים באמצעות Gemini בעזרת המסגרות וערכות ה-SDK הבאות:

- ‫[**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=he): יצירת תהליכי עבודה מורכבים של אפליקציות ומערכות מרובות סוכנים באמצעות מבני גרפים.
- ‫[**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=he): חיבור סוכני Gemini לנתונים פרטיים כדי לשפר את תהליכי העבודה באמצעות RAG.
- ‫[**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=he): ארגון של סוכני AI אוטונומיים שמשתפים פעולה ומגלמים תפקידים.
- ‫[**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=he): פיתוח ממשקי משתמש וסוכנים מבוססי-AI ב-JavaScript/TypeScript.
- ‫[**Google ADK**](https://google.github.io/adk-docs/get-started/python/): מסגרת קוד פתוח ליצירה ולתיאום של סוכני AI עם יכולת פעולה הדדית.
- ‫[**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=he): יצירה של סוכני AI אוטונומיים באמצעות אותם כלים, לולאת סוכן וניהול הקשר שמופעלים על ידי Google Antigravity, ניתנים לתכנות ב-Python.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-16 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-16 (שעון UTC)."],[],[]]
