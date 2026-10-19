---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=vi
fetched_at: 2026-10-19T05:32:40.659759+00:00
title: "T\u1ea1o nh\u1ea1c b\u1eb1ng Lyria 3.5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo nhạc bằng Lyria 3.5

Lyria 3.5 là nhóm mô hình tạo nhạc của Google, có sẵn thông qua Gemini API. Với Lyria 3.5, bạn có thể tạo âm thanh nổi 44, 1 kHz chất lượng cao từ câu lệnh bằng văn bản hoặc từ hình ảnh. Các mô hình này mang đến sự nhất quán về cấu trúc, bao gồm cả giọng hát, lời bài hát có dấu thời gian và bản phối nhạc cụ hoàn chỉnh.

Nhóm mô hình Lyria bao gồm:

| Mô hình | Mã kiểu máy | Phù hợp nhất cho | Thời lượng | Đầu ra |
| --- | --- | --- | --- | --- |
| **Đoạn video Lyria 3** | `lyria-3-clip-preview` | Đoạn video ngắn, video lặp lại, bản xem trước | 30 giây | MP3 |
| **Lyria 3.5** | `lyria-3.5` | Bài hát có thời lượng đầy đủ với các đoạn thơ, điệp khúc, cầu nối | Vài phút (có thể kiểm soát bằng câu lệnh) | MP3 |

Bạn có thể sử dụng cả hai mô hình bằng [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) mới, hỗ trợ các đầu vào đa phương thức (văn bản và hình ảnh) và tạo ra âm thanh **âm thanh nổi có độ trung thực cao 44,1 kHz**.

## Tạo đoạn nhạc

Mô hình Lyria 3 Clip luôn tạo một đoạn video dài **30 giây**. Để tạo một đoạn video, hãy gọi phương thức `interactions.create` bằng một câu lệnh văn bản. Phản hồi luôn bao gồm lời bài hát và cấu trúc bài hát được tạo cùng với âm thanh trong giản đồ `steps`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(InteractionsInput.of("A short instrumental acoustic guitar piece."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("music.mp3"), audioBytes);
}

interaction.outputText().ifPresent(lyrics -> System.out.println("Lyrics:\n" + lyrics));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3-clip-preview"),
            Input: interactions.NewInteractionsInput("A short instrumental acoustic guitar piece."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        audioBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("music.mp3", audioBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Lyrics:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Bạn có thể truy xuất dữ liệu nhạc đã tạo bằng cách sử dụng thuộc tính `interaction.output_audio`. Thuộc tính này trả về khối âm thanh được tạo gần đây nhất. Bạn cũng có thể truy xuất lời bài hát và cấu trúc của bài hát bằng cách sử dụng thuộc tính `interaction.output_text`. Để biết thông tin chi tiết về các thuộc tính tiện lợi, hãy xem bài viết [Tổng quan về các hoạt động tương tác](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi#convenience-properties).

## Tạo bài hát có thời lượng đầy đủ

Sử dụng mô hình `lyria-3.5` để tạo các bài hát dài vài phút. Mô hình Pro hiểu cấu trúc âm nhạc và có thể sáng tác các bản nhạc có đoạn thơ, điệp khúc và đoạn chuyển riêng biệt. Bạn có thể điều chỉnh thời lượng bằng cách chỉ định thời lượng trong câu lệnh (ví dụ: "tạo một bài hát dài 2 phút") hoặc bằng cách sử dụng [dấu thời gian](#timing) để xác định cấu trúc.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody."
}'
```

## Chọn định dạng đầu ra

Theo mặc định, các mô hình Lyria 3.5 tạo âm thanh ở định dạng **MP3**. Đối với Lyria 3.5, bạn cũng có thể yêu cầu đầu ra ở định dạng **WAV** bằng cách đặt `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A beautiful piano melody."))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A beautiful piano melody."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Phân tích cú pháp phản hồi

Phản hồi của Lyria 3.5 chứa nhiều khối nội dung trong giản đồ `steps`.
Các lượt tương tác trả về một chuỗi các bước, trong đó các bước `model_output` chứa nội dung được tạo.
Các khối nội dung văn bản chứa lời bài hát được tạo hoặc nội dung mô tả bằng JSON về cấu trúc bài hát.
Các khối nội dung có loại `audio` chứa dữ liệu âm thanh được mã hoá base64.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("output.mp3"), audioBytes);
}

if (interaction.outputText().isPresent()) {
  System.out.println("Lyrics:\n" + interaction.outputText().get());
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A song about a starry night."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        audioBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("output.mp3", audioBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Lyrics:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Lời bài hát và nhạc xen kẽ

Vì đầu ra của Lyria 3.5 rất phức tạp (chứa các bước và khối riêng biệt cho lời bài hát (văn bản) được tạo và bản thân bài hát (âm thanh)), nên các thuộc tính tiện lợi sẽ cung cấp một lối tắt nhanh chóng và được đề xuất.

Tuy nhiên, nếu muốn kiểm soát hoàn toàn, theo chương trình đối với dòng thời gian thô của các bước do máy chủ trả về (chẳng hạn như ghi nhật ký các khối nội dung riêng lẻ khi chúng được nhận), bạn có thể lặp lại `steps` theo cách thủ công:

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

List<String> lyrics = new ArrayList<>();
byte[] audioData = null;

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof AudioContent) {
            AudioContent audioBlock = (AudioContent) contentBlock;
            if (audioBlock.data().isPresent()) {
              audioData = Base64.getDecoder().decode(audioBlock.data().get());
            }
          } else if (contentBlock instanceof TextContent) {
            TextContent textBlock = (TextContent) contentBlock;
            textBlock.text().ifPresent(lyrics::add);
          }
        }
      }
    }
  }
}

