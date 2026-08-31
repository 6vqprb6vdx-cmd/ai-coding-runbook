---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=he
fetched_at: 2026-08-31T06:29:55.649688+00:00
title: "\u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05de\u05e4\u05ea\u05d7\u05d9\u05dd \u05e9\u05dc Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)

שליחת משוב

# מדריך למפתחים של Gemini 3

‫Gemini 3 היא משפחת המודלים הכי חכמה שלנו עד היום, והיא מבוססת על יכולות חשיבה רציונלית המתקדמות ביותר. הוא נועד להפוך כל רעיון למציאות באמצעות שליטה בתהליכי עבודה של סוכנים, בתכנות אוטונומי ובמשימות מולטי-מודאליות מורכבות.
במדריך הזה מוסברות התכונות העיקריות של משפחת מודלים Gemini 3 ואיך להפיק ממנה את המרב.

כדאי לעיין ב[אוסף האפליקציות של Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=he) כדי לראות איך המודל מתמודד עם חשיבה רציונלית משופרת, תכנות אוטונומי ומשימות מורכבות מולטי-מודאליות.

כדי להתחיל, אפשר להשתמש בכמה שורות קוד:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## הכרת סדרת Gemini 3

‫Gemini 3.1 Pro הוא המודל הכי טוב למשימות מורכבות שדורשות ידע רחב על העולם וחשיבה רציונלית משופרת במגוון אופנים.

‫Gemini 3 Flash הוא המודל העדכני ביותר בסדרת 3, עם יכולות AI חכמות ברמת Pro, במהירות ובמחיר של Flash.

‫Nano Banana Pro (שנקרא גם Gemini 3 Pro Image) הוא המודל שלנו ליצירת תמונות באיכות הכי גבוהה, ו-Nano Banana 2 (שנקרא גם Gemini 3.1 Flash Image) הוא המודל המקביל ליצירת תמונות בכמויות גדולות, ביעילות גבוהה ובמחיר נמוך יותר.

‫Gemini 3.1 Flash-Lite הוא המודל המתקדם שלנו שנועד לבצע משימות בהיקף גדול בצורה חסכונית.

כל המודלים של Gemini 3 נמצאים כרגע בגרסת Preview.

| מזהה דגם | חלון ההקשר (בפנים / בחוץ) | תאריך סף הידע | מחירים (קלט / פלט)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | ‫1M / 64k | ינואר 2025 | ‫0.25$ (טקסט, תמונה, סרטון), 0.50$ (אודיו) / 1.50$ |
| **gemini-3.1-flash-image-preview** | ‫128k / 32k | ינואר 2025 | ‫0.25$ (קלט טקסט) / 0.067$ (פלט תמונה)\*\* |
| **gemini-3.1-pro-preview** | ‫1M / 64k | ינואר 2025 | ‫2$ / 12$ (פחות מ-200k טוקנים)   4$ / 18$ (יותר מ-200k טוקנים) |
| **gemini-3-flash-preview** | ‫1M / 64k | ינואר 2025 | ‫0.50$ / 3$‎ |
| **gemini-3-pro-image-preview** | ‫65,000 / 32,000 | ינואר 2025 | ‫2$ (הזנת טקסט) / 0.134$ (פלט תמונה)\*\* |

*\* המחירים הם למיליון טוקנים, אלא אם צוין אחרת.*
*\*\* המחיר של התמונות משתנה בהתאם לרזולוציה. פרטים נוספים מופיעים ב[דף התמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he).*

מידע נוסף על מגבלות, תמחור ופרטים נוספים זמין ב[דף המודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he).

## תכונות חדשות ב-Gemini 3 API

‫Gemini 3 כולל פרמטרים חדשים שנועדו לתת למפתחים יותר שליטה על זמן האחזור, העלות והדיוק של המודל הרב-אופני.

### רמת החשיבה

מודלים מסדרת Gemini 3 משתמשים כברירת מחדל בחשיבה דינמית כדי להסיק מסקנות מההנחיות. אפשר להשתמש בפרמטר `thinking_level` כדי לשלוט ב**עומק** המקסימלי של תהליך החשיבה הרציונלית הפנימי של המודל לפני שהוא מפיק תשובה. ‫Gemini 3 מתייחס לרמות האלה כאל הקצאות יחסיות של משאבים לצורך חשיבה, ולא כאל הבטחות מחמירות לגבי טוקנים.

אם לא מציינים את `thinking_level`, Gemini 3 ישתמש כברירת מחדל ב-`high`. כדי לקבל תשובות מהירות יותר עם חביון נמוך יותר כשלא נדרשת חשיבה רציונלית מורכבת, אפשר להגביל את רמת החשיבה של המודל ל-`low`.

