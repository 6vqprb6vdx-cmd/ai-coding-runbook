---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=he
fetched_at: 2026-09-28T06:07:20.105888+00:00
title: "\u05d4\u05d2\u05d3\u05e8\u05d5\u05ea \u05d1\u05d8\u05d9\u05d7\u05d5\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הגדרות בטיחות

ממשק ה-API של Gemini מספק הגדרות בטיחות שניתן להתאים במהלך שלב בניית האב-טיפוס כדי לקבוע אם היישום שלך דורש תצורת בטיחות מגבילה יותר או פחות. באפשרותך להתאים הגדרות אלו על פני ארבע קטגוריות סינון כדי להגביל או לאפשר סוגים מסוימים של תוכן.

מדריך זה מכסה כיצד ממשק ה-API של Gemini מטפל בהגדרות בטיחות וסינון וכיצד ניתן לשנות את הגדרות הבטיחות עבור האפליקציה שלך.

## מסנני בטיחות

מסנני הבטיחות המתכווננים של ממשק ה-API של Gemini מכסים את הקטגוריות הבאות:

| קטגוריה | תיאור |
| --- | --- |
| הטרדה | הערות שליליות או מזיקות המכוונות לזהות ו/או למאפיינים מוגנים. |
| דברי שטנה | תוכן גס רוח, חסר כבוד או חילול קודש. |
| תוכן מיני בוטה | מכיל התייחסויות למעשים מיניים או לתוכן מגונה אחר. |
| תוכן מסוכן | מקדם, מקל או מעודד מעשים מזיקים. |

