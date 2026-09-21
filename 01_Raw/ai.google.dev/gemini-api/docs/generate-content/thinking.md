---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=vi
fetched_at: 2026-09-21T05:57:31.955424+00:00
title: "T\u01b0 duy c\u1ee7a Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Tư duy của Gemini

[Các mô hình thuộc dòng Gemini 3 và 2.5](https://ai.google.dev/gemini-api/docs/models?hl=vi) sử dụng một "quy trình tư duy" nội bộ giúp cải thiện đáng kể khả năng suy luận và lập kế hoạch nhiều bước, khiến các mô hình này trở nên hiệu quả cao đối với các nhiệm vụ phức tạp như lập trình, toán học nâng cao và phân tích dữ liệu.

Hướng dẫn này cho bạn biết cách khai thác khả năng tư duy của Gemini bằng Gemini API.

## Tạo nội dung bằng tư duy

Việc bắt đầu một yêu cầu bằng mô hình tư duy cũng tương tự như mọi yêu cầu tạo nội dung khác. Điểm khác biệt chính nằm ở việc chỉ định một trong các [mô hình có hỗ trợ tư duy](#supported-models) trong trường `model`, như minh hoạ trong ví dụ [tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#text-input) sau đây:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  model := "gemini-3.6-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
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
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Tóm tắt suy nghĩ

Bản tóm tắt suy nghĩ là phiên bản tóm tắt về những suy nghĩ thô của mô hình và cung cấp thông tin chi tiết về quy trình suy luận nội bộ của mô hình. Xin lưu ý rằng các cấp độ và ngân sách tư duy áp dụng cho suy nghĩ thô của mô hình chứ không áp dụng cho bản tóm tắt suy nghĩ.

Bạn có thể bật tính năng tóm tắt suy nghĩ bằng cách đặt `includeThoughts` thành `true` trong cấu hình yêu cầu. Sau đó, bạn có thể truy cập vào bản tóm tắt bằng cách lặp lại thông số `parts` của `response` và kiểm tra boolean `thought`.

Dưới đây là ví dụ minh hoạ cách bật và truy xuất bản tóm tắt ý tưởng mà không cần truyền trực tuyến. Cách này sẽ trả về một bản tóm tắt ý tưởng cuối cùng duy nhất cùng với phản hồi:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  model := "gemini-3.6-flash"
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

Sau đây là ví dụ về cách sử dụng tính năng suy nghĩ bằng cách phát trực tuyến, tính năng này trả về các bản tóm tắt tăng dần, liên tục trong quá trình tạo:

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  model := "gemini-3.6-flash"

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

Theo mặc định, các mô hình Gemini tham gia vào quá trình tư duy linh hoạt bằng cách tự động điều chỉnh mức độ nỗ lực suy luận dựa trên độ phức tạp của yêu cầu của người dùng.
Tuy nhiên, nếu có các hạn chế cụ thể về độ trễ hoặc yêu cầu mô hình tham gia vào quá trình suy luận sâu hơn bình thường, thì bạn có thể tuỳ ý sử dụng các tham số để kiểm soát hành vi suy nghĩ.

### Cấp độ tư duy (Gemini 3)

Tham số `thinkingLevel` (nên dùng cho các mô hình Gemini 3 trở lên) cho phép bạn kiểm soát hành vi suy luận.

Bảng sau đây trình bày chi tiết các chế độ cài đặt `thinkingLevel` cho từng loại mô hình:

| Cấp độ tư duy | Gemini 3.6 và 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 và 3.1 Flash-Lite | Hình ảnh Gemini 3.1 Flash-Lite | Gemini 3 Flash | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Được hỗ trợ | Không được hỗ trợ | Được hỗ trợ (Mặc định) | Được hỗ trợ (Mặc định) | Được hỗ trợ | Phù hợp với chế độ cài đặt "không suy nghĩ" cho hầu hết các cụm từ tìm kiếm. Xin lưu ý rằng `minimal` không đảm bảo rằng tính năng suy nghĩ sẽ tắt, mô hình có thể suy luận rất ít cho các tác vụ phức tạp. |
| **`low`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Không được hỗ trợ | Được hỗ trợ | Giảm thiểu độ trễ và chi phí. |
| **`medium`** | Được hỗ trợ (Mặc định) | Được hỗ trợ | Được hỗ trợ | Không được hỗ trợ | Được hỗ trợ | Tư duy cân bằng cho hầu hết các nhiệm vụ. |
| **`high`** | Được hỗ trợ (Động) | Được hỗ trợ (Mặc định, Động) | Được hỗ trợ (Động) | Được hỗ trợ (Động) | Được hỗ trợ (Mặc định, Động) | Tối đa hoá độ sâu suy luận. Mô hình có thể mất nhiều thời gian hơn đáng kể để đạt được mã thông báo đầu tiên (không phải mã thông báo tư duy), nhưng đầu ra sẽ được suy luận cẩn thận hơn. |

Ví dụ sau đây cho thấy cách thiết lập cấp độ tư duy.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  model := "gemini-3.6-flash"
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Bạn không thể tắt tính năng suy nghĩ cho Gemini 3.1 Pro. Gemini 3 Flash và Flash-Lite cũng không hỗ trợ tính năng tắt hoàn toàn chế độ tư duy. Nếu bạn không chỉ định cấp độ tư duy, Gemini sẽ sử dụng cấp độ tư duy mặc định của các mô hình Gemini 3 (ví dụ: `"high"` cho Gemini 3.1 Pro và `"medium"` cho Gemini 3.5 Flash).

Các mô hình Gemini 2.5 không hỗ trợ `thinkingLevel`; thay vào đó, hãy sử dụng `thinkingBudget`.

### Ngân sách tư duy

Tham số `thinkingBudget` (được giới thiệu cùng với dòng Gemini 2.5) hướng dẫn mô hình về số lượng mã thông báo tư duy cụ thể cần sử dụng để suy luận.

Sau đây là `thinkingBudget` thông tin chi tiết về cấu hình cho từng loại mô hình.
Bạn có thể tắt tính năng suy nghĩ bằng cách đặt `thinkingBudget` thành 0.
Việc đặt `thinkingBudget` thành -1 sẽ bật **tư duy linh hoạt**, tức là mô hình sẽ điều chỉnh ngân sách dựa trên độ phức tạp của yêu cầu.

| Mô hình | Chế độ cài đặt mặc định (Chưa đặt ngân sách suy nghĩ) | Phạm vi | Tắt tính năng tư duy | Bật tính năng tư duy linh hoạt |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Tư duy linh hoạt | `128` đến `32768` | Không áp dụng: Không tắt được tính năng tư duy | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash Preview** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash Lite** | Mô hình không suy nghĩ | `512` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Mô hình không suy nghĩ | `512` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |
| **2.5 Flash Bản xem trước âm thanh gốc trực tiếp (tháng 9 năm 2025)** | Tư duy linh hoạt | `0` đến `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Mặc định) |

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

Tuỳ thuộc vào câu lệnh, mô hình có thể vượt quá hoặc không đạt được hạn mức mã thông báo.

## Chữ ký của suy nghĩ

Gemini API là API không trạng thái, vì vậy mô hình này xử lý độc lập mọi yêu cầu API và không có quyền truy cập vào ngữ cảnh suy nghĩ từ các lượt tương tác trước đó trong các lượt tương tác nhiều lượt.

Để duy trì bối cảnh tư duy trong các lượt tương tác nhiều lượt, Gemini trả về chữ ký tư duy. Đây là các biểu thị được mã hoá của quy trình tư duy nội bộ của mô hình.

- **Các mô hình Gemini 2.5** trả về chữ ký suy nghĩ khi bạn bật tính năng suy nghĩ và yêu cầu bao gồm [lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#thinking), cụ thể là [khai báo hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#step-2).
- **Các mô hình Gemini 3** có thể trả về chữ ký suy nghĩ cho tất cả các loại [phần](https://ai.google.dev/api/caching?hl=vi#Part).
  Bạn nên luôn truyền tất cả chữ ký trở lại như đã nhận, nhưng đây là *yêu cầu bắt buộc* đối với chữ ký gọi hàm. Hãy đọc trang [Chữ ký tư duy](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=vi) để tìm hiểu thêm.

Những hạn chế khác về việc sử dụng cần cân nhắc khi gọi hàm bao gồm:

- Chữ ký được trả về từ mô hình trong các phần khác của phản hồi, ví dụ: gọi hàm hoặc các phần văn bản.
  [Trả về toàn bộ câu trả lời](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#step-4) với tất cả các phần cho mô hình trong các lượt tiếp theo.
- Đừng nối các phần có chữ ký với nhau.
- Không được hợp nhất một phần có chữ ký với một phần không có chữ ký.

## Giá

Khi chế độ suy nghĩ được bật, giá phản hồi là tổng số mã thông báo đầu ra và mã thông báo suy nghĩ. Bạn có thể lấy tổng số mã thông báo tư duy đã tạo từ trường `thoughtsTokenCount`.

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

Các mô hình tư duy tạo ra những suy nghĩ đầy đủ để cải thiện chất lượng của câu trả lời cuối cùng, sau đó đưa ra [bản tóm tắt](#summaries) để cung cấp thông tin chi tiết về quy trình tư duy. Vì vậy, giá được tính dựa trên số lượng mã thông báo đầy đủ mà mô hình cần tạo để tạo bản tóm tắt, mặc dù chỉ có bản tóm tắt được xuất ra từ API.

Bạn có thể tìm hiểu thêm về mã thông báo trong hướng dẫn [Đếm mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi).

## Các phương pháp hay nhất

Phần này bao gồm một số hướng dẫn để sử dụng hiệu quả các mô hình tư duy.
Như thường lệ, việc làm theo [hướng dẫn và các phương pháp hay nhất về câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi) sẽ giúp bạn đạt được kết quả tốt nhất.

### Gỡ lỗi và điều hướng

- **Xem xét suy luận**: Khi không nhận được câu trả lời như mong đợi từ các mô hình tư duy, bạn có thể phân tích kỹ lưỡng bản tóm tắt suy nghĩ của Gemini.
  Bạn có thể xem cách AI phân tích nhiệm vụ và đi đến kết luận, đồng thời sử dụng thông tin đó để điều chỉnh cho phù hợp với kết quả mong muốn.
- **Đưa ra hướng dẫn về suy luận**: Nếu muốn nhận được kết quả đặc biệt dài, bạn có thể đưa ra hướng dẫn trong câu lệnh để hạn chế [lượng tư duy](#set-budget) mà mô hình sử dụng. Điều này cho phép bạn dành nhiều mã thông báo đầu ra hơn cho câu trả lời của mình.

### Độ phức tạp của nhiệm vụ

- **Nhiệm vụ dễ dàng (Có thể TẮT tính năng tư duy):** Đối với những yêu cầu đơn giản không đòi hỏi khả năng suy luận phức tạp, chẳng hạn như truy xuất thông tin thực tế hoặc phân loại, bạn không cần phải tư duy. Ví dụ:
  - "DeepMind được thành lập ở đâu?"
  - "Email này có yêu cầu tổ chức cuộc họp hay chỉ cung cấp thông tin?"
- **Các yêu cầu ở mức trung bình (Mặc định/Cần suy nghĩ):** Nhiều yêu cầu phổ biến cần được xử lý từng bước hoặc cần hiểu biết sâu sắc hơn. Gemini có thể linh hoạt sử dụng khả năng tư duy cho các nhiệm vụ như:
  - So sánh quang hợp và quá trình trưởng thành.
  - So sánh và đối chiếu xe điện và xe lai điện.
- **Nhiệm vụ khó (Khả năng tư duy tối đa):** Đối với những thử thách thực sự phức tạp, chẳng hạn như giải các bài toán phức tạp hoặc nhiệm vụ lập trình, bạn nên đặt ngân sách tư duy cao. Những loại nhiệm vụ này đòi hỏi mô hình phải sử dụng toàn bộ khả năng suy luận và lập kế hoạch, thường liên quan đến nhiều bước nội bộ trước khi đưa ra câu trả lời. Ví dụ:
  - Giải bài toán 1 trong AIME 2025: Tìm tổng của tất cả các cơ số nguyên b > 9 sao cho 17b là ước số của 97b.
  - Viết mã Python cho một ứng dụng web trực quan hoá dữ liệu thị trường chứng khoán theo thời gian thực, bao gồm cả xác thực người dùng. Hãy làm cho nó hiệu quả nhất có thể.

## Các mô hình, công cụ và chức năng được hỗ trợ

Các tính năng tư duy được hỗ trợ trên tất cả các mô hình thuộc dòng 3 và 2.5.
Bạn có thể tìm thấy tất cả các chức năng của mô hình trên trang [tổng quan về mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi).

Các mô hình tư duy hoạt động với tất cả các công cụ và chức năng của Gemini. Điều này cho phép các mô hình tương tác với các hệ thống bên ngoài, thực thi mã hoặc truy cập thông tin theo thời gian thực, kết hợp kết quả vào quá trình suy luận và phản hồi cuối cùng của chúng.

Bạn có thể thử các ví dụ về cách sử dụng công cụ với mô hình tư duy trong [Thinking cookbook][Colab].

## Tiếp theo là gì?

- Thông tin về phạm vi hỗ trợ có trong hướng dẫn [Khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi#thinking) của chúng tôi.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-12 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-12 UTC."],[],[]]
