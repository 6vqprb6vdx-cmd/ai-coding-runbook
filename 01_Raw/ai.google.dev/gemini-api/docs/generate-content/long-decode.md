---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=he
fetched_at: 2026-10-26T05:54:43.028998+00:00
title: "\u05e4\u05e2\u05e0\u05d5\u05d7 \u05d0\u05e8\u05d5\u05da \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# פענוח ארוך

התכונה "פענוח ארוך" מאפשרת ל-Gemini 4 Argon לחרוג ממגבלת הפלט לבקשה אחת במשימות של חשיבה מעמיקה, עד לחלון ההקשר המאוחד של מיליון טוקנים (1,048,576 טוקנים שמשותפים לקלט, לחשיבה ולפלט).

שינוי מזהה המודל לבדו לא מפעיל פענוח ארוך. בלי הגדרה נוספת, הפלט נעצר ב-64,000 אסימונים לקריאות בסטרימינג וב-32,000 אסימונים לקריאות שלא בסטרימינג. הדרך המהירה ביותר להפעיל פענוח ארוך היא לשדרג את Google GenAI SDK ולהגדיר את `max_output_tokens` לערך שגדול מ-65,536. במדריך הזה מוסבר איך פועל פענוח ארוך, מתי להשתמש בו ואיך להפעיל אותו באמצעות `generateContent`.

## How long decode works

בקשת סטרימינג או בקשת SDK אחת יוצרת עד 64,000 טוקנים, ובקשת REST שאינה סטרימינג יוצרת עד 32,000 טוקנים. כשתשובה דורשת יותר אסימונים, המודל יוצר אותה בכמה דילוגים של בקשה ותגובה, שכל אחד מהם ממשיך מהמקום שבו הדילוג הקודם נעצר.

- **מגבלה מאוחדת על טוקנים של קלט ופלט:** הקלט, תהליך החשיבה, בקשות להפעלת פונקציות והתשובה הסופית חולקים חלון אחד של מיליון טוקנים. הפלט יכול להשתמש בעד 1,048,576 אסימונים פחות אסימוני הקלט.
- **מגבלה על כל שלב:** שלב אחד מחזיר עד 65,536 טוקנים של פלט. בקשות REST שלא מבוססות על סטרימינג מחזירות עד 32,768.
- **אות המשך:** אם המודל מגיע למגבלה ונותרו לו אסימונים, התשובה מסתיימת ב-`finish_reason: CONTINUATION` וב-`continuation_token`.
- **הצעד הבא:** הלקוח שולח שוב את אותה בקשה עם הטוקן. המודל ממשיך מהמקום שבו הוא הפסיק.
- **סכום כולל אחד לכל הדילוגים:** `max_output_tokens` מגדיר את המספר הכולל של טוקנים לחשיבה ולפלט לכל הדילוגים ביחד.
- **אות עצירה:** כשהמודל משתמש בכל `max_output_tokens`, התשובה מסתיימת ב-`finish_reason: MAX_TOKENS`.

בבעיות קשות, ה-hop יכול להשתמש בכל הטוקנים שלו לחשיבה פנימית ולהחזיר טקסט ריק עם `continuation_token`. זה מצב תקין, והתשובה הסופית מגיעה בקפיצות הבאות.

## מגבלות ברירת המחדל של הפלט

אם לא משתמשים בפענוח ארוך, בקשה אחת נעצרת במגבלות הבאות לכל בקשה:

- **בקשות סטרימינג ובקשות ללא סטרימינג דרך Google GenAI SDK‏ (`generate_content`):** ברירת המחדל היא 64,000 טוקנים של פלט.
- **קריאות REST ישירות ללא סטרימינג (`generateContent`):** ברירת המחדל היא 32,000 טוקנים של פלט. אם מגדירים את `max_output_tokens` לערך שגדול מ-32,768 בקריאת REST ללא סטרימינג ובלי `continuation_token`, מוחזרת השגיאה `400`.

