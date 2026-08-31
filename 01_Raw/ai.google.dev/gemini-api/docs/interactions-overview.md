---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he
fetched_at: 2026-08-31T06:29:10.881250+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# Interactions API

‫Interactions API הוא הדרך הכי טובה לבנות באמצעות מודלים וסוכנים של Gemini. החל מיוני 2026, הוא זמין לכלל המשתמשים ומומלץ לכל הפרויקטים החדשים. ממשק ה-API המקורי של [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=he) עדיין נתמך באופן מלא, אבל הוא נחשב עכשיו לגרסה מדור קודם.

## למה כדאי להשתמש ב-Interactions API?

- **ממשק אוניברסלי לכל האפליקציות**: הממשק הזה נועד להיות הממשק הסטנדרטי לכל תרחישי השימוש, כולל יצירת טקסט בשיחה אחת, הבנה מולטי-מודאלית, פלט מובנה, תיאום כלים ותהליכי עבודה מבוססי-סוכן.
- **ממשק API יחיד למודלים ולסוכנים**: נקודת קצה (Endpoint) ותבנית מאוחדות לקריאה למודלים רגילים של Gemini וגם לסוכנים מיוחדים ישירות (כמו Deep Research וסוכנים מנוהלים בהתאמה אישית).
- **יכולות חדשות שזמינות לשימוש מיידי**: תכונות כמו מצב שיחה אופציונלי בצד השרת באמצעות `previous_interaction_id`, שלבי ביצוע שניתנים לצפייה לצורך ניפוי באגים ועיבוד ממשק משתמש, ו[ביצוע ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) של משימות ארוכות טווח באמצעות `background=true`.
- **עלות נמוכה יותר עם שיעורי פגיעה גבוהים יותר במטמון**: כשמשתמשים בשיחות מרובות תורות, ניהול מצב אופציונלי בצד השרת מאפשר שמירה יעילה יותר של הקשר במטמון בין התורות, וכך מקטין את עלויות האסימונים.
- **איפה יושקו התכונות החדשות**: מעכשיו, כל המודלים החדשים, היכולות המולטימודאליות, הכלים והתכונות של הסוכנים יושקו ב-Interactions API.