| רמת ההעמקה | ‫Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | תיאור |
| --- | --- | --- | --- | --- |
| **`minimal`** | לא נתמך | נתמך (ברירת מחדל) | נתמך | מתאים להגדרה 'ללא חשיבה' ברוב השאילתות. יכול להיות שהמודל יחשוב מעט מאוד כדי לעבוד על משימות תכנות מורכבות. מצמצם את זמן האחזור של אפליקציות צ'אט או אפליקציות עם תפוקה גבוהה. הערה: `minimal` לא מבטיח שהחשיבה מושבתת. |
| **`low`** | נתמך | נתמך | נתמך | מצמצם את זמן האחזור ואת העלות. הכי טוב למעקב אחרי הוראות פשוטות, לצ'אט או לאפליקציות עם תפוקה גבוהה. |
| **`medium`** | נתמך | נתמך | נתמך | חשיבה מאוזנת לרוב המשימות. |
| **`high`** | נתמך (ברירת מחדל, דינמי) | נתמך (דינמי) | נתמך (ברירת מחדל, דינמי) | העומק המקסימלי של החשיבה הרציונלית. יכול להיות שיעבור הרבה יותר זמן עד שהמודל יגיע לטוקן הפלט הראשון (שלא קשור לחשיבה), אבל הפלט יהיה מנומק יותר. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### טמפרטורה

בכל המודלים של Gemini 3, מומלץ מאוד להשאיר את פרמטר רמת האקראיות בערך ברירת המחדל שלו, `1.0`.

במודלים קודמים, כדאי היה לשנות את הגדרת רמת האקראיות כדי לשלוט באיזון בין יצירתיות לבין דטרמיניזם. לעומת זאת, יכולות החשיבה הרציונלית של Gemini 3 מותאמות להגדרת ברירת המחדל. שינוי הטמפרטורה (הגדרה של ערך נמוך מ-1.0) עלול להוביל להתנהגות לא צפויה, כמו לולאות או ביצועים ירודים, במיוחד במשימות מורכבות שקשורות למתמטיקה או להיגיון.

### חתימות של מחשבות

מודלים של Gemini 3 משתמשים בחתימות מחשבה כדי לשמור על הקשר של הנימוקים בקריאות ל-API. החתימות האלה הן ייצוגים מוצפנים של תהליך החשיבה הפנימי של המודל.

- **מצב Stateful (מומלץ)**: כשמשתמשים ב-Interactions API במצב Stateful (מספקים `previous_interaction_id`), השרת מנהל באופן אוטומטי את היסטוריית השיחות ואת חתימות המחשבה.
- **מצב בלי שמירת מצב**: אם אתם מנהלים את היסטוריית השיחות באופן ידני, אתם צריכים לכלול בלוקים של מחשבות עם החתימות שלהם בבקשות הבאות כדי לאמת את האותנטיות.

מידע מפורט זמין בדף [חתימות מחשבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he).

### פלט מובנה עם כלים

