---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=he
fetched_at: 2026-08-03T04:30:17.858524+00:00
title: "\u05d9\u05e6\u05d9\u05e8\u05d4 \u05d5\u05e2\u05e8\u05d9\u05db\u05d4 \u05e9\u05dc \u05e1\u05e8\u05d8\u05d5\u05e0\u05d9\u05dd \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# יצירה ועריכה של סרטונים באמצעות Gemini Omni Flash

‫Gemini Omni Flash‏ (`gemini-omni-flash-preview`) הוא מודל רב-אופני עם ביצועים גבוהים, שנועד ליצירה ועריכה של סרטונים במהירות גבוהה ולשליטה קולנועית.
‫Gemini Omni מבוסס על היכולות הבסיסיות הבאות שמבדילות אותו ממודלים קודמים של סרטונים:

- **מולטי-מודאליות מובנית:** הוא מעבד טקסט, תמונות, אודיו וסרטונים בו-זמנית, ומספק פלט מגובש, עקבי וניתן לשליטה.
- **עריכה באמצעות שיחה:** התכונה הזו מופעלת על ידי [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he), והיא מאפשרת לכם לשפר ולערוך את הסרטונים שלכם באופן איטרטיבי באמצעות שיחה בשפה טבעית. מתארים את השינוי שרוצים לבצע, והמודל מבצע את העריכה תוך שמירה על החלקים בסרטון שרוצים להשאיר.
- **ידע על העולם:** ‫Gemini Omni משלב בין הבנה של פיזיקה לבין הידע של Gemini בהיסטוריה, במדע ובהקשר תרבותי, ומגשר על הפער בין ריאליזם צילומי לבין סיפור משמעותי.

## יצירת סרטונים לפי טקסט

