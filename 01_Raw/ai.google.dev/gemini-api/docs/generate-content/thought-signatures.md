---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=bn
fetched_at: 2026-10-19T05:38:18.480917+00:00
title: "\u099a\u09bf\u09a8\u09cd\u09a4\u09be \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4 \u09b8\u09cd\u09ac\u09be\u0995\u09cd\u09b7\u09b0 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# চিন্তা সংক্রান্ত স্বাক্ষর

থট সিগনেচার হল মডেলের ইন্টার্নাল চিন্তাভাবনার প্রসেসের এনক্রিপ্ট করা উপস্থাপনা এবং
মাল্টি-স্টেপ ইন্টার‍্যাকশন জুড়ে রিজনিংয়ের প্রসঙ্গ বজায় রাখতে
ব্যবহার করা হয়।
থিংকিং মডেল (যেমন, Gemini 4, 3 ও 2.5 সিরিজ) ব্যবহার করার সময়, API
উত্তরের [কন্টেন্ট পার্টের](https://ai.google.dev/api/caching?hl=bn#Part) মধ্যে `thoughtSignature` ফিল্ড
ফেরাতে পারে (যেমন, `text` বা `functionCall` পার্ট)।

সাধারণ নিয়ম হিসেবে, মডেলের উত্তরে কোনও থট সিগনেচার পেলে,
পরবর্তী ধাপে কথোপকথনের
ইতিহাস পাঠানোর সময় সেটি ঠিক যেভাবে পেয়েছেন সেভাবেই পাঠাতে হবে।
**Gemini 4 ও Gemini 3 মডেল ব্যবহার করার সময়, আপনাকে অবশ্যই ফাংশন কলিংয়ের সময়
থট সিগনেচার পাস করতে হবে, তা না হলে আপনি যাচাইকরণ সংক্রান্ত সমস্যা পাবেন** (4xx স্ট্যাটাস কোড)।
এর মধ্যে Gemini 3 Flash-এর জন্য `minimal`
[থিঙ্কিং লেভেল](https://ai.google.dev/gemini-api/docs/thinking?hl=bn#thinking-levels) সেটিং ব্যবহার করার সময়ও অন্তর্ভুক্ত।

## এটি কীভাবে কাজ করে

নিচের গ্রাফিক থেকে Gemini API-তে [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)-এর ক্ষেত্রে "টার্ন" ও "স্টেপ" বলতে কী বোঝায় তা বোঝা যাবে। "টার্ন"
হল ব্যবহারকারী ও মডেলের মধ্যে কথোপকথনের একটি সম্পূর্ণ অংশ। "ধাপ"
হল মডেলের মাধ্যমে করা আরও সূক্ষ্ম অ্যাকশন বা অপারেশন, যা প্রায়শই একটি টার্ন সম্পূর্ণ করার জন্য
বৃহত্তর প্রক্রিয়ার অংশ হিসেবে করা হয়।

![ফাংশন কলিং টার্ন ও ধাপের ডায়াগ্রাম](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=bn)

*এই ডকুমেন্ট Gemini 4 ও Gemini 3 মডেলের জন্য ফাংশন কলিং ম্যানেজ করার উপর ফোকাস করে। 2.5-এর সাথে পার্থক্য সম্পর্কে জানতে*[মডেলের আচরণ](#model-behavior) বিভাগ দেখুন।

Gemini 4 এবং Gemini 3, ফাংশন কলের মাধ্যমে সব মডেলের উত্তরের (API থেকে পাওয়া উত্তর) জন্য থট সিগনেচার রিটার্ন করে। নিম্নলিখিত ক্ষেত্রে
থট সিগনেচার দেখানো হয়:

- [সমান্তরাল ফাংশন](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn#parallel_function_calling)
  কল থাকলে, মডেলের দেওয়া উত্তরের প্রথম ফাংশন কল অংশে একটি
  চিন্তা সংক্রান্ত সিগনেচার থাকবে।
- সিকোয়েন্সিয়াল ফাংশন কল (একাধিক ধাপ) থাকলে, প্রতিটি ফাংশন কলের
  একটি করে সিগনেচার থাকবে এবং আপনাকে সব সিগনেচার ফেরত পাঠাতে হবে।
- ফাংশন কল ছাড়া মডেলের উত্তর, মডেলের দেওয়া শেষ অংশের মধ্যে
  একটি থট সিগনেচার রিটার্ন করবে।

নিম্নলিখিত সারণীটি মাল্টি-স্টেপ ফাংশন কলের একটি ভিজ্যুয়ালাইজেশন প্রদান করে,
উপরে উল্লিখিত সিগনেচারের ধারণার সাথে টার্ন এবং ধাপের সংজ্ঞা একত্রিত করে:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **টার্ন** | **ধাপ** | **ব্যবহারকারীর অনুরোধ** | **মডেলের উত্তর** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | কোনওটিই নয় |

## ফাংশন কলিং পার্টে সিগনেচার

Gemini যখন কোনও `functionCall` তৈরি করে, তখন এটি `thought_signature`-এর উপর নির্ভর করে
যাতে পরবর্তী ধাপে টুলের আউটপুট সঠিকভাবে প্রসেস করা যায়।

- **আচরণ**:
  - **সিঙ্গেল ফাংশন কল**: `functionCall` অংশে `thought_signature` থাকবে।
  - **প্যারালাল ফাংশন কল**: কোনও উত্তরে মডেল প্যারালাল ফাংশন কল জেনারেট করলে, `thought_signature` **শুধুমাত্র প্রথম**
    `functionCall` অংশের সাথে
    অ্যাটাচ করা হয়। একই উত্তরের পরবর্তী `functionCall`টি অংশে
    স্বাক্ষর থাকবে **না**।
- **প্রয়োজনীয়তা**: কথোপকথনের ইতিহাস ফেরত পাঠানোর সময়, এই স্বাক্ষরটি ঠিক সেই অংশে ফেরত দিতে **হবে** যেখানে এটি
  পাওয়া গেছে।
- **যাচাইকরণ**: বর্তমান টার্নের মধ্যে
  সব ফাংশন কলের জন্য কঠোর যাচাইকরণ প্রয়োগ করা হয়। (শুধুমাত্র বর্তমান টার্ন প্রয়োজন; আমরা আগের টার্ন
  যাচাই করি না)
  - API ইতিহাসে (নতুন থেকে পুরনো) ফিরে গিয়ে সবচেয়ে সাম্প্রতিক
    **ব্যবহারকারীর** মেসেজ খুঁজে দেখে যাতে স্ট্যান্ডার্ড কন্টেন্ট (যেমন, `text`) আছে (যা
    বর্তমান টার্নের শুরু হবে)। এটি `functionResponse` **be** না।
  - **সব** মডেল `functionCall` টার্ন যা নির্দিষ্ট ব্যবহারের পরে ঘটে
    মেসেজকে টার্নের অংশ হিসেবে বিবেচনা করা হয়।
  - বর্তমান টার্নের **প্রতিটি ধাপের** **প্রথম** `functionCall` অংশে
    **অবশ্যই** এর `thought_signature` অন্তর্ভুক্ত করতে হবে।
  - বর্তমান টার্নের কোনও ধাপে প্রথম `functionCall` অংশের জন্য আপনি `thought_signature` বাদ দিলে, অনুরোধটি 400 ত্রুটি সহ ব্যর্থ হবে।
- **সঠিক সিগনেচার না পাওয়া গেলে, এখানে কীভাবে সমস্যা হবে তা বলা হল**
  - Gemini 3 মডেল: স্বাক্ষর অন্তর্ভুক্ত করতে না পারলে, 400 সমস্যা হবে। শব্দগুলি এই ধরনের হবে:
    - `<index of contents array>`
      কন্টেন্ট ব্লকে ফাংশন কল `<Function Call>`-এ `thought_signature` নেই। যেমন, *কন্টেন্ট ব্লকে `1.` Function
      call `FC1`-এ একটি `thought_signature` নেই।*

### সিকোয়েন্সিয়াল ফাংশন কলিংয়ের উদাহরণ

এই বিভাগে একাধিক ফাংশন কলের একটি উদাহরণ দেখানো হয়েছে যেখানে ব্যবহারকারী একটি
জটিল প্রশ্ন জিজ্ঞাসা করেছেন যার জন্য একাধিক টাস্ক প্রয়োজন।

আসুন, একাধিক-বার ফাংশন কল করার একটি উদাহরণ দেখে নেওয়া যাক যেখানে ব্যবহারকারী
একাধিক টাস্কের প্রয়োজন হয় এমন একটি জটিল প্রশ্ন জিজ্ঞাসা করেছেন: `"Check flight status for AA100 and
book a taxi if delayed"`।

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **টার্ন** | **ধাপ** | **ব্যবহারকারীর অনুরোধ** | **মডেলের উত্তর** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

নিচের কোডটি উপরের সারণীতে দেখানো ক্রমকে ব্যাখ্যা করে।

**১ম বার, ১ম ধাপ (ব্যবহারকারীর অনুরোধ)**

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

**টার্ন ১, ধাপ ১ (মডেলের উত্তর)**

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

**টার্ন ১, ধাপ ২ (ব্যবহারকারীর উত্তর - টুলের আউটপুট পাঠানো)** যেহেতু ব্যবহারকারীর এই টার্নে
শুধুমাত্র `functionResponse` (নতুন কোনও টেক্সট নেই) আছে, তাই আমরা এখনও টার্ন ১-এ আছি। আমাদের
`<Signature_A>` সংরক্ষণ করতে হবে।

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

**১ম টার্ন, ২য় ধাপ (মডেল)** মডেলটি এখন
আগের টুলের আউটপুটের উপর ভিত্তি করে ট্যাক্সি বুক করার সিদ্ধান্ত নেয়।

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

**টার্ন ১, ধাপ ৩ (ব্যবহারকারী - টুলের আউটপুট পাঠানো)** ট্যাক্সি বুকিং
কনফার্মেশন পাঠানোর জন্য, এই লুপে **সব** ফাংশন কলের সিগনেচার অন্তর্ভুক্ত করতে হবে
(`<Signature A>` + `<Signature B>`)।

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

### প্যারালাল ফাংশন কলিংয়ের উদাহরণ

আসুন, প্যারালাল ফাংশন কলিংয়ের একটি উদাহরণ দেখে নেওয়া যাক যেখানে ব্যবহারকারী
`"Check weather in Paris and London"` মডেলটি কোথায় ভ্যালিডেশন করে তা দেখতে চান।

| **টার্ন** | **ধাপ** | **ব্যবহারকারীর অনুরোধ** | **মডেলের উত্তর** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + স্বাক্ষর  FC2 ("লন্ডন") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (কোনও FC নেই) | কোনওটিই নয় |

নিম্নলিখিত কোডটি উপরের সারণীর ক্রম ব্যাখ্যা করে।

**১ম বার, ১ম ধাপ (ব্যবহারকারীর অনুরোধ)**

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

**১ম টার্ন, ১ম ধাপ (মডেলের উত্তর)**

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

**টার্ন ১, ধাপ ২ (ব্যবহারকারীর উত্তর - টুল আউটপুট পাঠানো)** আমাদের অবশ্যই প্রথম অংশে
`<Signature_A>` ঠিক যেমনভাবে পাওয়া গেছে তেমনভাবে সংরক্ষণ করতে হবে।

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

## `functionCall` নয় এমন অংশে স্বাক্ষর

এছাড়াও, Gemini `thought_signatures` রিটার্ন করতে পারে
ফাংশন-কল না করা অংশে উত্তরের শেষ ভাগে।

- **আচরণ**: মডেলের দেওয়া কন্টেন্টের শেষ অংশে (`text, inlineData…`) `thought_signature` থাকতে পারে।
- **সাজেশন**: মডেল যাতে খুব ভাল কোয়ালিটির রিজনিং বজায় রাখতে পারে তা নিশ্চিত করার জন্য এই সিগনেচার রিটার্ন করার **সাজেশন দেওয়া হয়**, বিশেষ করে জটিল নির্দেশাবলী অনুসরণ করা বা সিমুলেটেড এজেন্টসুলভ ওয়ার্কফ্লোর ক্ষেত্রে।
- **যাচাইকরণ**: API যাচাইকরণ কঠোরভাবে প্রয়োগ করে **না**। আপনি সেগুলি বাদ দিলে, কোনও
  ব্লকিং সংক্রান্ত সমস্যা পাবেন না, তবে পারফর্ম্যান্স খারাপ হতে পারে।

### টেক্সট/ইন-কনটেক্সট রিজনিং (যাচাইকরণ নেই)

**১ম টার্ন, ১ম ধাপ (মডেলের উত্তর)**

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

**দ্বিতীয় রাউন্ড, প্রথম ধাপ (ব্যবহারকারী)**

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

## OpenAI compatibility-র জন্য সিগনেচার

[OpenAI কম্প্যাটিবিলিটি](https://ai.google.dev/gemini-api/docs/openai?hl=bn) ব্যবহার করে চ্যাট সম্পূর্ণ করার API-এর জন্য কীভাবে থট সিগনেচার ম্যানেজ করতে হয় তা নিম্নলিখিত উদাহরণে দেখানো হয়েছে।

### সিকোয়েন্সিয়াল ফাংশন কলিংয়ের উদাহরণ

এটি একাধিক ফাংশন কলিংয়ের একটি উদাহরণ যেখানে ব্যবহারকারী একটি জটিল
প্রশ্ন জিজ্ঞাসা করেছেন যার জন্য একাধিক টাস্ক প্রয়োজন।

আসুন, একাধিক-বার ফাংশন কল করার একটি উদাহরণ দেখে নেওয়া যাক যেখানে ব্যবহারকারী
`Check flight status for AA100 and book a taxi if delayed` প্রশ্ন করেছেন এবং আপনি দেখতে পাবেন যে
ব্যবহারকারী একাধিক টাস্কের প্রয়োজন হয় এমন কোনও জটিল প্রশ্ন করলে কী হয়।

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **টার্ন** | **ধাপ** | **ব্যবহারকারীর অনুরোধ** | **মডেলের উত্তর** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

নিচে দেওয়া কোডটি প্রদত্ত ক্রম অনুযায়ী কাজ করে।

**১ম বার, ১ম ধাপ (ব্যবহারকারীর অনুরোধ)**

```
{
  "model": "google/gemini-4-argon",
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

**১ম টার্ন, ১ম ধাপ (মডেলের উত্তর)**

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

**১ম টার্ন, ২য় ধাপ (ব্যবহারকারীর উত্তর - টুল আউটপুট পাঠানো)**

যেহেতু এই ব্যবহারকারীর টার্নে শুধু `functionResponse` (নতুন কোনও টেক্সট নেই) আছে, তাই আমরা
এখনও টার্ন ১-এ আছি এবং `<Signature_A>` অবশ্যই বজায় রাখতে হবে।

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

**১ম চাল, ২য় ধাপ (মডেল)**

মডেল এখন আগের টুল আউটপুটের ভিত্তিতে ট্যাক্সি বুক করার সিদ্ধান্ত নেয়।

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

**টার্ন ১, ধাপ ৩ (ব্যবহারকারী - টুল আউটপুট পাঠানো)**

ট্যাক্সি বুকিং কনফার্মেশন পাঠানোর জন্য, এই লুপে (`<Signature A>` + `<Signature B>`) সমস্ত
ফাংশন কলের জন্য আমাদের অবশ্যই স্বাক্ষর অন্তর্ভুক্ত করতে হবে।

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

### প্যারালাল ফাংশন কলিংয়ের উদাহরণ

আসুন, প্যারালাল ফাংশন কলিংয়ের একটি উদাহরণ দেখে নেওয়া যাক, যেখানে ব্যবহারকারী
`"Check weather in Paris and London"` প্রশ্ন করেছেন এবং আপনি দেখতে পাবেন যে মডেলটি কোথায়
ভ্যালিডেশন করেছে।

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **টার্ন** | **ধাপ** | **ব্যবহারকারীর অনুরোধ** | **মডেলের উত্তর** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

প্রদত্ত সিকোয়েন্সের মাধ্যমে ওয়াক থ্রু করার কোড এখানে দেওয়া হল।

**টার্ন ১, ধাপ ১ (ব্যবহারকারীর অনুরোধ)**

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

**১ম টার্ন, ১ম ধাপ (মডেলের উত্তর)**

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

**টার্ন ১, ধাপ ২ (ব্যবহারকারীর উত্তর - টুল আউটপুট পাঠানো)**

প্রথম অংশে `<Signature_A>` যেভাবে পেয়েছেন ঠিক সেইভাবেই রাখতে হবে।

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

## প্রায়শই জিজ্ঞাসিত প্রশ্ন

1. **বর্তমান টার্ন ও ধাপে ফাংশন কল পার্ট সহ অন্য মডেল থেকে Gemini 4 বা Gemini 3-তে আমি কীভাবে ইতিহাস ট্রান্সফার করব? API তৈরি করেনি এমন ফাংশন কলের
   পার্ট আমাকে দিতে হবে, তাই সেটির সাথে কোনও সংশ্লিষ্ট
   থট সিগনেচার নেই?**

   অনুরোধে কাস্টম ফাংশন কল ব্লক ইনজেক্ট করাকে কঠোরভাবে নিরুৎসাহিত করা হলেও, যেসব ক্ষেত্রে এটি এড়ানো যায় না, যেমন ক্লায়েন্ট দ্বারা নির্ধারকভাবে কার্যকর করা
   ফাংশন কল এবং প্রতিক্রিয়ার মডেলকে তথ্য প্রদান করা, অথবা অন্য কোনও মডেল থেকে
   ট্রেস ট্রান্সফার করা যাতে থট সিগনেচার অন্তর্ভুক্ত নয়, সেক্ষেত্রে আপনি যাচাইকরণ
   এড়াতে থট সিগনেচার ফিল্ডে `"context_engineering_is_the_way_to_go"` বা `"skip_thought_signature_validator"`-এর নিম্নলিখিত ডামি সিগনেচার সেট করতে পারেন।
2. **আমি ইন্টারলিভড প্যারালাল ফাংশন কল ও উত্তর ফেরত পাঠাচ্ছি এবং
   API একটি 400 ফেরত পাঠাচ্ছে। কেন?**

   API যখন সমান্তরাল ফাংশন কল "FC1 + signature, FC2" রিটার্ন করে, তখন
   ব্যবহারকারীর প্রত্যাশিত উত্তর হল "FC1+ signature, FC2, FR1, FR2"। সেগুলি "FC1 + signature, FR1, FC2, FR2" হিসেবে ইন্টারলিভ করা থাকলে
   API 400
   এরর কোড রিটার্ন করবে।
3. **স্ট্রিমিংয়ের সময় এবং মডেল ফাংশন কল রিটার্ন না করলে আমি থট সিগনেচার
   খুঁজে পাই না**

   স্ট্রিমিং অনুরোধ সহ FC নেই এমন মডেল রেসপন্সের সময়, মডেলটি খালি টেক্সট কন্টেন্ট পার্ট সহ একটি পার্টে থট সিগনেচার ফেরত দিতে পারে। মডেলের থেকে `finish_reason`
   ফেরত না পাওয়া পর্যন্ত সম্পূর্ণ অনুরোধ পার্স করার পরামর্শ দেওয়া হয়।

## বিভিন্ন মডেলের জন্য থট সিগনেচার

[Gemini 4](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=bn), [Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-3) এবং Gemini 2.5 মডেল
ফাংশন কলে থট সিগনেচারের সাথে আলাদাভাবে আচরণ করে:

- কোনও উত্তরে ফাংশন কল থাকলে,
  - Gemini 4 ও Gemini 3-তে প্রথম ফাংশন কলের অংশে সবসময় সিগনেচার থাকবে।
    ওই অংশটি ফেরত দেওয়া **বাধ্যতামূলক**।
  - Gemini 2.5-এর প্রথম অংশে স্বাক্ষর থাকবে (ধরন যাই হোক না কেন)। সেই অংশ ফেরত দেওয়া **ঐচ্ছিক**।
- কোনও উত্তরে ফাংশন কল না থাকলে,
  - Gemini 4 এবং Gemini 3-এর ক্ষেত্রে, মডেল কোনও চিন্তা জেনারেট করলে, শেষ অংশে স্বাক্ষর থাকবে।
  - Gemini 2.5-এর কোনও অংশে স্বাক্ষর থাকবে না।

আরও তুলনামূলক বিবরণের জন্য [চিন্তাভাবনা](https://ai.google.dev/gemini-api/docs/thinking?hl=bn#signatures) পৃষ্ঠা দেখুন।
Gemini 3 ইমেজ মডেলের জন্য
[ইমেজ জেনারেশন](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn#thinking-process) গাইডের থিঙ্কিং প্রসেস বিভাগ দেখুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
