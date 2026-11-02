---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=bn
fetched_at: 2026-11-02T07:09:55.093513+00:00
title: "Gemini 4 Argon-\u098f \u09a8\u09a4\u09c1\u09a8 \u0995\u09c0 \u0986\u099b\u09c7 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# Gemini 4 Argon-এ নতুন কী আছে

Gemini 4 Argon (`gemini-4-argon`) হল আমাদের লেটেস্ট, সবচেয়ে দক্ষ মডেল। জটিল কোডিং, এজেন্টিক, গণিত এবং বিজ্ঞান সংক্রান্ত টাস্কে আরও ভালো ফলাফল পেতে এটি কঠিন সমস্যার উপর দীর্ঘ সময় ধরে যুক্তি দিতে পারে। Gemini API এবং Google AI Studio-তে Gemini 4 Argon উপলভ্য।

Gemini 4 Argon-এ ১ মিলিয়ন ইনপুট-আউটপুট টোকেন লিমিট, ১ মিলিয়ন টোকেন পর্যন্ত লং ডিকোড এবং টিউন করা যায় এমন থিঙ্কিং লেভেল (`low`, `medium`, `high`) রয়েছে।

[experiment

AI Studio-তে এটি ব্যবহার করে দেখুন

Gemini 4 Argon এবং AI Studio-এর সাহায্যে একদম শুরু থেকে অ্যাপ তৈরি করুন।](https://aistudio.google.com/apps?model=gemini-4-argon&hl=bn)
[smart\_toy

অ্যাপ গ্যালারি

Gemini 4 Argon দিয়ে তৈরি অ্যাপ খেলুন ও রিমিক্স করুন।](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=bn)
[rocket\_launch

শুরু করুন

স্টার্টার প্রম্পট দিয়ে Gemini 4 Argon ব্যবহার করা শুরু করুন।](https://aistudio.google.com/learn/gemini-4-argon?hl=bn)

এই গাইডে Gemini 4 Argon-এ নতুন কী আছে, API পরিবর্তন, কোডের উদাহরণ এবং মাইগ্রেশন সংক্রান্ত নির্দেশিকা ব্যাখ্যা করা হয়েছে।

## নতুন মডেল

| মডেল | মডেল আইডি | ডিফল্ট থিঙ্কিং লেভেল | দাম | বিবরণ |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | ৩০ নভেম্বর, ২০২৬ পর্যন্ত $২/১ মিলিয়ন ইনপুট টোকেন এবং $১০/১ মিলিয়ন আউটপুট টোকেনের প্রাথমিক মূল্যে উপলভ্য (তারপরে $৪/১ মিলিয়ন ইনপুট এবং $২০/১ মিলিয়ন আউটপুট)। আরও জানতে [দাম](https://ai.google.dev/gemini-api/docs/pricing?hl=bn) দেখুন। | আমাদের সবচেয়ে দক্ষ মডেল, যা বাস্তব-জগতের সফ্টওয়্যার ইঞ্জিনিয়ারিং এবং জ্ঞান সংক্রান্ত কাজের টাস্ক জুড়ে গভীরতা এবং নির্ভুলতার সাথে সবচেয়ে কঠিন সমস্যার সমাধান করার জন্য তৈরি করা হয়েছে। |

## কুইকস্টার্ট

সাজেস্ট করা ডিফল্ট `thinking_level` (`medium`) এবং 64K আউটপুট টোকেন সীমা সহ `gemini-4-argon`-এ অনুরোধ পাঠাতে নিম্নলিখিত উদাহরণটি ব্যবহার করুন:

### Python

```
pip install -U "google-genai>=2.30.1"
```

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
    config=types.GenerateContentConfig(
        max_output_tokens=65536,
        thinking_config=types.ThinkingConfig(thinking_level="medium"),
    ),
)

print(response.text)
```

### জাভাস্ক্রিপ্ট

```
npm install "@google/genai@>=2.29.1"
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-4-argon",
  contents: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
  config: {
    maxOutputTokens: 65536,
    thinkingConfig: {
      thinkingLevel: "medium",
    },
  },
});

