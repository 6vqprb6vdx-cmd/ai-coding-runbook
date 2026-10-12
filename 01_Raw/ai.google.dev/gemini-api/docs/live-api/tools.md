---
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools?hl=he
fetched_at: 2026-10-12T07:05:44.752363+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05db\u05dc\u05d9 \u05e2\u05dd Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שימוש בכלי עם Live API

השימוש בכלי מאפשר ל-Live API לעשות יותר מסתם שיחה, ולבצע פעולות בעולם האמיתי ולשלוף הקשר חיצוני תוך שמירה על חיבור בזמן אמת.
אפשר להגדיר כלים כמו [בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) ו[חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he) באמצעות Live API.

## סקירה כללית של הכלים הנתמכים

סקירה כללית קצרה של הכלים הזמינים למודלים של Live API:

| כלי | ‫Gemini 3.1 Flash Live Preview | גרסת טרום-השקה של Gemini 2.5 Flash |
| --- | --- | --- |
| **חיפוש** | נתמך | נתמך |
| **בקשה להפעלת פונקציה** | נתמך (סינכרוני בלבד) | נתמך (סינכרוני ו[אסינכרוני](#async-function-calling)) |
| **מפות Google** | לא נתמך | לא נתמך |
| **הרצת קוד** | לא נתמך | לא נתמך |
| **הקשר של כתובת ה-URL** | לא נתמך | לא נתמך |

## בקשה להפעלת פונקציה

‫Live API תומך בבקשות להפעלת פונקציות, בדיוק כמו בקשות רגילות ליצירת תוכן. התכונה 'קריאה לפונקציה' מאפשרת ל-Live API לקיים אינטראקציה עם נתונים ותוכניות חיצוניים, וכך להרחיב משמעותית את היכולות של האפליקציות שלכם.

אפשר להגדיר הצהרות על פונקציות כחלק מהגדרת הסשן.
אחרי קבלת קריאות לכלים, הלקוח צריך להגיב עם רשימה של אובייקטים מסוג `FunctionResponse` באמצעות השיטה `session.send_tool_response`.

מידע נוסף זמין [במדריך להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-live"

# Simple function definitions
turn_on_the_lights = {"name": "turn_on_the_lights"}
turn_off_the_lights = {"name": "turn_off_the_lights"}

tools = [{"function_declarations": [turn_on_the_lights, turn_off_the_lights]}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "Turn on the lights please"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for response in session.receive():
            if response.data is not None:
                wf.writeframes(response.data)
            elif response.tool_call:
                print("The tool was called")
                function_responses = []
                for fc in response.tool_call.function_calls:
                    function_response = types.FunctionResponse(
                        id=fc.id,
                        name=fc.name,
                        response={ "result": "ok" } # simple, hard-coded function response
                    )
                    function_responses.append(function_response)

                await session.send_tool_response(function_responses=function_responses)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

// Simple function definitions
const turn_on_the_lights = { name: "turn_on_the_lights" } // , description: '...', parameters: { ... }
const turn_off_the_lights = { name: "turn_off_the_lights" }

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      } else if (message.toolCall) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
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

  const inputTurns = 'Turn on the lights please';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  for (const turn of turns) {
    if (turn.toolCall) {
      console.debug('A tool was called');
      const functionResponses = [];
      for (const fc of turn.toolCall.functionCalls) {
        functionResponses.push({
          id: fc.id,
          name: fc.name,
          response: { result: "ok" } // simple, hard-coded function response
        });
      }

      console.debug('Sending tool response...\n');
      session.sendToolResponse({ functionResponses: functionResponses });
    }
  }

  // Check again for new messages
  turns = await handleTurn();

  // Combine audio data strings and save as wave file
  const combinedAudio = turns.reduce((acc, turn) => {
      if (turn.data) {
          const buffer = Buffer.from(turn.data, 'base64');
          const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);
          return acc.concat(Array.from(intArray));
      }
      return acc;
  }, []);

  const audioBuffer = new Int16Array(combinedAudio);

  const wf = new WaveFile();
  wf.fromScratch(1, 24000, '16', audioBuffer);  // output is 24kHz
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

מתוך הנחיה אחת, המודל יכול ליצור כמה קריאות לפונקציות ואת הקוד שנדרש כדי לשרשר את הפלט שלהן. הקוד הזה מופעל בסביבת ארגז חול, ויוצר הודעות [BidiGenerateContentToolCall](https://ai.google.dev/api/live?hl=he#bidigeneratecontenttoolcall) נוספות.

## קריאה אסינכרונית להפעלת פונקציות

כברירת מחדל, קריאות להפעלת פונקציות מתבצעות באופן רציף, כלומר הביצוע מושהה עד שהתוצאות של כל קריאה להפעלת פונקציה זמינות. כך מובטח עיבוד רציף, כלומר לא תוכלו להמשיך באינטראקציה עם המודל בזמן שהפונקציות פועלות.

אם אתם לא רוצים לחסום את השיחה, אתם יכולים להנחות את המודל להפעיל את הפונקציות באופן אסינכרוני. כדי לעשות את זה, קודם צריך להוסיף `behavior` להגדרות הפונקציה:

### Python

```
# Non-blocking function definitions
turn_on_the_lights = {"name": "turn_on_the_lights", "behavior": "NON_BLOCKING"} # turn_on_the_lights will run asynchronously
turn_off_the_lights = {"name": "turn_off_the_lights"} # turn_off_the_lights will still pause all interactions with the model
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior } from '@google/genai';

// Non-blocking function definitions
const turn_on_the_lights = {name: "turn_on_the_lights", behavior: Behavior.NON_BLOCKING}

// Blocking function definitions
const turn_off_the_lights = {name: "turn_off_the_lights"}

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]
```

‫`NON-BLOCKING` מוודא שהפונקציה פועלת באופן אסינכרוני, כך שאתם יכולים להמשיך באינטראקציה עם המודל.

לאחר מכן צריך להגדיר למודל איך להתנהג כשהוא מקבל את `FunctionResponse` באמצעות הפרמטר `scheduling`. הוא יכול:

- להתפרץ לפעולה שהוא מבצע ולספר לכם על התשובה שהוא קיבל באופן מיידי
  (`scheduling="INTERRUPT"`),
- תחכה עד שהפעולה הנוכחית תסתיים (`scheduling="WHEN_IDLE"`),
- או לא לעשות כלום ולהשתמש בידע הזה בהמשך השיחה
  (`scheduling="SILENT"`)

### Python

```
# for a non-blocking function definition, apply scheduling in the function response:
  function_response = types.FunctionResponse(
      id=fc.id,
      name=fc.name,
      response={
          "result": "ok",
          "scheduling": "INTERRUPT" # Can also be WHEN_IDLE or SILENT
      }
  )
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior, FunctionResponseScheduling } from '@google/genai';

// for a non-blocking function definition, apply scheduling in the function response:
const functionResponse = {
  id: fc.id,
  name: fc.name,
  response: {
    result: "ok",
    scheduling: FunctionResponseScheduling.INTERRUPT  // Can also be WHEN_IDLE or SILENT
  }
}
```

## עיגון באמצעות חיפוש Google

אפשר להפעיל את העיגון באמצעות חיפוש Google כחלק מהגדרת הסשן. כך משפרים את הדיוק של Live API ומונעים הזיות. מידע נוסף זמין [במדריך בנושא ביסוס](https://ai.google.dev/gemini-api/docs/grounding?hl=he).

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-live"

tools = [{'google_search': {}}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "When did the last Brazil vs. Argentina soccer match happen?"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for chunk in session.receive():
            if chunk.server_content:
                if chunk.data is not None:
                    wf.writeframes(chunk.data)

                # The model might generate and execute Python code to use Search
                model_turn = chunk.server_content.model_turn
                if model_turn:
                    for part in model_turn.parts:
                        if part.executable_code is not None:
                            print(part.executable_code.code)

                        if part.code_execution_result is not None:
                            print(part.code_execution_result.output)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const tools = [{ googleSearch: {} }]
const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      } else if (message.toolCall) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
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

  const inputTurns = 'When did the last Brazil vs. Argentina soccer match happen?';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  let combinedData = '';
  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.modelTurn && turn.serverContent.modelTurn.parts) {
      for (const part of turn.serverContent.modelTurn.parts) {
        if (part.executableCode) {
          console.debug('executableCode: %s\n', part.executableCode.code);
        }
        else if (part.codeExecutionResult) {
          console.debug('codeExecutionResult: %s\n', part.codeExecutionResult.output);
        }
        else if (part.inlineData && typeof part.inlineData.data === 'string') {
          combinedData += atob(part.inlineData.data);
        }
      }
    }
  }

  // Convert the base64-encoded string of bytes into a Buffer.
  const buffer = Buffer.from(combinedData, 'binary');

  // The buffer contains raw bytes. For 16-bit audio, we need to interpret every 2 bytes as a single sample.
  const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);

  const wf = new WaveFile();
  // The API returns 16-bit PCM audio at a 24kHz sample rate.
  wf.fromScratch(1, 24000, '16', intArray);
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## שילוב של כמה כלים

אפשר לשלב כמה כלים ב-Live API כדי להרחיב עוד יותר את היכולות של האפליקציה:

### Python

```
prompt = """
Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
"""

tools = [
    {"google_search": {}},
    {"function_declarations": [turn_on_the_lights, turn_off_the_lights]},
]

config = {"response_modalities": ["AUDIO"], "tools": tools}

# ... remaining model call
```

### JavaScript

```
const prompt = `Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
`

const tools = [
  { googleSearch: {} },
  { functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }
]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

// ... remaining model call
```

## המאמרים הבאים

- ב[מדריך המתכונים לשימוש בכלי](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=he) יש עוד דוגמאות לשימוש בכלי באמצעות Live API.
- ב[מדריך היכולות של Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=he) אפשר לקרוא את כל הפרטים על התכונות וההגדרות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-17 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-17 (שעון UTC)."],[],[]]
