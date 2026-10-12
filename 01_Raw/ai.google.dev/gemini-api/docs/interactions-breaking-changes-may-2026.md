---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=he
fetched_at: 2026-10-12T07:15:46.855721+00:00
title: "\u202bInteractions API: \u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05d4\u05e2\u05d1\u05e8\u05ea \u05e9\u05d9\u05e0\u05d5\u05d9\u05d9\u05dd \u05e9\u05d2\u05d5\u05e8\u05de\u05d9\u05dd \u05dc\u05d1\u05e2\u05d9\u05d5\u05ea (\u05de\u05d0\u05d9 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ‫Interactions API: מדריך להעברת שינויים שגורמים לבעיות (מאי 2026)

ב-`v1beta` Interactions API מוצגים שינויים שעלולים לשבור את התאימות לאחור. השינויים האלה משנים את מבנה ה-API כדי לתמוך ביכולות עתידיות כמו ניהול של שיחות עם כלים בזמן שהן מתנהלות ושימוש בכלים אסינכרוניים. בדף הזה אנחנו מסבירים מה משתנה ומספקים דוגמאות לקוד לפני ואחרי השינוי כדי לעזור לכם לבצע את המעבר. יש שתי קטגוריות של שינויים:

1. [**סכימת השלבים**](#steps-schema): מערך `steps` חדש מחליף את מערך `outputs`, ומספק ציר זמן מובנה של כל תור לאינטראקציה.
2. [**הגדרת פורמט הפלט**](#output-format-config): פולימורפיזם חדש של `response_format` מאחד את כל אמצעי הבקרה של פורמט הפלט ומסיר את `response_mime_type`.

כדי לעדכן את השילוב, פועלים לפי השלבים במאמר [איך מעבירים לסקירה החדשה](#how-to-migrate).

## שינוי מרכזי: `outputs` ל-`steps`

הסכימה החדשה מחליפה את המערך `outputs` במערך `steps`.

- **גרסה קודמת**: התשובות הוחזרו כמערך שטוח `outputs` שמכיל רק את התוכן שנוצר על ידי המודל.
- **סכימה חדשה**: התשובות מחזירות מערך `steps` שמכיל שלבים מובנים עם מפלים של סוגים.

‫`POST /interactions` מחזירה רק שלבי פלט. ‫`GET /interactions/{id}`
מחזירה את ציר הזמן המלא של השלב, כולל השלב הראשוני `user_input`.

### קלט/פלט בסיסי (אונרי)

#### לפני (הגרסה הקודמת)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### אחרי (סכימה חדשה)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

‫

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

‫[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### בקשה להפעלת פונקציה

מבנה הבקשה נשאר ללא שינוי, אבל בתגובה התוכן השטוח `outputs` מוחלף בשלבים מובנים.

#### לפני (הגרסה הקודמת)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### אחרי (סכימה חדשה)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### כלים בצד השרת

כלים בצד השרת (כמו חיפוש Google או Code Execution) מחזירים עכשיו סוגים ספציפיים של שלבים במערך `steps`. בזמן שהסכימה הקודמת החזירה את הפעולות האלה כסוגי תוכן ספציפיים במערך `outputs`, הסכימה החדשה מעבירה אותן למערך `steps`. הדוגמאות הבאות מתבססות על חיפוש Google.

#### לפני (הגרסה הקודמת)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: ${output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: ${output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### אחרי (סכימה חדשה)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: ${step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: ${step.result[0].search_suggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### סטרימינג

הסטרימינג חושף סוגים חדשים של אירועים:

#### סוגי אירועים חדשים

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### סוגי אירועים שיצאו משימוש

סוגי האירועים הבאים מדור קודם מוחלפים באירועים החדשים שמופיעים למעלה:

- `interaction.start` ← `interaction.created`
- `content.start` ← `step.start`
- `content.delta` ← `step.delta`
- `content.stop` ← `step.stop`
- `interaction.complete` ← `interaction.completed`
- ‫`interaction.status_update` ← הוחלף על ידי `interaction.in_progress`, `interaction.requires_action` וכו'.

**הזרמת קריאות לפונקציות**: כשמשתמשים בהזרמה עם קריאות לפונקציות, האירוע `step.start` מעביר את שם הפונקציה, והאירועים `step.delta` מזרימים את הארגומנטים כמחרוזות JSON חלקיות (באמצעות `arguments_delta`). צריך לצבור את הדלתאות האלה כדי לקבל את הארגומנטים המלאים. זה שונה מקריאות unary שבהן מקבלים את האובייקט המלא של הקריאה לפונקציה בבת אחת.

#### דוגמאות

##### לפני (גרסה קודמת)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### אחרי (סכימה חדשה)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.6-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.6-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.6-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### היסטוריית שיחות ללא שמירת מצב

אם אתם מנהלים את היסטוריית השיחות באופן ידני בצד הלקוח (תרחיש שימוש בלי שמירת מצב), אתם צריכים לעדכן את האופן שבו אתם מחברים בין תורות קודמות.

- **גרסה קודמת**: מפתחים אספו לעיתים קרובות את מערך `outputs` מהתגובות ושלחו אותן בחזרה בשדה `input` בתור הבא.
- **סכימה חדשה**: עכשיו צריך לאסוף את מערך `steps` מהתגובה ולהעביר אותו בשדה `input` של הבקשה הבאה, ולצרף את תור המשתמש החדש כשלב `user_input`.

## הגדרות פורמט הפלט: `response_format` שינויים

ב-API המעודכן, כל אמצעי הבקרה של פורמט הפלט מאוחדים בשדה `response_format` פולימורפי. ההגדרה הזו מרכזת את הגדרת הפלט ברמה העליונה, ומאפשרת להתמקד בהתנהגות המודל (כמו רמת אקראיות, Top-P וחשיבה).`generation_config`

### שינויים מרכזיים

- **ה-API מסיר את `response_mime_type`.** עכשיו מציינים את סוג ה-MIME לכל רשומה של פורמט בתוך `response_format`.
- **`response_format` הוא עכשיו אובייקט פולימורפי (או מערך).** לכל רשומה יש דיסקרימינטור `type` (`text`, ‏ `audio`, ‏ `image`) ושדות ספציפיים לסוג. כדי לבקש כמה אופנים של פלט, מעבירים מערך של רשומות פורמט.
- **`image_config` עובר מ-`generation_config` אל `response_format`.**
  עכשיו אפשר לציין הגדרות של פלט תמונה כמו `aspect_ratio` ו-`image_size`
  בתוך רשומה של `response_format` עם `"type": "image"`.

### פלט מובנה (JSON)

הסכימה החדשה מסירה את השדה `response_mime_type`. במקום זאת, מציינים את סוג ה-MIME ואת סכימת ה-JSON בתוך אובייקט `response_format` עם `"type": "text"`.

#### לפני (הגרסה הקודמת)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### אחרי (סכימה חדשה)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### הגדרת תמונה

הסכימה החדשה מסירה את `image_config` מ-`generation_config`. עכשיו אפשר לציין הגדרות של פלט תמונה ברשומה `response_format` עם `"type": "image"`.

#### לפני (הגרסה הקודמת)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### אחרי (סכימה חדשה)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### הגדרת האודיו

הסכימה החדשה מחליפה את `response_modalities: ["audio"]` בערך `response_format` של `"type": "audio"`.

#### לפני (הגרסה הקודמת)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### אחרי (סכימה חדשה)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

כדי לבקש כמה פורמטים של פלט (לדוגמה, טקסט ואודיו ביחד), צריך להעביר מערך של רשומות פורמט אל `response_format` במקום אובייקט יחיד.

## איך עוברים לסכימה החדשה

### משתמשי SDK

שדרוג לגרסת ה-SDK העדכנית ביותר (Python ≥2.0.0, ‏ JavaScript ≥2.0.0). ה-SDK מפעיל את הסכימה החדשה באופן אוטומטי – לא צריך לשנות את הקוד, רק לעדכן את אופן קריאת התגובות (ראו דוגמאות למעלה). שימו לב שרק הסכימה החדשה נתמכת בגרסאות האלה של ה-SDK. גרסאות ישנות יותר של SDK‏ (Python 1.x.x,‏ JavaScript 1.x.x) ימשיכו לפעול עד להסרת הסכימה מדור קודם ב-**8 ביוני 2026**.

### משתמשי REST API

כדי להצטרף לסקירה של הסכימה החדשה, מוסיפים את הכותרת `Api-Revision: 2026-05-20` לבקשות. אחרי **26 במאי**, הסכימה החדשה תהפוך לברירת המחדל לכל הבקשות. אפשר להשבית את השימוש ב-API באופן זמני באמצעות `Api-Revision: 2026-05-07`
עד **8 ביוני**, התאריך שבו הסכימה מדור קודם תוסר מה-API לצמיתות.

### ציר הזמן

| תאריך | שלב | משתמשי SDK | משתמשי REST API |
| --- | --- | --- | --- |
| **‫7 במאי** | הבעת הסכמה | גרסת SDK חדשה זמינה (Python ≥2.0.0, ‏ JS ≥2.0.0). כדי לקבל את הסכימה החדשה באופן אוטומטי, צריך לשדרג. | הוספת הכותרת `Api-Revision: 2026-05-20` להסכמה להצטרפות. ברירת המחדל נשארת מדור קודם. |
| **26 במאי** | היפוך ברירת המחדל | אם כבר שדרגתם, לא צריך לעשות כלום. ‫SDKs ישנים (Python 1.x.x,‏ JS 1.x.x) עדיין פועלים, אבל מחזירים תשובות מדור קודם. | הסכימה החדשה מוגדרת עכשיו כברירת מחדל. כדי לבטל את ההסכמה, שולחים את הכותרת `Api-Revision: 2026-05-07`. |
| **8 ביוני** | שקיעה | גרסאות Python 1.x.x ו-JS 1.x.x SDK יפסיקו לפעול בקריאות ל-Interactions API. | הסרנו את הסכימה הקודמת של Interactions API. הכותרת `Api-Revision` לא נכללה. |

## הגירה - רשימת משימות לביצוע

### סכימת השלבים (`steps`)

- צריך לעדכן את הקוד כדי לקרוא את תוכן התשובה מהמערך `steps` במקום מ-`outputs`. [דוגמאות](#basic-unary)
- מוודאים שהקוד מטפל בשני סוגי השלבים: `user_input` ו-`model_output`. [דוגמאות](#basic-unary)
- (הפעלת פונקציות) מעדכנים את הקוד כדי למצוא את השלבים של `function_call` במערך `steps`. [דוגמאות](#function-calling)
- (כלים בצד השרת) מעדכנים את הקוד כדי לטפל בשלבים ספציפיים לכלים (למשל `google_search_call`, `google_search_result`). [דוגמאות](#server-side-tools)
- (היסטוריה בלי שמירת מצב) עדכון של ניהול ההיסטוריה כדי להעביר את מערך `steps` בשדה `input` של הבקשה הבאה. [פרטים נוספים](#stateless-history)
- (סטרימינג בלבד) צריך לעדכן את הלקוח כדי להאזין לסוגים חדשים של אירועי SSE (‏`interaction.created`, ‏`step.delta` וכו'). [דוגמאות](#streaming)

### הגדרת פורמט הפלט (`response_format`)

- מחליפים את `response_mime_type` בשדה `mime_type` בתוך `response_format`. [דוגמאות](#structured-output)
- עוטפים את סכימת ה-JSON הקיימת `response_format` באובייקט `{"type": "text", "schema": ...}`. [דוגמאות](#structured-output)
- (יצירת תמונות) העברה של `image_config` מ-`generation_config` לרשומה `{"type": "image", ...}` ב-`response_format`. [דוגמאות](#image-config)
- (יצירת דיבור) מחליפים את `response_modalities=["audio"]` בערך `{"type": "audio"}` ב-`response_format`. [דוגמאות](#audio-config)
- (מולטימודאלי) המרת `response_format` מאובייקט יחיד למערך כשמבקשים כמה אופנים של פלט.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-12 (שעון UTC)."],[],[]]
