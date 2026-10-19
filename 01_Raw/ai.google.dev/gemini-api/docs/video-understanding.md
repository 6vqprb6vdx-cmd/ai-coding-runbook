---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=th
fetched_at: 2026-10-19T05:42:42.605399+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e27\u0e34\u0e14\u0e35\u0e42\u0e2d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจวิดีโอ

> ดูข้อมูลเกี่ยวกับการสร้างวิดีโอได้ที่คู่มือ [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=th)

โมเดล Gemini สามารถประมวลผลวิดีโอได้ ซึ่งช่วยให้นักพัฒนาแอปสามารถใช้กรณีการใช้งานที่ล้ำสมัยมากมายซึ่งในอดีตต้องใช้โมเดลเฉพาะโดเมน
ความสามารถด้านการมองเห็นบางอย่างของ Gemini ได้แก่ ความสามารถในการอธิบาย แบ่งส่วน และดึงข้อมูลจากวิดีโอ ตอบคำถามเกี่ยวกับเนื้อหาวิดีโอ และอ้างอิงการประทับเวลาที่เฉพาะเจาะจงภายในวิดีโอ

คุณสามารถระบุวิดีโอเป็นอินพุตให้กับ Gemini ได้ด้วยวิธีต่อไปนี้

| วิธีการป้อนข้อมูล | ขนาดสูงสุด | กรณีการใช้งานที่แนะนำ |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (แบบชำระเงิน) / 2 GB (ฟรี) | ไฟล์ขนาดใหญ่ (100 MB ขึ้นไป), วิดีโอความยาวมาก (10 นาทีขึ้นไป), ไฟล์ที่ใช้ซ้ำได้ |
| [การลงทะเบียน Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th#registration) | 2 GB (ต่อไฟล์ ไม่จำกัดพื้นที่เก็บข้อมูล) | ไฟล์ขนาดใหญ่ (100 MB ขึ้นไป), วิดีโอความยาวมาก (10 นาทีขึ้นไป), ไฟล์ที่คงอยู่และใช้ซ้ำได้ |
| [ข้อมูลแบบอินไลน์](#inline-video) | < 100 MB | ไฟล์ขนาดเล็ก (<100 MB), ระยะเวลาสั้น (<1 นาที), อินพุตแบบครั้งเดียว |
| [URL ของ YouTube](#youtube) | ไม่มี | วิดีโอ YouTube แบบสาธารณะ |

> **หมายเหตุ:** เราขอแนะนำให้ใช้ [File API](#upload-video) สำหรับกรณีการใช้งานส่วนใหญ่ โดยเฉพาะอย่างยิ่งสำหรับไฟล์ที่มีขนาดใหญ่กว่า 100 MB หรือเมื่อคุณต้องการใช้ไฟล์ซ้ำในคำขอหลายรายการ

ดูข้อมูลเกี่ยวกับวิธีการป้อนไฟล์อื่นๆ เช่น การใช้ URL ภายนอกหรือไฟล์
ที่จัดเก็บไว้ใน Google Cloud ได้ที่
[คู่มือวิธีการป้อนไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

### อัปโหลดไฟล์วิดีโอ

โค้ดต่อไปนี้จะดาวน์โหลดวิดีโอตัวอย่าง อัปโหลดวิดีโอโดยใช้ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th),
รอให้ระบบประมวลผลวิดีโอ และใช้ข้อมูลอ้างอิงไฟล์ที่อัปโหลดเพื่อ
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

โปรดพิจารณาใช้
[การประมวลผลวิดีโอแบบเป็น Agent](#agentic-video-understanding) เพื่อเพิ่มประสิทธิภาพโทเค็นและประสิทธิภาพ

ใช้ Files API เสมอเมื่อขนาดคำขอทั้งหมด (รวมถึงไฟล์ พรอมต์ข้อความ คำแนะนำระบบ ฯลฯ) ใหญ่กว่า 20 MB ความยาววิดีโอมีความสำคัญ หรือหากคุณต้องการใช้วิดีโอเดียวกันในพรอมต์หลายรายการ
File API ยอมรับรูปแบบไฟล์วิดีโอโดยตรง

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับไฟล์สื่อได้ที่
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)

### ส่งข้อมูลวิดีโอแบบอินไลน์

คุณสามารถส่งวิดีโอขนาดเล็กโดยตรงในคำขอแทนการอัปโหลดไฟล์วิดีโอโดยใช้ File API วิธีนี้เหมาะสำหรับวิดีโอสั้นๆ ที่มีขนาดคำขอทั้งหมดไม่เกิน 20 MB

ตัวอย่างการระบุข้อมูลวิดีโอแบบอินไลน์มีดังนี้

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

คุณสามารถส่ง URL ของ YouTube ไปยัง Gemini API ได้โดยตรงเป็นส่วนหนึ่งของคำขอตามวิธีต่อไปนี้

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

**ข้อจำกัด**

- สำหรับแพ็กเกจฟรี คุณจะอัปโหลดวิดีโอ YouTube ได้ไม่เกิน 8 ชั่วโมงต่อวัน
- สำหรับแพ็กเกจแบบชำระเงิน จะไม่มีการจำกัดตามความยาววิดีโอ
- สำหรับโมเดลก่อน Gemini 2.5 คุณจะอัปโหลดวิดีโอได้เพียง 1 รายการต่อคำขอ สำหรับโมเดล Gemini 2.5 และรุ่นที่ใหม่กว่า คุณจะอัปโหลดวิดีโอได้สูงสุด 10 รายการต่อคำขอ
- คุณอัปโหลดได้เฉพาะวิดีโอสาธารณะ (ไม่ใช่ส่วนตัวหรือวิดีโอที่ไม่เป็นสาธารณะ)

## การทำความเข้าใจวิดีโอแบบเป็น Agent

โดยค่าเริ่มต้น อินพุตวิดีโอจะใช้การประมวลผลแบบคงที่ (ดึงเฟรมที่ 1 FPS) ในโมเดลทั้งหมด รวมถึง Gemini 4
โมเดล Gemini 4 Argon, 3.8 Flash, 3.6 Flash และ 3.5 Flash Lite ยังรองรับ
**การทำความเข้าใจวิดีโอแบบเป็น Agent** ซึ่งเป็นโหมดเลือกใช้ที่โมเดลจะสำรวจไทม์ไลน์วิดีโอ
แบบไดนามิก ตรวจสอบคำบรรยายอย่างเลือกสรร และปรับอัตราเฟรม
และความละเอียดแบบปรับเปลี่ยนได้ในทันทีตามพรอมต์

| **โหมด** | **คำอธิบาย** | **โมเดลที่รองรับ** |
| --- | --- | --- |
| **คงที่** (ค่าเริ่มต้น) | ดึงเฟรมในอัตราคงที่ (1 FPS) และวางเฟรมลงในบริบทในการประมวลผลครั้งเดียว ค่าเริ่มต้นสำหรับโมเดล Gemini ทั้งหมด รวมถึง Gemini 4 | โมเดล Gemini ทั้งหมด |
| **แบบเป็น Agent** | โมเดลจะนำทางไทม์ไลน์วิดีโอแบบไดนามิก โดยโหลดเฉพาะเนื้อหาที่ต้องการตามพรอมต์ ประหยัดโทเค็นมากขึ้นสูงสุด 88% และมีคุณภาพสูงขึ้น ~7% สำหรับเนื้อหารูปแบบยาว | Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### เลือกโหมดการประมวลผล

เลือกโหมดการประมวลผลที่ตรงกับความยาววิดีโอและประเภทคำค้นหา

- **คงที่ (ค่าเริ่มต้น):** เหมาะที่สุดสำหรับคลิปสั้นๆ (ไม่เกิน 5 นาที), สรุปวิดีโอแบบกว้างๆ ที่การบันทึกทั้งหมดมีความเกี่ยวข้อง, คำค้นหาที่ไวต่อเวลาในการตอบสนอง หรือความแม่นยำระดับเฟรมตลอดทั้งคลิป ในวิดีโอสั้นๆ หรือพรอมต์แบบกว้างๆ ที่ต้องตรวจสอบวิดีโอส่วนใหญ่ การประมวลผลแบบคงที่จะหลีกเลี่ยงโทเค็นการคิดเพิ่มเติม (`total_thought_tokens`) และการเรียกใช้เครื่องมือไปกลับ (`total_tool_use_tokens`) ที่เกิดจากการนำทางไทม์ไลน์
- **Agentic:** เหมาะที่สุดสำหรับวิดีโอแบบยาว (มากกว่า 5-10 นาที), การดึงข้อมูลที่เฉพาะเจาะจง หรือคำค้นหาที่กำหนดเป้าหมายไปยังช่วงเวลาหรือหัวข้อที่เฉพาะเจาะจง โมเดลจะตรวจสอบคำบรรยายก่อนและโหลดเฉพาะส่วนภาพที่เกี่ยวข้องตามความต้องการ ซึ่งจะช่วยลดการใช้โทเค็นอินพุตวิดีโอได้สูงสุด 88% โดยไม่ทำให้หน้าต่างบริบทเต็ม

> **หมายเหตุ:** สำหรับวิดีโอความยาวมากหรือพรอมต์ที่ซับซ้อนซึ่งการประมวลผลแบบเป็น Agent ใช้เวลา
> นานขึ้น ให้ใช้การสตรีม (`stream=True`) หรือ
> [การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th) (`background=True`)
> วิธีนี้จะทำให้การเชื่อมต่อยังคงใช้งานได้ แสดงขั้นตอนการให้เหตุผลระดับกลาง และ
> หลีกเลี่ยงการหมดเวลาการเชื่อมต่อหรือการตรวจสอบสิทธิ์

### ตั้งค่าโหมดการประมวลผล

หากต้องการใช้การทำความเข้าใจวิดีโอแบบเป็น Agent ให้ตั้งค่า `"processing": "agentic"` ในส่วนวิดีโอ
ในอาร์เรย์ `input`

การประมวลผลวิดีโอแบบเป็น Agent อาจใช้เวลานานขึ้นในวิดีโอความยาวมาก เนื่องจากโมเดลจะทำการตรวจสอบหลายครั้งเพื่อนำทางไทม์ไลน์ ตัวอย่างนี้ใช้ `background=True` เพื่อเรียกใช้ฟังก์ชันแบบไม่พร้อมกันในเซิร์ฟเวอร์เพื่อหลีกเลี่ยงการสูญเสียความคืบหน้าหากการเชื่อมต่อเครือข่ายขาดหาย
นอกจากนี้ คุณยังเรียกใช้คำขอแบบพร้อมกันได้โดยไม่ต้องดำเนินการเบื้องหลังด้วยการละเว้นพารามิเตอร์ `background` ซึ่งเหมาะสำหรับวิดีโอสั้นๆ

ดูรายละเอียดเกี่ยวกับการโพล ดึงข้อมูลผลลัพธ์ และจัดการฟังก์ชันเบื้องหลังได้ที่
คู่มือ[การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)

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

> **หมายเหตุ:** หากต้องการยืนยันว่ามีการใช้การประมวลผลแบบเป็น Agent ให้ตรวจสอบ `interaction.steps` การมี `processing_call` และ `processing_result` บ่งบอกว่าโมเดลได้นำทางวิดีโอแบบไดนามิก

### ขั้นตอนการตอบกลับ

การประมวลผลแบบเป็น Agent จะเพิ่มขั้นตอนใหม่ 2 ประเภทลงในอาร์เรย์ `steps` ดังนี้

- `processing_call`: โมเดลขอส่วนวิดีโอหรือคำบรรยายเสียง ซึ่งระบุโดย `id`
- `processing_result`: ผลลัพธ์ของการโหลดดังกล่าว ซึ่งลิงก์โดย `call_id`

ขั้นตอนเหล่านี้จะปรากฏสลับกับขั้นตอน `thought` (เมื่อเปิดใช้การสรุป) และอยู่ก่อนขั้นตอน `model_output` สุดท้าย คุณสามารถใช้ขั้นตอนเหล่านี้เพื่อแสดงการติดตามความคืบหน้าใน UI แต่ไม่จำเป็นต้องมีการตอบกลับ

ตัวอย่างต่อไปนี้แสดงเพย์โหลดการตอบกลับที่มีขั้นตอนการประมวลผลแบบสลับ

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

### การสนทนาแบบหลายรอบเกี่ยวกับวิดีโอ

ระบบจะเก็บรักษาบริบทวิดีโอไว้ตลอดการสนทนา เมื่อใช้การประมวลผลแบบเป็น Agent

- **โหมดเก็บสถานะ** (ใช้ `previous_interaction_id`): เซิร์ฟเวอร์จะเก็บรักษาบริบทวิดีโอไว้ คุณไม่จำเป็นต้องจัดการเพิ่มเติม
- **โหมดไม่เก็บสถานะ** (ใช้ `step_list`): ในโหมดไม่เก็บสถานะ การตอบกลับจะมีขั้นตอน `processing_call` และ `processing_result` ที่เข้ารหัสบริบทวิดีโอ คุณต้องรวมขั้นตอนทั้งหมดจากการตอบกลับไว้ใน `step_list` ของคำขอถัดไปเพื่อเก็บรักษาบริบทวิดีโอ แม้ว่าการละเว้นขั้นตอนเหล่านี้จะไม่ทำให้เกิดข้อผิดพลาด API ในปัจจุบัน แต่บริบทวิดีโอจะหายไป ซึ่งจะลดคุณภาพการตอบกลับคำถามติดตามผลลงอย่างมาก โปรดทราบว่าขั้นตอนที่ส่งคืนซึ่งส่งในคำขอที่ตามมาจะมีส่วนทำให้จำนวนโทเค็นอินพุตเพิ่มขึ้น

## อ้างอิงการประทับเวลาในเนื้อหา

คุณสามารถถามคำถามเกี่ยวกับจุดที่เฉพาะเจาะจงในวิดีโอได้โดยใช้การประทับเวลาในรูปแบบ `MM:SS`

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

โมเดล Gemini มีความสามารถอันทรงพลังในการทำความเข้าใจเนื้อหาวิดีโอโดยการประมวลผลข้อมูลจากทั้งสตรีม**เสียงและภาพ** ซึ่งช่วยให้คุณดึงรายละเอียดมากมาย รวมถึงสร้างคำอธิบายเกี่ยวกับสิ่งที่เกิดขึ้นในวิดีโอและตอบคำถามเกี่ยวกับเนื้อหาของวิดีโอ

สำหรับคำอธิบายภาพ โมเดลจะสุ่มตัวอย่างวิดีโอในอัตรา **1 เฟรมต่อวินาที** (FPS) อัตราการสุ่มตัวอย่างเริ่มต้นนี้เหมาะกับเนื้อหาส่วนใหญ่ แต่โปรดทราบว่าอาจพลาดรายละเอียดในวิดีโอที่มีการเคลื่อนไหวอย่างรวดเร็วหรือการเปลี่ยนฉากอย่างรวดเร็ว

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

คุณสามารถปรับแต่งการประมวลผลวิดีโอใน Gemini API ได้โดยการตั้งค่าช่วงการตัดหรือระบุการสุ่มตัวอย่างอัตราเฟรมที่กำหนดเอง ระบบจะรองรับตัวเลือกการปรับแต่งเหล่านี้
เมื่อประมวลผลวิดีโอในโหมด `"static"` เท่านั้น

### ตั้งค่าช่วงการตัด

คุณสามารถตัดวิดีโอได้โดยระบุ `start_offset` และ `end_offset` ในออบเจ็กต์การกำหนดค่า `processing`

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

คุณสามารถตั้งค่าการสุ่มตัวอย่างอัตราเฟรมที่กำหนดเองได้โดยส่งอาร์กิวเมนต์ `fps` ในออบเจ็กต์การกำหนดค่า `processing`

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

Gemini รองรับประเภท MIME รูปแบบวิดีโอต่อไปนี้

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

- **โมเดลและบริบทที่รองรับ**: โมเดล Gemini ทั้งหมดสามารถประมวลผลข้อมูลวิดีโอได้
  - โมเดลที่มีหน้าต่างบริบทขนาด 1 ล้านโทเค็นสามารถประมวลผลวิดีโอได้นานสูงสุด 3 ชั่วโมงโดยค่าเริ่มต้น (ที่ความละเอียดสื่อต่ำ) หรือนานสูงสุด 1 ชั่วโมงที่ความละเอียดสื่อสูง
- **โหมดการประมวลผล**: โมเดล Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite,
  และรุ่นที่ใหม่กว่ารองรับโหมดการประมวลผลวิดีโอ 2 โหมด ได้แก่
  - **คงที่**: ดึงเฟรมที่ 1 FPS และวางเฟรมลงในบริบท (ค่าเริ่มต้น
    สำหรับโมเดลทั้งหมด) ระบบจะประมวลผลเสียงที่ 1 Kbps (ช่องเดียว)
    และเพิ่มการประทับเวลาทุกวินาที โหมดนี้เหมาะที่สุดสำหรับคลิปสั้นๆ หรือเมื่อทุกเฟรมมีความสำคัญ (เช่น การตรวจสอบแบบเฟรมต่อเฟรม) โปรดทราบว่าลำดับการทำงานที่รวดเร็วอาจสูญเสียรายละเอียดเนื่องจากอัตราการสุ่มตัวอย่าง 1 FPS
  - **แบบเป็น Agent**: โมเดลจะนำทางวิดีโอแบบไดนามิก โดยโหลด
    คำบรรยายและ/หรือเฟรมและ/หรือเสียงตามความต้องการ โหมดนี้ใช้โทเค็นน้อยลงสูงสุด 88% สำหรับเนื้อหารูปแบบยาว แม้ว่าการนำทางอาจเพิ่มเวลาในการแสดงผลโทเค็นแรก (TTFT) และการใช้โทเค็นทั้งหมดในคลิปสั้นๆ (<5 นาที) หรือคำค้นหาแบบกว้างๆ เนื่องจากการให้เหตุผลภายในและการเรียกใช้เครื่องมือไปกลับ โหมดนี้เหมาะที่สุดสำหรับวิดีโอแบบยาวและการค้นหาที่กำหนดเป้าหมายเพื่อเพิ่มประสิทธิภาพค่าใช้จ่ายโทเค็นและคุณภาพการตอบกลับ
    รองรับใน Gemini 4 Argon, 3.8 Flash, 3.6 Flash และ 3.5 Flash Lite
    ดูรายละเอียดได้ที่[การทำความเข้าใจวิดีโอแบบเป็น Agent](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#agentic-video-understanding)
- **การคำนวณโทเค็น (โหมดคงที่)**: ระบบจะแปลงวิดีโอแต่ละวินาทีเป็นโทเค็นดัง
  นี้:
  - เฟรมแต่ละเฟรม (สุ่มตัวอย่างที่ 1 FPS):
    - หากตั้งค่า `media_resolution` เป็นต่ำ ระบบจะแปลงเฟรมเป็นโทเค็นที่ 66 โทเค็นต่อเฟรม
    - ไม่เช่นนั้น ระบบจะแปลงเฟรมเป็นโทเค็นที่ 258 โทเค็นต่อเฟรม
  - เสียง: 32 โทเค็นต่อวินาที
  - รวมข้อมูลเมตาด้วย
  - รวม: ประมาณ 100 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อเริ่มต้น (ต่ำ) หรือประมาณ 300 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อสูง
- **การคำนวณโทเค็น (โหมดแบบเป็น Agent)**: การใช้โทเค็นจะแตกต่างกันไปตามความซับซ้อนของเนื้อหา
  และกลยุทธ์การนำทางของโมเดล โทเค็นการให้เหตุผลในการนำทาง
  ที่สร้างขึ้นระหว่างการสำรวจวิดีโอจะถือเป็น **โทเค็นการคิด**
  (`total_thought_tokens`) ในขณะที่เฟรม เสียง และคำบรรยายที่โหลดตาม
  ความต้องการจะถือเป็นโทเค็นการใช้เครื่องมือ (`total_tool_use_tokens`)
  โดยทั่วไปแล้ว การประมวลผลแบบเป็น Agent จะใช้โทเค็นทั้งหมดน้อยลงสูงสุด 88% เมื่อเทียบกับการประมวลผลแบบคงที่
  สำหรับเนื้อหารูปแบบยาว เนื่องจากโมเดลจะโหลดเฉพาะคำบรรยาย
  และ/หรือเฟรมและ/หรือเสียงที่จำเป็นในการตอบพรอมต์ (ดู
  [คู่มือโทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th#video-token-usage))
- **ความละเอียดสื่อ**: Gemini 3 ขอแนะนำการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลการมองเห็นแบบหลายรูปแบบ
  ด้วยพารวมิเตอร์ `media_resolution` พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุดที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ** ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง พารามิเตอร์ `media_resolution` และ `processing` เป็นอิสระจากกัน โดยคุณสามารถตั้งค่าทั้ง 2 อย่างในอินพุตวิดีโอเดียวกันได้

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการคำนวณโทเค็นได้ที่
[คู่มือโทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)

- **รูปแบบการประทับเวลา**: เมื่ออ้างอิงช่วงเวลาที่เฉพาะเจาะจงในวิดีโอภายใน
  พรอมต์ ให้ใช้รูปแบบ `MM:SS` (เช่น `01:15` สำหรับ 1 นาที 15
  วินาที)
- **ตำแหน่งพรอมต์**: หากรวมข้อความและวิดีโอเดียว ให้วางพรอมต์ข้อความ
  *หลังจาก* ส่วนวิดีโอในอาร์เรย์ `input`
- **การหมดเวลาสำหรับคำขอที่ยาว**: สำหรับวิดีโอที่ต้องใช้เวลาประมวลผลนานขึ้นหรือการให้เหตุผลหลายขั้นตอนที่ซับซ้อน ให้ใช้การสตรีม
  (`stream=True`) หรือ [การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)
  (`background=True`) คำขอแบบซิงโครนัสที่ไม่ใช่การสตรีมซึ่งมีการลองใหม่ที่แบ็กเอนด์ภายใต้ความต้องการสูงอาจเกินหน้าต่างความถูกต้องของการเชื่อมต่อหรือโทเค็นการตรวจสอบสิทธิ์ ซึ่งอาจปรากฏเป็นข้อผิดพลาด `401 Unauthorized` หรือข้อผิดพลาดการหมดเวลาที่ไม่คาดคิด
  การสตรีมจะทำให้การเชื่อมต่อยังคงใช้งานได้และแสดงการให้เหตุผลระดับกลางและความคืบหน้าในการเรียกใช้เครื่องมือ

## ขั้นตอนถัดไป

- [ความละเอียดสื่อ](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th): ควบคุม
  ความละเอียดของเฟรมวิดีโอเพื่อปรับสมดุลคุณภาพและการใช้โทเค็น
- [โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th): ทำความเข้าใจวิธีแปลงเนื้อหาวิดีโอเป็นโทเค็น
  ในโหมดการประมวลผลแบบคงที่และแบบเป็น Agent
- [การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th): เรียกใช้
  ฟังก์ชันการทำความเข้าใจวิดีโอที่ใช้เวลานานแบบไม่พร้อมกันเพื่อหลีกเลี่ยงการหมดเวลาการเชื่อมต่อ
- [คำแนะนำระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำแนะนำระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตาม
  ความต้องการและกรณีการใช้งานที่เฉพาะเจาะจง
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th): ดูข้อมูลเพิ่มเติมเกี่ยวกับการอัปโหลดและจัดการ
  ไฟล์เพื่อใช้กับ Gemini
- [กลยุทธ์การเขียนพรอมต์ไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide): Gemini
  API รองรับการเขียนพรอมต์ด้วยข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ ซึ่งเรียกอีกอย่างว่า
  การเขียนพรอมต์แบบหลายรูปแบบ
- [คำแนะนำด้านความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=th): บางครั้งโมเดล Generative AI
  จะสร้างเอาต์พุตที่ไม่คาดคิด เช่น เอาต์พุตที่ไม่ถูกต้อง
  มีอคติ หรือไม่เหมาะสม การประมวลผลภายหลังและการประเมินจากเจ้าหน้าที่เป็นสิ่งสำคัญในการจำกัดความเสี่ยงที่จะเกิดอันตรายจากเอาต์พุตดังกล่าว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-13 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-13 UTC"],[],[]]