יצירת סרטון מהנחיית טקסט. המודל יוצר סרטון עם אודיו על סמך תיאור הטקסט שהזנתם. כדי לקבל את התוצאות הטובות ביותר, כדאי לכתוב הנחיות עם פרטים כמו תיאור הסצנה, תנועת המצלמה, התאורה והאווירה.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({  
  model: 'gemini-omni-flash-preview',  
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### סכימת תגובת REST

שדה הנוחות `interaction.output_video` הוא **SDK בלבד**.
כשמשתמשים ישירות ב-API בארכיטקטורת REST, מקבלים את פלט הסרטון ממערך `steps`.

**מבנה JSON גולמי של REST:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

### שליטה ביחס הגובה-רוחב

כדי ליצור סרטונים בפורמט אנכי, מגדירים את `aspect_ratio` ל-`"9:16"`. ברירת המחדל היא לרוחב (16:9).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

## יצירת סרטון מתמונה

אתם יכולים לספק תמונה לדוגמה עם הנחייה טקסטואלית. בהתאם להנחיה, המודל יחליט איך להשתמש בתמונה. התכונה הזו שימושית כדי להפיח חיים בתמונות של מוצרים, באיורים או בתמונות.

בדוגמה הבאה אפשר לראות איך משתמשים בתמונה לדוגמה של ציור של דג שקופץ מהמים:

![ציור של דג שקופץ מתוך המים](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=he)

עם ההנחיה הבאה:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

כדי ליצור סרטון ריאליסטי של הציור.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### הפניה לנושא הצילום

אתם יכולים ליצור סרטון שכולל נושאים ספציפיים שסיפקתם כתמונות לדוגמה.
לדוגמה, הקוד הבא מראה איך מספקים 2 תמונות של חתול וכדור צמר כדי ליצור סרטון של החתול משחק עם כדור הצמר.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### פרמטר המשימות

משתמשים בפרמטר `task` ב-`video-config` כדי לציין בבירור את ההתנהגות הרצויה. לדוגמה, אם רוצים שהמודל ייצור סרטון מתמונה, אפשר להגדיר את הפרמטר ל-`image_to_video`. אם לא מגדירים את הפרמטר הזה, המודל יסיק מההנחיה מה רוצים.

הערכים המותרים הם:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`

בדוגמה הבאה אפשר לראות איך מגדירים את זה עבור הדוגמה שלמעלה, שבה תמונה מוצגת לפני סרטון.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-flash-preview",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## עריכת סרטונים עם שמירת מצב

ליצור סרטון ולערוך אותו באופן איטרטיבי באמצעות הנחיות המשך. כל תור
מבוסס על התוצאה הקודמת. המודל זוכר את ההקשר של הסרטון, ומחיל את השינויים שלכם תוך שמירה על רכיבים שלא הזכרתם. אפשר להשתמש ב-`previous_interaction_id` כדי לעקוב אחרי היסטוריית השיחות ומצב הסרטון שנוצר בלי להעלות מחדש את הסרטון הקודם.

בדוגמה הבאה אפשר לראות איך יוצרים סרטון ראשון ואז עורכים אותו:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-flash-preview", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-flash-preview",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

דוגמה לסרטון מקורי:

דוגמה לסרטון ערוך:

כל תור בשיחה יוצר סרטון חדש. המודל מבין את ההקשר מהתורות הקודמות, כך שאפשר לבצע שינויים מצטברים כמו התאמת התאורה והחלפת הרקע, בלי לתאר מחדש את כל הסצנה.

### עריכת סרטונים משלכם

אפשר להעלות סרטונים באמצעות [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he) כדי לערוך אותם באמצעות Gemini Omni Flash.

בדוגמה הבאה אפשר לראות איך עורכים את הסרטון המקורי הבא:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-flash-preview",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

דוגמה לסרטון ערוך:

## אחזור סרטונים באמצעות URI

משתמשים בפרמטר `delivery="uri"` ב-`response_format` כדי לאחזר סרטונים שנוצרו בגודל של יותר מ-4MB.
הפעולה הזו מחזירה URI שמתארח ב-Google, שאפשר לשלוח לו בקשות עד שהסרטון `ACTIVE` לפני ההורדה.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**מבנה JSON גולמי של REST (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

## שיטות מומלצות

- **שימוש בהעברת URI לסרטונים גדולים:** לסרטונים בגודל של יותר מ-4MB (‎>720p
  when available), צריך להשתמש ב-`delivery="uri"` ב-`response_format` כדי להימנע ממגבלות על גודל המטען הייעודי.
- **ביצועים אופטימליים:** מגדירים את `background=false`,‏ `store=false` ו-`stream=false` כדי ליצור תשובות מהר יותר ובאופן סינכרוני. שימו לב: הגדרה של `store=false` פירושה שלא ניתן יהיה לערוך את הסרטון שנוצר בפעולות הבאות באמצעות `previous_interaction_id`.
- **דיוק ההנחיה:** פרטים נוספים זמינים בקטע [הנחיות לכתיבת הנחיות](#prompt-guide).

## מגבלות

- העלאה ועריכה של תמונות המכילות קטינים אינה נתמכת באזור הכלכלי האירופי, בשווייץ ובבריטניה.
- העלאה ועריכה של תמונות המכילות אנשים מסוימים שניתן לזהות אינה נתמכת.
- בשלב הזה אי אפשר לערוך סרטונים שהועלו באזור הכלכלי האירופי (EEA), בשווייץ ובבריטניה (אפשר לערוך סרטונים שנוצרו על ידי המודל).
- העלאת הפניות לאודיו לא נתמכת בגרסה הנוכחית של ה-API.
- סכימת ה-API מקבלת הפניות לסרטונים באורך של עד 3 שניות, אבל המודל לא מעבד אותן בצורה נכונה בשלב הזה.
- אי אפשר להפנות לכמה סרטונים או להסיק מסקנות על סמך כמה סרטונים. ניסיון ליצור הנחיות לכמה סרטונים עלול להוביל לירידה בביצועי המודל או לפלטים לא צפויים.
- אין תמיכה בסיומת וידאו ובאינטרפולציה של וידאו (יצירת וידאו בין המסגרת הראשונה לאחרונה).
- אין תמיכה בעריכה קולית.
- אין תמיכה ברוחב פס מוקצה.
- אין תמיכה בהוראות מערכת, בטמפרטורה, ב-`top_p`, ברצפי עצירה ובהנחיות שליליות (אפשר להוסיף את ההנחיות השליליות להנחיה הרגילה, למשל: "אל תעשה X").
- אין תמיכה בשימוש בסרטונים ב-YouTube כמקור מדיה.

## פרטים טכניים

- כל הסרטונים שנוצרים כוללים סימני מים של SynthID, שלא נראים לצופים אבל אפשר לזהות אותם באופן פרוגרמטי כדי לאמת את המקור.
- זמני יצירת הסרטונים משתנים בהתאם למשך, לרזולוציה ולעומס הנוכחי על ה-API. יצירת סרטונים ארוכים יותר וברזולוציה גבוהה יותר נמשכת זמן רב יותר.
- פילטרים של בטיחות תוכן מופעלים גם על הנחיות קלט וגם על סרטונים שנוצרו (והם תלויים באזור שלכם). הנחיות שמפירות את מדיניות השימוש ייחסמו.
- יש תמיכה מלאה באנגלית (EN), אבל שפות אחרות לא נבדקו, ולכן יכול להיות שהן יפעלו אבל התוצאות עשויות להיות שונות.

## מדריך לכתיבת הנחיות ל-Gemini Omni Flash

בקטע הזה יש טיפים ודוגמאות שיעזרו לכם לנסח הנחיות יעילות ל-Gemini Omni Flash.

### סצנה אחת

כברירת מחדל, Omni Flash ינסה ליצור סרטון עם כמה צילומים שונים.
הוא ינסה ליצור סיפור מעניין על סמך ההנחיה.

אם אתם רוצים שסרטון הפלט יכיל סצנה אחת, אתם צריכים לציין זאת בהנחיה:

- בסצנה רציפה אחת
- בצילום רציף אחד
- אין מעברים בין סצנות

לדוגמה:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### הסרת אלמנטים לא רצויים

אם הסרטון שנוצר מכיל דברים שלא רציתם, אפשר להוסיף הנחיות שליליות פשוטות כדי להימנע מהם:

- אין דיאלוג
- אין קישוטים
- אין אפקטים קוליים נוספים

### הנחיות לעריכה

ההנחיות הכי טובות לעריכת סרטונים הן הנחיות פשוטות. הנחיות מפורטות מדי עלולות להוביל לשינויים לא רצויים.

הנה עוד דוגמאות להנחיות פשוטות לעריכה:

- הסרטון ייראה כמו אנימה
- תשים כובע אופנתי על האדם הזה
- תשנה את התאורה כך שתהיה יותר דרמטית
- שינוי הטקסט בשלט ל-Omni Flash

כשעורכים היבט ספציפי של הסרטון, כדאי להוסיף את התג `"Keep everything else the same"` כדי לשמור על עקביות חזותית.

ריכזנו כאן כמה דוגמאות שימחישו איך זה עובד.

- **יש להימנע מ:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **לפשט:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **יש להימנע מ:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **לפשט:** `Make the phone invisible. Keep everything else the
    same.`

### הנחיית האודיו

כברירת מחדל, המודל ינסה ליצור טראק אודיו מתאים לסרטון. יכול להיות שזה לא מה שרציתם. אתם יכולים להשתמש בהנחיה כדי לתאר את סוג האודיו שאתם רוצים. זה חשוב במיוחד אם אתם רוצים להוסיף מוזיקה לסרטון:

- הוספת מוזיקת רקע רגועה
- הסרטון כולל ביט טכנו קצבי
- ברקע נשמעת תוכנית רדיו חלשה ומתכתית, שבה מושמע שיר

### אירועי תזמון

אתם יכולים להנחות את המודל לבצע פעולות בשעות ספציפיות בסרטון, בלי צורך בתחביר מדויק, באמצעות שפה טבעית. האפשרות הזו שימושית במיוחד כשרוצים ליצור סצנות משלכם, קצב או רצפים מהירים.
דוגמאות:

- אחרי 3 שניות, אישה נכנסת לסצנה.
- בדקה 5 הפזמון מתחיל באודיו ברקע.
- כל 2 שניות מתבצע מעבר לפריים חדש.
- בסצנת ירי מהיר, כל חצי שנייה (12 פריימים ב-24fps) משנים את הסצנה למיקום חדש.

אפשר גם להשתמש בתחביר של קוד זמן:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### שיפור הנחיות בעזרת AI

אתם יכולים לבקש מ-Gemini Omni Flash לשים לב לאיכויות כלליות או לעקרונות של יצירת סרטונים:

- כדי ליצור סצנה עשירה ומפורטת אבל טבעית לחלוטין, חשוב להתייחס לפרטים הקטנים, להבעה ולתזמון.
- הקפידו על תיאורים מפורטים מאוד של הדמויות והסביבות.
  יישום עקרונות של עיצוב תלבושות על דמויות. צריך להיות ספציפיים מאוד לגבי האנשים, הפריטים והאובייקטים בסצנה.
- כדי שהסצנה תיראה מציאותית וטבעית, חשוב להוסיף הרבה פרטים מתאימים לרכיבי הרקע.
- תכין סרטון מהיר שבו מוצגות `[thing]` שונות ונדירות כל שנייה, עם מוזיקה קצבית, ותוסיף טקסט כדי לתת שם לכל דבר.

### טקסט בסרטונים

אתם יכולים להנחות את Gemini Omni לכלול טקסט בסרטון, והוא יעבד את הטקסט בצורה נכונה וקריאה. אם בסרטון שלכם יופיע טקסט באופן טבעי, גם ברכיבי הרקע, כדאי להגדיר מה צריך להיות כתוב.

- מילה אחת בכל פעם במסך: "did, you, know, that, Omni, can, do,
  awesome, text?" כל מילה מופיעה למשך שנייה אחת בסגנון אנימציה שונה. אין דיאלוג.
- יש תמרור עם הכיתוב: "This is an AI generation by Omni" (התמונה הזו נוצרה על ידי AI באמצעות Omni), יש חזית חנות עם הכיתוב: "All you need AI" (כל מה שצריך AI), יש מכונית עם לוחית רישוי עם הכיתוב: "OMN111"

### שימוש בתגים בהנחיות כדי להגדיר תפקידי תמונה

אתם יכולים להשתמש בתגים כדי לקשר בין מדיה שהועלתה לבין תפקידי יצירה ספציפיים. כך תוכלו לציין אם כל תמונה היא פריים ראשוני או פריים להשוואה.

#### 1. תגים פשוטים (מומלץ)

במקרים פשוטים שבהם התפקידים של התמונות ברורים מההנחיה, אפשר לקשר תמונות לתפקידים ישירות:

- ‫**`<FIRST_FRAME>`**: שימוש בתמונה כמסגרת הפתיחה של הסרטון, לדוגמה: `<FIRST_FRAME> a woman is walking`
- ‫**`<IMAGE_REF_N>`**: שימוש בתמונה כהפניה, לדוגמה: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (שילוב של הפניה לסגנון מהתמונה הראשונה והפניה לנושא מהתמונה השנייה).
  התמונות לדוגמה מתחילות מ-0.

דוגמה עם 6 תמונות להשוואה:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. הצהרות מפורשות

במקרים מורכבים יותר עם כמה תמונות וכמה תפקידים, אפשר להשתמש בתגי קידומת מפורשים בשילוב עם סיומות של הוראות בשפה טבעית.

- **הצהרה על מקורות ותמונות לדוגמה**:
  - ‫`[# Sources <FIRST_FRAME>@Image1]` ישתמש בתמונה הראשונה כפריים ההתחלתי.
  - ‫`[# References <IMAGE_REF_0>@Image1]` ישתמש בתמונה הראשונה כדוגמה.
  - ‫`[# References <IMAGE_REF_1>@Image2]` ישתמש בתמונה השנייה כדוגמה.
  - ‫`[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` ישתמש בשתי התמונות כדוגמאות.
  - ‫`[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` ישתמש בתמונה הראשונה כפריים התחלתי ובתמונה השנייה כהפניה.
- **הוראות מנחות**: מוסיפים הוראות מנחות בסוף ההנחיה:
  - פריים התחלה: `"Use this image as the starting frame."`
  - לתמונות לדוגמה: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`

דוגמה להנחיה מורחבת:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

## המאמרים הבאים

- כדי להתחיל לעבוד עם Gemini Omni Flash, אפשר להתנסות ב-[Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=he).
- כדי ללמוד איך לכתוב הנחיות טובות עוד יותר, אפשר לעיין ב[מבוא לעיצוב הנחיות](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
