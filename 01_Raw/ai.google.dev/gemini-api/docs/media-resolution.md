---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=bn
fetched_at: 2026-10-26T05:44:35.551523+00:00
title: "\u09ae\u09bf\u09a1\u09bf\u09df\u09be\u09b0 \u09b0\u09c7\u099c\u09cb\u09b2\u09bf\u0989\u09b6\u09a8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# মিডিয়ার রেজোলিউশন

`media_resolution` প্যারামিটার নিয়ন্ত্রণ করে যে Gemini API কীভাবে ছবি, ভিডিও, অডিও এবং PDF ডকুমেন্টের মতো মিডিয়া ইনপুট প্রসেস করে। এটি মিডিয়া ইনপুটের জন্য বরাদ্দ করা **টোকেনের সর্বাধিক সংখ্যা** নির্ধারণ করে, যা আপনাকে লেটেন্সি এবং খরচের বিপরীতে উত্তরের কোয়ালিটির ভারসাম্য বজায় রাখতে সাহায্য করে। ভিজ্যুয়াল ও ডকুমেন্ট ইনপুট রেজোলিউশন সেটিংসের উপর ভিত্তি করে টোকেন বরাদ্দ করে, অডিও ইনপুট সব রেজোলিউশন লেভেল জুড়ে প্রতি সেকেন্ডে একটি নির্দিষ্ট হারে টোকেনাইজ করা হয়। বিভিন্ন সেটিংস, ডিফল্ট ভ্যালু এবং টোকেনের সাথে সেগুলি কীভাবে সম্পর্কিত তা জানতে, [টোকেন কাউন্ট](#token-counts) বিভাগ দেখুন।

আপনার অনুরোধের (Gemini 4 ও Gemini 3 মডেল) মধ্যে থাকা আলাদা আলাদা মিডিয়া অবজেক্টের (কন্টেন্ট আইটেম) জন্য মিডিয়া রেজোলিউশন কনফিগার করতে পারবেন।

## প্রতি কন্টেন্ট-আইটেম মিডিয়া রেজোলিউশন (Gemini 4 ও Gemini 3 মডেল)

Gemini 4 এবং Gemini 3 মডেল আপনাকে অনুরোধের মধ্যে আলাদা আলাদা মিডিয়া অবজেক্টের জন্য মিডিয়া রেজোলিউশন সেট করার অনুমতি দেয়, যা টোকেন ব্যবহারের সূক্ষ্ম অপ্টিমাইজেশন অফার করে। আপনি একটি অনুরোধে রেজোলিউশন লেভেল মিক্স করতে পারবেন। যেমন, জটিল ডায়াগ্রামের জন্য হাই রেজোলিউশন এবং সাধারণ প্রাসঙ্গিক ছবির জন্য লো রেজোলিউশন ব্যবহার করা।

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### বিশ্রাম

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## উপলভ্য রেজোলিউশন ভ্যালু

Gemini API মিডিয়া রেজোলিউশনের জন্য নিম্নলিখিত লেভেলগুলি নির্ধারণ করে:

- `unspecified`: ডিফল্ট সেটিং। Gemini 4/3 এবং আগের Gemini মডেলের মধ্যে এই লেভেলের টোকেন সংখ্যায় উল্লেখযোগ্য পার্থক্য রয়েছে।
- `low`: টোকেনের সংখ্যা কম, ফলে প্রসেসিং দ্রুত হয় এবং খরচও কম হয়, তবে এতে কম বিবরণ থাকে।
- `medium`: বিবরণ, খরচ ও লেটেন্সির মধ্যে ব্যালেন্স।
- `high`: টোকেনের সংখ্যা বেশি, মডেলের কাজ করার জন্য আরও বেশি বিবরণ প্রদান করে, তবে এর ফলে লেটেন্সি ও খরচ বেড়ে যায়।
- `ultra_high` (প্রতিটি কন্টেন্ট আইটেমের জন্য): টোকেনের সর্বোচ্চ সংখ্যা, [কম্পিউটার ব্যবহারের](https://ai.google.dev/gemini-api/docs/computer-use?hl=bn) মতো নির্দিষ্ট ব্যবহারের ক্ষেত্রে প্রয়োজন।

মনে রাখবেন, বেশিরভাগ ব্যবহারের ক্ষেত্রে `high` সবচেয়ে ভালো পারফর্ম্যান্স প্রদান করে।

এই প্রতিটি লেভেলের জন্য তৈরি করা টোকেনের সঠিক সংখ্যা **মিডিয়ার ধরন** (ছবি, ভিডিও, অডিও, PDF) এবং **মডেল ভার্সন**, উভয়ের উপর নির্ভর করে।

## টোকেনের সংখ্যা

নিচের সারণীতে প্রতিটি `media_resolution` ভ্যালু এবং মডেল ফ্যামিলি প্রতি মিডিয়ার ধরনের জন্য আনুমানিক টোকেন কাউন্টের সংক্ষিপ্ত বিবরণ দেওয়া হল।

**Gemini 4 ও Gemini 3 মডেল**

| MediaResolution | ছবি | ভিডিও | অডিও | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (ডিফল্ট) | 1120 | 70 | ২৫ (প্রতি সেকেন্ডে) | 560 |
| `low` | 280 | 70 | ২৫ (প্রতি সেকেন্ডে) | ২৮০ + নেটিভ টেক্সট |
| `medium` | 560 | 70 | ২৫ (প্রতি সেকেন্ডে) | ৫৬০ + নেটিভ টেক্সট |
| `high` | 1120 | 280 | ২৫ (প্রতি সেকেন্ডে) | 1120 + Native Text |
| `ultra_high` | 2240 | প্রযোজ্য নয় | প্রযোজ্য নয় | প্রযোজ্য নয় |

## সঠিক রেজোলিউশন বেছে নেওয়া

- **ডিফল্ট (`unspecified`):** ডিফল্ট দিয়ে শুরু করুন। সবচেয়ে সাধারণ ব্যবহারের ক্ষেত্রে কোয়ালিটি, লেটেন্সি ও খরচের মধ্যে ভাল ব্যালেন্স বজায় রাখার জন্য এটি টিউন করা হয়েছে।
- **`low`:** এমন পরিস্থিতিতে ব্যবহার করুন যেখানে খরচ এবং লেটেন্সি সবচেয়ে গুরুত্বপূর্ণ এবং সূক্ষ্ম বিবরণ কম গুরুত্বপূর্ণ।
- **`medium` / `high`:** মিডিয়ার মধ্যে জটিল বিবরণ বোঝার প্রয়োজন হলে রেজোলিউশন বাড়ান। জটিল ভিজ্যুয়াল বিশ্লেষণ, চার্ট পড়া বা ঘন ডকুমেন্ট বোঝার জন্য প্রায়ই এটির প্রয়োজন হয়।
- **`ultra_high`** - শুধুমাত্র কন্টেন্ট আইটেম পিছু সেটিংয়ের জন্য উপলভ্য। কম্পিউটার ব্যবহার বা যেখানে টেস্টিং `high`-এর থেকে স্পষ্ট উন্নতি দেখায়, এমন নির্দিষ্ট ব্যবহারের ক্ষেত্রে সাজেস্ট করা হয়।
- **কন্টেন্ট-আইটেম প্রতি কন্ট্রোল (Gemini 4 এবং Gemini 3):** টোকেন ব্যবহার অপ্টিমাইজ করে। যেমন, একাধিক ছবি সহ প্রম্পটে, জটিল ডায়াগ্রামের জন্য `high` এবং তুলনামূলক সহজ প্রাসঙ্গিক ছবির জন্য `low` বা `medium` ব্যবহার করুন।

**সাজেস্ট করা সেটিংস**

নিচে প্রতিটি কাজ করে এমন মিডিয়ার ধরনের জন্য সাজেস্ট করা মিডিয়া রেজোলিউশন সেটিংসের তালিকা দেওয়া হল।

| মিডিয়ার ধরন | সাজেস্ট করা সেটিং | সর্বাধিক টোকেন | ব্যবহার সংক্রান্ত নির্দেশিকা |
| --- | --- | --- | --- |
| **ছবি** | `high` | 1120 | সর্বাধিক কোয়ালিটি নিশ্চিত করতে, বেশিরভাগ ছবি বিশ্লেষণ সংক্রান্ত টাস্কের জন্য সাজেস্ট করা হয়। |
| **পিডিএফ** | `medium` | 560 | ডকুমেন্ট বোঝার জন্য সবচেয়ে উপযুক্ত; কোয়ালিটি সাধারণত `medium`-এ স্যাচুরেট করে। `high` বাড়ালে, সাধারণ ডকুমেন্টের ক্ষেত্রে OCR ফলাফল খুব কমই উন্নত হয়। |
| **ভিডিও** (সাধারণ) | `low` (বা `medium`) | ৭০ (প্রতি ফ্রেম) | **মনে রাখবেন:** ভিডিওর ক্ষেত্রে, `low` ও `medium` সেটিংসকে একই রকম (৭০টি টোকেন) হিসেবে বিবেচনা করা হয়, যাতে প্রসঙ্গ ব্যবহারের ক্ষেত্রে অপ্টিমাইজ করা যায়। বেশিরভাগ অ্যাকশন শনাক্তকরণ ও বিবরণ সংক্রান্ত টাস্কের জন্য এটি যথেষ্ট। |
| **ভিডিও** (টেক্সট-বহুল) | `high` | ২৮০ (প্রতি ফ্রেম) | ব্যবহারের ক্ষেত্রে ঘন টেক্সট (OCR) বা ভিডিও ফ্রেমের মধ্যে ছোট বিবরণ পড়ার প্রয়োজন হলেই শুধু এটি প্রয়োজন। |
| **অডিও** | `unspecified` (ডিফল্ট) | ২৫ (প্রতি সেকেন্ডে) | সব কাজ করে এমন রেজোলিউশন সেটিংস (`unspecified`, `low`, `medium` এবং `high`) জুড়ে অডিও প্রতি সেকেন্ডে ২৫টি টোকেনের নির্দিষ্ট রেটে টোকেনাইজ করা হয়। |

কোয়ালিটি, লেটেন্সি ও খরচের মধ্যে সবচেয়ে ভালো ব্যালেন্স খুঁজে পেতে, আপনার অ্যাপ্লিকেশনে বিভিন্ন রেজোলিউশন সেটিংসের প্রভাব সবসময় পরীক্ষা করে দেখুন ও মূল্যায়ন করুন।

## ভিডিও প্রসেসিং মোডের সাথে সম্পর্ক

`media_resolution` এবং প্রসেসিং প্যারামিটার ভিডিও ইনপুটের বিভিন্ন দিক কন্ট্রোল করে:

- `media_resolution` প্রতিটি ফ্রেমের **রেজোলিউশন** (ফ্রেম প্রতি টোকেনের সংখ্যা) নিয়ন্ত্রণ করে।
- `processing` / `media_processing` **ভিডিওর কোন কন্টেন্ট** কন্টেক্সটে লোড করা হবে তা নিয়ন্ত্রণ করে।

আপনি একই ভিডিও ইনপুটে দুটিই সেট করতে পারবেন। যেমন, আপনি কোনও দীর্ঘ ভিডিওর জন্য মোট টোকেন ব্যবহার কমাতে কম মিডিয়া রেজোলিউশন সহ এজেন্টিক প্রসেসিং ব্যবহার করতে পারেন।

ভিডিও প্রসেসিং মোড সম্পর্কে বিস্তারিত জানতে, [এজেন্টিক ভিডিও আন্ডারস্ট্যান্ডিং](https://ai.google.dev/gemini-api/docs/video-understanding?hl=bn#agentic-video-understanding) গাইড দেখুন।

## ভার্সন মানানসই হওয়ার সারাংশ

- `resolution`-কে স্বতন্ত্র কন্টেন্ট আইটেমে সেট করার সুবিধা **Gemini 4 ও Gemini 3 মডেলে উপলভ্য**।

## পরবর্তী ধাপ

- Gemini API-এর মাল্টিমডেল ক্ষমতা সম্পর্কে আরও জানুন
  [ছবি বুঝতে পারা](https://ai.google.dev/gemini-api/docs/image-understanding?hl=bn),
  [ভিডিও বুঝতে পারা](https://ai.google.dev/gemini-api/docs/video-understanding?hl=bn), [অডিও বুঝতে পারা](https://ai.google.dev/gemini-api/docs/audio?hl=bn),
  এবং [ডকুমেন্ট বুঝতে পারা](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn) সংক্রান্ত গাইডে।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
