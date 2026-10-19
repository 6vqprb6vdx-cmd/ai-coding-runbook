---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he
fetched_at: 2026-10-19T05:41:58.404510+00:00
title: "\u05ea\u05d7\u05d9\u05dc\u05ea \u05d4\u05e2\u05d1\u05d5\u05d3\u05d4 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# תחילת העבודה

במדריך הזה מוסבר איך להתחיל להשתמש ב-API מדור קודם **generateContent**. בפרויקטים ובאפליקציות חדשים, מומלץ מאוד להשתמש במקום זאת ב-**Interactions API** החדש, שהוא הדרך הפשוטה והטובה ביותר שלנו לבנות באמצעות מודלים וסוכנים של Gemini.

במדריך למתחילים הזה מוסבר איך להתקין את [הספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he) שלנו, לשלוח את הבקשה הראשונה, להזרים תשובות, ליצור שיחות מרובות שלבים ולהשתמש בכלים באמצעות השיטה הרגילה `generateContent`.

## קבלת מפתח API

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

## התקנה של Google GenAI SDK

### Python

באמצעות [Python 3.9 ואילך](https://www.python.org/downloads/), מתקינים את [החבילה `google-genai`](https://pypi.org/project/google-genai/) באמצעות [פקודת pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) הבאה:

```
pip install -q -U google-genai
```

### JavaScript

באמצעות [Node.js v18+‎](https://nodejs.org/en/download/package-manager), מתקינים את [Google Gen AI SDK ל-TypeScript ול-JavaScript](https://www.npmjs.com/package/@google/genai) באמצעות [פקודת npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) הבאה:

```
npm install @google/genai
```

## יצירת טקסט

משתמשים ב-`models.generate_content` method כדי [ליצור תשובת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## הצגת התשובות באופן שוטף

כברירת מחדל, המודל מחזיר תשובה רק אחרי שתהליך היצירה כולו מסתיים. כדי לקבל חוויה מהירה ואינטראקטיבית יותר, אתם יכולים [להזרים את התשובה](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#stream) בחלקים בזמן שהיא נוצרת.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## שיחות עם זיכרון

בשיחות מרובות תפניות, ערכות ה-SDK מספקות `chats`עזר עם שמירת מצב כדי ליצור [חוויית צ'אט מרובת תפניות](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#chat) שמנהלת באופן אוטומטי את היסטוריית השיחות.

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## שימוש בכלים

להרחיב את היכולות של המודל על ידי [עיגון התשובות באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) כדי לגשת לתוכן מהאינטרנט שמתעדכן בזמן אמת. המודל מחליט באופן אוטומטי מתי לבצע חיפוש, מריץ שאילתות ומסנתז תשובה.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

‫Gemini API תומך גם בכלים מובנים אחרים:

- **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**:
  מאפשרת למודל לכתוב ולהריץ קוד Python כדי לפתור בעיות מורכבות במתמטיקה.
- **[הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**: מאפשר להשתמש בכתובות URL ספציפיות של דפי אינטרנט שאתם מספקים כדי להוסיף הקשר לתשובות.
- **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**: מאפשר להעלות קבצים ולבסס את התשובות על התוכן שלהם באמצעות חיפוש סמנטי.
- ‫**[מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**: מאפשרת להשתמש בנתוני מיקום כדי להציג תשובות, לחפש מקומות, מסלולים ומפות.
- **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**: מאפשר למודל ליצור אינטראקציה עם מסך מחשב וירטואלי, מקלדת ועכבר כדי לבצע משימות.

## הפעלת פונקציות מותאמות אישית

משתמשים ב**[קריאה לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)** כדי לחבר מודלים לכלים ולממשקי API בהתאמה אישית. המודל קובע מתי להפעיל את הפונקציה ומחזיר `functionCall` בתשובה כדי שהאפליקציה תבצע אותה.

בדוגמה הזו מוגדרת פונקציית טמפרטורה מדומה ונבדק אם המודל רוצה להפעיל אותה.

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## המאמרים הבאים

אחרי שהתחלתם להשתמש ב-Gemini API, כדאי לעיין במדריכים הבאים כדי ליצור אפליקציות מתקדמות יותר:

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he)
- [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)
- [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he)
- [חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)
- [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
- [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he)
- [הקשר רחב](https://ai.google.dev/gemini-api/docs/long-context?hl=he)
- [הטמעות](https://ai.google.dev/gemini-api/docs/embeddings?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-12 (שעון UTC)."],[],[]]
