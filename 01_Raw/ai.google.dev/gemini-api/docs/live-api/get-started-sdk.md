---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=he
fetched_at: 2026-09-07T05:35:18.661875+00:00
title: "\u05ea\u05d7\u05d9\u05dc\u05ea \u05d4\u05e2\u05d1\u05d5\u05d3\u05d4 \u05e2\u05dd Gemini Live API \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# תחילת העבודה עם Gemini Live API באמצעות Google GenAI SDK

‫Gemini Live API מאפשר אינטראקציה דו-כיוונית עם מודלים של Gemini בזמן אמת, ותומך בקלט של אודיו, וידאו וטקסט, וגם בפלט אודיו מקורי. במדריך הזה מוסבר איך לבצע שילוב עם ה-API באמצעות Google GenAI SDK בשרת.

[אפשר לנסות את Live API ב-Google AI Studiomic](https://aistudio.google.com/live?hl=he)
[שיבוט של אפליקציית הדוגמה מ-GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[שימוש במיומנויות של סוכן תכנותterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he)

## סקירה כללית

‫Gemini Live API משתמש ב-WebSockets לתקשורת בזמן אמת. ערכת ה-SDK של `google-genai` מספקת ממשק אסינכרוני ברמה גבוהה לניהול החיבורים האלה.

מושגים מרכזיים:

- **סשן**: חיבור קבוע למודל.
- **הגדרה**: הגדרת אופנים (אודיו/טקסט), קול והוראות מערכת.
- **קלט בזמן אמת**: שליחת פריימים של אודיו ווידאו כ-blobs.

## התחברות ל-Live API

כדי להתחיל סשן API בזמן אמת באמצעות מפתח API:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## נשלחת הודעת טקסט

אפשר לשלוח טקסט באמצעות `send_realtime_input` (Python) או `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## שליחת אודיו

צריך לשלוח את האודיו כנתוני PCM גולמיים (אודיו PCM גולמי של 16 ביט, 16kHz, little-endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

דוגמה לאופן שבו מקבלים את האודיו ממכשיר הלקוח (למשל, הדפדפן) מופיעה בדוגמה המפורטת ב-[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## שליחת הסרטון מתבצעת

פריימים של סרטונים נשלחים כתמונות נפרדות (למשל, JPEG או PNG) בקצב פריימים ספציפי (עד פריים אחד לשנייה).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

דוגמה לאופן קבלת הסרטון ממכשיר הלקוח (למשל, הדפדפן) מופיעה בדוגמה המפורטת ב-[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## קבלת אודיו

התשובות הקוליות של המודל מתקבלות כנתונים בחלקים.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

אפשר לראות את האפליקציה לדוגמה ב-GitHub כדי ללמוד איך [לקבל את האודיו בשרת](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) ו[להפעיל אותו בדפדפן](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## מתקבל טקסט

תמלילים של קלט של משתמשים ושל פלט המודל זמינים בתוכן השרת.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## טיפול בקריאות לכלי

ה-API תומך בהפעלת כלים (קריאה לפונקציות). כשהמודל מבקש הפעלת כלי, אתם צריכים להפעיל את הפונקציה ולשלוח את התשובה בחזרה.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## המאמרים הבאים

- במדריך המלא בנושא [יכולות](https://ai.google.dev/gemini-api/docs/live-guide?hl=he) של Live API מוסבר על היכולות וההגדרות העיקריות, כולל זיהוי פעילות קולית ותכונות אודיו מקוריות.
- במדריך [שימוש בכלי](https://ai.google.dev/gemini-api/docs/live-tools?hl=he) מוסבר איך לשלב את Live API עם כלים ובקשות להפעלת פונקציות.
- כדי לנהל שיחות ארוכות, כדאי לקרוא את המדריך בנושא [ניהול סשנים](https://ai.google.dev/gemini-api/docs/live-session?hl=he).
- קוראים את המדריך בנושא [טוקנים זמניים](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=he) לאימות מאובטח באפליקציות [client-to-server](https://ai.google.dev/gemini-api/docs/live-api?hl=he#implementation-approach).
- מידע נוסף על WebSockets API מופיע ב[מאמרי העזרה של ה-API של WebSockets](https://ai.google.dev/api/live?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-04 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-04 (שעון UTC)."],[],[]]
