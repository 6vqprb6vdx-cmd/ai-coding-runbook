---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi
fetched_at: 2026-11-02T07:04:47.556162+00:00
title: "Hi\u1ec3u video \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hiểu video

> Để tìm hiểu về tính năng tạo video, hãy xem hướng dẫn về [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=vi).

Các mô hình Gemini có thể xử lý video, cho phép nhiều trường hợp sử dụng tiên tiến dành cho nhà phát triển mà trước đây cần đến các mô hình dành riêng cho từng miền.
Một số tính năng về hình ảnh của Gemini bao gồm khả năng: mô tả, phân đoạn và trích xuất thông tin từ video, trả lời các câu hỏi về nội dung video và tham khảo các dấu thời gian cụ thể trong video.

Bạn có thể cung cấp video làm dữ liệu đầu vào cho Gemini theo những cách sau:

| Phương thức nhập | Kích thước tối đa | Trường hợp sử dụng được đề xuất |
| --- | --- | --- |
| [API Tệp](#upload-video) | 20 GB (trả phí) / 2 GB (miễn phí) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp có thể dùng lại. |
| [Đăng ký Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi#registration) | 2 GB (mỗi tệp, không giới hạn dung lượng lưu trữ) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp liên tục, có thể dùng lại. |
| [Dữ liệu nội tuyến](#inline-video) | < 100 MB | Tệp nhỏ (dưới 100 MB), thời lượng ngắn (dưới 1 phút), dữ liệu đầu vào một lần. |
| [URL YouTube](#youtube) | Không áp dụng | Video công khai trên YouTube. |

> **Lưu ý:** Bạn nên sử dụng [API Tệp](#upload-video) cho hầu hết các trường hợp sử dụng, đặc biệt là đối với các tệp lớn hơn 100 MB hoặc khi bạn muốn dùng lại tệp đó cho nhiều yêu cầu.

Để tìm hiểu về các phương thức nhập tệp khác, chẳng hạn như sử dụng URL bên ngoài hoặc tệp
được lưu trữ trong Google Cloud, hãy xem hướng dẫn về
[Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi).

### Tải tệp video lên

Đoạn mã sau đây tải một video mẫu xuống, tải video đó lên bằng [API Tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi), chờ video được xử lý rồi sử dụng tệp đối chiếu đã tải lên để tóm tắt video.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
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
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Để tối ưu hoá hiệu quả và hiệu suất của mã thông báo, hãy cân nhắc sử dụng
[tính năng xử lý video bằng tác nhân](#agentic-video-understanding).

Luôn sử dụng API Tệp khi tổng kích thước yêu cầu (bao gồm tệp, câu lệnh văn bản, hướng dẫn của hệ thống, v.v.) lớn hơn 20 MB, thời lượng video đáng kể hoặc nếu bạn dự định sử dụng cùng một video trong nhiều câu lệnh.
API Tệp chấp nhận trực tiếp các định dạng tệp video.

Để tìm hiểu thêm về cách làm việc với tệp nội dung nghe nhìn, hãy xem
[API Tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi).

### Truyền dữ liệu video nội tuyến

Thay vì tải tệp video lên bằng API Tệp, bạn có thể truyền trực tiếp các video nhỏ hơn trong yêu cầu. Phương thức này phù hợp với các video ngắn hơn có tổng kích thước yêu cầu dưới 20 MB.

Dưới đây là ví dụ về cách cung cấp dữ liệu video nội tuyến:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### Truyền URL YouTube

Bạn có thể truyền trực tiếp URL YouTube đến Gemini API như một phần của yêu cầu như sau:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

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

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Giới hạn:**

- Đối với gói miễn phí, bạn không thể tải lên quá 8 giờ video trên YouTube mỗi ngày.
- Đối với gói trả phí, không có giới hạn dựa trên thời lượng video.
- Đối với các mô hình trước Gemini 2.5, bạn chỉ có thể tải lên 1 video cho mỗi yêu cầu. Đối với các mô hình Gemini 2.5 trở lên, bạn có thể tải lên tối đa 10 video cho mỗi yêu cầu.
- Bạn chỉ có thể tải lên video công khai (không tải lên video riêng tư hoặc video không công khai).

## Tính năng hiểu video bằng tác nhân

Theo mặc định, dữ liệu đầu vào video sử dụng quy trình xử lý tĩnh (trích xuất khung hình ở tốc độ 1 khung hình/giây) trên tất cả các mô hình, bao gồm cả Gemini 4.
Các mô hình Gemini 4 Argon, 3.8 Flash, 3.6 Flash và 3.5 Flash Lite cũng hỗ trợ
**tính năng hiểu video bằng tác nhân**, một chế độ chọn tham gia trong đó mô hình này khám phá dòng thời gian của video
một cách linh hoạt, chọn lọc kiểm tra bản ghi và điều chỉnh tốc độ khung hình
cũng như độ phân giải một cách thích ứng ngay lập tức dựa trên lời nhắc.

| **Chế độ** | **Nội dung mô tả** | **Mô hình được hỗ trợ** |
| --- | --- | --- |
| **Tĩnh** (mặc định) | Trích xuất khung hình ở tốc độ cố định (1 khung hình/giây) và đặt các khung hình đó vào bối cảnh trong một lần truyền. Mặc định cho tất cả các mô hình Gemini, bao gồm cả Gemini 4. | Tất cả các mô hình Gemini |
| **Tác nhân** | Mô hình này điều hướng dòng thời gian của video một cách linh hoạt, chỉ tải nội dung cần thiết dựa trên lời nhắc. Hiệu quả hơn đến 88% về mã thông báo và chất lượng cao hơn khoảng 7% đối với nội dung dài. | Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### Chọn chế độ xử lý

Chọn chế độ xử lý phù hợp với thời lượng video và loại truy vấn:

- **Tĩnh (mặc định):** Phù hợp nhất với các đoạn video ngắn (dưới 5 phút), bản tóm tắt video đầy đủ và rộng rãi trong đó toàn bộ bản ghi đều có liên quan, các truy vấn nhạy cảm với độ trễ hoặc độ chính xác ở cấp khung hình trên toàn bộ đoạn video. Đối với các video ngắn hoặc câu lệnh rộng rãi yêu cầu kiểm tra hầu hết video, quy trình xử lý tĩnh sẽ tránh các token tư duy bổ sung (`total_thought_tokens`) và các chuyến khứ hồi gọi công cụ (`total_tool_use_tokens`) phát sinh do điều hướng dòng thời gian.
- **Tác nhân:** Phù hợp nhất với các video dài (từ 5 đến 10 phút trở lên), truy xuất thông tin khó tìm hoặc các truy vấn nhắm đến các khoảnh khắc hoặc chủ đề cụ thể. Mô hình này kiểm tra bản ghi trước và chỉ tải các phân đoạn hình ảnh có liên quan theo yêu cầu, giảm mức sử dụng mã thông báo đầu vào video xuống đến 88% mà không cần điền vào cửa sổ bối cảnh.

> **Lưu ý:** Đối với các video dài hoặc lời nhắc phức tạp mà quy trình xử lý bằng tác nhân mất
> nhiều thời gian hơn, hãy sử dụng tính năng phát trực tuyến (`stream=True`) hoặc
> [thực thi dưới nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi) (`background=True`).
> Điều này giúp duy trì kết nối, hiển thị các bước suy luận trung gian và
> tránh thời gian chờ kết nối hoặc xác thực.

### Đặt chế độ xử lý

Để sử dụng tính năng hiểu video bằng tác nhân, hãy đặt `"processing": "agentic"` trên phần video
trong mảng `input`.

Quy trình xử lý video bằng tác nhân có thể mất nhiều thời gian hơn đối với các video dài vì mô hình này thực hiện nhiều lần kiểm tra để điều hướng dòng thời gian. Để tránh mất tiến trình nếu kết nối mạng bị gián đoạn, ví dụ này sử dụng `background=True` để chạy tác vụ không đồng bộ trên máy chủ.
Bạn cũng có thể chạy các yêu cầu một cách đồng bộ mà không cần thực thi dưới nền bằng cách bỏ qua tham số `background`. Phương thức này hoạt động hiệu quả đối với các video ngắn hơn.

Để biết thông tin chi tiết về việc thăm dò ý kiến, truy xuất kết quả và quản lý các tác vụ dưới nền, hãy xem
hướng dẫn [thực thi dưới nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi).

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

> **Lưu ý:** Để xác minh rằng quy trình xử lý bằng tác nhân đã được sử dụng, hãy kiểm tra `interaction.steps`. Sự xuất hiện của `processing_call` và `processing_result` cho biết rằng mô hình này đã điều hướng video một cách linh hoạt.

### Các bước phản hồi

Quy trình xử lý bằng tác nhân thêm hai loại bước mới vào mảng `steps`:

- `processing_call`: mô hình đã yêu cầu một phân đoạn video hoặc bản ghi âm thanh, được xác định bằng `id`.
- `processing_result`: kết quả của lượt tải đó, được liên kết bằng `call_id`.

Các bước này xuất hiện xen kẽ với các bước `thought` (khi bạn bật tính năng tóm tắt) và đứng trước bước `model_output` cuối cùng. Bạn có thể sử dụng các bước này để hiển thị dấu vết tiến trình trong giao diện người dùng nhưng không yêu cầu phản hồi.

Ví dụ sau đây cho thấy tải trọng phản hồi với các bước xử lý xen kẽ:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### Kết hợp các chế độ xử lý trên nhiều video

Đặt các chế độ xử lý khác nhau cho từng video trong cùng một yêu cầu:

### Python

```
import time
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

### Cuộc trò chuyện nhiều lượt với video

Bối cảnh video được giữ nguyên trong các lượt trò chuyện. Khi sử dụng quy trình xử lý bằng tác nhân:

- **Chế độ có trạng thái** (sử dụng `previous_interaction_id`): Máy chủ giữ lại bối cảnh video. Bạn không cần xử lý thêm.
- **Chế độ không lưu trạng thái** (sử dụng `step_list`): Ở chế độ không lưu trạng thái, phản hồi bao gồm các bước `processing_call` và `processing_result` mã hoá bối cảnh video. Bạn phải đưa tất cả các bước từ phản hồi vào `step_list` của yêu cầu tiếp theo để giữ lại bối cảnh video. Mặc dù việc bỏ qua các bước này hiện không trả về lỗi API, nhưng bối cảnh video sẽ bị mất, làm giảm đáng kể chất lượng phản hồi đối với các câu hỏi tiếp theo. Xin lưu ý rằng các bước được trả về trong các yêu cầu tiếp theo sẽ góp phần vào số lượng mã thông báo đầu vào.

## Tham khảo dấu thời gian trong nội dung

Bạn có thể đặt câu hỏi về các điểm cụ thể trong video bằng cách sử dụng dấu thời gian ở dạng `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Trích xuất thông tin chi tiết từ video

Các mô hình Gemini cung cấp các tính năng mạnh mẽ để hiểu nội dung video bằng cách xử lý thông tin từ cả luồng **âm thanh và hình ảnh**. Điều này cho phép bạn trích xuất một tập hợp thông tin chi tiết phong phú, bao gồm cả việc tạo nội dung mô tả về những gì đang diễn ra trong video và trả lời các câu hỏi về nội dung của video đó.

Đối với nội dung mô tả bằng hình ảnh, mô hình này lấy mẫu video ở tốc độ **1 khung hình/giây** (FPS). Tốc độ lấy mẫu mặc định này hoạt động hiệu quả đối với hầu hết nội dung, nhưng xin lưu ý rằng tốc độ này có thể bỏ lỡ thông tin chi tiết trong các video có chuyển động nhanh hoặc thay đổi cảnh nhanh.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Tuỳ chỉnh quy trình xử lý video

Bạn có thể tuỳ chỉnh quy trình xử lý video trong Gemini API bằng cách đặt khoảng thời gian cắt hoặc cung cấp mẫu tốc độ khung hình tuỳ chỉnh. Các tuỳ chọn tuỳ chỉnh này
chỉ được hỗ trợ khi xử lý video ở chế độ `"static"`.

### Đặt khoảng thời gian cắt

Bạn có thể cắt video bằng cách chỉ định `start_offset` và `end_offset` trong đối tượng cấu hình `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### Đặt tốc độ khung hình tuỳ chỉnh

Bạn có thể đặt mẫu tốc độ khung hình tuỳ chỉnh bằng cách truyền đối số `fps` trong đối tượng cấu hình `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## Định dạng video được hỗ trợ

Gemini hỗ trợ các loại MIME định dạng video sau:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Thông tin chi tiết kỹ thuật về video

- **Mô hình và bối cảnh được hỗ trợ**: Tất cả các mô hình Gemini đều có thể xử lý dữ liệu video.
  - Theo mặc định, các mô hình có cửa sổ bối cảnh 1 triệu có thể xử lý video dài tối đa 3 giờ (ở độ phân giải nội dung nghe nhìn thấp) hoặc dài tối đa 1 giờ ở độ phân giải nội dung nghe nhìn cao.
- **Chế độ xử lý**: Các mô hình Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite,
  và các mô hình sau này hỗ trợ 2 chế độ xử lý video:
  - **Tĩnh**: Các khung hình được trích xuất ở tốc độ 1 khung hình/giây và được đặt vào bối cảnh (mặc định
    cho tất cả các mô hình). Âm thanh được xử lý ở tốc độ 1 Kbps (một kênh).
    Dấu thời gian được thêm mỗi giây. Phù hợp nhất với các đoạn video ngắn hoặc khi mọi khung hình đều quan trọng (chẳng hạn như kiểm tra từng khung hình). Xin lưu ý rằng các chuỗi hành động nhanh có thể bị mất thông tin chi tiết do tốc độ lấy mẫu là 1 khung hình/giây.
  - **Tác nhân**: Mô hình này điều hướng video một cách linh hoạt, tải
    bản ghi và/hoặc khung hình và/hoặc âm thanh theo yêu cầu. Phương thức này sử dụng ít hơn đến 88% mã thông báo cho nội dung dài, mặc dù việc điều hướng có thể làm tăng Thời gian hiển thị mã thông báo đầu tiên (TTFT) và tổng mức sử dụng mã thông báo trên các đoạn video ngắn (dưới 5 phút) hoặc các truy vấn rộng rãi do suy luận nội bộ và các chuyến khứ hồi công cụ. Phù hợp nhất với các video dài và các truy vấn có mục tiêu để tối ưu hoá chi phí mã thông báo và chất lượng phản hồi.
    Được hỗ trợ trên Gemini 4 Argon, 3.8 Flash, 3.6 Flash và 3.5 Flash Lite.
    Xem phần [Tính năng hiểu video bằng tác nhân](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi#agentic-video-understanding) để biết thông tin chi tiết.
- **Tính toán mã thông báo (chế độ tĩnh)**: Mỗi giây video được mã hoá thành mã thông báo như
  sau:
  - Khung hình riêng lẻ (lấy mẫu ở tốc độ 1 khung hình/giây):
    - Nếu `media_resolution` được đặt ở mức thấp, các khung hình sẽ được mã hoá thành 66 mã thông báo cho mỗi khung hình.
    - Nếu không, các khung hình sẽ được mã hoá thành 258 mã thông báo cho mỗi khung hình.
  - Âm thanh: 32 mã thông báo mỗi giây.
  - Siêu dữ liệu cũng được đưa vào.
  - Tổng cộng: Khoảng 100 mã thông báo mỗi giây video ở độ phân giải nội dung nghe nhìn mặc định (thấp) hoặc khoảng 300 mã thông báo mỗi giây video ở độ phân giải nội dung nghe nhìn cao.
- **Tính toán mã thông báo (chế độ tác nhân)**: Mức sử dụng mã thông báo khác nhau dựa trên độ phức tạp của nội dung
  và chiến lược điều hướng của mô hình. Các mã thông báo suy luận điều hướng
  được tạo trong quá trình khám phá video được tính là **mã thông báo tư duy**
  (`total_thought_tokens`), trong khi các khung hình, âm thanh và bản ghi được tải theo
  yêu cầu được tính là mã thông báo sử dụng công cụ (`total_tool_use_tokens`).
  Quy trình xử lý bằng tác nhân thường sử dụng ít hơn đến 88% tổng số mã thông báo so với quy trình xử lý tĩnh
  đối với nội dung dài vì mô hình này chỉ tải bản ghi và/hoặc khung hình và/hoặc âm thanh cần thiết để trả lời lời nhắc (xem
  [hướng dẫn về mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi#video-token-usage)).
- **Độ phân giải nội dung nghe nhìn**: Gemini 3 giới thiệu tính năng kiểm soát chi tiết quy trình xử lý hình ảnh đa phương thức
  bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi hình ảnh đầu vào hoặc khung hình video.** Độ phân giải càng cao thì khả năng đọc văn bản chi tiết hoặc xác định các chi tiết nhỏ của mô hình càng được cải thiện, nhưng mức sử dụng mã thông báo và độ trễ sẽ tăng lên. Các tham số `media_resolution` và `processing` độc lập với nhau: bạn có thể đặt cả hai tham số này trên cùng một dữ liệu đầu vào video.

Để biết thêm thông tin chi tiết về cách tính toán mã thông báo, hãy xem hướng dẫn về
[mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi).

- **Định dạng dấu thời gian**: Khi tham khảo các khoảnh khắc cụ thể trong video trong
  lời nhắc, hãy sử dụng định dạng `MM:SS` (ví dụ: `01:15` cho 1 phút 15
  giây).
- **Vị trí câu lệnh văn bản**: Nếu kết hợp văn bản và một video, hãy đặt câu lệnh văn bản
  *sau* phần video trong mảng `input`.
- **Thời gian chờ cho các yêu cầu dài**: Đối với các video yêu cầu thời gian xử lý kéo dài hoặc suy luận đa bước phức tạp, hãy sử dụng tính năng truyền trực tuyến
  (`stream=True`) hoặc [thực thi dưới nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi)
  (`background=True`).
  Các yêu cầu đồng bộ, không truyền trực tuyến gặp phải các lần thử lại ở phần phụ trợ trong điều kiện nhu cầu cao có thể vượt quá thời gian hiệu lực của mã thông báo kết nối hoặc xác thực,
  có thể xuất hiện dưới dạng lỗi `401 Unauthorized` hoặc lỗi thời gian chờ không mong muốn.
  Tính năng phát trực tuyến giúp duy trì kết nối và hiển thị tiến trình suy luận trung gian và tiến trình gọi công cụ.

## Bước tiếp theo

- [Độ phân giải nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi): Kiểm soát
  độ phân giải của khung hình video để cân bằng chất lượng và mức sử dụng mã thông báo.
- [Mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi): Tìm hiểu cách nội dung video được mã hoá thành mã thông báo
  ở cả chế độ xử lý tĩnh và chế độ xử lý bằng tác nhân.
- [Thực thi dưới nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi): Chạy
  các tác vụ hiểu video chạy trong thời gian dài một cách không đồng bộ để tránh thời gian chờ kết nối.
- [Hướng dẫn của hệ thống](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#system-instructions):
  Hướng dẫn của hệ thống cho phép bạn điều chỉnh hành vi của mô hình dựa trên
  nhu cầu và trường hợp sử dụng cụ thể của mình.
- [API Tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý
  tệp để sử dụng với Gemini.
- [Chiến lược đưa ra lời nhắc bằng tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide): API Gemini
  hỗ trợ đưa ra lời nhắc bằng dữ liệu văn bản, hình ảnh, âm thanh và video, còn được gọi là
  lời nhắc đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh
  tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Việc xử lý hậu kỳ và đánh giá của con người là rất cần thiết để hạn chế nguy cơ gây hại từ những kết quả như vậy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
