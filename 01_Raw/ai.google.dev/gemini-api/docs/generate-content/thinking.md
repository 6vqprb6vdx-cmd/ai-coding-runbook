---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=vi
fetched_at: 2026-11-02T07:19:05.616545+00:00
title: "T\u01b0 duy c\u1ee7a Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Tư duy của Gemini

[Các mô hình Gemini](https://ai.google.dev/gemini-api/docs/models?hl=vi) sử dụng "quy trình tư duy" nội bộ giúp cải thiện đáng kể khả năng suy luận và lập kế hoạch nhiều bước, khiến các mô hình này trở nên hiệu quả cao đối với các tác vụ phức tạp như lập trình, toán học nâng cao và phân tích dữ liệu.

Hướng dẫn này trình bày cách sử dụng khả năng tư duy của Gemini bằng Gemini API.

## Tạo nội dung có suy nghĩ

Việc bắt đầu một yêu cầu bằng mô hình tư duy cũng tương tự như mọi yêu cầu tạo nội dung khác. Điểm khác biệt chính nằm ở việc chỉ định một trong các [mô hình có hỗ trợ tư duy](#tools) trong trường `model`, như minh hoạ trong ví dụ về [tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi) sau đây:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Tóm tắt suy nghĩ

Bản tóm tắt suy nghĩ là phiên bản tóm tắt của những suy nghĩ thô của mô hình và cung cấp thông tin chi tiết về quy trình suy luận nội bộ của mô hình. Xin lưu ý rằng
mức độ và ngân sách suy nghĩ áp dụng cho suy nghĩ thô của mô hình chứ không áp dụng cho
bản tóm tắt suy nghĩ.

Bạn có thể bật tính năng tóm tắt suy nghĩ bằng cách đặt `includeThoughts` thành `true` trong cấu hình yêu cầu. Sau đó, bạn có thể truy cập vào bản tóm tắt bằng cách lặp lại `parts` của tham số `response` và kiểm tra giá trị boolean `thought`.

Dưới đây là ví dụ minh hoạ cách bật và truy xuất bản tóm tắt suy nghĩ mà không cần truyền trực tuyến. Ví dụ này sẽ trả về một bản tóm tắt suy nghĩ cuối cùng duy nhất cùng với phản hồi:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Sau đây là ví dụ về cách sử dụng quy trình suy nghĩ với tính năng truyền trực tuyến, trả về các bản tóm tắt liên tục, gia tăng trong quá trình tạo:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Tư duy kiểm soát

Theo mặc định, các mô hình Gemini sẽ tham gia vào quá trình suy nghĩ linh hoạt, tự động điều chỉnh
mức độ nỗ lực suy luận dựa trên độ phức tạp của yêu cầu từ người dùng.
Tuy nhiên, nếu có các hạn chế cụ thể về độ trễ hoặc yêu cầu mô hình tham gia vào quá trình suy luận sâu hơn bình thường, thì bạn có thể tuỳ ý sử dụng các tham số để kiểm soát hành vi suy nghĩ.

### Cấp độ tư duy (Gemini 4 và Gemini 3)

Tham số `thinkingLevel` (bắt buộc đối với Gemini 4 và nên dùng cho các mô hình Gemini 3) cho phép bạn kiểm soát hành vi suy luận. Gemini 4 (`gemini-4-argon`) hỗ trợ `low`, `medium` (mặc định) và `high`.

Bảng sau đây trình bày chi tiết các chế độ cài đặt `thinkingLevel` cho từng loại mô hình:

| Cấp độ tư duy | Gemini 3.8 Flash | Gemini 3.6 Flash | Gemini 4 Argon | Gemini 3.5 và 3.1 Flash-Lite | Hình ảnh Gemini 3.1 Flash-Lite | Gemini 3 Flash | Gemini Robotics ER 2 | Mô tả |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Không được hỗ trợ (lỗi) | Được hỗ trợ | Không được hỗ trợ (lỗi) | Được hỗ trợ (Mặc định) | Được hỗ trợ (Mặc định) | Được hỗ trợ | Được hỗ trợ | Phù hợp với chế độ cài đặt "không suy nghĩ" cho hầu hết các câu hỏi. Xin lưu ý rằng `minimal` không đảm bảo rằng tính năng suy nghĩ sẽ tắt. Mô hình có thể suy luận rất ít cho các tác vụ phức tạp. |
| **`low`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Không được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Giảm thiểu độ trễ và chi phí. |
| **`medium`** | Được hỗ trợ (Mặc định) | Được hỗ trợ (Mặc định) | Được hỗ trợ (Mặc định) | Được hỗ trợ | Không được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Tư duy cân bằng cho hầu hết các nhiệm vụ. |
| **`high`** | Được hỗ trợ (Động) | Được hỗ trợ (Động) | Được hỗ trợ (Động) | Được hỗ trợ (Động) | Được hỗ trợ (Động) | Được hỗ trợ (Mặc định, Động) | Được hỗ trợ (Mặc định, Động) | Tối đa hoá độ sâu suy luận. Mô hình có thể mất nhiều thời gian hơn đáng kể để đạt được mã thông báo đầu ra đầu tiên (không phải mã thông báo tư duy), nhưng đầu ra sẽ được suy luận cẩn thận hơn. |

Ví dụ sau đây cho thấy cách đặt mức độ tư duy.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Bạn không thể tắt tính năng suy nghĩ cho Gemini 4 Argon. Gemini 3 Flash và Flash-Lite cũng không hỗ trợ tắt hoàn toàn chế độ tư duy. Nếu bạn không chỉ định cấp độ tư duy, Gemini sẽ sử dụng cấp độ tư duy mặc định của mô hình (ví dụ: `"medium"` cho Gemini 4 Argon, Gemini 3.8 Flash và Gemini 3.6 Flash).

Các mô hình thuộc dòng Gemini 2.5 không hỗ trợ `thinkingLevel`; hãy sử dụng `thinkingBudget`.

### Giới hạn về mã thông báo và `max_output_tokens`

Tham số tạo [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=vi#v1beta.GenerationConfig) đặt số lượng mã thông báo tối đa mà một câu trả lời có thể tạo, bao gồm cả mã thông báo suy nghĩ.

Khi được đặt, tham số này đóng vai trò là giới hạn cứng do cơ sở hạ tầng thực thi mà không thay đổi cách mô hình phân bổ ngân sách suy nghĩ (`thinking_level`).

Nếu mô hình đạt đến giới hạn này trong khi suy luận, mô hình sẽ ngừng tạo bằng `finish_reason: MAX_TOKENS` và trả về kết quả bị cắt bớt hoặc trống (trong khi vẫn tính phí cho mọi token tư duy được tạo). Để giảm chi phí hoặc độ trễ mà không
cắt bớt câu trả lời, hãy giảm `thinking_level` (`low` hoặc `medium`) thay vì
đặt `max_output_tokens` nhỏ.

Đối với các mô hình Gemini 4 (`gemini-4-argon`), hãy lưu ý những giới hạn sau về ngữ cảnh và đầu ra:

- **Cửa sổ ngữ cảnh 1 triệu token dùng chung:** Token đầu vào, token suy nghĩ và token đầu ra dùng chung một cửa sổ ngữ cảnh 1 triệu token (`1,048,576` token). Nếu các mã thông báo đầu vào cộng với `max_output_tokens` vượt quá 1.048.576 mã thông báo, API sẽ tự động giới hạn số lượng mã thông báo đầu ra ở khoảng trống còn lại trong cửa sổ ngữ cảnh (`1,048,576` trừ đi các mã thông báo đầu vào).
- **Giới hạn đầu ra cho mỗi yêu cầu (64K đối với yêu cầu truyền trực tuyến / 32K đối với yêu cầu không truyền trực tuyến) và giải mã dài (tối đa 1 triệu token):** Một yêu cầu truyền trực tuyến duy nhất (`streamGenerateContent`) trả về tối đa `65,536` token và một yêu cầu không truyền trực tuyến duy nhất (`generateContent`) trả về tối đa `32,768` token. Để tạo vượt quá giới hạn cho mỗi yêu cầu (tối đa `1,048,576` mã trừ đi dữ liệu đầu vào), hãy đặt `max_output_tokens` cao hơn giới hạn. Theo mặc định, các SDK Google GenAI mới nhất sẽ tự động tiếp tục qua các bước nhảy (`automatic_continuation=True`) hoặc bạn có thể chạy vòng lặp ứng dụng bằng cách sử dụng `continuation_token` được trả về khi một bước nhảy dừng lại bằng `finish_reason: "CONTINUATION"`. Xem phần [Giải mã dài](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=vi) để biết các ví dụ về mã.

### Ngân sách tư duy

Tham số `thinkingBudget`, được giới thiệu cùng với dòng mô hình Gemini 2.5, hướng dẫn
mô hình về số lượng token tư duy cụ thể cần sử dụng để suy luận.

Sau đây là thông tin chi tiết về cấu hình `thinkingBudget` cho từng loại mô hình.
Bạn có thể tắt tính năng suy nghĩ bằng cách đặt `thinkingBudget` thành 0.
Việc đặt `thinkingBudget` thành -1 sẽ bật **tư duy linh hoạt**, nghĩa là mô hình sẽ điều chỉnh ngân sách dựa trên độ phức tạp của yêu cầu.

| Mô hình | Chế độ cài đặt mặc định (Chưa đặt ngân sách suy nghĩ) | Phạm vi | Tắt tính năng tư duy | Bật tính năng tư duy linh hoạt |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Tư duy linh hoạt | `128` đến `32768` | Không áp dụng: Không thể tắt tính năng suy nghĩ | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash Preview** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash Lite** | Mô hình không suy nghĩ | `512` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Bản xem trước của 2.5 Flash Lite** | Mô hình không suy nghĩ | `512` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |
| **Bản xem trước tính năng âm thanh gốc của 2.5 Flash Live (09-2025)** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

Tuỳ thuộc vào câu lệnh, mô hình có thể vượt quá hoặc không đạt đến ngân sách mã thông báo.

## Chữ ký suy nghĩ

Gemini API không có trạng thái, vì vậy, mô hình sẽ xử lý từng yêu cầu API một cách độc lập và không có quyền truy cập vào bối cảnh suy nghĩ từ các lượt trước trong các lượt tương tác nhiều lượt.

Để duy trì bối cảnh tư duy trong các lượt tương tác nhiều lượt, Gemini trả về chữ ký tư duy. Đây là các biểu thị được mã hoá của quy trình tư duy nội bộ của mô hình.

- **Các mô hình Gemini 2.5** trả về chữ ký suy nghĩ khi bạn bật tính năng suy nghĩ và yêu cầu bao gồm [lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#thinking), cụ thể là [khai báo hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#step-2).
- **Các mô hình Gemini 4 và Gemini 3** có thể trả về chữ ký suy nghĩ cho tất cả các loại [phần](https://ai.google.dev/api/caching?hl=vi#Part). Bạn nên luôn truyền tất cả chữ ký trở lại như đã nhận, nhưng đây là *yêu cầu bắt buộc* đối với chữ ký gọi hàm. Hãy đọc trang [Chữ ký tư duy](https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=vi) để tìm hiểu thêm.

Những hạn chế khác về việc sử dụng cần cân nhắc khi gọi hàm bao gồm:

- Chữ ký được trả về từ mô hình trong các phần khác của phản hồi,
  ví dụ: gọi hàm hoặc phần văn bản.
  [Trả về toàn bộ phản hồi](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#step-4) cùng tất cả các phần cho mô hình trong các lượt tiếp theo.
- Đừng nối các phần có chữ ký với nhau.
- Đừng hợp nhất một phần có chữ ký với một phần không có chữ ký.

## Giá

Khi chế độ suy nghĩ được bật, giá của câu trả lời là tổng của token đầu ra và token tư duy. Bạn có thể lấy tổng số mã thông báo tư duy được tạo từ trường `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Mô hình tư duy tạo ra các suy nghĩ đầy đủ để cải thiện chất lượng của câu trả lời cuối cùng, sau đó đưa ra [bản tóm tắt](#summaries) để cung cấp thông tin chi tiết về quá trình tư duy. Vì vậy, giá được tính dựa trên số lượng mã thông báo đầy đủ mà mô hình cần tạo để tạo bản tóm tắt, mặc dù chỉ có bản tóm tắt được xuất ra từ API.

Bạn có thể tìm hiểu thêm về mã thông báo trong hướng dẫn [Đếm mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi).

## Các phương pháp hay nhất

Phần này đưa ra một số hướng dẫn để sử dụng mô hình tư duy một cách hiệu quả.
Như thường lệ, bạn nên làm theo
[hướng dẫn và các phương pháp hay nhất về câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi)
để đạt được kết quả tốt nhất.

### Gỡ lỗi và điều hướng

- **Xem xét lập luận**: Khi bạn không nhận được câu trả lời như mong đợi từ các mô hình tư duy, bạn có thể phân tích kỹ lưỡng bản tóm tắt suy nghĩ của Gemini.
  Bạn có thể xem cách mô hình phân tích nhiệm vụ và đưa ra kết luận, đồng thời sử dụng thông tin đó để điều chỉnh cho ra kết quả chính xác.
- **Đưa ra hướng dẫn về lập luận**: Nếu muốn có một kết quả đặc biệt dài, bạn có thể đưa ra hướng dẫn trong câu lệnh để hạn chế [lượng tư duy](#set-budget) mà mô hình sử dụng. Điều này cho phép bạn dành nhiều mã thông báo đầu ra hơn cho câu trả lời của mình.

### Độ phức tạp của nhiệm vụ

- **Nhiệm vụ dễ dàng (Có thể TẮT tính năng tư duy):** Đối với những yêu cầu đơn giản không đòi hỏi khả năng suy luận phức tạp, chẳng hạn như truy xuất thông tin hoặc phân loại, bạn không cần phải tư duy. Ví dụ:
  - "DeepMind được thành lập ở đâu?"
  - "Email này yêu cầu họp hay chỉ cung cấp thông tin?"
- **Việc có độ phức tạp trung bình (Mặc định/Cần suy nghĩ một chút):** Nhiều yêu cầu phổ biến cần được xử lý từng bước hoặc cần được hiểu sâu hơn. Gemini có thể linh hoạt sử dụng khả năng tư duy cho các nhiệm vụ như:
  - So sánh quá trình quang hợp và quá trình trưởng thành.
  - So sánh và đối chiếu xe điện và xe lai điện.
- **Nhiệm vụ khó (Khả năng tư duy tối đa):** Đối với những thử thách thực sự phức tạp, chẳng hạn như giải các bài toán phức tạp hoặc nhiệm vụ lập trình, bạn nên đặt ngân sách tư duy cao. Những loại nhiệm vụ này đòi hỏi mô hình phải vận dụng
  toàn bộ khả năng suy luận và lập kế hoạch, thường
  bao gồm nhiều bước nội bộ trước khi đưa ra câu trả lời. Ví dụ:
  - Giải bài toán 1 trong kỳ thi AIME 2025: Tìm tổng của tất cả các cơ số nguyên b > 9 sao cho 17b là ước số của 97b.
  - Viết mã Python cho một ứng dụng web trực quan hoá dữ liệu thị trường chứng khoán theo thời gian thực, bao gồm cả quy trình xác thực người dùng. Hãy làm cho nó hiệu quả nhất có thể.

## Các mô hình, công cụ và chức năng được hỗ trợ

Các tính năng tư duy được hỗ trợ trên tất cả các mô hình thuộc dòng 4, 3 và 2.5.
Bạn có thể tìm thấy tất cả các chức năng của mô hình trên trang [tổng quan về mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi).

Mô hình tư duy hoạt động với tất cả các công cụ và tính năng của Gemini. Điều này cho phép các mô hình tương tác với các hệ thống bên ngoài, thực thi mã hoặc truy cập thông tin theo thời gian thực, kết hợp kết quả vào quá trình suy luận và phản hồi cuối cùng của chúng.

Bạn có thể thử các ví dụ về cách sử dụng công cụ với các mô hình tư duy trong [Sổ tay tư duy][Colab].

## Tiếp theo là gì?

- Thông tin về phạm vi hỗ trợ có trong hướng dẫn [Khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi#thinking) của chúng tôi.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-14 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-14 UTC."],[],[]]
