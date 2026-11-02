---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=he
fetched_at: 2026-11-02T07:31:07.635838+00:00
title: "\u05e2\u05d9\u05e6\u05d5\u05d1 \u05e7\u05d5\u05dc\u05d9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# עיצוב קולי

עיצוב קול מאפשר לכם ליצור פרסונה קולית חדשה וקבועה מתיאור בשפה טבעית באמצעות נקודת הקצה Voices של Gemini API ‏(`POST /v1beta/voices`). במקום להיות מוגבלים לקולות מוכנים מראש או להקלטת אודיו להפניה, אתם יכולים לתאר את הגיל, גוון הקול, המבטא וסגנון הדיבור של הדמות, ולקבל מזהה `voice_...` לשימוש חוזר שנשמר בפרויקט שלכם.

הדרך הכי מהירה לעצב קולות מותאמים אישית, לבדוק אותם ולשפר אותם היא באמצעות סטודיו **Voice Design** האינטראקטיבי ב-[Google AI Studio](https://aistudio.google.com/generate-speech?hl=he). אתם יכולים ליצור פרסונות מותאמות אישית מהנחיות טקסט, לבדוק אותן באמצעות סקריפטים לדוגמה ולהעתיק את מזהה `voice_...` שנוצר ישירות לקוד האפליקציה.

[לניסיון ב-Google AI Studio](https://aistudio.google.com/generate-speech?hl=he)

‫[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=he)‏ (`gemini-3.8-flash-tts`) ו-[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=he)‏ (`gemini-3.8-flash-lite-tts`) תומכים בעיצוב קולי.

## יצירת קול מעוצב

אפשר להשתמש ב-Google GenAI SDK (גרסה `google-genai` 2.25.0 ואילך / גרסה `@google/genai` 2.24.0 ואילך) או ב-API בארכיטקטורת REST כדי ליצור קול בהתאמה אישית מתיאור טקסטואלי. עבור קולות `"prompted"`, גם `voices.create` (`CreateVoice`) וגם `voices.get` (`GetVoice`) מחזירים שדה `sample_audio` (`mime_type: "audio/wav"`,‏ `data` בקידוד base64) שמוגדר רק לפלט, כדי שתוכלו לשמוע מיד את הקול שנוצר:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## איך עיצוב הקול פועל

1. **יצירת קול בהנחיה:** התקשר אל `voices.create` (`POST /v1beta/voices`)
   עם `type="prompted"` ו-`store=True`.
2. **קבלת תצוגה מקדימה קבועה של `voice_id` ו-`sample_audio`:** ה-API יוצר את הזהות הקולית, מאחסן אותה בפרויקט ומחזיר מזהה קבוע (לדוגמה, `voice_abc123...`) יחד עם `sample_audio` (`mime_type: "audio/wav"`, מקודד ב-Base64 `data`) שמכיל את האודיו של התצוגה המקדימה שנוצר עבור הקול.
3. **סינתזת דיבור:** מעבירים את `voice_id` לכל מקום שבו שם של קול מתקבל בבקשות הסינתזה.

## סינתזת דיבור באמצעות קול שעיצבתם

אחרי שיוצרים קול, מעבירים את הערך `id` (`voice_...`) שלו אל Interactions API כדי ליצור דיבור:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## ניהול הקולות

אתם יכולים לראות, לסנן, לבדוק ולמחוק את הקולות השמורים מתי שתרצו באמצעות Voices API (ראו [ספריית קולות מורחבת וסינון](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he#voice-library) לכל פרמטרי הסינון).

- **מגבלות אחסון ואורך חיים (TTL):** לקולות עם שמירת מצב (`store=True`, משותפים בין קולות שנוצרו בהנחיה וקולות משוכפלים) יש מגבלה של **200 קולות לכל פרויקט** ו**אורך חיים של שנה אחת**.
- **זמינות `sample_audio`:** הערכים `voices.create()` (`CreateVoice`) ו-`voices.get()` (`GetVoice`) מאכלסים את `sample_audio` (`mime_type:
  "audio/wav"`, בקידוד base64 `data`) עבור קולות `"prompted"`. כדי שהכרטיסייה תהיה קלה יותר, `voices.list()` (`ListVoices`) משמיט את `sample_audio` (`sample_audio` ולא מוגדר עבור קולות `"replicated"` ו-`"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## שיטות מומלצות לכתיבת פרומפטים לעיצוב קולי

- **מגדירים מאפיינים קוליים קבועים בעיצוב הקול, ולא ב-`style`:** מגדירים מאפיינים קבועים – כמו גיל, מגדר, גוון, מרקם קולי ומבטא אזורי – כשיוצרים את הקול ב-`voices.create`.
- **שמרו את `speech_metadata.style` למצבים שבהם נדרשת הבעת רגש:** אחרי שיוצרים את הקול המותאם אישית, משתמשים בהנחיות קצרות `style` (לדוגמה, `"whispered urgently"` או `"cheerful and energetic"`) כדי לכוון את המשחק לפי תורות בלי לשנות את הזהות הבסיסית של הדובר.
- **היו ספציפיים ותמציתיים:** תיאור ברור של משפט או שניים (למשל *"שדרנית ספורט אנרגטית בת 30 עם מבטא קל של המערב התיכון"*) יניב תוצאות טובות ועקביות יותר מאשר פסקאות סותרות או ארוכות מדי.

## המאמרים הבאים

- למדו איך לשכפל קול של דובר קיים באמצעות [רפליקציה של קולות](https://ai.google.dev/gemini-api/docs/voice-replication?hl=he).
- ב[מדריך להמרת טקסט לדיבור](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he) אפשר לקרוא על עיצוב ברמת הפנייה, תגים מוטבעים ודיאלוג עם כמה דוברים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-24 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-24 (שעון UTC)."],[],[]]