| איך קוראים למודל | מגבלת פלט בלי פענוח ארוך | פענוח ארוך בזמן ההפעלה | מה לעשות? |
| --- | --- | --- | --- |
| הגרסה העדכנית של Google GenAI SDK | 64K | כן, ה-SDK ממשיך בשבילך | מגדירים את `max_output_tokens`. |
| ‫Google GenAI SDK, גרסה ישנה יותר, ללא סטרימינג | 64K | לא | משדרגים את ה-SDK. |
| REST `streamGenerateContent` | 64K | כן, עם לולאה משלכם | כותבים לולאה. [אפשרות 2](#option-2-loop). |
| REST `generateContent` | 32K | כן, עם לולאה משלכם | כותבים לולאה. [אפשרות 2](#option-2-loop). |

## מתי כדאי להשתמש בפענוח ארוך

רוב הבקשות מסתיימות במסגרת המגבלה לבקשה אחת (64,000 טוקנים לסטרימינג ולקריאות SDK, או 32,000 טוקנים לקריאות REST ללא סטרימינג). משתמשים בפענוח ארוך כשהתשובה צריכה יותר טוקנים משולבים של חשיבה ופלט ממה שמאפשרת בקשה אחת. הגדלת `max_output_tokens` מאפשרת למודל להגיע לתובנות לגבי בעיות קשות, במקום להאריך תשובות רגילות.

| עומס עבודה | להשתמש בפענוח ארוך? | סיבה |
| --- | --- | --- |
| מתמטיקה, מדע, מחקר והוכחות פורמליות ברמה גבוהה | כן | המודל יכול להשתמש ביותר מ-64,000 טוקנים כדי לבדוק את תהליך החשיבה שלו. |
| משימות התכנות והמשימות האג'נטיות הכי קשות | כן | יש משימות שדורשות יותר מ-64,000 טוקנים של חשיבה וקוד בתשובה אחת. רוב משימות התכנות והמשימות לנציגים מסתיימות עם פחות מ-64K. |
| כלי הערכה שעוצרים במגבלת הפלט | כן | פענוח ארוך מונע תשובות חלקיות כשהמודל משקיע את כל הבקשה של 64K או 32K בחשיבה. |
| צ'אט, שאלות ותשובות, סיכום, סיווג וחילוץ | לא | המשימות האלה מסתיימות עם הרבה פחות מ-32,000 טוקנים. |
| בקשות לאורך קבוע, כמו "תכתוב ספר באורך 700,000 מילים" | לא | המודל לא עומד ביעדי האורך. |
| סוכנים שקוראים לכלים בהרבה תורות קצרות | לא | כל תור הוא קצר. פלט גדול בכל סבב ממלא במהירות את חלון הקלט והפלט המאוחד של מיליון טוקנים. |
| הנחיות שמתקרבות למגבלת הקלט של מיליון טוקנים | לא | הפלט יכול להשתמש רק ב-1M פחות הקלט שלכם. |
| בקשות שרגישות לזמן האחזור | לא | פענוח ארוך יכול להימשך כמה דקות. |

הגדרה של `max_output_tokens` גבוה מאפשרת למודל לחשוב יותר זמן על בעיות קשות, אבל המודל עדיין מחליט כמה לכתוב. כדי לשלוט במידת המאמץ של המודל להסיק מסקנות, מגדירים את [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=he).

## הפעלת פענוח ארוך

אתם יכולים להריץ פענוח ארוך באופן אוטומטי באמצעות Google GenAI SDK (אפשרות 1, מומלצת לרוב האפליקציות) או לכתוב לולאת המשך משלכם (אפשרות 2). שתי האפשרויות תומכות בחלון הקשר מלא של מיליון טוקנים.

|  | אפשרות 1: Google GenAI SDK (מומלצת) | אפשרות 2: לולאת סטרימינג משלכם | אפשרות 2: לולאה משלכם שלא מועברת בסטרימינג |
| --- | --- | --- | --- |
| **מי מתחיל כל שלב** | ערכת ה-SDK. הגדרת את `max_output_tokens`. | הקוד שלכם, בכל נקודת בדיקה או אחרי שידור שנכשל | הקוד שלכם, כל 32,000 טוקנים |
| **טוקנים לכל בקשה** | ‫64K לכל קפיצה | ‫64,000 לכל סטרימינג, עם נקודת ביקורת כל 5,000 טוקנים אחרי 32,000 | ‫32K לכל בקשה |
| **מגבלת זמן לכל בקשה** | 20 דקות | 20 דקות | 20 דקות |
| **אחסון** | אין אחסון בשרת | אין אחסון בשרת | אין אחסון בשרת |
| **מתאים במיוחד ל** | רוב האפליקציות | מתקשרים של REST ורכיבי עזר מותאמים אישית שמשדרים | מסגרות פשוטות להערכה |

ה-`continuation_token` המוצפן מעביר את מצב המודל בין הבקשות, כך ששום דבר לא נשמר בשרת.

### אפשרות 1: שימוש ב-Google GenAI SDK (מומלץ)

בגרסה האחרונה של Google GenAI SDK, האפשרות `automatic_continuation` מופעלת כברירת מחדל גם לקריאות בסטרימינג וגם לקריאות שלא בסטרימינג, כך שאין צורך להגדיר אותה. כשמגדירים את `max_output_tokens` מעל המכסה לכל בקשה, ה-SDK מפעיל באופן אוטומטי את הדילוגים להמשך ומחזיר תגובה משולבת אחת.

1. משדרגים את ה-SDK.

   ### Python

   ```
   pip install -U "google-genai>=2.30.1"
   ```

   ### JavaScript

   ```
   npm install "@google/genai@>=2.29.1"
   ```
2. מגדירים את `max_output_tokens` לערך שגדול מ-65,536.

   ### Python

   ```
   from google import genai
   from google.genai import types

   client = genai.Client()  # Reads GEMINI_API_KEY

   response = client.models.generate_content(
       model="gemini-4-argon",
       contents="Write a complete, rigorous proof of the prime number theorem.",
       config=types.GenerateContentConfig(
           max_output_tokens=262_144,  # Total thinking and output for all hops
           thinking_config=types.ThinkingConfig(thinking_level="high"),
           automatic_continuation=True,  # Default. Shown for clarity.
       ),
   )

   print(response.text)
   print("Finish reason:", response.candidates[0].finish_reason)
   print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
   print("Billed tokens:", response.usage_metadata.total_token_count)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI, ThinkingLevel } from "@google/genai";

   const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY

   const response = await ai.models.generateContent({
     model: "gemini-4-argon",
     contents: "Write a complete, rigorous proof of the prime number theorem.",
     config: {
       maxOutputTokens: 262144, // Total thinking and output for all hops
       thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
       automaticContinuation: true, // Default. Shown for clarity.
     },
   });

   console.log(response.text);
   console.log("Finish reason:", response.candidates?.[0]?.finishReason);
   console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
   console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
   ```

חשוב לזכור:

- **סטרימינג:** גם המינויים ל-`generate_content_stream` (Python) ול-`generateContentStream` (JavaScript) ימשיכו לפעול. אם השידור נקטע אחרי נקודת ביקורת, ה-SDK ממשיך מאותה נקודת ביקורת.
- **פסק זמן (timeout):** פסק זמן וניסיונות חוזרים חלים על כל קפיצה, ולא על הריצה המלאה.
- **שליטה ידנית:** כדי להריץ את הלולאה בעצמכם, מגדירים את `automatic_continuation=False` (Python) או את `automaticContinuation: false` (JavaScript). אחר כך פועלים לפי הוראות אפשרות 2.
- **שימוש:** בשדות השימוש מוצג הסכום של כל הקפיצות. כדי לדעת מה הגודל של ההנחיה, קראו את `initial_prompt_token_count`. [ספירת טוקנים](#count-tokens)

### אפשרות 2: כתיבת לולאה משלכם

אם אתם קוראים ל-REST ישירות, משתמשים בשפה בלי ה-SDK העדכני ביותר או צריכים שליטה מלאה, אתם יכולים לכתוב לולאה משלכם. אפשר גם לעיין בהטמעות של Google GenAI SDK ב-[Python](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) וב-[JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88) כדוגמאות.

חשוב להקפיד על הכללים הבאים:

1. **שולחים את אותה בקשה בכל דילוג.** שליחת `contents`,‏ `system_instruction`,‏ `tools` ו-`generation_config` המקוריים. לא לשנות את `max_output_tokens`.
2. **אל תוסיפו פלט חלקי ל-`contents`.** ה-`continuation_token` מכיל את מצב המודל, כולל תהליך החשיבה שלו.
3. **שולחים רק את הטוקן האחרון.** כל אסימון מכיל את כל ההתקדמות הקודמת.
4. **המשך כל עוד `finish_reason` הוא `CONTINUATION`.** הפסקה מכל סיבה אחרת לסיום.
5. **חיבור החלקים אחרי הקפיצה האחרונה.** לשלב את החלקים מכל הדילוגים לתור אחד של המודל בהיסטוריית השיחות.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()  # Reads GEMINI_API_KEY
PROMPT = "Write a complete, rigorous proof of the prime number theorem."
parts = []
token = None

while True:
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents=PROMPT,  # The original contents on every request
        config=types.GenerateContentConfig(
            max_output_tokens=262_144,  # The same total on every request
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=False,  # You run the loop
            continuation_token=token,
        ),
    )
    candidate = response.candidates[0]
    if candidate.content and candidate.content.parts:
        parts.extend(candidate.content.parts)
    token = candidate.continuation_token
    if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
        break

print("".join(p.text for p in parts if p.text and not p.thought))
print("Finish reason:", candidate.finish_reason)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
const parts = [];
let token = undefined;
let candidate = undefined;

while (true) {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: PROMPT, // The original contents on every request
    config: {
      maxOutputTokens: 262144, // The same total on every request
      thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
      automaticContinuation: false, // You run the loop
      continuationToken: token,
    },
  });
  candidate = response.candidates?.[0];
  if (candidate?.content?.parts) {
    parts.push(...candidate.content.parts);
  }
  token = candidate?.continuationToken;
  if (candidate?.finishReason !== "CONTINUATION" || !token) {
    break;
  }
}

