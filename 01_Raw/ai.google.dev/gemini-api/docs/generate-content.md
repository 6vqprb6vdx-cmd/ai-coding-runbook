---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=he
fetched_at: 2026-10-05T06:33:46.360210+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

# Gemini API

‫Gemini API היא הדרך הכי מהירה להפוך הנחיה למוצר מוגמר באמצעות Gemini,‏ Veo,‏ Nano Banana ועוד. הוא מאפשר לכם לשלב את המודלים הגנרטיביים האלה באפליקציות שלכם כדי ליצור טקסט ותמונות, לנתח קלט מולטי-מודאלי ולבנות סוכנים שיכולים לנהל שיחות.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#‎

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[אני רוצה להתחיל לפתח](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)

---

## היכרות עם המודלים

[הצג הכול](https://ai.google.dev/gemini-api/docs/models?hl=he)

[auto\_awesome
Gemini 3.1 Pro
חדש

המודל הכי חכם שלנו, הכי טוב בעולם בהבנה מולטימודלית, והכול מבוסס על יכולות רציונליות מתקדמות.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he)
[spark
Gemini 3.6 Flash
חדש

המודל העדכני שלנו, שמשלב בין מהירות לבין יכולות AI חכמות כדי לספק ביצועים טובים במשימות אקטיביות ומולטי-מודאליות.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=he)
[spark
Gemini 3.5 Flash

ביצועים ברמה של Frontier, שמתחרים במודלים גדולים יותר בעלות נמוכה בהרבה.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he)
[graphic\_eq
Gemini 3.8 Flash TTS
חדש

מודל להמרת טקסט לדיבור ברמה של אולפן, עם משחק אקספרסיבי, עיצוב קול מותאם אישית ושכפול קול.](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=he)
[spark
Gemini 3.5 Flash-Lite
חדש

מודל בנפח גבוה ובעלות נמוכה, שעבר אופטימיזציה למשימות של סוכני משנה עם זמן אחזור נמוך וקצב העברה גבוה.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=he)
[spark
Gemini 3.1 Flash-Lite

מודל שמתאים לעיבוד נפחים גדולים של נתונים, רגיש לעלויות וכולל את הביצועים והאיכות של סדרת Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he)
[spark
‫Gemini 3 Flash

ביצועים ברמה של Frontier, שמתחרים במודלים גדולים יותר בעלות נמוכה בהרבה.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he)
[🍌
‫Nano Banana 2 ו-Nano Banana Pro

מודלים חדשניים ומתקדמים ליצירה ולעריכה של תמונות.](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)
[video\_library
Veo 3.1

מודל ליצירת וידאו המתקדם ביותר שלנו, עם אודיו מובנה.](https://ai.google.dev/gemini-api/docs/video?hl=he)
[spark
Gemini Robotics

מודל ראייה-שפה (VLM) שמביא את יכולות אג'נטיות של Gemini לרובוטיקה ומאפשר חשיבה רציונלית משופרת בעולם הפיזי.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he)

## פרטים על היכולות

[imagesmode

יצירת תמונות באופן מובנה (Nano Banana)

אתם יכולים ליצור ולערוך תמונות עם הקשר רחב באמצעות Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)
[article

הקשר רחב

להזין מיליוני טוקנים למודלים של Gemini ולקבל תובנות מתמונות, סרטונים ומסמכים לא מובנים.](https://ai.google.dev/gemini-api/docs/long-context?hl=he)
[code

פלט מובנה

מגבילים את Gemini לתגובה ב-JSON, שהוא פורמט נתונים מובְנה שמתאים לעיבוד אוטומטי.](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)
[functions

בקשה להפעלת פונקציה

אפשר לבנות תהליכי עבודה מבוססי-סוכנים על ידי חיבור של Gemini לממשקי API ולכלים חיצוניים.](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
[videocam

יצירת סרטונים באמצעות Veo 3.1

אתם יכולים ליצור תוכן וידאו באיכות גבוהה מפרומפטים של טקסט או תמונה באמצעות המודל המתקדם ביותר (SOTA) שלנו.](https://ai.google.dev/gemini-api/docs/video?hl=he)
[android\_recorder

סוכנים קוליים עם Live API

אתם יכולים ליצור סוכנים ואפליקציות קוליות בזמן אמת באמצעות ממשק Live API.](https://ai.google.dev/gemini-api/docs/live-api?hl=he)
[build

כלים

אפשר לחבר את Gemini לעולם באמצעות כלים מובנים כמו חיפוש Google, הקשר של כתובת URL, מפות Google, הפעלת קוד ושימוש במחשב.](https://ai.google.dev/gemini-api/docs/tools?hl=he)
[stacks

הבנת מסמכים

לעבד עד 1,000 דפים של קובצי PDF עם הבנה מולטי-מודאלית מלאה או סוגים אחרים של קבצים מבוססי-טקסט.](https://ai.google.dev/gemini-api/docs/document-processing?hl=he)
[cognition\_2

מעמיק

כדאי לבדוק איך יכולות החשיבה משפרות את ההיגיון במשימות מורכבות ובסוכנים.](https://ai.google.dev/gemini-api/docs/thinking?hl=he)

[Google AI Studio

אפשר לבדוק הנחיות, לנהל את מפתחות ה-API, לעקוב אחרי השימוש וליצור אבות טיפוס.](https://aistudio.google.com?hl=he)
[group

קהילת המפתחים

לשאול שאלות ולמצוא פתרונות ממפתחים אחרים וממהנדסי Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=he)
[menu\_book

הפניית API

מידע מפורט על Gemini API זמין במסמכי העזרה הרשמיים.](https://ai.google.dev/api?hl=he)
[sensors

סטטוס

בדיקת הסטטוס של Gemini API,‏ Google AI Studio ושירותי המודלים שלנו.](https://aistudio.google.com/status?hl=he)

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-24 (שעון UTC).

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-24 (שעון UTC)."],[],[]]
