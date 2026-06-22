---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=he
fetched_at: 2026-06-22T06:29:17.760160+00:00
title: "\u202bGemini Developer API \u05dc\u05e2\u05d5\u05de\u05ea \u05e4\u05dc\u05d8\u05e4\u05d5\u05e8\u05de\u05ea \u05d4\u05e1\u05d5\u05db\u05e0\u05d9\u05dd \u05e9\u05dc Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ‫Gemini Developer API לעומת פלטפורמת הסוכנים של Gemini Enterprise

כשמפתחים פתרונות AI גנרטיבי עם Gemini, ‏ Google מציעה שני מוצרי API:
‫[Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=he) ו-[Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=he).

‫Gemini Developer API הוא הדרך המהירה ביותר לבנות אפליקציות מבוססות-Gemini, להעביר אותן לייצור ולהרחיב אותן. רוב המפתחים צריכים להשתמש ב-Gemini Developer API, אלא אם יש צורך באמצעי בקרה ספציפיים לארגונים.

‫Gemini Enterprise Agent Platform מציעה מערכת אקולוגית מקיפה של תכונות ושירותים שמוכנים לשימוש בארגונים, ליצירה ולפריסה של אפליקציות AI גנרטיבי שמגובות על ידי Google Cloud Platform.

לאחרונה פישטנו את תהליך המעבר בין השירותים האלה. אפשר לגשת גם אל Gemini Developer API וגם אל Gemini Enterprise Agent Platform API דרך [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=he) המאוחד.

## השוואת קוד

בדף הזה מוצגות השוואות קוד זו לצד זו בין Gemini Developer API לבין מדריכי התחלה מהירה של Gemini Enterprise Agent Platform ליצירת טקסט.

### Python

אפשר לגשת גם ל-Gemini Developer API וגם לשירותים של Gemini Enterprise Agent Platform דרך ספריית `google-genai`. הוראות להתקנת `google-genai` מופיעות בדף [ספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he).

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### ‫JavaScript ו-TypeScript

אפשר לגשת לשירותים Gemini Developer API ו-Gemini Enterprise Agent Platform דרך ספריית `@google/genai`. הוראות להתקנת `@google/genai` זמינות בדף [ספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he).

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

אפשר לגשת לשירותים Gemini Developer API ו-Gemini Enterprise Agent Platform דרך ספריית `google.golang.org/genai`. הוראות להתקנת `google.golang.org/genai` זמינות בדף [ספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he).

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### תרחישי שימוש ופלטפורמות אחרים

ב[מסמכי התיעוד של Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=he) וב[מסמכי התיעוד של Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=he) אפשר למצוא מדריכים ספציפיים לתרחישי שימוש בפלטפורמות אחרות.

## שיקולים לגבי מיגרציה

כשמבצעים העברה:

- תצטרכו להשתמש בחשבונות שירות של Google Cloud כדי לבצע אימות. מידע נוסף זמין [במסמכי התיעוד של Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=he).
- אפשר להשתמש בפרויקט קיים ב-Google Cloud (אותו פרויקט שבו השתמשתם כדי ליצור את מפתח ה-API) או [ליצור פרויקט חדש ב-Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=he).
- יכול להיות שהאזורים הנתמכים שונים בין Gemini Developer API לבין Gemini Enterprise Agent Platform API. [רשימת האזורים הנתמכים ל-AI גנרטיבי ב-Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=he)
- צריך לאמן מחדש ב-Gemini Enterprise Agent Platform את כל המודלים שיצרתם ב-Google AI Studio.

אם אתם לא צריכים יותר להשתמש במפתח Gemini API עבור Gemini Developer API, מומלץ לפעול לפי השיטות המומלצות לאבטחה ולמחוק אותו.

כדי למחוק מפתח API:

1. פותחים את הדף [Google Cloud API Credentials](https://console.cloud.google.com/apis/credentials?hl=he).
2. מאתרים את מפתח ה-API שרוצים למחוק ולוחצים על סמל **הפעולות**.
3. בוחרים באפשרות **מחיקת מפתח API**.
4. בחלון **מחיקת פרטי הכניסה**, לוחצים על **מחיקה**.

   תהליך המחיקה של מפתח API נמשך כמה דקות. אחרי שההפצה מסתיימת, כל תנועת גולשים שמשתמשת במפתח ה-API שנמחק נדחית.

## השלבים הבאים

- [במאמר הזה](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=he) יש מידע נוסף על פתרונות AI גנרטיבי בפלטפורמת הסוכנים של Gemini Enterprise.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-18 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-18 (שעון UTC)."],[],[]]