if (!lyrics.isEmpty()) {
  System.out.println("Lyrics:\n" + String.join("\n", lyrics));
}

if (audioData != null) {
  Files.write(Paths.get("output.mp3"), audioData);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"
    "strings"

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A song about a starry night."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var lyrics []string
    var audioData []byte

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.AudioContent != nil && contentBlock.AudioContent.Data != nil {
                    decoded, err := base64.StdEncoding.DecodeString(*contentBlock.AudioContent.Data)
                    if err != nil {
                        log.Fatal(err)
                    }
                    audioData = decoded
                } else if contentBlock.TextContent != nil {
                    lyrics = append(lyrics, contentBlock.TextContent.Text)
                }
            }
        }
    }

    if len(lyrics) > 0 {
        fmt.Printf("Lyrics:\n%s\n", strings.Join(lyrics, "\n"))
    }

    if audioData != nil {
        if err := os.WriteFile("output.mp3", audioData, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

## Tạo nhạc từ hình ảnh

Lyria 3.5 hỗ trợ nhiều phương thức nhập dữ liệu. Bạn có thể cung cấp tối đa **10 hình ảnh** cùng với câu lệnh văn bản trong danh sách `input` và mô hình sẽ sáng tác nhạc dựa trên nội dung trực quan.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3.5",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3.5",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
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
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("desert_sunset.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

Content textContent =
    TextContent.builder()
        .text("An atmospheric ambient track inspired by the mood and colors in this image.")
        .build();
Content imageContent =
    ImageContent.builder()
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .data(imageB64)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction response =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

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

    imageBytes, err := os.ReadFile("desert_sunset.jpg")
    if err != nil {
        log.Fatal(err)
    }
    imageB64 := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        }),
        interactions.NewContent(interactions.ImageContent{
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
            Data:     genai.Ptr(imageB64),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3.5",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Cung cấp lời bài hát tuỳ chỉnh

Bạn có thể tự viết lời bài hát và đưa vào câu lệnh. Sử dụng các thẻ phần như `[Verse]`, `[Chorus]` và `[Bridge]` để giúp mô hình hiểu cấu trúc bài hát:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Create a dreamy indie pop song with the following lyrics:\n\n"
        + "[Verse 1]\n"
        + "Walking through the neon glow,\n"
        + "city lights reflect below,\n"
        + "every shadow tells a story,\n"
        + "every corner, fading glory.\n\n"
        + "[Chorus]\n"
        + "We are the echoes in the night,\n"
        + "burning brighter than the light,\n"
        + "hold on tight, don't let me go,\n"
        + "we are the echoes down below.\n\n"
        + "[Verse 2]\n"
        + "Footsteps lost on empty streets,\n"
        + "rhythms sync to heartbeats,\n"
        + "whispers carried by the breeze,\n"
        + "dancing through the autumn leaves.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    prompt := "Create a dreamy indie pop song with the following lyrics:\n\n" +
        "[Verse 1]\n" +
        "Walking through the neon glow,\n" +
        "city lights reflect below,\n" +
        "every shadow tells a story,\n" +
        "every corner, fading glory.\n\n" +
        "[Chorus]\n" +
        "We are the echoes in the night,\n" +
        "burning brighter than the light,\n" +
        "hold on tight, don't let me go,\n" +
        "we are the echoes down below.\n\n" +
        "[Verse 2]\n" +
        "Footsteps lost on empty streets,\n" +
        "rhythms sync to heartbeats,\n" +
        "whispers carried by the breeze,\n" +
        "dancing through the autumn leaves."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Kiểm soát thời gian và cấu trúc

Bạn có thể chỉ định chính xác những gì xảy ra tại các thời điểm cụ thể trong bài hát bằng cách sử dụng dấu thời gian. Điều này rất hữu ích để kiểm soát thời điểm nhạc cụ bắt đầu, thời điểm lời bài hát được gửi và cách bài hát tiến triển:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n"
        + "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n"
        + "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n"
        + "[0:50 - 1:00] Outro: Fade out with the piano melody alone.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    prompt := "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n" +
        "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n" +
        "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n" +
        "[0:50 - 1:00] Outro: Fade out with the piano melody alone."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Tạo bản nhạc không lời

Đối với nhạc nền, nhạc trò chơi hoặc bất kỳ trường hợp sử dụng nào không yêu cầu giọng hát, bạn có thể nhắc mô hình tạo ra các bản nhạc chỉ có nhạc cụ:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(
            InteractionsInput.of(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3-clip-preview"),
            Input: interactions.NewInteractionsInput(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Tạo nhạc bằng nhiều ngôn ngữ

Lyria 3.5 tạo lời bài hát bằng ngôn ngữ trong câu lệnh của bạn. Để tạo một bài hát có lời bằng tiếng Pháp, hãy viết câu lệnh bằng tiếng Pháp. Mô hình này điều chỉnh phong cách giọng nói và cách phát âm cho phù hợp với ngôn ngữ.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Trí tuệ của mô hình

Lyria 3.5 phân tích quy trình tạo câu lệnh, trong đó mô hình suy luận thông qua cấu trúc âm nhạc (đoạn mở đầu, đoạn thơ, điệp khúc, đoạn chuyển, v.v.) dựa trên câu lệnh của bạn.
Việc này xảy ra trước khi âm thanh được tạo và đảm bảo tính nhất quán về cấu trúc cũng như tính nhạc.

## Hướng dẫn đặt câu lệnh

Để tìm hiểu cách soạn câu lệnh hiệu quả cho thể loại nhạc, nhạc cụ, cấu trúc bài hát, lời bài hát tuỳ chỉnh và phong cách thể hiện giọng hát, hãy xem [hướng dẫn về câu lệnh cho Lyria](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=vi).

## Các phương pháp hay nhất

- **Lặp lại với Đoạn video trước.** Sử dụng mô hình `lyria-3-clip-preview` nhanh hơn để thử nghiệm các câu lệnh trước khi tạo một hình ảnh/video dài bằng `lyria-3.5`.
- **Mô tả cụ thể.** Câu lệnh mơ hồ sẽ tạo ra kết quả chung chung. Đề cập đến nhạc cụ, số nhịp/phút, khoá nhạc, tâm trạng và cấu trúc để có kết quả tốt nhất.
- **Ngôn ngữ phải phù hợp.** Câu lệnh bằng ngôn ngữ bạn muốn có lời bài hát.
- **Sử dụng thẻ phần.** Các thẻ `[Verse]`, `[Chorus]`, `[Bridge]` giúp mô hình có cấu trúc rõ ràng để tuân theo.
- **Tách lời bài hát khỏi hướng dẫn.** Khi cung cấp lời bài hát tuỳ chỉnh, hãy tách biệt rõ ràng lời bài hát đó với hướng dẫn về hướng đi của bản nhạc.

## Các điểm hạn chế

- **An toàn**: Tất cả câu lệnh đều được bộ lọc an toàn kiểm tra. Những câu lệnh kích hoạt bộ lọc sẽ bị chặn. Quy định này áp dụng cho cả những câu lệnh yêu cầu giọng nói của một nghệ sĩ cụ thể hoặc tạo ra lời bài hát có bản quyền.
- **Tạo hình mờ**: Tất cả âm thanh được tạo đều có [thuỷ vân âm thanh SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=vi) để nhận dạng. Hình mờ này không thể nhận thấy bằng tai thường và không ảnh hưởng đến trải nghiệm nghe.
- **Chỉnh sửa nhiều lượt**: Tính năng tạo nhạc là một quy trình chỉ diễn ra một lượt.
  Phiên bản Lyria 3.5 hiện tại không được hỗ trợ việc chỉnh sửa lặp đi lặp lại hoặc tinh chỉnh một đoạn video được tạo thông qua nhiều câu lệnh.
- **Độ dài**: Mô hình Đoạn video luôn tạo ra các đoạn video dài 30 giây. Mô hình Pro tạo ra những bài hát có thời lượng vài phút; thời lượng chính xác có thể bị ảnh hưởng thông qua câu lệnh của bạn.
- **Tính xác định**: Kết quả có thể khác nhau giữa các lệnh gọi, ngay cả khi dùng cùng một câu lệnh.

## Bước tiếp theo

- Xem [giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) của các mô hình Lyria 3.5.
- Thử [tạo nhạc trực tuyến theo thời gian thực](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi) bằng Lyria RealTime.
- Tạo các cuộc trò chuyện có nhiều người nói bằng [mô hình TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi).
- Khám phá cách tạo [hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) hoặc [video](https://ai.google.dev/gemini-api/docs/video?hl=vi).
- Tìm hiểu cách Gemini có thể [hiểu các tệp âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi).
- Trò chuyện theo thời gian thực với Gemini bằng [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-01 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-01 UTC."],[],[]]