קטגוריות אלה מוגדרות ב[`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=he). באפשרותך להשתמש במסננים אלה כדי להתאים את מה שמתאים למקרה השימוש שלך. לדוגמה, אם אתם בונים דיאלוגים במשחקי וידאו, ייתכן שתראו שזה מקובל לאפשר תוכן נוסף שמדורג כ*מסוכן* עקב אופי המשחק.

בנוסף למסנני הבטיחות הניתנים להתאמה, ל-API של Gemini יש הגנות מובנות מפני נזקים מרכזיים, כגון תוכן המסכן את בטיחות הילדים.
סוגי נזק אלה תמיד חסומים ולא ניתן לתקן אותם.

### רמת הסינון של בטיחות התוכן

‫Gemini API מסווג את רמת ההסתברות לכך שהתוכן לא בטוח כ-`HIGH`, `MEDIUM`, `LOW` או `NEGLIGIBLE`.

‫Gemini API חוסם תוכן על סמך הסבירות שהתוכן לא בטוח, ולא על סמך חומרת התוכן. חשוב לקחת את זה בחשבון כי יש תכנים שהסיכוי שהם לא בטוחים הוא נמוך, אבל חומרת הנזק שעלולה להיגרם מהם עדיין גבוהה. לדוגמה, בהשוואה בין המשפטים:

1. הרובוט נתן לי אגרוף.
2. הרובוט חתך אותי.

המשפט הראשון עשוי להוביל לסבירות גבוהה יותר של תוצאה לא בטוחה, אבל יכול להיות שהמשפט השני ייחשב לחמור יותר מבחינת אלימות.
לכן חשוב לבדוק בקפידה ולשקול מה רמת החסימה המתאימה שנדרשת כדי לתמוך בתרחישי השימוש העיקריים שלכם, תוך צמצום הפגיעה במשתמשי הקצה.

### סינון בטיחות לכל בקשה

אתם יכולים לשנות את הגדרות הבטיחות לכל בקשה שאתם שולחים ל-API. כששולחים בקשה, התוכן נותח ומוקצה לו סיווג בטיחות. דירוג הבטיחות כולל את הקטגוריה ואת הסיווג של הסבירות לפגיעה. לדוגמה, אם התוכן נחסם כי הסבירות שהוא משתייך לקטגוריית ההטרדה גבוהה, דירוג הבטיחות שיוחזר יכלול את הקטגוריה `HARASSMENT` ואת הסבירות לפגיעה `HIGH`.

בגלל הבטיחות המובנית של המודל, מסננים נוספים **מושבתים** כברירת מחדל.
אם תבחרו להפעיל אותן, תוכלו להגדיר את המערכת לחסימת תוכן על סמך הסבירות שהוא לא בטוח. התנהגות המודל שמוגדרת כברירת מחדל מתאימה לרוב תרחישי השימוש, ולכן כדאי לשנות את ההגדרות האלה רק אם נדרשת עקביות באפליקציה שלכם.

בטבלה הבאה מתוארות הגדרות החסימה שאפשר לשנות בכל קטגוריה. לדוגמה, אם הגדרתם את הגדרת החסימה ל**חסימה של מעט** בקטגוריה **דברי שטנה**, כל מה שיש לו סיכוי גבוה להיות תוכן של דברי שטנה ייחסם. אבל מותר להשתמש בכל ערך עם הסתברות נמוכה יותר.

| סף (Google AI Studio) | סף (API) | תיאור |
| --- | --- | --- |
| מושבת | `OFF` | השבתת מסנן הבטיחות |
| לא לחסום אף אחד | `BLOCK_NONE` | הצגה תמיד, ללא קשר להסתברות של תוכן לא בטוח |
| חסימה של כמה אנשים | `BLOCK_ONLY_HIGH` | חסימה כשיש סבירות גבוהה לתוכן לא בטוח |
| חסימת חלק מהמשתמשים | `BLOCK_MEDIUM_AND_ABOVE` | חסימה כשיש הסתברות בינונית או גבוהה לתוכן לא בטוח |
| חסימה של רוב האנשים | `BLOCK_LOW_AND_ABOVE` | חסימה כשההסתברות לתוכן לא בטוח נמוכה, בינונית או גבוהה |
| לא רלוונטי | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | הסף לא צוין, חסימה באמצעות סף ברירת המחדל |

אם לא מגדירים את הסף, סף החסימה שמוגדר כברירת מחדל הוא **מושבת** למודלים של Gemini 2.5 ו-3.

אפשר להגדיר את ההגדרות האלה לכל בקשה ששולחים לשירות הגנרטיבי.
פרטים נוספים זמינים במאמר בנושא [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=he#harmblockthreshold) API Reference.

### משוב בנושא בטיחות

‫[`generateContent`](https://ai.google.dev/api/generate-content?hl=he#method:-models.generatecontent)
מחזירה את
‫[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=he#generatecontentresponse) שכוללת משוב בנושא בטיחות.

המשוב על ההנחיות כלול ב-[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=he#promptfeedback). אם הערך של `promptFeedback.blockReason` מוגדר, סימן שהתוכן של ההנחיה נחסם.

המשוב על המועמדים לתשובה נכלל ב[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=he#candidate) וב[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=he#candidate). אם תוכן התגובה נחסם והערך של `finishReason` היה `SAFETY`, אפשר לבדוק את `safetyRatings` כדי לקבל פרטים נוספים. התוכן שנחסם לא יוחזר.

## שינוי הגדרות הבטיחות

בקטע הזה מוסבר איך לשנות את הגדרות הבטיחות ב-Google AI Studio ובקוד.

### Google AI Studio

אתם יכולים לשנות את הגדרות הבטיחות ב-Google AI Studio.

לוחצים על **הגדרות בטיחות** בקטע **הגדרות מתקדמות** בחלונית **הגדרות ההרצה** כדי לפתוח את תיבת הדו-שיח **הגדרות הבטיחות של ההרצה**. בחלון הקופץ, אפשר להשתמש בפסי ההזזה כדי לשנות את רמת סינון התוכן לפי קטגוריית בטיחות:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=he)

כששולחים בקשה (לדוגמה, על ידי שאילת שאלה למודל), מופיעה הודעת warning
**תוכן חסום** אם תוכן הבקשה חסום. כדי לראות פרטים נוספים, החזק את המצביע מעל הטקסט **תוכן חסום** כדי לראות את הקטגוריה ואת סיווג ההסתברות לנזק.

### דוגמאות קוד

קטע הקוד הבא מראה כיצד להגדיר הגדרות בטיחות בשיחת `GenerateContent` שלך. זה קובע את הסף לקטגוריית דברי שטנה (`HARM_CATEGORY_HATE_SPEECH`). הגדרת קטגוריה זו ל-`BLOCK_LOW_AND_ABOVE` חוסמת כל תוכן שיש לו סבירות נמוכה או גבוהה יותר להיות דברי שטנה. כדי להבין את הגדרות הסף, ראו [סינון בטיחות לפי בקשה](#safety-filtering-per-request).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
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

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .category(HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH)
        .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(Arrays.asList(hateSpeechSafety))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Some potentially unsafe prompt.", config);

System.out.println(response.text());
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## השלבים הבאים

- עיין ב[הפניה ל-API](https://ai.google.dev/api?hl=he) כדי ללמוד עוד על ה-API המלא.
- עיין ב[הנחיות הבטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he) לקבלת מבט כללי על שיקולי בטיחות בעת פיתוח עם תואר שני במשפטים.
- למידע נוסף על הערכת הסתברות לעומת חומרה מצוות [Jigsaw](https://developers.perspectiveapi.com/s/about-the-api-score)
- למידע נוסף על המוצרים התורמים לפתרונות בטיחות כמו [Perspective API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7).
  \* ניתן להשתמש בהגדרות בטיחות אלה כדי ליצור מסווג רעילות. ראה את [דוגמת הסיווג](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=he) כדי להתחיל.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-18 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-18 (שעון UTC)."],[],[]]