כברירת מחדל, ה-Interactions API שומר בקשות כדי שתוכלו להשתמש בתכונות של ניהול מצב בצד השרת באמצעות `previous_interaction_id`. כדי להפעיל התנהגות חסרת מצב, צריך להגדיר את
`store=false`. פרטים נוספים זמינים בקטע [שמירת נתונים](#data-storage-retention).

## שנתחיל?

- **הגדרת סוכן התכנות**: מתחברים ל-**Gemini Docs MCP** ומתקינים את מיומנות `gemini-interactions-api` כדי לתת לעוזר הדיגיטלי גישה ישירה למסמכי העזרה למפתחים ולשיטות המומלצות העדכניים ביותר. הוראות מפורטות מופיעות במאמר בנושא [הגדרת סוכן קידוד](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he).
- **מעבר מ-`generateContent`**: אם יש לכם שילוב קיים, כדאי לעיין [במדריך למעבר](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=he) כדי לעבור ל-Interactions API.
- **איך מתחילים**: פועלים לפי השלבים במדריך [איך מתחילים להשתמש ב-Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=he).

### מדריכים לתכונות

במדריכים האלה מוסבר על היכולות הספציפיות של Interactions API. אפשר להשתמש במתג בדפים האלה כדי לעבור בין generateContent לבין Interactions API:

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he)
- [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)
- [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he)
- [הבנת אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he)
- [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he)
- [עיבוד מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he)
- [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
- [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=he)
- [הסקת מסקנות גמישה](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)
- [הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)

## איך Interactions API פועל

ה-API של אינטראקציות מתמקד במשאב ליבה: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=he#Resource:Interaction). `Interaction` מייצג תור שלם בשיחה או במשימה. הוא משמש כתיעוד של סשן, ומכיל את כל ההיסטוריה של אינטראקציה כרצף כרונולוגי של **שלבי ביצוע**. השלבים האלה כוללים את המחשבות של המודל, קריאות לכלים ותוצאות בצד השרת או בצד הלקוח (כמו `function_call` ו-`function_result`), ואת `model_output` הסופי. המשאב המאוחסן (שמאוחזר באמצעות `interactions.get`) כולל גם `user_input` שלבים להקשר מלא, אבל התשובה `interactions.create` מחזירה רק שלבים שנוצרו על ידי המודל.

כשמתקשרים אל [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=he#CreateInteraction), יוצרים משאב `Interaction` חדש.

### ניהול מצב בצד השרת

אפשר להשתמש ב-`id` של אינטראקציה שהושלמה בקריאה הבאה באמצעות הפרמטר `previous_interaction_id` כדי להמשיך את השיחה. השרת משתמש במזהה הזה כדי לאחזר את היסטוריית השיחות, וכך לא צריך לשלוח מחדש את כל היסטוריית הצ'אט.

הפרמטר `previous_interaction_id` שומר רק את היסטוריית השיחות (קלט ופלט) באמצעות `previous_interaction_id`. הפרמטרים האחרים הם **בטווח האינטראקציה**
וחלים רק על האינטראקציה הספציפית שאתם יוצרים כרגע:

- `tools`
- `system_instruction`
- `generation_config` (כולל `thinking_level`,‏ `temperature` וכו')

כלומר, אם רוצים שהפרמטרים האלה יחולו, צריך לציין אותם מחדש בכל אינטראקציה חדשה. ניהול המצב בצד השרת הוא אופציונלי. אפשר גם לפעול במצב חסר מצב (stateless) על ידי שליחת היסטוריית השיחות המלאה בכל בקשה.

### אחסון ושמירה של נתונים

כברירת מחדל, ה-API שומר את כל אובייקטי האינטראקציה (`store=true`) כדי לפשט את השימוש בתכונות של ניהול מצב בצד השרת (עם `previous_interaction_id`), [הפעלה ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) (באמצעות `background=true`) ולמטרות ניטור.

- **מהדורה בתשלום**: המערכת שומרת את האינטראקציות למשך **55 ימים**.
- **רמת שירות בחינם**: המערכת שומרת את האינטראקציות למשך **יום אחד**.

אם לא רוצים בכך, אפשר להגדיר `store=false` בבקשה. הפקד הזה נפרד מניהול המצב. אתם יכולים לבחור לא לאחסן נתונים של אינטראקציות. עם זאת, חשוב לזכור ש-`store=false` לא תואם ל[הרצה ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) ומונע את השימוש ב-`previous_interaction_id` בתורות הבאות.

בפרויקטים בתוכנית בתשלום, אפשר להגדיר את חלון השמירה ב-[AI Studio](https://aistudio.google.com/logs?hl=he) כדי לסמן באופן אוטומטי יומנים למחיקה מאחסון הפרויקט אחרי 7, 14, 28 או 55 ימים. תקופת שמירה קצרה יותר עשויה להשפיע על אחזור שיחות קודמות.

אתם יכולים למחוק אינטראקציות שמורות בכל שלב באמצעות השיטה [`delete`](https://ai.google.dev/api/interactions-api?hl=he#deleteInteraction) באופן פרוגרמטי, שדורשת את מזהה האינטראקציה. ב-[AI Studio](https://aistudio.google.com/logs?hl=he) אפשר גם לראות ולנהל את יומני האינטראקציות המאוחסנים, כולל מחיקה מאחסון הפרויקט.

אחרי שתקופת השמירה תסתיים, הנתונים יימחקו באופן אוטומטי.

אובייקטים של אינטראקציות מעובדים בהתאם [לתנאים](https://ai.google.dev/gemini-api/terms?hl=he).

### צפייה באינטראקציות ב-AI Studio

ממשק ה-API שומר בקשות של Interactions API שמופעלות באמצעות `store=true` עבור פרויקטים ברמה בתשלום. אפשר לראות אותם ישירות ב[דף היומנים ב-Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=he). מידע נוסף זמין [במדריך ליומנים](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=he).

## שיטות מומלצות

- **שיעור מציאות במטמון**: שמירה במטמון באופן מרומז נתמכת במצב עם שמירת מצב ובמצב בלי שמירת מצב (ראו [מדריך למתחילים](https://ai.google.dev/gemini-api/docs/get-started?hl=he#4_multi-turn_conversations)). השימוש ב-`previous_interaction_id` (עם שמירת מצב) כדי להמשיך שיחות מאפשר למערכת להשתמש בקלות רבה יותר בשמירת מטמון מרומזת של היסטוריית השיחות, וכך לשפר את הביצועים ולהפחית את העלויות.
- **שילוב אינטראקציות**: אתם יכולים לשלב בין אינטראקציות עם נציג ועם מודל במהלך שיחה. לדוגמה, אפשר להשתמש בסוכן מיוחד, כמו סוכן Deep Research, לאיסוף נתונים ראשוני, ואז להשתמש במודל Gemini רגיל למשימות המשך כמו סיכום או עיצוב מחדש, ולקשר בין השלבים האלה באמצעות `previous_interaction_id`.

## מודלים וסוכנים נתמכים

| שם דגם | סוג | מזהה דגם |
| --- | --- | --- |
| Gemini 3.5 Flash | מודל | `gemini-3.5-flash` |
| ‫Gemini 3.1 Pro Preview | מודל | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | מודל | `gemini-3.1-flash-lite` |
| ‫Gemini 3 Flash Preview | מודל | `gemini-3-flash-preview` |
| Gemini ‎2.5 Pro | מודל | `gemini-2.5-pro` |
| Gemini ‎2.5 Flash | מודל | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | מודל | `gemini-2.5-flash-lite` |
| ‫Gemini 3 Pro Image | מודל | `gemini-3-pro-image` |
| תמונה של Gemini 3.1 Flash | מודל | `gemini-3.1-flash-image` |
| ‫Gemini 3.1 Flash TTS Preview | מודל | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | מודל | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | מודל | `gemma-4-26b-a4b-it` |
| תצוגה מקדימה של קליפ ב-Lyria 3 | מודל | `lyria-3-clip-preview` |
| גרסת טרום-השקה (Preview) של Lyria 3 Pro | מודל | `lyria-3-pro-preview` |
| גרסת טרום-השקה (Preview) של Deep Research | סוכן | `deep-research-preview-04-2026` |
| גרסת טרום-השקה (Preview) של Deep Research | סוכן | `deep-research-max-preview-04-2026` |
| תצוגה מקדימה של Antigravity | סוכן | `antigravity-preview-05-2026` |

## ערכות SDK

אתם יכולים להשתמש בגרסה העדכנית של Google GenAI SDK כדי לגשת ל-Interactions API.

- ב-Python, זו חבילת `google-genai` החל מגרסה `2.3.0`.
- ב-JavaScript, זה חבילת `@google/genai` מגרסה `2.3.0` ואילך.

מידע נוסף על התקנת ערכות ה-SDK זמין בדף [ספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he).

## מגבלות

- **MCP מרוחק**: Gemini 3 לא תומך ב-MCP מרוחק, אבל התמיכה הזו תגיע בקרוב.
- **תאימות של מודלים עם כמה תפניות**: כשמשלבים בין מודלים שונים בשיחה (עם שמירת מצב או בלי), המודלים הבאים צריכים לתמוך בשיטות הפלט של המודלים הקודמים כקלט. לדוגמה, אם יוצרים תמונה באמצעות `gemini-3.1-flash-image`, אי אפשר להמשיך את השיחה עם מודל שלא מקבל קלט של תמונות (כמו מודל שמקבל רק טקסט או מודל ליצירת מוזיקה כמו Lyria).

התכונות הבאות נתמכות על ידי [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=he) API, אבל **עדיין לא זמינות** ב-Interactions API:

- **[מטא-נתונים של סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he)**: השדה `video_metadata`, שמשמש להגדרת מרווחי זמן של קליפים וקצבי פריימים מותאמים אישית להבנת סרטונים.
- ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**
- **[הפעלת פונקציות אוטומטית (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=he#automatic_function_calling_python_only)**
- **[שמירה במטמון באופן מפורש](https://ai.google.dev/gemini-api/docs/caching?hl=he)**: שימו לב ששמירה במטמון באופן מרומז בצד השרת זמינה ב-Interactions API באמצעות `previous_interaction_id`.
- **[הגדרות בטיחות](https://ai.google.dev/gemini-api/docs/safety-settings?hl=he)**: הגדרות בטיחות בהתאמה אישית לא נתמכות ב-API של אינטראקציות.

## משוב

המשוב שלכם חשוב מאוד לפיתוח של Interactions API.
אתם יכולים לשתף את המחשבות שלכם, לדווח על באגים או לבקש תכונות ב[פורום הקהילה של מפתחי Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=he).

## המאמרים הבאים

- אפשר לנסות את [המדריך למתחילים ל-Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=he).
- [מידע נוסף על סוכן Deep Research ב-Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-16 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-16 (שעון UTC)."],[],[]]
