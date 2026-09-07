---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=he
fetched_at: 2026-09-07T05:43:59.864396+00:00
title: "\u05d7\u05ea\u05d9\u05de\u05d5\u05ea \u05e9\u05dc \u05de\u05d7\u05e9\u05d1\u05d5\u05ea \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# חתימות של מחשבות

חתימות מחשבה הן ייצוגים מוצפנים של תהליך החשיבה הפנימי של המודל, והן משמשות לשמירה על הקשר של הנימוקים במהלך אינטראקציות מרובות שלבים.
כשמשתמשים במודלים של חשיבה (כמו סדרות Gemini 3 ו-2.5), ה-API עשוי להחזיר `thoughtSignature` שדה בתוך [חלקי התוכן](https://ai.google.dev/api/caching?hl=he#Part) של התגובה (למשל, חלקים `text` או `functionCall`).

ככלל, אם קיבלתם חתימת מחשבה בתשובה של מודל, אתם צריכים להעביר אותה בדיוק כמו שהיא כשאתם שולחים את היסטוריית השיחה בתור הבא.
**כשמשתמשים במודלים של Gemini 3, צריך להעביר חתימות של מחשבות במהלך קריאה לפונקציה, אחרת תוצג שגיאת אימות** (קוד סטטוס 4xx).
זה כולל שימוש בהגדרה `minimal`
[רמת החשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#thinking-levels) של Gemini 3 Flash.

## איך זה עובד

בתרשים שלמטה אפשר לראות את המשמעות של המונחים 'תור' ו'שלב' בהקשר של [בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) ב-Gemini API. "תור" הוא תגובה אחת מלאה בשיחה בין משתמש לבין מודל. 'שלב' הוא פעולה או תהליך מפורטים יותר שהמודל מבצע, לרוב כחלק מתהליך גדול יותר להשלמת תור.

![תרשים של תורות ושלבים של קריאה להפעלת פונקציות](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=he)

*המאמר הזה מתמקד בטיפול בבקשות להפעלת פונקציות במודלים של Gemini 3. בקטע [התנהגות המודל](#model-behavior) מוסבר על אי-התאמות בגרסה 2.5.*

‫Gemini 3 מחזיר חתימות של מחשבות לכל התשובות של המודל (תשובות מ-API) עם קריאה לפונקציה. חתימות מחשבה מופיעות במקרים הבאים:

- כשמתבצעות קריאות ל[פונקציות מקבילות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#parallel_function_calling), לחלק הראשון של קריאת הפונקציה שמוחזר בתגובת המודל תהיה חתימת מחשבה.
- כשמבצעים קריאות לפונקציות ברצף (כמה שלבים), לכל קריאה לפונקציה יש חתימה, ואתם צריכים להעביר את כל החתימות בחזרה.
- תשובות של מודלים ללא קריאה לפונקציה יחזירו חתימה של מחשבה בחלק האחרון שהוחזר על ידי המודל.

בטבלה הבאה מוצגת ויזואליזציה של קריאות לפונקציות מרובות שלבים, שמשלבת את ההגדרות של תורות ושלבים עם המושג של חתימות שהוצג למעלה:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **התור שלך** | **שלב** | **בקשת משתמש** | **תשובת המודל** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | ללא |

## חתימות בחלקים של קריאה להפעלת פונקציות

כש-Gemini יוצר `functionCall`, הוא מסתמך על `thought_signature`
כדי לעבד את הפלט של הכלי בצורה נכונה בתור הבא.

- **התנהגות**:
  - **קריאה לפונקציה אחת**: החלק `functionCall` יכיל `thought_signature`.
  - **קריאות מקבילות לפונקציות**: אם המודל יוצר קריאות מקבילות לפונקציות בתגובה, `thought_signature` מצורף **רק לחלק הראשון**
    `functionCall`. חלקים הבאים של אותה תשובה `functionCall`**לא** יכילו חתימה.
- **דרישה**: כששולחים בחזרה את היסטוריית השיחה, **חובה** להחזיר את החתימה הזו בדיוק בחלק שבו היא התקבלה.
- **אימות**: מתבצע אימות קפדני של כל הקריאות לפונקציות במהלך התור הנוכחי . (נדרש רק התור הנוכחי, אנחנו לא מאמתים תורות קודמים)
  - ה-API יחפש בהיסטוריה (מהחדש לישן) את ההודעה האחרונה של **המשתמש** שמכילה תוכן רגיל (למשל, `text`) ( שזו תהיה תחילת התור הנוכחי). הפעולה הזו לא **be** יהיה `functionResponse`.
  - כל התורות של מודל **All** `functionCall` שמתרחשות אחרי הודעת השימוש הספציפית הזו נחשבות לחלק מהתור.
  - החלק **הראשון** `functionCall` **בכל שלב** של התור הנוכחי **חייב** לכלול את `thought_signature` שלו.
  - אם לא תציינו `thought_signature` עבור החלק הראשון `functionCall` בכל שלב של התור הנוכחי, הבקשה תיכשל ותוחזר שגיאת 400.
- **אם לא מוחזרות חתימות תקינות, כך תופיע השגיאה**
  - מודלים של Gemini 3: אם לא תכללו חתימות, תופיע שגיאת 400. הניסוח יהיה בפורמט הבא:
    - בקריאה לפונקציה `<Function Call>` בחסימת התוכן `<index of contents array>` חסר `thought_signature`. לדוגמה, *Function
      call `FC1` in the `1.` content block is missing a `thought_signature`.*

### דוגמה לבקשה להפעלת פונקציה באופן רציף

בקטע הזה מוצגת דוגמה לכמה קריאות לפונקציה, שבהן המשתמש שואל שאלה מורכבת שדורשת כמה משימות.

הנה דוגמה לשימוש בפונקציות עם כמה תורות, שבה המשתמש שואל שאלה מורכבת שדורשת כמה משימות: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **התור שלך** | **שלב** | **בקשת משתמש** | **תשובת המודל** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

הקוד הבא מדגים את הרצף שמופיע בטבלה שלמעלה.

**תור 1, שלב 1 (בקשת משתמש)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**תור 1, שלב 1 (תשובה לדוגמה)**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**תור 1, שלב 2 (תגובת המשתמש – שליחת פלט של כלי)** מכיוון שהתור הזה של המשתמש
מכיל רק `functionResponse` (ללא טקסט חדש), אנחנו עדיין בתור 1. אנחנו חייבים לשמור על `<Signature_A>`.

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**תור 1, שלב 2 (מודל)** המודל מחליט להזמין מונית על סמך הפלט הקודם של הכלי.

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**תור 1, שלב 3 (משתמש – שליחת פלט הכלי)** כדי לשלוח את אישור הזמנת המונית, צריך לכלול חתימות ל**כל** הקריאות לפונקציות בלולאה הזו (`<Signature A>` + `<Signature B>`).

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### דוגמה לקריאה לפונקציות במקביל

בואו נראה דוגמה לשימוש מקביל בפונקציות, שבה המשתמש מבקש מ-`"Check weather in Paris and London"` לראות איפה המודל מבצע אימות.

| **התור שלך** | **שלב** | **בקשת משתמש** | **תשובת המודל** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | ‫FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (אין כרטיסיות) | ללא |

הקוד הבא מדגים את הרצף שמופיע בטבלה שלמעלה.

**תור 1, שלב 1 (בקשת משתמש)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
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
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**תור 1, שלב 1 (תשובה לדוגמה)**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**תור 1, שלב 2 (תגובת המשתמש – שליחת תוצאות של כלי)** אנחנו צריכים לשמור על
`<Signature_A>` בחלק הראשון בדיוק כמו שהוא התקבל.

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## חתימות בחלקים שלא שייכים ל-`functionCall`

יכול להיות ש-Gemini יחזיר גם `thought_signatures` בחלק האחרון של התשובה בחלקים שלא קשורים לקריאה לפונקציה.

- **התנהגות**: החלק האחרון של התוכן (`text, inlineData…`) שמוחזר על ידי המודל עשוי להכיל `thought_signature`.
- **המלצה**: **מומלץ** להחזיר את החתימות האלה כדי לוודא שהמודל ישמור על יכולת חשיבה רציונלית באיכות גבוהה, במיוחד כשמדובר בהוראות מורכבות או בתהליכי עבודה מבוססי-סוכן מדומה.
- **אימות**: ממשק ה-API **לא** אוכף אימות באופן מחמיר. אם לא תכללו אותם, לא תקבלו שגיאת חסימה, אבל יכול להיות שהביצועים ייפגעו.

### טקסט/הסקה בהקשר (ללא אימות)

**תור 1, שלב 1 (תשובה לדוגמה)**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**תור 2, שלב 1 (משתמש)**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## חתימות לתאימות עם OpenAI

בדוגמה הבאה מוצגות דרכים לטפל בחתימות של מחשבות ב-API להשלמת צ'אט באמצעות [תאימות ל-OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he).

### דוגמה לבקשה להפעלת פונקציה באופן רציף

זו דוגמה לקריאה לכמה פונקציות, שבה המשתמש שואל שאלה מורכבת שדורשת כמה משימות.

בדוגמה הבאה נראה שימוש בפונקציות עם כמה תפניות שיחה. המשתמש שואל `Check flight status for AA100 and book a taxi if delayed` ואפשר לראות מה קורה כשהמשתמש שואל שאלה מורכבת שדורשת כמה משימות.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **התור שלך** | **שלב** | **בקשת משתמש** | **תשובת המודל** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

הקוד הבא מסביר את הרצף הנתון.

**תור 1, שלב 1 (בקשת משתמש)**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**תור 1, שלב 1 (תגובת המודל)**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**תור 1, שלב 2 (תגובת המשתמש – שליחת פלט של כלי)**

בגלל שהתור הזה של המשתמש מכיל רק `functionResponse` (ללא טקסט חדש), אנחנו עדיין בתור 1 וחייבים לשמור על `<Signature_A>`.

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**תור 1, שלב 2 (מודל)**

עכשיו המודל מחליט להזמין מונית על סמך הפלט הקודם של הכלי.

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**תור 1, שלב 3 (משתמש – שליחת פלט של כלי)**

כדי לשלוח את אישור הזמנת המונית, אנחנו צריכים לכלול חתימות לכל קריאות הפונקציה בלולאה הזו (`<Signature A>` + `<Signature B>`).

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### דוגמה לקריאה לפונקציות במקביל

נבחן דוגמה של קריאה לפונקציות במקביל, שבה המשתמש שואל `"Check weather in Paris and London"` ואפשר לראות איפה המודל מבצע אימות.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **התור שלך** | **שלב** | **בקשת משתמש** | **תשובת המודל** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

הנה הקוד להרצת הרצף הנתון.

**תור 1, שלב 1 (בקשת משתמש)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
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
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**תור 1, שלב 1 (תגובת המודל)**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**תור 1, שלב 2 (תגובת המשתמש – שליחת פלט של כלי)**

חובה לשמור על `<Signature_A>` בחלק הראשון בדיוק כפי שהתקבל.

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## שאלות נפוצות

1. **איך מעבירים היסטוריה ממודל אחר ל-Gemini 3 עם חלק של קריאה לפונקציה בתור ובשלב הנוכחיים? אני צריך לספק חלקים של בקשה להפעלת פונקציה שלא נוצרו על ידי ה-API, ולכן אין להם חתימה משויכת של מחשבה?**

   לא מומלץ להוסיף בלוקים של בקשות להפעלת פונקציות בהתאמה אישית, אבל במקרים שבהם אין ברירה, למשל כשמספקים למודל מידע על בקשות להפעלת פונקציות ותשובות שהלקוח ביצע באופן דטרמיניסטי, או כשמעבירים מעקב ממודל אחר שלא כולל חתימות של תהליך החשיבה, אפשר להגדיר את החתימות הבאות של placeholder ‏`"context_engineering_is_the_way_to_go"` או `"skip_thought_signature_validator"` בשדה של חתימת תהליך החשיבה כדי לדלג על האימות.
2. **אני שולח קריאות לפונקציות מקבילות ותשובות משולבות, וה-API מחזיר 400. למה?**

   כשה-API מחזיר קריאות מקבילות לפונקציות FC1 + signature, FC2, התגובה הצפויה מהמשתמש היא FC1+ signature, FC2, FR1, FR2. אם הם משולבים כמו 'FC1 + signature, FR1, FC2, FR2', ה-API יחזיר שגיאה 400.
3. **בסטרימינג, אם המודל לא מחזיר קריאה לפונקציה, אי אפשר למצוא את חתימת המחשבה**

   במהלך תגובה של מודל שלא מכילה FC עם בקשת סטרימינג, המודל עשוי להחזיר את חתימת המחשבה בחלק עם תוכן טקסט ריק. מומלץ לנתח את כל הבקשה עד שהמודל מחזיר את התו `finish_reason`.

## חתימות מחשבה למודלים שונים

[מודלים של Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-3) ומודלים של Gemini 2.5
מתנהגים באופן שונה עם חתימות מחשבה בבקשות להפעלת פונקציות:

- אם יש קריאות לפונקציות בתשובה,
  - החתימה של Gemini 3 תמיד תופיע בחלק הראשון של קריאת הפונקציה.
    **חובה** להחזיר את החלק הזה.
  - החתימה תופיע בחלק הראשון של Gemini 2.5 (בלי קשר לסוג). **לא חייבים** להחזיר את החלק הזה.
- אם אין קריאות לפונקציות בתשובה,
  - אם המודל יוצר מחשבה, החתימה של Gemini 3 תופיע בחלק האחרון.
  - ל-Gemini 2.5 לא תהיה חתימה באף חלק.

פרטים נוספים על ההשוואה מופיעים בדף [חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#signatures).
בקטע 'תהליך החשיבה' במדריך [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he#thinking-process) מוסבר על מודלים של Gemini 3 Image.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-08-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-08-19 (שעון UTC)."],[],[]]