console.log(response.text);
```

### বিশ্রাম

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."}]
    }],
    "generationConfig": {
      "maxOutputTokens": 65536,
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Gemini 4 Argon-এ নতুন কী আছে

- **ইউনিফায়েড ১ মিলিয়ন ইনপুট-আউটপুট টোকেন সীমা:** ইনপুট, থিঙ্কিং ও আউটপুট টোকেন একটি ১ মিলিয়ন টোকেন উইন্ডো শেয়ার করে, যেখানে নন-স্ট্রিমিং কলের জন্য অনুরোধ প্রতি ৩২ হাজার এবং স্ট্রিমিং কলের জন্য স্ট্রিম প্রতি ৬৪ হাজার টোকেনের সীমা রয়েছে।
- **১ মিলিয়ন টোকেন পর্যন্ত দীর্ঘ ডিকোড:** মডেলটি অনুরোধ প্রতি ক্যাপের বাইরে, আপনার ইনপুট বাদ দিয়ে ১ মিলিয়ন টোকেন পর্যন্ত জেনারেট করতে পারে। লেটেস্ট Google GenAI SDK ডিফল্ট হিসেবে আপনার জন্য কাজ করা চালিয়ে যায়।
- **এজেন্টিক ভিডিও আন্ডারস্ট্যান্ডিং (GA):** [এজেন্টিক ভিডিও আন্ডারস্ট্যান্ডিং](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=bn#agentic-video-understanding) এখন সাধারণভাবে উপলভ্য।
- **Managed Agents-এ কাজ করে:** Gemini Managed Agents-এ [Antigravity এজেন্ট](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=bn) এখন Gemini 4 Argon-এ কাজ করে।

আরও বিবরণের জন্য, [Gemini 4 Argon মডেল পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=bn) দেখুন। দাম সংক্রান্ত বিবরণের জন্য, [দাম সংক্রান্ত পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/pricing?hl=bn#gemini-4-argon) দেখুন।

## আরও বড় আউটপুট ও দীর্ঘ ডিকোড

কোনও টাস্কের জন্য গভীর রিজনিংয়ের প্রয়োজন হলে, Gemini 4 Argon আরও বেশি সময় ধরে চিন্তা করতে এবং আরও বেশি পরিশ্রম করতে পারে, যাতে জটিল গণিত, বিজ্ঞান এবং কোডিংয়ের সমস্যাগুলি একবারে সমাধান করা যায়।

- **ইউনিফায়েড ১ মিলিয়ন ইনপুট-আউটপুট টোকেন সীমা:** Argon, থিঙ্কিং ও আউটপুট মিলিয়ে, আপনার ইনপুট টোকেন বাদ দিয়ে, সর্বাধিক ১ মিলিয়ন টোকেন ব্যবহার করতে পারে।
- **থিঙ্কিং টোকেন `max_output_tokens`-এর জন্য গণনা করা হয়:** কঠিন টাস্কের ক্ষেত্রে, আরও ভালো উত্তর দেওয়ার জন্য মডেল আপনার `max_output_tokens` বাজেট আরও বেশি ব্যবহার করে। টোকেনের ব্যবহার নিয়ন্ত্রণ করতে `thinking_level` ব্যবহার করুন।
- **অনুরোধ প্রতি ক্যাপ (৬৪ হাজার স্ট্রিমিং / ৩২ হাজার নন-স্ট্রিমিং):** একটি স্ট্রিমিং অনুরোধ সর্বাধিক ৬৫,৫৩৬টি টোকেন রিটার্ন করে। একটি নন-স্ট্রিমিং অনুরোধ সর্বাধিক ৩২,৭৬৮ টোকেন রিটার্ন করে, যা Gemini 3.x-এ ৬৫,৫৩৬ থেকে কম। REST কলের ক্ষেত্রেও এই ক্যাপ ডিফল্ট হিসেবে সেট করা থাকে।

লেটেস্ট Google GenAI SDK ডিফল্ট হিসেবে আপনার জন্য লং ডিকোড রান করে। Python `google-genai` 2.30.1 বা তার পরবর্তী ভার্সন অথবা JavaScript `@google/genai` 2.29.1 বা তার পরবর্তী ভার্সন ব্যবহার করুন।

এইসব ভার্সনে, `automatic_continuation` ডিফল্ট হিসেবে `True` থাকে, তাই আপনাকে এটি সেট করতে হবে না। আপনি অনুরোধ প্রতি ক্যাপের উপরে `max_output_tokens` সেট করলে, মডেল শেষ না হওয়া বা `max_output_tokens`-এ না পৌঁছানো পর্যন্ত `generate_content` এবং `generate_content_stream` অটোমেটিক অনুরোধ জুড়ে চলতে থাকে এবং একটি সম্মিলিত উত্তর প্রদান করে।

```
response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a complete, rigorous proof of the prime number theorem.",
    config=types.GenerateContentConfig(
        max_output_tokens=262144,
        thinking_config=types.ThinkingConfig(thinking_level="high"),
        automatic_continuation=True,  # Default.
    ),
)
```

লুপ নিজে থেকে চালাতে, `automatic_continuation=False` সেট করুন। আপনি REST কল করলে বা পুরনো SDK ব্যবহার করলে, অনুরোধ প্রতি-অনুরোধের ক্যাপে থেমে যায়। REST লুপ, থার্ড-পার্টি ফ্রেমওয়ার্ক, টোকেন গণনা এবং কখন লং ডিকোড ব্যবহার করতে হবে সেই সম্পর্কে জানতে, [লং ডিকোড গাইড](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=bn) দেখুন।

### আউটপুট টোকেনের সীমা সেট করা

`max_output_tokens`, সমস্ত কন্টিনিউয়েশন অনুরোধ সহ, একটি জেনারেশনের জন্য মোট থিঙ্কিং ও আউটপুট টোকেন সেট করে। এটি যথেষ্ট বেশি সেট করুন যাতে চিন্তা করার সময় উত্তরটি ছোট না হয়ে যায়। কোনও হার্ড প্রম্পট সব খরচ করে ফেললে, খরচ সীমিত করার জন্য এটি যথেষ্ট কম সেট করুন।

শুরু করার জন্য নিম্নলিখিত নির্দেশিকা ব্যবহার করুন:

- **স্ট্যান্ডার্ড টাস্ক:** ডিফল্ট রাখুন।
- **আগে থেকে থাকা অ্যাপের সীমা ৩২ হাজারের কম হলে:** `max_output_tokens` বাড়িয়ে ৩২,৭৬৮ করুন। কম টোকেন ব্যবহার করতে, `thinking_level` কমান।
- **আগে যেসব টাস্কে ৩২ হাজারের বেশি টোকেন ব্যবহার করা হয়েছে:** `max_output_tokens`-এর ভ্যালু ৬৫,৫৩৬-এ সেট করুন।
- **জটিল যুক্তি ও কোডিং:** `max_output_tokens`-কে ১৩১,০৭২ বা ২৬২,১৪৪-এ সেট করুন, আপনার ইনপুট টোকেন বাদ দিয়ে ১,০৪৮,৫৭৬ পর্যন্ত।

কোনও অনুরোধে `max_output_tokens`-এর সবকটি ব্যবহার করা হলে, এটি `finish_reason: "MAX_TOKENS"` রিটার্ন করে এবং এতে `continuation_token` অন্তর্ভুক্ত থাকে। আপনি আবার চালু বা শুরু করতে পারবেন।

- **চেকপয়েন্ট থেকে আবার শুরু করুন:** লেটেস্ট `continuation_token` ও আরও বেশি `max_output_tokens` সহ আসল অনুরোধ পাঠান। আপনি `max_output_tokens` না বাড়ালে, অনুরোধটি `400 INVALID_ARGUMENT` রিটার্ন করে।
- **আবার শুরু করুন:** আরও বেশি `max_output_tokens` এবং কোনও `continuation_token` ছাড়াই আসল অনুরোধ পাঠান।

### থিঙ্কিং লেভেল সম্পর্কে বোঝা

Gemini 4 Argon-এ কোয়ালিটি, লেটেন্সি ও টোকেন ব্যবহারের উপর আপনার প্রধান কন্ট্রোল হল [চিন্তাভাবনার লেভেল](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=bn):

| থিঙ্কিং লেভেল | টোকেনের ব্যবহার | কখন ব্যবহার হবে |
| --- | --- | --- |
| `low` | সবচেয়ে কম টোকেন, সবচেয়ে কম লেটেন্সি | সহজ টাস্ক এবং খরচ-সংবেদনশীল কাজ। এছাড়াও, বিশ্লেষণ ও লেখার মতো কাজ যেগুলির জন্য খুব বেশি চিন্তাভাবনা করতে হয় না, সেগুলিও করতে পারে। কঠিন টাস্কের ক্ষেত্রে কোয়ালিটি খারাপ হতে পারে। |
| `medium` (ডিফল্ট) | ভারসাম্য রেখে | জটিল কোড ও এজেন্টিক ব্যবহারের কেস সহ বেশিরভাগ টাস্কের জন্য সাজেস্ট করা হয়। |
| `high` | সবচেয়ে বেশি টোকেন, সবচেয়ে ধীরগতির প্রথম টোকেন | জটিল রিজনিং, কঠিন অঙ্ক ও বিজ্ঞান এবং সবচেয়ে কঠিন কোড বা এজেন্ট টাস্ক। দীর্ঘ আউটপুটের জন্য দীর্ঘ ডিকোড সহ ভালভাবে পেয়ার করে। |

তিনটি লেভেলেই আপনার মূল্যায়ন রান করুন, যেখানে `max_output_tokens`-এর মান বেশি হবে, যাতে সীমা উত্তরকে ছোট না করে দেয়। তারপর, আপনার কোয়ালিটি বার পূরণ করে এমন সবচেয়ে কম `thinking_level` বেছে নিন।

## মাইগ্রেশন চেকলিস্ট

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### gemini-4-argon-এ মাইগ্রেট করুন

- **মডেল আইডি আপডেট করুন:** আপনার মডেল স্ট্রিং পরিবর্তন করে `gemini-4-argon` করুন।
- **স্পষ্টভাবে `max_output_tokens` সেট করুন:** স্ট্রিমিং ও SDK কলের জন্য ডিফল্ট হল 64K এবং নন-স্ট্রিমিং REST কলের জন্য 32K।
- **৩২ হাজারের কম ক্যাপ বাড়ান:** ৩২ হাজারের কম যেকোনও ক্যাপ অন্তত ৩২,৭৬৮ পর্যন্ত বাড়ান। টোকেন খরচ কমাতে `thinking_level` ব্যবহার করুন।
- **দীর্ঘ ডিকোড করার জন্য প্ল্যান:** অনুরোধ প্রতি ক্যাপের থেকে বেশি টাস্কের জন্য, লেটেস্ট SDK ব্যবহার করুন বা `continuation_token` লুপ যোগ করুন।
- **`thinking_budget`-এর পরিবর্তে `thinking_level` ব্যবহার করুন:** `thinking_budget` এখনও কাজ করে এবং সবচেয়ে কাছের `thinking_level`-এ ম্যাপ করে, তবে এটি একটি সতর্কতা দেখায়। `low`, `medium` এবং `high`-এ আপনার ওয়ার্কলোড পরীক্ষা করুন।
- **স্পষ্ট কনটেক্সট ক্যাশিং থেকে সরে আসুন:** স্পষ্ট ক্যাশিং (`cachedContents` /
  `caches.create`) Gemini 4 Argon-এ কাজ করে না এবং একটি সমস্যা দেখায়।
  `GenerateContentConfig`-এ `cached_content` তৈরি করে বা পাস করে এমন কল সরিয়ে দিন।
  কমপক্ষে ৪,০৯৬ টোকেনের প্রম্পটের জন্য ডিফল্ট হিসেবে [ইমপ্লিসিট ক্যাশিং](https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=bn) চালু করা থাকে এবং ক্যাশে হিট হলে ক্যাশে করা ইনপুট টোকেনে ৯৫% ছাড় দেয়।
- **বন্ধ হয়ে যাওয়া প্যারামিটার সরিয়ে দিন:** অনুরোধ থেকে `temperature`, `top_p`, `top_k` এবং `candidate_count` সরিয়ে দিন। প্রদান করা হলে, স্যাম্পলিং প্যারামিটার এড়িয়ে যাওয়া হয়।
- **ক্লায়েন্ট টাইমআউট বাড়ান:** HTTP ক্লায়েন্ট টাইমআউট প্রতি কলে অন্তত ২০ মিনিট হিসেবে সেট করুন।
- **থট সিগনেচার সংরক্ষণ করা:** মাল্টি-টার্ন এবং ফাংশন-কলিং অনুরোধে [থট সিগনেচার](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=bn#signatures) সহ সম্পূর্ণ কথোপকথনের ইতিহাস পাস করুন।
- **আপনার আনুমানিক খরচ পর্যালোচনা করুন:** মডেলের প্রসেস করা প্রতিটি টোকেনের জন্য বিল করা হয়, যার মধ্যে ইন্টার্নাল টুল সিস্টেম নির্দেশাবলী এবং গ্রাউন্ডিং ব্যবহার করার সময় ফাংশন ডিক্লারেশন অন্তর্ভুক্ত থাকে ([দাম](#pricing) দেখুন)।

## দাম

৩০ নভেম্বর, ২০২৬ পর্যন্ত Gemini 4 Argon শুরুর দিকের দামে উপলভ্য:

- **ইনপুট টোকেন:** প্রতি ১ মিলিয়ন টোকেনে $২.০০ ($৪.০০, ১ ডিসেম্বর, ২০২৬ থেকে শুরু)
  - **ক্যাশে করা ইনপুট টোকেন:** ইমপ্লিসিট ক্যাশিং, ক্যাশে করা ইনপুটে ৯৫% ছাড় দেয়, যা প্রতি ১ মিলিয়ন টোকেনে $০.১০ ($০.২০, ১ ডিসেম্বর, ২০২৬ থেকে শুরু)।
- **থিঙ্কিং টোকেন সহ আউটপুট টোকেন:** প্রতি ১ মিলিয়ন টোকেনে $১০.০০ (১ ডিসেম্বর, ২০২৬ থেকে $২০.০০)

মডেল প্রসেস করে এমন প্রতিটি টোকেন গণনা করা হয় এবং বিল করা হয়, যার মধ্যে রয়েছে থিঙ্কিং টোকেন এবং ইন্টার্নাল টুল সিস্টেম নির্দেশাবলী এবং গ্রাউন্ডিং ব্যবহার করার সময় ফাংশন ঘোষণা। Grounding with Google Search-এর ক্ষেত্রেও কোয়েরি প্রতি বিল করা হয়।

Gemini 4 Argon ফ্রি টিয়ারে উপলভ্য নয়। মূল্যের সম্পূর্ণ টিয়ার দেখতে, [মূল্যের পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/pricing?hl=bn#gemini-4-argon) দেখুন।

## অন্যান্য মডেল

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8?hl=bn)
- [Gemini 3.6 Flash এবং 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=bn)
- [সব মডেল দেখুন](https://ai.google.dev/gemini-api/docs/models?hl=bn)

## এর পরে কী করতে হবে

- সম্পূর্ণ স্ট্রিমিং, রিকানেকশন ও টোকেন-কাউন্টিং প্যাটার্নের জন্য [লং ডিকোড ডেভেলপার গাইড](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=bn) পড়ুন।
- [থিঙ্কিং গাইড](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=bn) থেকে থিঙ্কিং লেভেল ও থট সামারি কীভাবে কাজ করে তা জানুন।
- [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)-তে Gemini 4 Argon টেস্ট করুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-27 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-27 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
