---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn
fetched_at: 2026-11-02T06:59:53.699286+00:00
title: "Interactions API: \u09ac\u09cd\u09b0\u09c7\u0995\u09bf\u0982 \u09aa\u09b0\u09bf\u09ac\u09b0\u09cd\u09a4\u09a8 \u09ae\u09be\u0987\u0997\u09cd\u09b0\u09c7\u09b6\u09a8 \u0997\u09be\u0987\u09a1 (\u09ae\u09c7 \u09e8\u09e6\u09e8\u09ec) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Interactions API: ব্রেকিং পরিবর্তন মাইগ্রেশন গাইড (মে ২০২৬)

`v1beta` Interactions API-তে ব্রেকিং পরিবর্তন করা হচ্ছে যার ফলে API-এর গঠন
পুনর্বিন্যাস করা হবে যাতে মিড-ফ্লাইট স্টিয়ারিং ও
অ্যাসিঙ্ক্রোনাস টুল কলের মতো ভবিষ্যতের ক্ষমতাগুলি কাজ করে। এই পৃষ্ঠায় কী কী পরিবর্তন হচ্ছে তা ব্যাখ্যা করা হয়েছে এবং
মাইগ্রেট করার ব্যাপারে আপনাকে সাহায্য করতে আগে ও পরে কোডের উদাহরণ দেওয়া হয়েছে। পরিবর্তনের দুটি বিভাগ
আছে:

1. [**ধাপের স্কিমা**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#steps-schema):
   একটি নতুন `steps` অ্যারে `outputs` অ্যারেকে প্রতিস্থাপন করে, প্রতিটি ইন্টার‍্যাকশন টার্নের একটি স্ট্রাকচার্ড
   টাইমলাইন প্রদান করে।
2. [**আউটপুট ফর্ম্যাট কনফিগারেশন**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#output-format-config):
   একটি নতুন পলিমরফিক `response_format` সব আউটপুট ফর্ম্যাট কন্ট্রোল একত্রিত করে
   এবং `response_mime_type` সরিয়ে দেয়।

আপনার ইন্টিগ্রেশন আপডেট করতে
[নতুন স্কিমায় কীভাবে মাইগ্রেট করবেন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#how-to-migrate)
লিঙ্কে দেওয়া ধাপগুলি অনুসরণ করুন।

## মূল পরিবর্তন: `outputs` থেকে `steps`

নতুন স্কিমা `outputs` অ্যারের পরিবর্তে `steps` অ্যারে ব্যবহার করে।

- **লিগ্যাসি**: উত্তরে একটি ফ্ল্যাট `outputs` অ্যারে দেখানো হয়েছে যাতে শুধুমাত্র মডেলের জেনারেট করা কন্টেন্ট রয়েছে।
- **নতুন স্কিমা**: উত্তরে একটি `steps` অ্যারে থাকে যাতে টাইপ ডিসক্রিমিনেটর সহ স্ট্রাকচার্ড ধাপ থাকে।

`POST /interactions` শুধুমাত্র আউটপুট ধাপগুলি রিটার্ন করে। `GET /interactions/{id}`
প্রাথমিক `user_input` ধাপ সহ সম্পূর্ণ ধাপের টাইমলাইন দেখায়।

### প্রাথমিক ইনপুট/আউটপুট (ইউনারি)

#### আগে (পুরনো)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### জাভাস্ক্রিপ্ট

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

#### পরে (নতুন স্কিমা)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### বিশ্রাম

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
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

### ফাংশন কলিং

অনুরোধের স্ট্রাকচার অপরিবর্তিত থাকে, তবে উত্তরটি ফ্ল্যাট
`outputs` কন্টেন্টকে স্ট্রাকচার্ড ধাপ দিয়ে প্রতিস্থাপন করে।

#### আগে (পুরনো)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### জাভাস্ক্রিপ্ট

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
    }
}
```

### বিশ্রাম

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

#### পরে (নতুন স্কিমা)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### জাভাস্ক্রিপ্ট

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
    }
}
```

### বিশ্রাম

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

### সার্ভার-সাইড টুল

সার্ভার-সাইড টুল (যেমন Google Search বা কোড এক্সিকিউশন) এখন `steps` অ্যারেতে নির্দিষ্ট
ধাপের ধরন প্রদান করে। পুরনো স্কিমা `outputs` অ্যারের মধ্যে নির্দিষ্ট কন্টেন্টের ধরন হিসেবে এইসব অপারেশন
ফেরত পাঠালেও, নতুন স্কিমা
সেগুলিকে `steps` অ্যারেতে সরিয়ে দেয়। নিম্নলিখিত উদাহরণগুলি Google Search ব্যবহার করে।

#### আগে (পুরনো)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### জাভাস্ক্রিপ্ট

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

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

#### পরে (নতুন স্কিমা)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### জাভাস্ক্রিপ্ট

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

### বিশ্রাম

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
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

### স্ট্রিমিং

স্ট্রিমিং নতুন ইভেন্টের ধরন দেখায়:

#### নতুন ইভেন্টের ধরন

- `interaction.created`
- `interaction.completed`
- `step.start`
- `step.delta`
- `step.stop`

`interaction.status_update` অপরিবর্তিত রয়েছে। এতে নতুন `status` (যেমন
`in_progress` বা `requires_action`) থাকে। প্রতিটি ইভেন্ট JSON পেলোডের `event_type` ফিল্ডে
তার ধরন উল্লেখ করে, যা SSE `event:` লাইনের সাথে মেলে।

#### বাতিল করা ইভেন্টের ধরন

নিচে উল্লেখ করা পুরনো ইভেন্টের ধরন উপরে তালিকাভুক্ত নতুন ইভেন্ট দ্বারা পরিবর্তন করা হয়েছে:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`

**ফাংশন কল স্ট্রিম করা**: ফাংশন কলের সাথে স্ট্রিমিং ব্যবহার করলে,
`step.start` ইভেন্ট ফাংশনের নাম ডেলিভার করে এবং `step.delta` ইভেন্ট
আর্গুমেন্টকে আংশিক JSON স্ট্রিং (`arguments_delta` ব্যবহার করে) হিসেবে স্ট্রিম করে। সম্পূর্ণ আর্গুমেন্ট পেতে
আপনাকে এইসব ডেল্টা একত্রিত করতে হবে। এটি
ইউনারি কলের থেকে আলাদা যেখানে আপনি সম্পূর্ণ ফাংশন কল অবজেক্ট একবারে পান।

#### উদাহরণ

##### আগে (লিগ্যাসি)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### জাভাস্ক্রিপ্ট

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
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

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

##### পরে (নতুন স্কিমা)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### জাভাস্ক্রিপ্ট

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
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

### বিশ্রাম

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.8-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.8-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.status_update
 // data: {"interaction_id": "int_xyz", "status": "in_progress", "event_type": "interaction.status_update"}
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
 // data: {"index": 1, "event_type": "step.stop"}
 //
 // event: interaction.completed
 // data: {"interaction": {"id": "int_xyz", "status": "completed", "usage": {"total_input_tokens": 10, "total_output_tokens": 5, "total_tokens": 15}}, "event_type": "interaction.completed"} // NEW: Dedicated completion event
```

### স্টেটলেস কথোপকথনের ইতিহাস

আপনি যদি ক্লায়েন্ট সাইডে (স্টেটলেস ব্যবহারের ক্ষেত্রে) ম্যানুয়ালি কথোপকথনের ইতিহাস ম্যানেজ করেন, তাহলে আপনাকে অবশ্যই আগের টার্নগুলি কীভাবে স্ট্রিং করবেন তা আপডেট করতে হবে।

- **লিগ্যাসি**: ডেভেলপাররা প্রায়ই উত্তর থেকে `outputs` অ্যারে সংগ্রহ করে এবং পরবর্তী টার্নে `input` ফিল্ডে সেগুলি ফেরত পাঠায়।
- **নতুন স্কিমা**: আপনাকে এখন উত্তর থেকে `steps` অ্যারে সংগ্রহ করতে হবে এবং পরবর্তী অনুরোধের `input` ফিল্ডে এটি পাস করতে হবে, আপনার নতুন ব্যবহারকারীর টার্নকে `user_input` ধাপ হিসেবে যোগ করতে হবে।

## আউটপুট ফর্ম্যাট কনফিগারেশন: `response_format`টি পরিবর্তন

আপডেট করা API সব আউটপুট ফর্ম্যাট কন্ট্রোলকে একটি ইউনিফায়েড,
পলিমরফিক `response_format` ফিল্ডে একত্রিত করে। এটি টপ লেভেলে আউটপুট কনফিগারেশনকে সেন্ট্রালাইজ করে এবং
`generation_config`-কে মডেলের আচরণের (যেমন
তাপমাত্রা, top\_p এবং থিঙ্কিং) উপর ফোকাস করতে সাহায্য করে।

### গুরুত্বপূর্ণ পরিবর্তন

- **API `response_mime_type` সরিয়ে দেয়।** আপনি এখন `response_format`-এর মধ্যে প্রতিটি ফর্ম্যাট এন্ট্রির জন্য
  MIME-এর ধরন নির্দিষ্ট করতে পারবেন।
- **`response_format` এখন একটি পলিমরফিক অবজেক্ট (বা অ্যারে)।** প্রতিটি
  এন্ট্রিতে একটি `type` ডিসক্রিমিনেটর (`text`, `audio`, `image`) এবং
  টাইপ-নির্দিষ্ট ফিল্ড থাকে। একাধিক আউটপুট মোডালিটির অনুরোধ করতে, ফর্ম্যাট এন্ট্রির
  অ্যারে পাস করুন।
- **`image_config` `generation_config` থেকে `response_format`-এ সরানো হয়েছে।**
  আপনি এখন `"type": "image"` সহ `response_format` এন্ট্রিতে `aspect_ratio` এবং `image_size`-এর মতো
  ইমেজ আউটপুট সেটিংস নির্দিষ্ট করতে পারবেন।

### স্ট্রাকচার্ড আউটপুট (JSON)

নতুন স্কিমা `response_mime_type` ফিল্ড সরিয়ে দেয়। পরিবর্তে, `"type": "text"` সহ `response_format` অবজেক্টের মধ্যে MIME-এর ধরন এবং JSON স্কিমা উল্লেখ করুন।

#### আগে (পুরনো)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
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

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

#### পরে (নতুন স্কিমা)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
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

### বিশ্রাম

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
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

### ছবির কনফিগারেশন

নতুন স্কিমা `generation_config` থেকে `image_config` সরিয়ে দেয়। আপনি এখন `"type": "image"` সহ `response_format` এন্ট্রিতে
ইমেজ আউটপুট সেটিংস নির্দিষ্ট করতে পারবেন।

#### আগে (পুরনো)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### পরে (নতুন স্কিমা)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
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

### বিশ্রাম

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### অডিও কনফিগারেশন

নতুন স্কিমা `response_modalities: ["audio"]`-এর পরিবর্তে `"type": "audio"`-এর `response_format` এন্ট্রি ব্যবহার করে।

#### আগে (পুরনো)

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

### জাভাস্ক্রিপ্ট

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

### বিশ্রাম

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

#### পরে (নতুন স্কিমা)

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

### জাভাস্ক্রিপ্ট

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

### বিশ্রাম

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

একাধিক আউটপুট মোডালিটির (যেমন, টেক্সট ও অডিও একসাথে) অনুরোধ করতে,
একটি অবজেক্টের পরিবর্তে `response_format`-এ ফর্ম্যাট এন্ট্রির একটি অ্যারে
পাস করুন।

## নতুন স্কিমায় কীভাবে মাইগ্রেট করবেন

### SDK ব্যবহারকারী

লেটেস্ট SDK ভার্সনে (Python ≥২.০.০, JavaScript ≥২.০.০) আপগ্রেড করুন। SDK
অটোমেটিক আপনাকে নতুন স্কিমায় অপ্ট-ইন করে — আপনি কীভাবে উত্তর পড়েন তা আপডেট করা ছাড়া
অন্য কোনও কোড পরিবর্তন করার প্রয়োজন নেই (উপরে উদাহরণ দেখুন)। মনে রাখবেন, এই SDK ভার্সনে শুধু নতুন
স্কিমা কাজ করে। পুরনো SDK ভার্সন
(Python 1.x.x, JavaScript 1.x.x) **৮ জুন, ২০২৬**-এ লিগ্যাসি
স্কিমা সরিয়ে না দেওয়া পর্যন্ত কাজ করা চালিয়ে যাবে।

### REST API ব্যবহারকারী

নতুন স্কিমা এখনই চালু করতে আপনার অনুরোধে `Api-Revision: 2026-05-20` হেডার যোগ করুন। **২৬ মে**-এর পরে, নতুন স্কিমা সব অনুরোধের জন্য ডিফল্ট
হয়ে যাবে। আপনি `Api-Revision: 2026-05-07`-এর মাধ্যমে সাময়িকভাবে অপ্ট-আউট করতে পারবেন
**৮ জুন** পর্যন্ত, যখন API স্থায়ীভাবে লিগ্যাসি স্কিমা সরিয়ে দেবে।

### টাইমলাইন

| তারিখ | ধাপ | SDK ব্যবহারকারী | REST API ব্যবহারকারী |
| --- | --- | --- | --- |
| **৭ মে** | অপ্ট-ইন করুন | নতুন SDK ভার্সন উপলভ্য (Python ≥২.০.০, JS ≥২.০.০)। অটোমেটিক নতুন স্কিমা পেতে আপগ্রেড করুন। | চালু করতে `Api-Revision: 2026-05-20` হেডার যোগ করুন। ডিফল্ট হিসেবে লিগ্যাসিই থেকে যায়। |
| **২৬ মে** | ডিফল্ট ফ্লিপ | আগে থেকেই আপগ্রেড করা থাকলে কোনও অ্যাকশন নিতে হবে না। পুরনো SDK (Python 1.x.x, JS 1.x.x) এখনও কাজ করে তবে পুরনো উত্তর দেয়। | নতুন স্কিমা এখন ডিফল্ট হিসেবে সেট করা হয়েছে। অপ্ট-আউট করতে `Api-Revision: 2026-05-07` হেডার পাঠান। |
| **৮ জুন** | সানসেট | Interactions API কলের জন্য Python 1.x.x এবং JS 1.x.x SDK ভার্সন কাজ করবে না। | Interactions API-এর জন্য লিগ্যাসি স্কিমা সরিয়ে দেওয়া হয়েছে। `Api-Revision` হেডার উপেক্ষা করা হয়েছে। |

## মাইগ্রেশন চেকলিস্ট

### ধাপের স্কিমা (`steps`)

- `outputs`-এর পরিবর্তে `steps` অ্যারে থেকে উত্তরের কন্টেন্ট পড়তে কোড আপডেট করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#basic-unary)।
- আপনার কোড `user_input` এবং `model_output` দুই ধরনের ধাপই ম্যানেজ করে কিনা তা যাচাই করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#basic-unary)।
- (ফাংশন কলিং) `steps` অ্যারেতে `function_call` ধাপ খুঁজে পেতে কোড আপডেট করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#function-calling)।
- (সার্ভার-সাইড টুল) টুল-নির্দিষ্ট ধাপ (যেমন, `google_search_call`, `google_search_result`) ম্যানেজ করার জন্য কোড আপডেট করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#server-side-tools)।
- (স্টেটলেস ইতিহাস) পরবর্তী অনুরোধের `input` ফিল্ডে `steps` অ্যারে পাস করার জন্য ইতিহাস ম্যানেজমেন্ট আপডেট করুন।
  [বিবরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#stateless-history)।
- (শুধু স্ট্রিমিং) নতুন SSE ইভেন্টের ধরন (`interaction.created`, `step.delta` ইত্যাদি) শোনার জন্য ক্লায়েন্ট আপডেট করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#streaming)।

### আউটপুট ফর্ম্যাট কনফিগারেশন (`response_format`)

- `response_format`-এর মধ্যে `response_mime_type`-এর জায়গায় `mime_type` ফিল্ড ব্যবহার করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#structured-output)।
- আপনার আগে থেকে থাকা `response_format` JSON স্কিমা `{"type": "text", "schema": ...}` অবজেক্টের মধ্যে র‍্যাপ করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#structured-output)।
- (Image Generation) Move `image_config` from `generation_config` to a `{"type": "image", ...}` entry in `response_format`.
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#image-config)।
- (স্পিচ জেনারেশন) `response_format`-এ `response_modalities=["audio"]`-এর জায়গায় `{"type": "audio"}` এন্ট্রি ব্যবহার করুন।
  [উদাহরণ দেখুন](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn#audio-config)।
- (মাল্টিমোডাল) একাধিক আউটপুট মোডালিটির অনুরোধ করার সময় `response_format`-কে একটি অবজেক্ট থেকে অ্যারেতে কনভার্ট করুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-27 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-27 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
