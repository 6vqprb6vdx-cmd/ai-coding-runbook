---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=he
fetched_at: 2026-07-06T05:15:21.647226+00:00
title: "\u05ea\u05d7\u05d9\u05dc\u05ea \u05d4\u05e2\u05d1\u05d5\u05d3\u05d4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# תחילת העבודה

במדריך הזה נסביר איך להתחיל להשתמש ב-Gemini API באמצעות [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he). תבצעו את הקריאה הראשונה ל-API תוך פחות מדקה, ותכירו את התכונות הבאות: יצירת טקסט, הבנה מולטי-מודאלית, יצירת תמונות, פלט מובנה, כלים, בקשות להפעלת פונקציות, סוכנים והפעלה ברקע.

ה-API של האינטראקציות זמין דרך ה-SDK של [Python](https://github.com/googleapis/python-genai) ו-[JavaScript](https://github.com/googleapis/js-genai), וגם דרך REST.

## 1. קבלת מפתח API

כדי להשתמש ב-Gemini API, צריך מפתח API כדי לאמת את הבקשות, לאכוף מגבלות אבטחה ולעקוב אחרי השימוש בחשבון.

- מערכת Google AI Studio יוצרת באופן אוטומטי פרויקט ומפתח API למשתמשים חדשים.
  אפשר להעתיק אותו מ[דף מפתחות ה-API](https://aistudio.google.com/api-keys?hl=he).
- אם אתם צריכים מפתח חדש, לוחצים על **Create API key** (יצירת מפתח API) ב-AI Studio ופועלים לפי ההוראות בתיבת הדו-שיח כדי להוסיף צמד חדש של מפתח ופרויקט.

[יצירת מפתח Gemini API](https://aistudio.google.com/apikey?hl=he)

מגדירים את המפתח כמשתנה סביבה:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### שדרוג לרמה בתשלום

שדרוג לתוכנית בתשלום מגדיל את מגבלות הקצב ומחייב הגדרה של חיוב ב-Cloud.

- לוחצים על **הגדרת חיוב** בדפים [מפתחות API](https://aistudio.google.com/api-keys?hl=he) או [פרויקטים](https://aistudio.google.com/projects?hl=he) ב-AI Studio.
- פועלים לפי ההוראות בתיבת הדו-שיח של החיוב ב-Cloud כדי ליצור או לקשר חשבון לחיוב, להוסיף אמצעי תשלום ולשלם מראש לפחות 10$ (או סכום שווה ערך במטבע אחר) בקרדיטים בתשלום.
- אפשר לראות את השימוש ב-API ב-[Google AI Studio](https://aistudio.google.com/usage?hl=he) בקטע **מרכז הבקרה** > **שימוש**.

מידע נוסף זמין [בדף החיוב](https://ai.google.dev/gemini-api/docs/billing?hl=he).

## 2. התקנה של SDK וביצוע השיחה הראשונה

מתקינים את ה-SDK ויוצרים טקסט באמצעות קריאה אחת ל-API.

### Python

מתקינים את ה-SDK:

```
pip install -U google-genai
```

מאחלים את הלקוח ושולחים בקשה:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

מתקינים את ה-SDK:

```
npm install @google/genai
```

מאחלים את הלקוח ושולחים בקשה:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**תשובה:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

כשמשתמשים ב-REST, ה-API מחזיר את משאב `Interaction` המלא שמכיל מטא-נתונים, נתוני שימוש והיסטוריה מפורטת של התור.

ערכות ה-SDK חושפות את התשובה המלאה, אבל הן גם מספקות מאפיינים נוחים כמו `interaction.output_text` ו-`interaction.output_image` כדי לגשת ישירות לתוצרים הסופיים. ב[סקירה הכללית על אינטראקציות](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) מוסבר על מבנה התשובות, וב[מדריך ליצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he) מפורטים הוראות המערכת והגדרות היצירה.

## 3. הצגת התשובה באופן שוטף

כדי שהאינטראקציה תהיה חלקה יותר, אפשר להזרים את התשובה בזמן שהיא נוצרת. כל אירוע `step.delta` מספק נתח טקסט שאפשר להציג באופן מיידי.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

בסטרימינג, השרת מגיב בסטרים של אירועים שנשלחים מהשרת (SSE). כל אירוע כולל סוג ונתוני JSON.

**תשובה:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

ב[מדריך לאינטראקציות עם סטרימינג](https://ai.google.dev/gemini-api/docs/streaming?hl=he) מוסבר בפירוט איך לטפל באירועים של סטרימינג ובסוגי דלתא.

## 4. שיחות רב-שלביות

‫Interactions API תומך בשיחות מרובות שלבים בשתי גישות:

- **Stateful (מומלץ)**: המשך שיחה בשרת באמצעות `previous_interaction_id`. אידיאלי לרוב תהליכי העבודה של צ'אטים וסוכנים שבהם רוצים שהשרת ינהל את ההיסטוריה ויבצע אופטימיזציה של שמירת המידע במטמון.
- **ללא שמירת מצב**: כדי לנהל את היסטוריית השיחות בצד הלקוח, צריך להעביר את כל התורות הקודמות (כולל שלבי החשיבה והשימוש בכלי של המודל) בכל בקשה.

### עם שמירת מצב (מומלץ)

אפשר ליצור שרשרת של אינטראקציות על ידי העברת `previous_interaction_id`. השרת מנהל את היסטוריית השיחות המלאה בשבילכם.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### בלי שמירת מצב

להגדיר את היסטוריית השיחות עם `store=false` ולנהל אותה בצד הלקוח. אתם צריכים לשמור את כל השלבים שנוצרו על ידי המודל (כולל השלבים `thought` ו-`function_call`) ולשלוח אותם מחדש בדיוק כפי שהם התקבלו.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**תשובה:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

האינטראקציה השנייה מחזירה אובייקט תגובה מלא שכולל רק את השלבים החדשים, אבל הוא מבוסס על ההקשר של התור הקודם. מידע נוסף על שמירת מצב ב[מדריך לשיחות רב-שלביות](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#multi-turn-conversations). אפשר גם לעיין במידע על [מצב בלי שמירת מצב](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#stateless-conversations) לניהול היסטוריה בצד הלקוח.

## 5. הבנה מולטי-מודאלית

מודלים של Gemini מבינים תמונות, אודיו, סרטונים ומסמכים באופן מובנה. העברת מדיה לצד טקסט בבקשה אחת.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**תשובה:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

[במדריך להבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he) מוסבר איך מעבירים תמונות, סרטונים וקובצי אודיו.

[hearing

הבנת אודיו

לתמלל קובצי אודיו, לסכם אותם או לענות על שאלות לגביהם.](https://ai.google.dev/gemini-api/docs/audio?hl=he)
[videocam

הבנת סרטונים

לנתח את תוכן הסרטון, לאתר אירועים ולתאר פעולות.](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he)
[description

עיבוד מסמכים

חילוץ מידע מקובצי PDF ומפורמטים אחרים של מסמכים.](https://ai.google.dev/gemini-api/docs/document-processing?hl=he)

## 6. יצירה מולטי-מודאלית

‫Gemini יכול ליצור תמונות באופן טבעי באמצעות מודלי התמונות [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=he).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**תשובה:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

כשהמודל יוצר תמונה, הוא מחזיר את נתוני התמונה בקידוד base64 בשלב במערך `steps`, וגם באמצעות מאפיין הנוחות `output_image`. [במדריך ליצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he) אפשר לקרוא על יחסי גובה-רוחב, עריכת תמונות והפניות.

[record\_voice\_over

יצירת דיבור

יצירת דיבור רגשי של כמה דוברים באמצעות Gemini 3.1 Flash TTS.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)
[music\_note

יצירת מוזיקה

אתם יכולים ליצור קליפים ושירים באורך מלא עם Lyria 3.](https://ai.google.dev/gemini-api/docs/music-generation?hl=he)

## 7. שימוש בפלט מובנה

הגדרת המודל להחזרת JSON שתואם לסכימה שהגדרתם. פלט מובנה פועל עם [Pydantic](https://docs.pydantic.dev/latest/) ‏ (Python) ועם [Zod](https://zod.dev/) ‏ (JavaScript).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**תשובה:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

בלוק הפלט של הטקסט מכיל מחרוזת JSON תקינה שתואמת בדיוק לסכימה המבוקשת. ב[מדריך לפלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) מוסבר איך מגדירים מבנים מורכבים יותר וסכימות רקורסיביות.

## 8. שימוש בכלים

להשתמש בחיפוש Google כדי להוסיף לתשובה של המודל מידע בזמן אמת. ה-API מחפש באופן אוטומטי, מעבד את התוצאות ומחזיר ציטוטים.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**תשובה:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

השלבים של החיפוש מפורטים בהיסטוריית האינטראקציות, והפלט הסופי כולל ציטוטים מוטמעים שמפנים למקורות באינטרנט.

ב[מדריך להארקה של חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) מוסבר איך לחלץ ציטוטים מחיפוש Google, וב[מדריך לשילוב כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he) מוסבר איך לשלב בין כמה כלים.

[code

הרצת קוד

להריץ קוד Python בסביבת Borg מאובטחת שפועלת בארגז חול.](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)
[link

ההקשר של כתובת ה-URL

העברת כתובות URL ציבוריות באינטרנט ישירות כדי לבסס את התשובות על תוכן דף האינטרנט.](https://ai.google.dev/gemini-api/docs/url-context?hl=he)
[search

חיפוש קבצים

יצירת אינדקס וחיפוש במסמכים ובקובצי מדיה שהועלו.](https://ai.google.dev/gemini-api/docs/file-search?hl=he)
[map

מפות Google

התשובות מבוססות על נתונים גיאו-מרחביים ונתוני מיקום מהעולם האמיתי.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)
[computer

שימוש במחשב

אוטומציה של דפדפן ואינטראקציה עם המסך.](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)

## 9. הפעלת פונקציות משלכם

התכונה 'הפעלת פונקציות' מאפשרת לכם לחבר את המודל לקוד שלכם. אתם מצהירים על השם והפרמטרים של הפונקציה, המודל מחליט מתי להפעיל אותה ומחזיר ארגומנטים מובנים, ואתם מפעילים אותה באופן מקומי ושולחים את התוצאה בחזרה.

### עם שמירת מצב (מומלץ)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### בלי שמירת מצב

אפשר גם להשתמש בהפעלת פונקציות במצב חסר מצב (stateless) על ידי ניהול היסטוריית השיחות בצד הלקוח והגדרת `store=false`. במצב ללא שמירת סטטוס, צריך להעביר את ההיסטוריה המלאה של השיחה בשדה `input` של כל בקשה עוקבת. ההיסטוריה הזו צריכה לכלול:

1. השלב הראשוני `user_input`.
2. כל השלבים שנוצרו על ידי המודל ומוחזרים בתור 1 (כולל השלבים `thought` ו-`function_call`) בדיוק כפי שהתקבלו.
3. השלב `function_result` שמכיל את הפלט של הפונקציה שהופעלה.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**תשובה:**

במהלך תור 1, המודל מחזיר תשובה עם הסטטוס `requires_action` והשלב `function_call`:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

אחרי שמריצים את הפונקציה באופן מקומי ושולחים את התוצאה (תור 2), האינטראקציה הסופית שהושלמה מחזירה:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

למידע על תכונות מתקדמות כמו קריאה מקבילה לפונקציות או מצבי בחירת פונקציות, אפשר לעיין [במדריך לקריאה לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).

## 10. הפעלת סוכן מנוהל

סוכנים מנוהלים פועלים בארגז חול מרוחק עם גישה לכלים כמו הרצת קוד וניהול קבצים. מעבירים `agent` במקום `model` ומגדירים את `environment="remote"`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

אתם יכולים גם להגדיר ולשמור [סוכנים מותאמים אישית](https://ai.google.dev/gemini-api/docs/custom-agents?hl=he) עם הוראות, כישורים ומקורות נתונים משלכם.

[rocket\_launch

מדריך למתחילים

איך מתקשרים לסוכן, משדרים תשובות ויוצרים סוכן בהתאמה אישית](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he)
[smart\_toy

Antigravity Agent

יכולות, כלים, קלט רב-אופני ותמחור של הסוכן שמוגדר כברירת מחדל.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he)
[experiment

סוכנים ב-AI Studio

סביבת משחקים ויזואלית ליצירת אב טיפוס של סוכנים בלי לכתוב קוד.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=he)

## 11. הפעלת משימות ברקע

מגדירים את `background=True` להרצת משימות ארוכות באופן אסינכרוני. סקר לתוצאות עם `interactions.get()`. פרטים נוספים זמינים ב[מדריך להרצת תהליכים ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**תשובה:**

התשובה הראשונית מוחזרת באופן מיידי עם הסטטוס `in_progress`:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

אחרי שהמשימה ברקע מסתיימת, בדיקת מצב האינטראקציה מחזירה:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

ב[מדריך להרצת מודלים וסוכנים ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) אפשר לקרוא על הרצת מודלים וסוכנים באופן אסינכרוני.

## המאמרים הבאים

- [הרצה ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he): הרצת משימות ארוכות באופן אסינכרוני וניהול מצב.
- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he): הוראות מערכת, הגדרות יצירה ותבניות טקסט מתקדמות.
- [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he): יחסי גובה-רוחב, עריכת תמונות ותמונות להמחשה.
- [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he): סיווג, זיהוי אובייקטים ושאלות ותשובות ויזואליות.
- [חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he): שימוש בשרשרת חשיבה למשימות מורכבות.
- [קריאה לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he): מצבי פונקציות מקבילים, קומפוזיציוניים ומוגבלים.
- [חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he): ביסוס, ציטוטים והצעות לחיפוש.
- [סוכנים מנוהלים](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he): סוכנים מוכנים מראש עם הרצת קוד וניהול קבצים.
- ‫[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he): מחקר אוטונומי רב-שלבי עם תכנון וסינתזה.
- ‫[Structured output](https://ai.google.dev/gemini-api/docs/structured-output?hl=he): סכימות JSON, סוגי enum והגדרות סוגים רקורסיביות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-01 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-01 (שעון UTC)."],[],[]]
