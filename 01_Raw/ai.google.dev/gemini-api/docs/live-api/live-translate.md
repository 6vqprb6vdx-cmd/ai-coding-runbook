---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=he
fetched_at: 2026-06-29T05:31:58.044875+00:00
title: "\u05ea\u05e8\u05d2\u05d5\u05dd \u05d1\u05d6\u05de\u05df \u05d0\u05de\u05ea \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# תרגום בזמן אמת באמצעות Gemini Live API

ממשק Gemini Live API תומך בתרגום דיבור לדיבור בזמן אמת עם זמן טעינה נמוך, בין יותר מ-70 שפות, באמצעות מודל [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=he). אם מגדירים את Live API עם הגדרות תרגום, אפשר להזרים אודיו בשפה אחת ולקבל פלט אודיו מתורגם בשפה אחרת, וכך ליהנות מתרגום קולי בזמן אמת.

[רוצים לנסות את התרגום בזמן אמת ב-Google AI Studio?mic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=he)
[משכפלים את אפליקציית הדוגמה מ-GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[שימוש במיומנויות של סוכן קודterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he#gemini-live-api-dev)

## נציג תמיכה לעומת תרגום בזמן אמת

שני הפיצ'רים משתמשים ב-Live API, אבל המודל המנטלי של תרגום בזמן אמת שונה מזה של אינטראקציות עם סוכנים בזמן אמת.

| נציג תמיכה | תרגום בזמן אמת |
| --- | --- |
| **המערכת פועלת כעוזרת.** היא מקשיבה, מסיקה מסקנות ומבצעת פעולות בשמכם. | **המודל פועל כמתורגמן.** הוא פועל כצינור לעיבוד נתונים של תרגום בזמן אמת. |
| **משתמש באינטראקציות מבוססות-תור.** התכונה מסתמכת על הפסקות בדיבור, זיהוי כוונות וטיפול בהפרעות. | **נעשה שימוש בעיבוד זרמי נתונים.** התרגום מתבצע בזמן שהדובר מדבר, בלי לחכות לתורו. |
| **תמיכה בכלים ובסוכנים.** תמיכה מובנית בהפעלת פונקציות, בחיפוש Google ובהוראות. | **תמיכה בתרגום בלבד.** תרגום טהור עם השהיה נמוכה, ללא תמיכה בכלים או בהוראות. |
| **מרובה מצבים באופן מלא.** הוא תומך בקלט של טקסט, אודיו, וידאו ותמונות. | **האודיו מוגבל.** הקלט מוגבל לאודיו כדי להבטיח סף מחמיר של זמן אחזור בזמן אמת. |
| **הגדרה מפורטת.** הוא משתמש בהוראות ליצירה, בדיבור, בכלים ובמערכת. | **הגדרה פשוטה יותר.** מגדירים את `target_language_code` ומפעילים או משביתים את המתגים כמו `echo_target_language`. |

## שנתחיל?

בדוגמאות הבאות מוצג איך לאתחל לקוח ולהתחבר ל-Live API עם הגדרת תרגום.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## שליחת אודיו

כדי להזרים קלט קולי לתרגום, שולחים אודיו PCM גולמי, little-endian, ‏ 16 ביט.

- **פורמט אודיו של הקלט**: PCM גולמי של 16 ביט ב-16kHz (מונו, little-endian).
- **פורמט אודיו של הפלט**: Raw 16-bit PCM at 24kHz (מונו, little-endian).
- **גודל קבוצת הנתונים וזמן הטעינה**: שליחת אודיו בקבוצות נתונים של 100 אלפיות השנייה.

בדוגמאות הבאות אפשר לראות איך שולחים מקטעי אודיו לסשן.

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

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## הגדרות אישיות

כדי להפעיל את התרגום, צריך לציין את `translationConfig` בתוך `generationConfig` במהלך הגדרת הסשן.

### הגדרת הודעות לגבי הגדרה

‫`generationConfig` תומך בשדות הבאים כדי להפעיל תמלילים:

- ‫**`inputAudioTranscription`**: אובייקט שמאפשר למודל לשלוח תמלילי טקסט של קלט האודיו, אם הוא קיים.
- ‫**`outputAudioTranscription`**: אובייקט שמאפשר למודל לשלוח תמלילי טקסט של פלט האודיו (מתורגם), אם הוא קיים.

‫`translationConfig` תומך בשדות הבאים:

- ‫**`targetLanguageCode`**: [קוד השפה מסוג BCP-47](#supported-languages) שאליה רוצים שהמודל יתרגם (למשל, `"pl"` לפולנית, `"es"` לספרדית). ברירת המחדל היא `"en"`.
- ‫**`echoTargetLanguage`**: ערך בוליאני שמציין איך לטפל באודיו של קלט שכבר קיים בשפת היעד. אם הערך מוגדר ל-`true`, המודל ישמיע הד של קלט אודיו שכבר קיים בשפת היעד. אם הערך הוא `false`, המודל יישאר שקט אם הדיבור שמוזן כבר בשפת היעד. ברירת המחדל היא `false`.

דוגמה למבנה של הודעת ההגדרה:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## טוקנים זמניים לאפליקציות בצד הלקוח

באפליקציות מסוג לקוח-שרת, אפשר להשתמש ב[אסימונים זמניים](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=he) (שנמצאים כרגע ב`v1alpha`) כדי להימנע מחשיפת מפתח ה-API.

כשמשתמשים בטוקנים זמניים עם תרגום בזמן אמת:

1. חובה להשתמש בנקודת הקצה `v1alpha`.
2. **נעילת ההגדרה:** כברירת מחדל, צריך לציין את `translationConfig` באילוצים של יצירת הטוקן בשרת. כך מוודאים שהגדרת התרגום נעולה ושהלקוח לא יכול לשנות אותה.
3. **ביטול הנעילה של ההגדרה:** אם רוצים להגדיר את `translationConfig` בצד הלקוח (לדוגמה, כדי לאפשר למשתמש לבחור את שפת היעד שלו), צריך להשמיט את ההגדרה הזו מבקשת יצירת הטוקן ולהגדיר במקומה את `"lock_additional_fields": []`. כך אפשר יהיה לבטל את הנעילה של `translationConfig` כדי להגדיר אותו בצד הלקוח.

### יצירת טוקן זמני מוגבל

בדוגמאות הבאות מוסבר איך ליצור אסימון זמני עם הגבלות תרגום.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha'}
)

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
        'http_options': {'api_version': 'v1alpha'},
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    },
});
```

## מגבלות

- **אמצעי קלט**: יש תמיכה רק בקלט אודיו לתרגום. אין תמיכה בהזנת טקסט.
- **שכפול קול**: שכפול קול יכול להיות לא עקבי. יכול להיות שהקולות ישתנו אחרי הפסקות ארוכות, שהמגדר ישתנה בהתאם לאופן שבו מתחיל הדיבור או שהקול יישאר קבוע במהלך שיחות מהירות עם כמה דוברים.
- **זיהוי שפות**: זיהוי שפות מתקשה בזיהוי מבטא כבד, שפות דומות (למשל ספרדית לעומת פורטוגזית) או מעברים מהירים בין שפות. **הערה:** הבעיה הזו אמורה להשפיע רק על התמליל של הקלט. קודי השפה והתרגום הסופי אמורים להיות מדויקים.
- **אודיו ברקע**: המודל נועד לסנן רעשים ומוזיקה כדי ליצור דיבור נקי, אבל יכול להיות שלא כל האודיו ברקע יסונן.
- **השפה של Echo Target**: אם האודיו שמוזן כבר בשפת היעד, רעשי רקע או מוזיקה עלולים לגרום לארטיפקטים באודיו המתורגם כשמשתמשים ב-`echoTargetLanguage: true`.

## שפות נתמכות

השפות הבאות נתמכות בתרגום בזמן אמת.

| שפה | קוד BCP-47 | שפה | קוד BCP-47 |
| --- | --- | --- | --- |
| אפריקאנס | af | קזחית | kk |
| אקאן | ak | חמרית | ק"מ |
| אלבנית | sq | קינירואנדה | rw |
| אמהרית | am | קוריאנית | ko |
| ערבית | ar | לאו | lo |
| ארמנית | hy | לטבית | lv |
| אזרית | az | ליטאית | lt |
| בסקית | eu | מקדונית | mk |
| בלארוסית | be | מלאית | ms |
| בנגלית | bn | מליאלאם | ml |
| בולגרית | bg | מראטהית | mr |
| בורמזית (מיאנמר) | my | מונגולית | mn |
| קטלאנית | ca | נפאלית | ne |
| סינית (פשוטה) | zh-Hans | נורווגית | no, nb |
| סינית (מסורתית) | zh-Hant | פרסית | fa |
| קרואטית | שעה | פולנית | pl |
| צ'כית | cs | פורטוגזית (ברזיל) | pt-BR |
| דנית | da | פורטוגזית (פורטוגל) | pt-PT |
| הולנדית | nl | פנג'אבי | pa |
| אנגלית | en | רומנית | ro |
| אסטונית | et | רוסית | ru |
| פיליפינית | fil | סרבית | sr |
| פינית | fi | סינדהית | SD |
| צרפתית | fr | סינהאלה | si |
| גליציאנית | gl | סלובקית | sk |
| גאורגית | ka | סלובנית | sl |
| גרמנית | de | ספרדית | es |
| יוונית | el | סונדנזית | su |
| גוג'ראטי | gu | סווהילי | sw |
| האוסה | ha | שוודית | sv |
| עברית | הוא | טמילית | ta |
| הינדי | hi | טלוגו | te |
| הונגרית | hu | תאית | th |
| איסלנדית | is | טורקית | tr |
| אינדונזית | id [מזהה] | אוקראינית | uk |
| איטלקית | it | אורדו | ur |
| יפנית | ja | אוזבקית | uz |
| ג'אווה | jv | וייטנאמית | vi |
| קנאדה | kn | זולו | zu |

## המאמרים הבאים

- אפשר לקרוא את המדריך המלא בנושא [יכולות](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=he) של Live API.
- קוראים את המדריך [איך מתחילים לעבוד עם ה-SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=he).
- מומלץ לקרוא את המדריך [איך מתחילים לעבוד עם WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=he).
- במדריך [טוקנים זמניים](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=he) מוסבר איך לבצע אימות מאובטח באפליקציות מסוג לקוח-שרת.
- משכפלים את [הדוגמאות ל-Live API](https://github.com/google-gemini/gemini-live-api-examples) מ-GitHub.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-09 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-09 (שעון UTC)."],[],[]]