מודלים של Gemini 3 מאפשרים לכם לשלב [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) עם כלים מובנים, כולל [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he), [URL Context](https://ai.google.dev/gemini-api/docs/url-context?hl=he), [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) ו[קריאה להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### יצירת תמונות

‫Gemini 3.1 Flash Image ו-Gemini 3 Pro Image מאפשרים ליצור ולערוך תמונות מהנחיות טקסט. הוא משתמש בחשיבה רציונלית כדי 'לחשוב' על פרומפט, ויכול לאחזר נתונים בזמן אמת – כמו תחזיות מזג אוויר או תרשימי מניות – לפני שהוא משתמש בעיגון של [חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) כדי ליצור תמונות ברמת דיוק גבוהה.

**יכולות חדשות ומשופרות:**

- **רזולוציית 4K ועיבוד טקסט:** אפשר ליצור טקסט ותרשימים חדים וקריאים ברזולוציות של עד 2K ו-4K.
- **יצירה מבוססת-קרקע:** אפשר להשתמש בכלי `google_search` כדי לאמת עובדות וליצור תמונות על סמך מידע מהעולם האמיתי. ‫Grounding עם חיפוש *תמונות* ב-Google זמין ל-Gemini 3.1 Flash Image.
- **עריכה בממשק שיחה:** עריכת תמונות רב-שלבית באמצעות הנחיות פשוטות (למשל, "הפוך את הרקע לשקיעה"). תהליך העבודה הזה מסתמך על **חתימות מחשבה** כדי לשמור על ההקשר החזותי בין התורות.

פרטים מלאים על יחסי גובה-רוחב, תהליכי עריכה ואפשרויות הגדרה זמינים [במדריך ליצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**דוגמה לתשובה**

![מזג האוויר בטוקיו](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=he)

### הרצת קוד עם תמונות

‫Gemini 3 Flash יכול להתייחס לראייה כאל חקירה פעילה, ולא רק כאל מבט סטטי. באמצעות שילוב של חשיבה רציונלית עם [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he), המודל מגבש תוכנית, ואז כותב ומריץ קוד Python כדי לבצע פעולות כמו הגדלה, חיתוך, הוספת הערות או שינוי תמונות בדרכים אחרות, שלב אחר שלב, כדי לעגן את התשובות שלו מבחינה ויזואלית.

**תרחישים לדוגמה:**

- **התקרבות ובדיקה:** המודל מזהה באופן מרומז מתי הפרטים קטנים מדי (למשל, קריאת מד מרחק או מספר סידורי) וכותב קוד לחיתוך ולבדיקה מחדש של האזור ברזולוציה גבוהה יותר.
- **מתמטיקה והצגה גרפית:** המודל יכול להריץ חישובים מרובי-שלבים באמצעות קוד (למשל, סיכום פריטים בחשבונית או יצירת תרשים Matplotlib מנתונים שחולצו).
- **הערות לתמונות:** המודל יכול לצייר חצים, תיבות תוחמות או הערות אחרות ישירות על תמונות כדי לענות על שאלות שקשורות למיקום, כמו "איפה צריך למקם את הפריט הזה?".

כדי להפעיל חשיבה ויזואלית, מגדירים את [הפעלת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) ככלי. המודל ישתמש אוטומטית בקוד כדי לערוך תמונות כשצריך.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

מידע נוסף על הרצת קוד עם תמונות זמין במאמר בנושא [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he#images).

### תשובות של פונקציות מרובות מצבים

[בקשות להפעלת פונקציות מולטי-מודאליות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#multimodal)
מאפשרות למשתמשים לקבל תשובות לפונקציות שמכילות
אובייקטים מולטי-מודאליים, וכך לשפר את השימוש ביכולות של המודל להפעלת פונקציות. קריאה רגילה לפונקציות תומכת רק בתשובות לפונקציות שמבוססות על טקסט:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### שילוב של כלים מובנים וקריאות לפונקציות

‫Gemini 3 מאפשר שימוש בכלים מובנים (כמו חיפוש Google, הקשר של כתובת URL ו[עוד](https://ai.google.dev/gemini-api/docs/tools?hl=he)) ובכלים מותאמים אישית של [בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) באותה קריאה ל-API, וכך מאפשר תהליכי עבודה מורכבים יותר.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## מעבר מ-Gemini 2.5

‫Gemini 3 היא משפחת המודלים הכי מתקדמת שלנו עד היום, והיא מציעה שיפור הדרגתי בהשוואה ל-Gemini 2.5. כשמבצעים העברה, חשוב לקחת בחשבון את הנקודות הבאות:

- **העמקה:** אם השתמשתם בעבר בהנדסת פרומפטים מורכבת (כמו שרשרת חשיבה) כדי לגרום ל-Gemini 2.5 להסיק מסקנות, נסו להשתמש ב-Gemini 3 עם `thinking_level: "high"` והנחיות פשוטות יותר.
- **הגדרות רמת אקראיות:** אם הקוד הקיים מגדיר רמת אקראיות באופן מפורש (במיוחד לערכים נמוכים של פלט דטרמיניסטי), מומלץ להסיר את הפרמטר הזה ולהשתמש בערך ברירת המחדל של Gemini 3, שהוא 1.0, כדי למנוע בעיות פוטנציאליות של לולאות או ירידה בביצועים במשימות מורכבות.
- **הבנת מסמכים ו-PDF:**
  אם הסתמכתם על התנהגות ספציפית של ניתוח מסמכים צפופים, כדאי לבדוק את ההגדרה החדשה `media_resolution_high` כדי לוודא שהדיוק נשמר.
- **צריכת טוקנים:** מעבר להגדרות ברירת המחדל של Gemini 3 עשוי **להגדיל** את השימוש בטוקנים בקובצי PDF, אבל **להקטין** את השימוש בטוקנים בסרטונים. אם הבקשות חורגות עכשיו מחלון ההקשר בגלל רזולוציות ברירת מחדל גבוהות יותר, מומלץ להקטין את רזולוציית המדיה באופן מפורש.
- **פילוח תמונות:** יכולות פילוח תמונות (החזרת מסכות של אובייקטים ברמת הפיקסל) לא נתמכות ב-Gemini 3 Pro או ב-Gemini 3 Flash. לגבי עומסי עבודה שדורשים חלוקת תמונות למקטעים מובנית, אנחנו ממליצים להמשיך להשתמש ב-Gemini 2.5 Flash עם השבתת התכונה 'חשיבה'.
- **שימוש במחשב:** מודלים Gemini 3 Pro ו-Gemini 3 Flash תומכים ב[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he). בשונה מסדרת 2.5, לא צריך להשתמש במודל נפרד כדי לגשת לכלי 'שימוש במחשב'.
- **תמיכה בכלי עזר**: [שילוב של כלי עזר מובנים עם בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he) נתמך עכשיו במודלים של Gemini 3. ‫[Maps grounding](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he) נתמך עכשיו גם במודלים של Gemini 3.

## תאימות ל-OpenAI

למשתמשים שמשתמשים ב[שכבת התאימות ל-OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he), פרמטרים רגילים (`reasoning_effort` של OpenAI) ממופים אוטומטית למקבילים ב-Gemini ‏ (`thinking_level`).

## שיטות מומלצות לכתיבת הנחיות

‫Gemini 3 הוא מודל חשיבה רציונלית, ולכן צריך לשנות את ההנחיות שנותנים לו.

- **הוראות מדויקות:** כדאי לנסח את ההנחיות בצורה תמציתית. ‫Gemini 3 מגיב הכי טוב להוראות ישירות וברורות. יכול להיות שהיא תנתח יתר על המידה טכניקות מפורטות או מורכבות מדי של הנדסת פרומפטים שמשמשות מודלים ישנים יותר.
- **פירוט הפלט:** כברירת מחדל, Gemini 3 פחות מפורט ומעדיף לספק תשובות ישירות ויעילות. אם התרחיש לדוגמה שלכם מחייב אישיות יותר שיחתית או "פטפטנית", אתם צריכים להנחות את המודל באופן מפורש בהנחיה (למשל, "תסביר את זה בתור עוזר ידידותי ופטפטן").
- **ניהול הקשר:** כשעובדים עם מערכי נתונים גדולים (למשל, ספרים שלמים, בסיסי קוד או סרטונים ארוכים), כדאי להציב את ההוראות או השאלות הספציפיות בסוף ההנחיה, אחרי הקשר של הנתונים. כדי להצמיד את ההסבר של המודל לנתונים שסיפקתם, כדאי להתחיל את השאלה בניסוח כמו "בהתבסס על המידע שלמעלה...".

מידע נוסף על אסטרטגיות לעיצוב פרומפטים זמין ב[מדריך להנדסת פרומפטים](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=he).

## שאלות נפוצות

1. **מהו תאריך סף הידע של Gemini 3?** למודלים של Gemini 3 יש תאריך סף ידע של ינואר 2025. כדי לקבל מידע עדכני יותר, אפשר להשתמש בכלי [הארקה של חיפוש](https://ai.google.dev/gemini-api/docs/google-search?hl=he).
2. **מהן המגבלות של חלון ההקשר?** מודלים של Gemini 3 תומכים בחלון הקשר של מיליון טוקנים של קלט ועד 64,000 טוקנים של פלט.
3. **יש תוכנית בחינם ל-Gemini 3?** ‫Gemini 3 Flash
   `gemini-3-flash-preview` כולל רמת שימוש חינמית ב-Gemini API. אתם יכולים לנסות את Gemini 3.1 Pro ו-3 Flash בחינם ב-Google AI Studio, אבל אין רמת שירות בחינם ל-`gemini-3.1-pro-preview` ב-Gemini API.
4. **האם הקוד הישן שלי של `thinking_budget` עדיין יעבוד?** כן, `thinking_budget` עדיין נתמך לצורך תאימות לאחור, אבל מומלץ לעבור ל-`thinking_level` כדי לקבל ביצועים צפויים יותר. אל תשתמשו בשניהם באותה בקשה.
5. **האם Gemini 3 תומך ב-Batch API?** כן, Gemini 3 תומך ב-[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he).
6. **האם יש תמיכה בשמירת נתונים במטמון לפי הקשר?** כן, [שמירת הקשר במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he) נתמכת ב-Gemini 3.
7. **אילו כלים נתמכים ב-Gemini 3?** ‫Gemini 3 תומך ב[חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he), ב[הארקה באמצעות מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he), ב[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he), ב[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) וב[הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he). הוא תומך גם ב[קריאה לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) סטנדרטית עבור כלים מותאמים אישית משלכם, וגם ב[שילוב עם כלים מובנים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).
8. **מה זה `gemini-3.1-pro-preview-customtools`?** אם אתם משתמשים ב-`gemini-3.1-pro-preview` והמודל מתעלם מהכלים המותאמים אישית שלכם ומעדיף פקודות bash, נסו להשתמש במודל `gemini-3.1-pro-preview-customtools`.
   מידע נוסף [כאן][customtools-model].

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-08-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-08-19 (שעון UTC)."],[],[]]
