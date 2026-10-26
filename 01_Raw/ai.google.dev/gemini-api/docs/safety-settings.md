---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=he
fetched_at: 2026-10-26T05:54:25.354798+00:00
title: "\u05d4\u05d2\u05d3\u05e8\u05d5\u05ea \u05d1\u05d8\u05d9\u05d7\u05d5\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הגדרות בטיחות

ממשק Gemini API מספק הגדרות בטיחות שאפשר לשנות בשלב יצירת אב טיפוס כדי לקבוע אם האפליקציה שלכם דורשת הגדרת בטיחות מגבילה יותר או פחות. אתם יכולים לשנות את ההגדרות האלה בקטגוריות של המסננים כדי להגביל סוגים מסוימים של תוכן או לאפשר אותם.

במדריך הזה מוסבר איך מגדירים הגדרות בטיחות באינטראקציה, מה קורה כשתוכן נחסם, באילו קטגוריות אפשר להשתמש ומהם ערכי הסף.

## קביעת הגדרות הבטיחות

מעבירים רשימה של `safety_settings` כשיוצרים אינטראקציה. כל הגדרה משלבת קטגוריית פגיעה (`type`) עם סף חסימה (`threshold`).

בדוגמה הבאה, הקטגוריה של דברי שטנה (`hate_speech`) מוגדרת לערך `block_low_and_above`, שחוסם כל תוכן שיש לו סבירות נמוכה או גבוהה יותר להיות דברי שטנה:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Some potentially unsafe prompt.",
    safety_settings=[
        {
            "type": "hate_speech",
            "threshold": "block_low_and_above",
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Some potentially unsafe prompt.",
    safety_settings: [
      {
        type: "hate_speech",
        threshold: "block_low_and_above",
      },
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.HarmCategory;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.SafetySetting;
import com.google.genai.gaos.models.interactions.Threshold;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .type(HarmCategory.HATE_SPEECH)
        .threshold(Threshold.BLOCK_LOW_AND_ABOVE)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Some potentially unsafe prompt."))
        .safetySettings(List.of(hateSpeechSafety))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Some potentially unsafe prompt."),
            SafetySettings: []interactions.SafetySetting{
                {
                    Type:      interactions.HarmCategoryHateSpeech,
                    Threshold: interactions.ThresholdBlockLowAndAbove,
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Some potentially unsafe prompt.",
    "safety_settings": [
      {"type": "hate_speech", "threshold": "block_low_and_above"}
    ]
  }'
```

אפשר לכלול הגדרה אחת לכל קטגוריה. בקטגוריות שלא תגדירו, יחול סף ברירת המחדל, שהוא **Off** במודלים של Gemini 2.5 ואילך.

## כשהתוכן חסום

אם מסנן בטיחות חוסם את הקלט או את התשובה של המודל, האינטראקציה נכשלת ומוצגת שגיאת HTTP `400`. התוכן החסום לא יוחזר.

השגיאה `code` מציינת את הסיבה לחסימת הבקשה:

- ‫`safety`: הקלט או התשובה נחסמו על ידי מסנן בטיחות.
- ‫`jailbreak`, ‏`prohibited_content` או `blocklist`: הקלט נחסם בגלל הסיבה הזו. השגיאה `message` מתחילה ב-`Input blocked:`.

לדוגמה:

```
{
  "error": {
    "code": "safety",
    "message": "Request blocked due to safety violations (harmful content). Please modify your input and retry."
  }
}
```

באינטראקציות ברקע (`background=true`), הערך של `status` באינטראקציה מוגדר כ-`failed`, ואותם `code` ו-`message` מופיעים ברשימת `errors` שלה.
בסטרימינג, השגיאה מגיעה כאירוע `error`.

## מסנני בטיחות

מסנני הבטיחות של Gemini API ניתנים להתאמה ומכסים את הקטגוריות הבאות:

| קטגוריה | ערך (API) | תיאור |
| --- | --- | --- |
| הטרדה | `harassment` | תוכן פוגעני, מאיים או תוכן שמטרתו להציק, לענות או ללעוג. |
| דברי שטנה | `hate_speech` | תוכן שמקדם אלימות או מסית לשנאה כלפי אנשים פרטיים או קבוצות על סמך מאפיינים מסוימים. |
| תוכן מיני בוטה | `sexually_explicit` | תוכן שמכיל חומר בעל אופי מיני בוטה. |
| תוכן מסוכן | `dangerous_content` | תוכן שמקדם, מעודד או מאפשר פעילויות מסוכנות. |
| פריצת Jailbreak | `jailbreak` | הנחיות שנועדו לעקוף מסנני בטיחות. |

אתם יכולים להשתמש במסננים האלה כדי להתאים את התוכן לתרחיש לדוגמה שלכם. לדוגמה, אם אתם יוצרים דיאלוג למשחק וידאו, יכול להיות שתחליטו שזה בסדר לאפשר יותר תוכן שמסווג כ*מסוכן* בגלל אופי המשחק.

בנוסף למסנני הבטיחות שניתנים להתאמה, Gemini API כולל אמצעי הגנה מובנים מפני נזקים מהותיים, כמו תוכן שמסכן את בטיחות הילדים.
סוגי הנזק האלה תמיד חסומים ואי אפשר לשנות את ההגדרות שלהם.

## ערכי סף לחסימה

בגלל הבטיחות המובנית של המודל, מסננים נוספים **מושבתים** כברירת מחדל.
ההתנהגות של המודל כברירת מחדל מכסה את רוב תרחישי השימוש, ולכן כדאי לשנות את ההגדרות האלה רק אם יש צורך עקבי בכך באפליקציה שלכם.

בטבלה הבאה מתוארים ערכי הסף שאפשר להגדיר לכל קטגוריה. לדוגמה, אם מגדירים את האפשרות **דברי שטנה** ל**חסימה של חלק מהתוכן** (`block_only_high`), תוכן שיש סבירות גבוהה שהוא דברי שטנה ייחסם, וכל תוכן אחר עם סבירות נמוכה יותר יאושר.

| סף (Google AI Studio) | סף (API) | תיאור |
| --- | --- | --- |
| מושבת | `off` | השבתת מסנן הבטיחות |
| חסימה של כמה אנשים | `block_only_high` | חסימה כשיש סבירות גבוהה לתוכן לא בטוח |
| חסימה של חלק מהאתרים | `block_medium_and_above` | חסימה כשיש הסתברות בינונית או גבוהה לתוכן לא בטוח |
| חסימה של רוב האנשים | `block_low_and_above` | חסימה כשההסתברות לתוכן לא בטוח היא נמוכה, בינונית או גבוהה |

### הסבירות לעומת רמת החומרה

ב-Gemini API, הסבירות שהתוכן לא בטוח מסווגת כגבוהה, בינונית, נמוכה או זניחה. הוא חוסם תוכן על סמך ההסתברות הזו, ולא על סמך חומרת הנזק. יכול להיות שתוכן מסוים יקבל ציון נמוך בסבירות שהוא לא בטוח, למרות שהנזק שהוא עלול לגרום חמור. לדוגמה, השוו בין המשפטים הבאים:

1. הרובוט נתן לי אגרוף.
2. הרובוט חתך אותי.

יכול להיות שהמשפט הראשון יהיה בעל סבירות גבוהה יותר להיות לא בטוח, אבל יכול להיות שתחשבו שהמשפט השני חמור יותר. חשוב לבדוק בקפידה כדי למצוא את רמת החסימה שתומכת בתרחיש לדוגמה שלכם, תוך צמצום הפגיעה במשתמשי הקצה.

## איך משנים את הגדרות הבטיחות ב-Google AI Studio

לוחצים על **הגדרות אבטחה** בקטע **הגדרות מתקדמות** בחלונית **הגדרות ההרצה** כדי לפתוח את תיבת הדו-שיח **הגדרות אבטחה של ההרצה**. בחלון הקופץ, אפשר להשתמש בפסי ההזזה כדי לשנות את רמת סינון התוכן לפי קטגוריית בטיחות:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=he)

כששולחים בקשה (למשל, שואלים את המודל שאלה), מופיעה ההודעה **התוכן חסום** warningאם התוכן של הבקשה חסום. כדי לראות פרטים נוספים, מעבירים את מצביע העכבר מעל הטקסט **התוכן נחסם** כדי לראות את הקטגוריה ואת הסבירות לסיווג הנזק.

## השלבים הבאים

- מידע נוסף על ה-API המלא זמין במאמרי העזרה של ה-API [Interactions API reference](https://ai.google.dev/api/interactions-api?hl=he).
- כדאי לעיין ב[הנחיות הבטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he) כדי לקבל סקירה כללית של שיקולי בטיחות בפיתוח עם מודלים של שפה גדולה (LLM).
- [מידע נוסף על הערכת הסבירות לעומת חומרת הבעיה](https://developers.perspectiveapi.com/s/about-the-api-score)
- [מידע נוסף על מוצרים שתורמים לפתרונות בטיחות כמו Perspective API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-15 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-15 (שעון UTC)."],[],[]]
