---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=he
fetched_at: 2026-10-26T05:52:04.782422+00:00
title: "\u05e1\u05e4\u05e8\u05d9\u05d5\u05ea Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ספריות Gemini API

כשמפתחים באמצעות Gemini API, מומלץ להשתמש ב-**Google GenAI SDK**.
אלה ספריות רשמיות שמוכנות לשימוש בסביבת ייצור, שאנחנו מפתחים ומתחזקים עבור השפות הפופולריות ביותר. הם נמצאים ב[זמינות לכלל המשתמשים (GA)](https://ai.google.dev/gemini-api/docs/libraries?hl=he#new-libraries) ומשמשים בכל התיעוד והדוגמאות הרשמיים שלנו.

אם אתם חדשים ב-Gemini API, כדאי לעיין ב[מדריך לתחילת העבודה](https://ai.google.dev/gemini-api/docs/get-started?hl=he).

## תמיכה בשפות והתקנה

ערכת Google GenAI SDK זמינה בשפות Python, ‏ JavaScript/TypeScript, ‏ Go ו-Java. אתם יכולים להתקין את הספרייה של כל שפה באמצעות מנהלי חבילות, או להיכנס למאגרים שלהם ב-GitHub כדי לקבל מידע נוסף:

### Python

- ספרייה: [`google-genai`](https://pypi.org/project/google-genai)
- מאגר GitHub: ‏ [googleapis/python-genai](https://github.com/googleapis/python-genai)
- התקנה: `pip install google-genai`

### JavaScript

- ספרייה: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- מאגר GitHub: ‏ [googleapis/js-genai](https://github.com/googleapis/js-genai)
- התקנה: `npm install @google/genai`

### Go

- ספרייה: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- מאגר GitHub: ‏ [googleapis/go-genai](https://github.com/googleapis/go-genai)
- התקנה: `go get google.golang.org/genai`

### Java

- ספרייה: `google-genai`
- מאגר GitHub: ‏ [googleapis/java-genai](https://github.com/googleapis/java-genai)
- התקנה: אם משתמשים ב-Maven, מוסיפים את הקוד הבא ליחסי התלות:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#‎

- ספרייה: `Google.GenAI`
- מאגר GitHub: ‏ [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- התקנה: `dotnet add package Google.GenAI`

## זמינות לכלל המשתמשים (GA)

החל ממאי 2025, ערכת Google GenAI SDK זמינה לכלל המשתמשים (GA) בכל הפלטפורמות הנתמכות, והיא הספרייה המומלצת לגישה ל-Gemini API.
הם יציבים, נתמכים באופן מלא לשימוש בסביבת הייצור ומתוחזקים באופן פעיל.
הם מספקים גישה לתכונות העדכניות ביותר ומציעים את הביצועים הטובים ביותר בעבודה עם Gemini.

אם אתם משתמשים באחת מהספריות הקודמות שלנו, מומלץ מאוד לעבור לספרייה החדשה כדי שתוכלו לגשת לתכונות העדכניות ביותר וליהנות מהביצועים הטובים ביותר בעבודה עם Gemini. מידע נוסף זמין בקטע [ספריות מדור קודם](https://ai.google.dev/gemini-api/docs/libraries?hl=he#previous-sdks).

## ספריות מדור קודם והעברה

אם אתם משתמשים באחת מהספריות הקודמות שלנו, מומלץ [לעבור לספריות החדשות](https://ai.google.dev/gemini-api/docs/migrate?hl=he).

הספריות מדור קודם לא מספקות גישה לתכונות חדשות (כמו [Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) ו-[Veo](https://ai.google.dev/gemini-api/docs/video?hl=he)), והן יוצאו משימוש החל מ-30 בנובמבר 2025.

סטטוס התמיכה של כל ספרייה מדור קודם משתנה, והוא מפורט בטבלה הבאה:

| שפה | ספרייה מדור קודם | סטטוס התמיכה | ספרייה מומלצת |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | לא מתוחזק באופן פעיל | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | לא מתבצע תחזוקה פעילה | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | לא מתבצע תחזוקה פעילה | `google.golang.org/genai` |
| **Dart ו-Flutter** | `google_generative_ai` | לא מתבצע תחזוקה פעילה | משתמשים ב-[Genkit Dart](https://genkit.dev/docs/dart/get-started/) או ב-[Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | לא מתוחזק באופן פעיל | שימוש ב-[Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=he) |
| **Android** | `generative-ai-android` | לא מתוחזק באופן פעיל | שימוש ב-[Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=he) |

**הערה למפתחי Java:** לא הייתה גרסה קודמת של Google-provided Java SDK ל-Gemini API, ולכן לא צריך לעבור מספרייה קודמת של Google. אפשר להתחיל ישירות עם הספרייה החדשה בקטע [Language support and installation](https://ai.google.dev/gemini-api/docs/libraries?hl=he#install).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-15 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-15 (שעון UTC)."],[],[]]