console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
console.log("Finish reason:", candidate?.finishReason);
```

### REST

```
# Hop 1: send the request with max_output_tokens.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    }
  }'

# Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    },
    "continuationToken": "TOKEN_FROM_HOP_1"
  }'
```

אם שלב מסוים מוקדש כולו לחשיבה, הוא יחזיר `text` ריק עם `finishReason: "CONTINUATION"`. התייחסו לזה כאל התקדמות רגילה ובקשו את הצעד הבא:

```
{
  "candidates": [{
    "content": {"role": "model", "parts": [{"text": ""}]},
    "finishReason": "CONTINUATION",
    "continuationToken": "CiQ4ZmQ3..."
  }],
  "usageMetadata": {
    "promptTokenCount": 142,
    "candidatesTokenCount": 0,
    "thoughtsTokenCount": 32768,
    "totalTokenCount": 32910
  }
}
```

**לולאות סטרימינג** צריכות כלל אחד נוסף. אחרי 32,768 הטוקנים הראשונים, הזרם שולח טוקן של נקודת ביקורת כל 5,000 טוקנים. שמירת קטעים חדשים ברשימת המתנה. כשהקטע מכיל `continuation_token`, מעבירים את הקטעים בהמתנה לפלט הסופי ושומרים את האסימון. אם הסטרימינג נקטע, צריך למחוק את החלקים בהמתנה ולהמשיך מהטוקן האחרון. אם הסטרימינג נקטע לפני נקודת הבדיקה הראשונה, צריך לשלוח שוב את הבקשה המקורית.

## הגדרה של `max_output_tokens`

‫`max_output_tokens` מגדיר את המגבלה המשולבת לחשיבה ולפלט בכל ההופעות. הורדת הערך לא גורמת למודל לחשוב בצורה תמציתית יותר, אלא מקצרת את התשובה.

| עומס העבודה שלכם | מומלץ `max_output_tokens` |
| --- | --- |
| אפליקציות קיימות עם מגבלה נמוכה מ-32K | מגדילים אותו ל-32,768. |
| משימות ארוכות של תכנות ונציגים | מתחילים ב-65,536. |
| מתמטיקה, מדע, מחקר והוכחות ברמה גבוהה | ערכי הבדיקה יכולים להיות מ-262,144 עד 1,048,576 פחות טוקני הקלט. |

כדי להשתמש בפחות אסימונים, צריך להקטין את הערך של `thinking_level`. אפשר להשתמש ב-`high` למשימות החשיבה הקשות ביותר. כדאי להשתמש ב-`medium` (ברירת המחדל) לרוב משימות התכנות והעבודה עם סוכנים. כדאי להשתמש ב-`low` למשימות פחות מורכבות.

## טיפול בבקשות ממושכות

מכיוון ש-Gemini 4 Argon חושב יותר זמן ממודלים של Gemini 3.x על בעיות קשות, כדאי להגדיל את הזמן הקצוב לתפוגה של הלקוח כדי שבקשות ארוכות לא יתנתקו מוקדם מדי.

- **שיחות ללא סטרימינג:** השרת סוגר את החיבור אחרי 10 דקות.
- **שיחות סטרימינג:** השרת סוגר את הסטרימינג אחרי 20 דקות.
- **זמן קצוב לתפוגה של לקוח:** מגדירים את הזמן הקצוב לתפוגה של קריאת HTTP ל-20 דקות. פסק זמן של 3 או 5 דקות יפסיק את הבקשה מוקדם יותר.

ב-Python, מגדירים את הזמן הקצוב לתפוגה בלקוח באלפיות השנייה:

```
client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
```

לגבי משימות שהלקוח מבצע לגביהן סקר, ממשק Interactions API מפעיל פענוח ארוך בשרת. מידע נוסף מופיע במאמר בנושא [הרצה ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he).

## המשך כשכל טוקני הפלט של המודל בשימוש

כשסיום התשובה הוא `MAX_TOKENS`, היא עדיין כוללת את `continuation_token`. יש לכם שתי אפשרויות:

- **המשך:** שולחים את אותה בקשה עם הטוקן וערך `max_output_tokens` גבוה יותר. הערך צריך להיות גבוה יותר מהטוקנים שנעשה בהם שימוש עד עכשיו. אחרת, ה-API מחזיר שגיאה 400.
- **מתחילים מחדש:** שולחים את הבקשה המקורית עם ערך גבוה יותר של `max_output_tokens` וללא טוקן. אתם משלמים על שתי ההפעלות.

## ספירת טוקנים

בשיטה של המשך אוטומטי, `usage_metadata` מדווח על הסכומים הכוללים בכל הקפיצות. ערכת ה-SDK מסכמת את כל שדות הספירה: `prompt_token_count`,‏ `cached_content_token_count`,‏ `candidates_token_count`,‏ `thoughts_token_count` ו-`total_token_count`.

‫`prompt_token_count` מסכם את אסימוני הקלט של כל שלב. בכל שלב, ההנחיה וכל מה שנוצר עד עכשיו נשלחים בחזרה למודל כקלט, כך שאותם אסימונים נספרים שוב בכל שלב מאוחר יותר. לדוגמה, ב-Google GenAI SDK, הנחיה של 1,000 אסימונים שמפיקה 200,000 אסימונים של חשיבה ופלט דורשת ארבעה דילוגים:

| Hop | הקלט שנשלח למודל | טוקנים של קלט |
| --- | --- | --- |
| 1 | פרומפט | 1,000 |
| 2 | פרומפט + קפיצה 1 | 66,536 |
| 3 | פרומפט + קפיצות 1 ו-2 | 132,072 |
| 4 | פרומפט + מעברים 1 עד 3 | 197,608 |
| **סה"כ** |  | **397,216** |

‫`prompt_token_count` מדווח על 397,000 טוקנים (עם הנחה אוטומטית של 95% על קלט חוזר של מעברים באמצעות שמירה מרומזת במטמון), ו-`total_token_count` מדווח על 597,000 טוקנים, למרות שגודל ההקשר בפועל הוא רק כ-201,000 טוקנים: ההנחיה של 1,000 טוקנים בתוספת 200,000 טוקנים של חשיבה ופלט. לולאת REST ללא סטרימינג משתמשת ב-32K קפיצות, ולכן נדרשות שבע קפיצות כדי לקבל את אותה התוצאה, והיא מדווחת על 695,128 טוקנים של קלט.

| איך מפעילים את המודל | מה `usage_metadata` מראה | בתשלום | לגודל הפרומפט |
| --- | --- | --- | --- |
| ‫Google GenAI SDK, המשך אוטומטי (ברירת המחדל) | סך הכול בכל הקפיצות | קוראים את שדות השימוש כמו שהם. | כדאי לקרוא את המאמרים בנושא `usage_metadata.initial_prompt_token_count` (Python) או `usageMetadata.initialPromptTokenCount` (JavaScript). |
| ‫SDK עם `automatic_continuation=False` או REST | דילוג אחד לכל תגובה | מוסיפים כל שדה בכל הקפיצות. | קריאת `prompt_token_count` מהקפיצה הראשונה. |

‫`prompt_token_count` ו-`total_token_count` הם הסכום של כל הדילוגים, ולא הגודל של ההקשר. אל תשתמשו בהם כדי להחליט מתי לסכם או לקצץ את היסטוריית השיחות (דחיסת ההקשר) או כדי לאכוף מגבלת הקשר. כדי לאמוד את גודל ההקשר, מוסיפים את גודל ההנחיה מהטבלה ל-`candidates_token_count` ול-`thoughts_token_count`.

לפני שמפעילים פענוח ארוך, צריך לעדכן את מסגרת הסוכן, את כלי ההערכה או את שרת ה-proxy:

- **סוכנים וכלי הערכה:** אם הקוד שלכם דוחס את ההקשר או מפסיק את ההפעלה במגבלת טוקנים, השתמשו ב-`initial_prompt_token_count` (או ב-`prompt_token_count` של הדילוג הראשון ב-REST) במקום ב-`prompt_token_count` המסוכם. בתשובות שמסתיימות בקפיצה אחת, הערך בשני השדות זהה, ולכן בבדיקות קצרות הבעיה לא מופיעה.
- **שערים ושרתי proxy שקוראים ל-REST:** כל תגובת REST מדווחת רק על הניתור שלה. מוסיפים כל שדה בכל הדילוגים כדי לראות את העלות, ושומרים על `promptTokenCount` של הדילוג הראשון כגודל ההנחיה. אחרת, המשתמשים שלכם יראו מספרים שונים מאלה שמשתמשי SDK רואים עבור אותה בקשה.
- **יומנים ותגובות שעברו סריאליזציה:** ערך `initial_prompt_token_count` מחושב על ידי ה-SDK בצד הלקוח. הוא לא מופיע בתגובת ה-REST או בפלט ה-JSON של ה-SDK, כמו `model_dump()`. אם תצטרכו אותו בהמשך, שמרו אותו כערך נפרד.

אם אתם משתמשים בלולאה משלכם לסטרימינג, הערך של `usage_metadata` הוא מצטבר בכל סטרימינג. שומרים רק את הערך האחרון של כל זרם, ואז מוסיפים את הערכים בין הדילוגים.

## הסבר על החיוב

אתם משלמים על כל טוקן בכל שלב, כולל שלבים שכוללים רק חשיבה.

- **הנחת מטמון:** הנחה מרומזת על שמירת נתונים במטמון, שבה הקלט החוזר בכל קפיצה מוזל ב-95%. במהלך תקופת ההיכרות, העלות של קלט שנשמר במטמון היא 0.10 $למיליון טוקנים במקום 2.00$.
- **תפוגת המטמון:** תוקף המטמון פג אחרי 15 עד 20 דקות ללא שימוש. אם יש הפסקה ארוכה בין הנסיעות, המערכת מחייבת שוב בתעריף המלא.
- **דילוגים שנכשלו בלי סטרימינג:** אתם משלמים רק כשהתשובה מושלמת. בקשה שנכשלה או נדחתה עולה 0$.
- **הזרמות שהופסקו:** הזרמה שהופסקה לפני שהגיע ל-32,000 טוקנים לא עולה כסף. אחרי זה, אתם משלמים עד לטוקן של נקודת הבדיקה האחרונה, כי אתם יכולים להמשיך ממנה.

## פתרון בעיות

| תיאור הבעיה | הסיבה והפתרון |
| --- | --- |
| הפלט נעצר ב-64K או ב-32K עם `CONTINUATION` | למודל נשארו טוקנים, אבל לא הייתה המשכיות לבקשה. משדרגים את ה-SDK או מוסיפים לולאה. |
| הפלט נעצר ב-64K או ב-32K עם `MAX_TOKENS` | הערך של `max_output_tokens` לא מוגדר או נמוך מדי. מגדירים אותו לערך גבוה מ-65,536. |
| טקסט ריק עם `MAX_TOKENS` | המודל השתמש בכל הטוקנים לתהליך החשיבה. מצביעים `max_output_tokens` או מפסיקים להצביע `thinking_level`. |
| ‫400: "אסימון ההמשך כבר השתמש באסימוני פלט..." | הערך `max_output_tokens` לא גבוה ממספר האסימונים שנעשה בהם שימוש עד עכשיו. מרימים את היד. |
| שגיאה ב-`thinking_level: "minimal"`, או ב-`thinking_budget` עם `thinking_level` | ‫Gemini 4 Argon לא תומך ב-`minimal`. אפשר להשתמש ב-`low`, ב-`medium` או ב-`high`. צריך להגדיר את `thinking_level` או את `thinking_budget`, אבל לא את שניהם. |
| אזהרה לגבי `thinking_budget`, `temperature`, `top_p` או `top_k` | ‫Gemini 4 Argon מתעלם מהשדות האלה או ממפה אותם. משתמשים ב-`thinking_level` ומסירים את פרמטרי הדגימה. |
| הבקשה מסתיימת אחרי 3 או 5 דקות | הזמן הקצוב לתפוגה של הלקוח קצר מדי. תגדיר אותו ל-20 דקות. |
| הדחיסה של ההקשר מתחילה מוקדם מדי | ה-harness קורא את הקלט המסוכם. במקום זאת, כדאי לקרוא את `initial_prompt_token_count`. |

## מגבלות

- **נקודת קצה (endpoint) תואמת ל-OpenAI:** אי אפשר להשתמש בפענוח ארוך. הפלט נעצר במגבלה לכל בקשה.
- **גרסאות SDK ישנות יותר:** גרסאות ישנות יותר מהגרסאות המינימליות שמופיעות בהערה לא ימשיכו לפעול באופן אוטומטי.
- **אורך:** המודל לא פועל לפי יעדים של אורך טוקן או מספר מילים.

## רשימת המשימות

- משדרגים את Google GenAI SDK לגרסה המינימלית.
- מגדירים את `max_output_tokens` לערך שגדול מ-65,536.
- צריך להשתמש ב-`thinking_level` (`low`,‏ `medium` או `high`), ולא ב-`thinking_budget`.
- מגדירים את זמן הקריאה הקצוב לתפוגה של HTTP ל-20 דקות.
- משתמשים ב-`initial_prompt_token_count` כדי להגדיר את גודל ההקשר והדחיסה.
- כדאי להריץ פרומפט אחד כבדיקה לפני שמבצעים הערכה נרחבת.

## השלבים הבאים

- [מה חדש ב-Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=he)
- [בתהליך חשיבה](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=he)
- [ספירת טוקנים](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-13 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-13 (שעון UTC)."],[],[]]
