---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=he
fetched_at: 2026-05-11T12:38:58.047349+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# מדריך להתחלה מהירה של Gemini API

במדריך למתחילים הזה מוסבר איך להתקין את [הספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he) שלנו ולשלוח את בקשת ה-API הראשונה ל-Gemini API באמצעות Interactions API.

## לפני שמתחילים

כדי להשתמש ב-Gemini API, צריך מפתח API. אפשר ליצור מפתח כזה בחינם כדי להתחיל.

[יצירת מפתח Gemini API](https://aistudio.google.com/app/apikey?hl=he)

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

## שליחת הבקשה הראשונה

הנה דוגמה לשימוש ב-Interactions API כדי לשלוח בקשה ל-Gemini API באמצעות מודל Gemini 3 Flash.

אם [מגדירים את מפתח ה-API](https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=he#set-api-env-var) כמשתנה הסביבה `GEMINI_API_KEY`, הלקוח יזהה אותו באופן אוטומטי כשמשתמשים ב[ספריות Gemini API](https://ai.google.dev/gemini-api/docs/libraries?hl=he).
אחרת, תצטרכו [להעביר את מפתח ה-API](https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=he#provide-api-key-explicitly) כארגומנט כשמפעילים את הלקוח.

שימו לב: כל דוגמאות הקוד במסמכי ה-Gemini API מניחות שהגדרתם את משתנה הסביבה `GEMINI_API_KEY`.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview", 
    input="Explain how AI works in a few words"
)

# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works in a few words",
  });

  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works in a few words"
  }'
```

## המאמרים הבאים

אחרי ששלחתם את הבקשה הראשונה ל-API, כדאי לעיין במדריכים הבאים שבהם אפשר לראות את Gemini בפעולה:

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=he)
- [יצירת תמונות](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=he)
- [הבנת תמונות](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=he)
- [תהליך החשיבה](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=he)
- [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=he)
- [הקשר רחב](https://ai.google.dev/gemini-api/docs/long-context?hl=he)
- [הטמעות](https://ai.google.dev/gemini-api/docs/embeddings?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-07 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-07 (שעון UTC)."],[],[]]
