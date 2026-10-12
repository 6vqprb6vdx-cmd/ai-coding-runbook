---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=th
fetched_at: 2026-10-12T07:04:52.805427+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e27\u0e34\u0e14\u0e35\u0e42\u0e2d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจวิดีโอ

> ดูข้อมูลเกี่ยวกับการสร้างวิดีโอได้ในคู่มือ [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=th)

โมเดล Gemini สามารถประมวลผลวิดีโอได้ ซึ่งช่วยให้ผู้พัฒนาที่อยู่แถวหน้าสามารถใช้กรณีการใช้งานต่างๆ
ที่ในอดีตต้องใช้โมเดลเฉพาะโดเมน
ความสามารถด้านการมองเห็นของ Gemini บางอย่าง ได้แก่ ความสามารถในการอธิบาย แบ่งกลุ่ม
และดึงข้อมูลจากวิดีโอ ตอบคำถามเกี่ยวกับเนื้อหาวิดีโอ และ
อ้างอิงการประทับเวลาที่เฉพาะเจาะจงภายในวิดีโอ

คุณสามารถป้อนวิดีโอไปยัง Gemini ได้ด้วยวิธีต่อไปนี้

| วิธีการป้อนข้อมูล | ขนาดสูงสุด | กรณีการใช้งานที่แนะนำ |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (แบบชำระเงิน) / 2 GB (ฟรี) | ไฟล์ขนาดใหญ่ (100 MB ขึ้นไป), วิดีโอยาว (10 นาทีขึ้นไป), ไฟล์ที่นำกลับมาใช้ซ้ำได้ |
| [การลงทะเบียน Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th#registration) | 2 GB (ต่อไฟล์ ไม่มีขีดจำกัดพื้นที่เก็บข้อมูล) | ไฟล์ขนาดใหญ่ (100 MB ขึ้นไป), วิดีโอยาว (10 นาทีขึ้นไป), ไฟล์ที่ใช้ซ้ำได้ |
| [ข้อมูลในบรรทัด](#inline-video) | < 100MB | ไฟล์ขนาดเล็ก (น้อยกว่า 100 MB), ระยะเวลาสั้น (น้อยกว่า 1 นาที), ข้อมูลที่ป้อนครั้งเดียว |
| [URL ของ YouTube](#youtube) | ไม่มี | วิดีโอ YouTube สาธารณะ |

> **หมายเหตุ:** เราขอแนะนำให้ใช้ [File API](#upload-video) สำหรับ Use Case ส่วนใหญ่ โดยเฉพาะอย่างยิ่งสำหรับไฟล์ที่มีขนาดใหญ่กว่า 100 MB หรือเมื่อคุณต้องการนำไฟล์ไปใช้ซ้ำในคำขอหลายรายการ

ดูข้อมูลเกี่ยวกับวิธีการป้อนไฟล์อื่นๆ เช่น การใช้ URL ภายนอกหรือไฟล์ที่เก็บไว้ใน Google Cloud ได้ที่คำแนะนำ[วิธีการป้อนไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

### อัปโหลดไฟล์วิดีโอ

โค้ดต่อไปนี้จะดาวน์โหลดวิดีโอตัวอย่าง อัปโหลดโดยใช้ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)
รอให้ประมวลผล แล้วใช้การอ้างอิงไฟล์ที่อัปโหลดเพื่อ
สรุปวิดีโอ

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

โปรดพิจารณาใช้[การประมวลผลวิดีโอแบบเอเจนต์](#agentic-video-understanding)เพื่อเพิ่มประสิทธิภาพและประสิทธิภาพของโทเค็น

ใช้ Files API เสมอเมื่อขนาดคำขอทั้งหมด (รวมถึงไฟล์ พรอมต์ข้อความ คำสั่งของระบบ ฯลฯ) ใหญ่กว่า 20 MB, ความยาววิดีโอมีความสำคัญ หรือหากคุณต้องการใช้วิดีโอเดียวกันในพรอมต์หลายรายการ
File API ยอมรับรูปแบบไฟล์วิดีโอโดยตรง

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับไฟล์สื่อได้ที่
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)

### ส่งข้อมูลวิดีโอแบบอินไลน์

คุณส่งวิดีโอขนาดเล็กกว่า
ในคำขอได้โดยตรงแทนที่จะอัปโหลดไฟล์วิดีโอโดยใช้ File API เหมาะสำหรับ
วิดีโอสั้นๆ ที่มีขนาดคำขอรวมไม่เกิน 20 MB

ตัวอย่างการระบุข้อมูลวิดีโอในหน้าเว็บมีดังนี้

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

### ส่ง URL ของ YouTube

คุณส่ง URL ของ YouTube ไปยัง Gemini API ได้โดยตรงเป็นส่วนหนึ่งของคำขอ ดังนี้

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

**ข้อจำกัด:**

- สำหรับแพ็กเกจฟรี คุณจะอัปโหลดวิดีโอ YouTube ได้ไม่เกิน 8 ชั่วโมงต่อวัน
- สำหรับแพ็กเกจแบบชำระเงิน จะไม่มีการจำกัดตามความยาวของวิดีโอ
- สำหรับโมเดลก่อน Gemini 2.5 คุณจะอัปโหลดวิดีโอได้เพียง 1 รายการต่อคำขอ สำหรับโมเดล Gemini 2.5 ขึ้นไป คุณจะอัปโหลดวิดีโอได้สูงสุด 10 รายการต่อคำขอ
- คุณอัปโหลดได้เฉพาะวิดีโอสาธารณะเท่านั้น (ไม่ใช่ส่วนตัวหรือที่ไม่เป็นสาธารณะ)

## การทำความเข้าใจวิดีโอแบบ Agent

โดยค่าเริ่มต้น อินพุตวิดีโอจะใช้การประมวลผลแบบคงที่ (ดึงเฟรมที่ 1 FPS)
โมเดล Gemini 3.8 Flash, 3.6 Flash และ 3.5 Flash Lite ยังรองรับ**การทำความเข้าใจวิดีโอแบบเอเจนต์** ซึ่งโมเดลจะสำรวจไทม์ไลน์วิดีโอแบบไดนามิก ตรวจสอบข้อความถอดเสียงอย่างเลือกสรร และปรับอัตราเฟรมและความละเอียดแบบปรับเปลี่ยนได้ทันทีตามพรอมต์

| **โหมด** | **คำอธิบาย** | **รุ่นที่รองรับ** |
| --- | --- | --- |
| **คงที่** (ค่าเริ่มต้น) | แยกเฟรมในอัตราคงที่ (1 FPS) และวางเฟรมเหล่านั้นลงในบริบทได้ในครั้งเดียว เหมาะสำหรับคลิปสั้นๆ | โมเดล Gemini ทั้งหมด |
| **Agentic** | โมเดลจะไปยังไทม์ไลน์ของวิดีโอแบบไดนามิก โดยจะโหลดเฉพาะเนื้อหาที่ต้องการตามพรอมต์ ประหยัดโทเค็นมากขึ้นสูงสุด 88% และมีคุณภาพสูงขึ้นประมาณ 7% ในเนื้อหาแบบยาว | Gemini 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### เลือกโหมดการประมวลผล

โดยหลักการทั่วไป ให้เริ่มต้นด้วยโหมด**เอเจนต์** โดยเฉพาะเมื่อเพิ่มประสิทธิภาพ
เพื่อคุณภาพการตอบกลับหรือประสิทธิภาพของโทเค็น

- **Agentic:** วิดีโอแบบยาวหรือคำค้นหาที่กำหนดเป้าหมายไปยังช่วงเวลาที่เฉพาะเจาะจง
  โมเดลจะไปยังไทม์ไลน์แบบไดนามิกเพื่อกำหนดเป้าหมายข้อมูลที่เกี่ยวข้องตามบริบท
  โดยไม่ต้องกรอกหน้าต่างบริบท
- **คงที่:** คำค้นหาที่คำนึงถึงเวลาในการตอบสนองในคลิปสั้น (ไม่เกิน 5 นาที) หรือ
  กรณีที่ต้องการความแม่นยำระดับเฟรมตลอดทั้งคลิป

> **หมายเหตุ:** สำหรับวิดีโอขนาดยาวหรือพรอมต์ที่ซับซ้อนซึ่งการประมวลผลแบบเอเจนต์ใช้เวลานานกว่า
> ให้ใช้การสตรีม (`stream=True`) หรือ
> [การดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th) (`background=True`)
> ซึ่งจะช่วยให้การเชื่อมต่อยังคงใช้งานได้ แสดงขั้นตอนการให้เหตุผลขั้นกลาง และ
> หลีกเลี่ยงการหมดเวลาการเชื่อมต่อหรือการตรวจสอบสิทธิ์

### ตั้งค่าโหมดการประมวลผล

หากต้องการใช้ความเข้าใจวิดีโอแบบเอเจนต์ ให้ตั้งค่า `"processing": "agentic"` ในส่วนวิดีโอ
ในอาร์เรย์ `input`

การประมวลผลวิดีโอแบบ Agentic อาจใช้เวลานานกว่าในวิดีโอแบบยาวเนื่องจากโมเดล
จะทำการตรวจสอบหลายครั้งเพื่อไปยังไทม์ไลน์ ตัวอย่างนี้ใช้ `background=True` เพื่อเรียกใช้
งานแบบไม่พร้อมกันในเซิร์ฟเวอร์เพื่อป้องกันไม่ให้ข้อมูลความคืบหน้าสูญหาย
หากการเชื่อมต่อเครือข่ายขาดหายไป
นอกจากนี้ คุณยังเรียกใช้คำขอแบบพร้อมกันได้โดยไม่ต้องดำเนินการในเบื้องหลังด้วยการ
ละเว้นพารามิเตอร์ `background` ซึ่งเหมาะสำหรับวิดีโอที่สั้นกว่า

ดูรายละเอียดเกี่ยวกับการสำรวจ การดึงผลลัพธ์ และการจัดการงานในเบื้องหลังได้ในคู่มือ[การดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)

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

> **หมายเหตุ:** หากต้องการยืนยันว่ามีการใช้การประมวลผลผ่านระบบที่เป็น Agent ให้ตรวจสอบ `interaction.steps` การมีอยู่ของ `processing_call` และ `processing_result` แสดงให้เห็นว่าโมเดลไปยังส่วนต่างๆ ของวิดีโอแบบไดนามิก

### ขั้นตอนการตอบกลับ

การประมวลผลแบบ Agentic จะเพิ่มขั้นตอนใหม่ 2 ประเภทลงในอาร์เรย์ `steps` ดังนี้

- `processing_call`: โมเดลขอส่วนวิดีโอหรือข้อความถอดเสียงที่ระบุโดย `id`
- `processing_result`: ผลลัพธ์ของการโหลดนั้น ซึ่งลิงก์โดย `call_id`

โดยจะปรากฏสลับกับ`thought` ขั้นตอน (เมื่อเปิดใช้สรุป) และอยู่ก่อน`model_output` ขั้นตอนสุดท้าย โดยสามารถใช้เพื่อแสดงร่องรอยความคืบหน้าใน UI แต่ไม่จำเป็นต้องมีการตอบกลับ

ตัวอย่างต่อไปนี้แสดงเพย์โหลดการตอบกลับพร้อมขั้นตอนการประมวลผลแบบสลับ

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

### ผสมโหมดการประมวลผลในวิดีโอ

ตั้งค่าโหมดการประมวลผลที่แตกต่างกันสำหรับวิดีโอแต่ละรายการในคำขอเดียวกัน

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

### การสนทนาผ่านวิดีโอแบบผ่านการสนทนาไปมา

บริบทของวิดีโอจะยังคงอยู่ตลอดการสนทนา เมื่อใช้การประมวลผลแบบเอเจนต์ ให้ทำดังนี้

- **โหมด Stateful** (ใช้ `previous_interaction_id`): เซิร์ฟเวอร์จะเก็บบริบทวิดีโอ
  ไว้ โดยคุณไม่ต้องดำเนินการใดๆ เพิ่มเติม
- **โหมดไม่เก็บสถานะ** (ใช้ `step_list`): ในโหมดไม่เก็บสถานะ คำตอบ
  จะมีขั้นตอน `processing_call` และ `processing_result` ที่เข้ารหัสบริบทวิดีโอ
  คุณต้องใส่ขั้นตอนทั้งหมดจากการตอบกลับใน`step_list`ของคำขอถัดไปเพื่อรักษาบริบทของวิดีโอ แม้ว่าการละเว้นจะไม่ทำให้เกิดข้อผิดพลาดของ API ในปัจจุบัน แต่บริบทวิดีโอจะหายไป ซึ่งจะลดคุณภาพการตอบกลับคำถามติดตามผลลงอย่างมาก โปรดทราบว่าขั้นตอนที่ส่งกลับ
  ในคำขอที่ตามมาจะนับรวมในจำนวนโทเค็นอินพุต

## อ้างอิงการประทับเวลาในเนื้อหา

คุณสามารถถามคำถามเกี่ยวกับช่วงเวลาที่เฉพาะเจาะจงภายในวิดีโอได้โดยใช้
การประทับเวลาในรูปแบบ `MM:SS`

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

## ดึงข้อมูลเชิงลึกโดยละเอียดจากวิดีโอ

โมเดล Gemini มีความสามารถอันทรงพลังในการทำความเข้าใจเนื้อหาวิดีโอโดย
การประมวลผลข้อมูลจากทั้งสตรีม**เสียงและภาพ** ซึ่งช่วยให้คุณ
ดึงรายละเอียดที่ครบถ้วนได้ รวมถึงสร้างคำอธิบายสิ่งที่
เกิดขึ้นในวิดีโอและตอบคำถามเกี่ยวกับเนื้อหาของวิดีโอ

สำหรับคำอธิบายภาพ โมเดลจะสุ่มตัวอย่างวิดีโอที่อัตรา **1 เฟรม
ต่อวินาที** (FPS) อัตราการสุ่มตัวอย่างเริ่มต้นนี้เหมาะกับเนื้อหาส่วนใหญ่ แต่โปรดทราบว่าอาจพลาดรายละเอียดในวิดีโอที่มีการเคลื่อนไหวอย่างรวดเร็วหรือการเปลี่ยนฉากอย่างรวดเร็ว

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

## ปรับแต่งการประมวลผลวิดีโอ

คุณปรับแต่งการประมวลผลวิดีโอใน Gemini API ได้โดยการตั้งค่าช่วงการตัด
หรือระบุการสุ่มตัวอย่างอัตราเฟรมที่กำหนดเอง ตัวเลือกการปรับแต่งเหล่านี้
ใช้ได้เมื่อประมวลผลวิดีโอในโหมด `"static"` เท่านั้น

### ตั้งค่าช่วงการตัด

คุณตัดวิดีโอได้โดยระบุ `start_offset` และ `end_offset` ในออบเจ็กต์การกำหนดค่า `processing`

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

### ตั้งค่าอัตราเฟรมที่กำหนดเอง

คุณตั้งค่าการสุ่มตัวอย่างอัตราเฟรมที่กำหนดเองได้โดยส่งอาร์กิวเมนต์ `fps` ในออบเจ็กต์การกำหนดค่า `processing`

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

## รูปแบบวิดีโอที่รองรับ

Gemini รองรับประเภท MIME ของรูปแบบวิดีโอต่อไปนี้

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## รายละเอียดทางเทคนิคเกี่ยวกับวิดีโอ

- **โมเดลและบริบทที่รองรับ**: โมเดล Gemini ทุกรุ่นสามารถประมวลผลข้อมูลวิดีโอได้
  - โมเดลที่มีหน้าต่างบริบทขนาด 1 ล้านสามารถประมวลผลวิดีโอได้นานสูงสุด 3 ชั่วโมงโดยค่าเริ่มต้น (ที่ความละเอียดของสื่อต่ำ) หรือนานสูงสุด 1 ชั่วโมงที่ความละเอียดของสื่อสูง
- **โหมดการประมวลผล**: Gemini 3.8 Flash, 3.6 Flash, 3.5 Flash Lite
  และโมเดลที่ใหม่กว่ารองรับโหมดการประมวลผลวิดีโอ 2 โหมด
  - **คงที่**: ระบบจะดึงข้อมูลเฟรมที่ 1 FPS และวางลงในบริบท (ค่าเริ่มต้น
    สำหรับทุกโมเดล) ระบบจะประมวลผลเสียงที่ 1Kbps (ช่องเดียว)
    ระบบจะเพิ่มการประทับเวลาทุกวินาที เหมาะที่สุดสำหรับคลิปสั้นๆ หรือเมื่อทุกเฟรม
    มีความสำคัญ (เช่น การตรวจสอบทีละเฟรม) โปรดทราบว่าลำดับการดำเนินการที่รวดเร็ว
    อาจสูญเสียรายละเอียดเนื่องจากอัตราการสุ่มตัวอย่าง 1 FPS
  - **เอเจนต์**: โมเดลจะไปยังส่วนต่างๆ ของวิดีโอแบบไดนามิก โดยจะโหลด
    ข้อความถอดเสียงและ/หรือเฟรมและ/หรือเสียงตามคำขอ ซึ่งจะใช้โทเค็นน้อยลงสูงสุด 88%
    สำหรับเนื้อหาแบบยาว แม้ว่าการนำทางอาจเพิ่ม
    เวลาในการแสดงผลโทเค็นแรก (TTFT) เล็กน้อยในคลิปสั้นๆ (น้อยกว่า 5 นาที) เนื่องจาก
    การให้เหตุผลภายในและการส่งคำขอไปกลับของเครื่องมือก่อนที่จะเริ่มสร้าง เหมาะ
    สำหรับวิดีโอแบบยาวเพื่อเพิ่มประสิทธิภาพต้นทุนโทเค็นและคุณภาพคำตอบ
    รองรับใน Gemini 3.8 Flash, 3.6 Flash และ 3.5 Flash Lite
    ดูรายละเอียดได้ที่[การทำความเข้าใจวิดีโอแบบเอเจนต์](#agentic-video-understanding)
- **การคำนวณโทเค็น (โหมดคงที่)**: ระบบจะแปลงวิดีโอแต่ละวินาทีเป็นโทเค็นดังนี้
  - เฟรมแต่ละเฟรม (สุ่มตัวอย่างที่ 1 FPS)
    - หากตั้งค่า `media_resolution` เป็นต่ำ ระบบจะแปลงเฟรมเป็นโทเค็นที่ 66
      โทเค็นต่อเฟรม
    - ไม่เช่นนั้น ระบบจะแปลงเฟรมเป็นโทเค็นที่ 258 โทเค็นต่อเฟรม
  - เสียง: 32 โทเค็นต่อวินาที
  - รวมถึงข้อมูลเมตาด้วย
  - ทั้งหมด: ประมาณ 100 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อเริ่มต้น (ต่ำ) หรือประมาณ 300 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อสูง
- **การคำนวณโทเค็น (โหมดตัวแทน)**: การใช้โทเค็นจะแตกต่างกันไปตามความซับซ้อนของเนื้อหาและกลยุทธ์การนำทางของโมเดล โทเค็นการให้เหตุผลในการนำทาง
  ที่สร้างขึ้นระหว่างการสำรวจวิดีโอจะถือเป็น**โทเค็นความคิด**
  (`total_thought_tokens`) ส่วนเฟรม เสียง และข้อความถอดเสียงที่โหลดตามคำขอจะถือเป็นโทเค็นการใช้เครื่องมือ (`total_tool_use_tokens`)
  โดยปกติแล้วการประมวลผลแบบเอเจนต์จะใช้โทเค็นทั้งหมดน้อยกว่าการประมวลผลแบบคงที่ถึง 88% สำหรับเนื้อหารูปแบบยาว เนื่องจากโมเดลจะโหลดเฉพาะข้อความถอดเสียงและ/หรือเฟรมและ/หรือเสียงที่จำเป็นต่อการตอบพรอมต์ (ดู[คำแนะนำเกี่ยวกับโทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th#video-token-usage))
- **ความละเอียดของสื่อ**: Gemini 3 มีการควบคุมการประมวลผลภาพหลายรูปแบบอย่างละเอียดด้วยพารามิเตอร์ `media_resolution` พารามิเตอร์
  `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุด
  ที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ** ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง พารามิเตอร์ `media_resolution` และ `processing`
  เป็นอิสระต่อกัน คุณตั้งค่าทั้ง 2 อย่างในอินพุตวิดีโอเดียวกันได้

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการคำนวณโทเค็นได้ที่คู่มือ[โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)

- **รูปแบบการประทับเวลา**: เมื่ออ้างอิงถึงช่วงเวลาที่เฉพาะเจาะจงในวิดีโอภายในพรอมต์ ให้ใช้รูปแบบ `MM:SS` (เช่น `01:15` สำหรับ 1 นาที 15 วินาที)
- **ตำแหน่งพรอมต์**: หากรวมข้อความและวิดีโอเดียว ให้วางพรอมต์ข้อความ*หลัง*ส่วนวิดีโอในอาร์เรย์ `input`
- **การหมดเวลาสำหรับคำขอที่ใช้เวลานาน**: สำหรับวิดีโอที่ต้องใช้เวลาประมวลผล
  นานขึ้นหรือการให้เหตุผลหลายขั้นตอนที่ซับซ้อน ให้ใช้การสตรีม
  (`stream=True`) หรือ[การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)
  (`background=True`)
  คำขอแบบซิงโครนัสที่ไม่ใช่การสตรีมซึ่งมีการลองใหม่ที่แบ็กเอนด์ภายใต้
  ดีมานด์สูงอาจเกินระยะเวลาที่ใช้ได้ของการเชื่อมต่อหรือโทเค็นการตรวจสอบสิทธิ์
  ซึ่งอาจแสดงเป็นข้อผิดพลาด `401 Unauthorized` หรือข้อผิดพลาดการหมดเวลาที่ไม่คาดคิด
  การสตรีมจะทำให้การเชื่อมต่อยังคงใช้งานได้และแสดงการให้เหตุผลระดับกลาง
  และความคืบหน้าในการเรียกใช้เครื่องมือ

## ขั้นตอนถัดไป

- [ความละเอียดของสื่อ](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th): ควบคุม
  ความละเอียดของเฟรมวิดีโอเพื่อปรับสมดุลคุณภาพและการใช้โทเค็น
- [โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th): ทำความเข้าใจวิธีแปลงเนื้อหาวิดีโอเป็นโทเค็น
  ในโหมดการประมวลผลแบบคงที่และแบบเอเจนต์
- [การดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th): เรียกใช้
  งานการทำความเข้าใจวิดีโอที่ใช้เวลานานแบบไม่พร้อมกันเพื่อหลีกเลี่ยงการหมดเวลา
  การเชื่อมต่อ
- [คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำสั่งของระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตามความต้องการ
  และกรณีการใช้งานที่เฉพาะเจาะจงได้
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th): ดูข้อมูลเพิ่มเติมเกี่ยวกับการอัปโหลดและจัดการ
  ไฟล์เพื่อใช้กับ Gemini
- [กลยุทธ์การเขียนพรอมต์ไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide): Gemini
  API รองรับการเขียนพรอมต์ด้วยข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ หรือที่เรียกว่าการเขียนพรอมต์แบบหลายรูปแบบ
- [คำแนะนำด้านความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=th): บางครั้งโมเดล Generative AI
  อาจสร้างเอาต์พุตที่ไม่คาดคิด เช่น เอาต์พุตที่ไม่ถูกต้อง
  มีอคติ หรือไม่เหมาะสม การประมวลผลภายหลังและการประเมินโดยเจ้าหน้าที่เป็นสิ่งจำเป็นเพื่อ
  จำกัดความเสี่ยงที่จะเกิดอันตรายจากเอาต์พุตดังกล่าว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-09 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-09 UTC"],[],[]]
