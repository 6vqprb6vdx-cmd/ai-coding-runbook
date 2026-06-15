---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=th
fetched_at: 2026-06-15T06:25:01.049878+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจรูปภาพ

โมเดล Gemini ถูกสร้างขึ้นตั้งแต่เริ่มต้นให้เป็นแบบหลายรูปแบบ ซึ่งช่วยให้สามารถทำงานประมวลผลรูปภาพและคอมพิวเตอร์วิชันได้หลากหลาย รวมถึงแต่ไม่จำกัดเพียงการใส่คำบรรยายรูปภาพ การจัดหมวดหมู่ และการตอบคำถามเกี่ยวกับภาพโดยไม่ต้องฝึกโมเดลแมชชีนเลิร์นนิงเฉพาะทาง

นอกจากความสามารถแบบหลายรูปแบบทั่วไปแล้ว โมเดล Gemini ยังมีความ
**แม่นยำที่เพิ่มขึ้น** สำหรับกรณีการใช้งานเฉพาะ เช่น [การตรวจหาออบเจ็กต์](#object-detection) ผ่านการฝึกเพิ่มเติม

## การส่งรูปภาพไปยัง Gemini

คุณสามารถระบุรูปภาพเป็นอินพุตไปยัง Gemini ได้ 2 วิธี ดังนี้

- [การส่งข้อมูลรูปภาพแบบอินไลน์](#inline-image): เหมาะสำหรับไฟล์ขนาดเล็ก (ขนาดคำขอทั้งหมด
  ไม่เกิน 20 MB รวมถึงพรอมต์)
- [การอัปโหลดรูปภาพโดยใช้ File API](#upload-image): แนะนำสำหรับไฟล์ขนาดใหญ่หรือสำหรับการ
  นำรูปภาพไปใช้ซ้ำในคำขอหลายรายการ

### การส่งข้อมูลรูปภาพแบบอินไลน์

คุณสามารถส่งข้อมูลรูปภาพแบบอินไลน์ในคำขอไปยัง `generateContent` ได้ โดยระบุข้อมูลรูปภาพเป็นสตริงที่เข้ารหัส Base64 หรืออ่านไฟล์ในเครื่องโดยตรง (ขึ้นอยู่กับภาษา)

ตัวอย่างต่อไปนี้แสดงวิธีอ่านรูปภาพจากไฟล์ในเครื่องและส่งไปยัง `generateContent` API เพื่อประมวลผล

### Python

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
  )

  print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile,
    },
  },
  { text: "Caption this image." },
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
bytes, _ := os.ReadFile("path/to/small-sample.jpg")

parts := []*genai.Part{
  genai.NewPartFromBytes(bytes, "image/jpeg"),
  genai.NewPartFromText("Caption this image."),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3.5-flash",
  contents,
  nil,
)

fmt.Println(result.Text())
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
B64FLAGS="--input"
else
B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{
    "parts":[
        {
            "inline_data": {
            "mime_type":"image/jpeg",
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"
            }
        },
        {"text": "Caption this image."},
    ]
    }]
}' 2> /dev/null
```

นอกจากนี้ คุณยังดึงรูปภาพจาก URL แปลงเป็นไบต์ และส่งไปยัง `generateContent` ได้ตามที่แสดงในตัวอย่างต่อไปนี้

### Python

```
from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=["What is this image?", image],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";

  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const result = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
    {
      inlineData: {
        mimeType: 'image/jpeg',
        data: base64ImageData,
      },
    },
    { text: "Caption this image." }
  ],
  });
  console.log(result.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "io"
  "net/http"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Download the image.
  imageResp, _ := http.Get("https://goo.gle/instrument-img")

  imageBytes, _ := io.ReadAll(imageResp.Body)

  parts := []*genai.Part{
    genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    genai.NewPartFromText("Caption this image."),
  }

  contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.5-flash",
    contents,
    nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Caption this image."}
        ]
      }]
    }' 2> /dev/null
```

### การอัปโหลดรูปภาพโดยใช้ File API

หากต้องการใช้ไฟล์ขนาดใหญ่หรือใช้ไฟล์รูปภาพเดียวกันซ้ำๆ ให้ใช้ Files API โค้ดต่อไปนี้จะอัปโหลดไฟล์รูปภาพ แล้วใช้ไฟล์ดังกล่าวในการเรียก `generateContent` ดูข้อมูลเพิ่มเติมและตัวอย่างได้ใน[คู่มือ Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)สำหรับ

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[my_file, "Caption this image."],
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Caption this image.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", nil)

  parts := []*genai.Part{
      genai.NewPartFromText("Caption this image."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
IMAGE_PATH="path/to/sample.jpg"
MIME_TYPE=$(file -b --mime-type "${IMAGE_PATH}")
NUM_BYTES=$(wc -c < "${IMAGE_PATH}")
DISPLAY_NAME=IMAGE

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Caption this image."}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## การใช้พรอมต์ที่มีรูปภาพหลายรูป

คุณสามารถระบุรูปภาพหลายรูปในพรอมต์เดียวได้โดยใส่ออบเจ็กต์ `Part` ของรูปภาพหลายรายการในอาร์เรย์ `contents` ซึ่งอาจเป็นข้อมูลแบบอินไลน์ (ไฟล์ในเครื่องหรือ URL) และการอ้างอิง File API ผสมกัน

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-3.5-flash",
    contents=[
        "What is different between these two images?",
        uploaded_file,  # Use the uploaded file reference
        types.Part.from_bytes(
            data=img2_bytes,
            mime_type='image/png'
        )
    ]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  // Upload the first image
  const image1_path = "path/to/image1.jpg";
  const uploadedFile = await ai.files.upload({
    file: image1_path,
    config: { mimeType: "image/jpeg" },
  });

  // Prepare the second image as inline data
  const image2_path = "path/to/image2.png";
  const base64Image2File = fs.readFileSync(image2_path, {
    encoding: "base64",
  });

  // Create the prompt with text and multiple images

  const response = await ai.models.generateContent({

    model: "gemini-3.5-flash",
    contents: createUserContent([
      "What is different between these two images?",
      createPartFromUri(uploadedFile.uri, uploadedFile.mimeType),
      {
        inlineData: {
          mimeType: "image/png",
          data: base64Image2File,
        },
      },
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
// Upload the first image
image1Path := "path/to/image1.jpg"
uploadedFile, _ := client.Files.UploadFromPath(ctx, image1Path, nil)

// Prepare the second image as inline data
image2Path := "path/to/image2.jpeg"
imgBytes, _ := os.ReadFile(image2Path)

parts := []*genai.Part{
  genai.NewPartFromText("What is different between these two images?"),
  genai.NewPartFromBytes(imgBytes, "image/jpeg"),
  genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3.5-flash",
  contents,
  nil,
)

fmt.Println(result.Text())
```

### REST

```
# Upload the first image
IMAGE1_PATH="path/to/image1.jpg"
MIME1_TYPE=$(file -b --mime-type "${IMAGE1_PATH}")
NUM1_BYTES=$(wc -c < "${IMAGE1_PATH}")
DISPLAY_NAME1=IMAGE1

tmp_header_file1=upload-header1.tmp

curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header1.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME1_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME1}'}}" 2> /dev/null

upload_url1=$(grep -i "x-goog-upload-url: " "${tmp_header_file1}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file1}"

curl "${upload_url1}" \
  -H "Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE1_PATH}" 2> /dev/null > file_info1.json

file1_uri=$(jq ".file.uri" file_info1.json)
echo file1_uri=$file1_uri

# Prepare the second image (inline)
IMAGE2_PATH="path/to/image2.png"
MIME2_TYPE=$(file -b --mime-type "${IMAGE2_PATH}")

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi
IMAGE2_BASE64=$(base64 $B64FLAGS $IMAGE2_PATH)

# Now generate content using both images
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "What is different between these two images?"},
          {"file_data":{"mime_type": "'"${MIME1_TYPE}"'", "file_uri": '$file1_uri'}},
          {
            "inline_data": {
              "mime_type":"'"${MIME2_TYPE}"'",
              "data": "'"$IMAGE2_BASE64"'"
            }
          }
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## การตรวจจับออบเจ็กต์

โมเดลได้รับการฝึกให้ตรวจหาออบเจ็กต์ในรูปภาพและรับพิกัดกรอบล้อมรอบ พิกัดจะปรับขนาดเป็น [0, 1000] โดยอิงตามขนาดรูปภาพ คุณต้องปรับขนาดพิกัดเหล่านี้ตามขนาดรูปภาพเดิม

### Python

```
from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-3.5-flash",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("/path/to/image.png", {
  encoding: "base64",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: [
    {
      inlineData: {
        mimeType: "image/png",
        data: base64ImageFile,
      },
    },
    "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."
  ],
  config: {
    responseMimeType: "application/json",
  },
});

const boundingBoxes = JSON.parse(response.text);
console.log(boundingBoxes);
// To convert normalized coordinates to absolute pixels:
// const absY1 = (boundingBoxes[0].box_2d[0] / 1000) * imageHeight;
// const absX1 = (boundingBoxes[0].box_2d[1] / 1000) * imageWidth;
```

### Go

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "image"
    _ "image/png" // Register PNG decoder
    "log"
    "os"

    "google.golang.org/genai"
)

type BoundingBox struct {
    Box2D []int  `json:"box_2d"`
    Label string `json:"label"`
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    imagePath := "/path/to/image.png"

    // Open the image to get dimensions
    file, err := os.Open(imagePath)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    imgConfig, _, err := image.DecodeConfig(file)
    if err != nil {
        log.Fatal(err)
    }
    width := imgConfig.Width
    height := imgConfig.Height

    // Read image bytes
    imageBytes, err := os.ReadFile(imagePath)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

    parts := []*genai.Part{
        genai.NewPartFromBytes(imageBytes, "image/png"),
        genai.NewPartFromText(prompt),
    }

    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        contents,
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    var boundingBoxes []BoundingBox
    err = json.Unmarshal([]byte(result.Text()), &boundingBoxes)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Image size: %d %d
", width, height)
    fmt.Println("Bounding boxes:")
    for _, box := range boundingBoxes {
        if len(box.Box2D) == 4 {
            absY1 := int(float64(box.Box2D[0]) / 1000.0 * float64(height))
            absX1 := int(float64(box.Box2D[1]) / 1000.0 * float64(width))
            absY2 := int(float64(box.Box2D[2]) / 1000.0 * float64(height))
            absX2 := int(float64(box.Box2D[3]) / 1000.0 * float64(width))
            fmt.Printf("- %s: [%d, %d, %d, %d]
", box.Label, absX1, absY1, absX2, absY2)
        }
    }
}
```

### REST

```
IMG_PATH="/path/to/image.png"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"       -H "x-goog-api-key: $GEMINI_API_KEY"       -H 'Content-Type: application/json'       -X POST       -d '{
    "contents": [{
      "parts":[
        {
          "inline_data": {
            "mime_type":"image/png",
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"
          }
        },
        {"text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."}
      ]
    }],
    "generationConfig": {
      "responseMimeType": "application/json"
    }
  }' 2> /dev/null
```

ดูตัวอย่างเพิ่มเติมได้ใน Notebook ต่อไปนี้ใน [Gemini Cookbook](https://github.com/google-gemini/cookbook):

- [Notebook ความเข้าใจเชิงพื้นที่ 2 มิติ](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=th)
- [Notebook การชี้เชิงพื้นที่ 3 มิติแบบทดลอง](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=th)

## รูปแบบรูปภาพที่รองรับ

Gemini รองรับประเภท MIME ของรูปแบบรูปภาพต่อไปนี้

- PNG - `image/png`
- JPEG - `image/jpeg`
- WebP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

ดูข้อมูลเกี่ยวกับวิธีการป้อนไฟล์อื่นๆ ได้ในคู่มือ
[วิธีการป้อนไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

## ความสามารถ

โมเดล Gemini ทุกเวอร์ชันเป็นแบบหลายรูปแบบและสามารถใช้ในงานประมวลผลรูปภาพและคอมพิวเตอร์วิทัศน์ได้หลากหลาย ซึ่งรวมถึงแต่ไม่จำกัดเพียงคำอธิบายภาพ การตอบคำถามเกี่ยวกับภาพ การจัดหมวดหมู่รูปภาพ และการตรวจจับออบเจ็กต์

Gemini สามารถลดความจำเป็นในการใช้โมเดลแมชชีนเลิร์นนิงเฉพาะทางได้ ทั้งนี้ขึ้นอยู่กับข้อกำหนดด้านคุณภาพและประสิทธิภาพ

โมเดลเวอร์ชันล่าสุดได้รับการฝึกมาโดยเฉพาะเพื่อปรับปรุงความแม่นยำของงานเฉพาะทาง นอกเหนือจากความสามารถทั่วไป เช่น [การตรวจจับออบเจ็กต์](#object-detection)ที่ได้รับการปรับปรุง

## ข้อจำกัดและข้อมูลทางเทคนิคที่สำคัญ

### ขีดจำกัดของไฟล์

โมเดล Gemini รองรับไฟล์รูปภาพสูงสุด 3,600 ไฟล์ต่อคำขอ

### การคำนวณโทเค็น

- 258 โทเค็นหากทั้ง 2 มิติมีขนาด <= 384 พิกเซล
  รูปภาพขนาดใหญ่จะถูกแบ่งเป็นรูปภาพขนาด 768x768 พิกเซล ซึ่งแต่ละรูปภาพใช้โทเค็น 258 รายการ

สูตรคร่าวๆ สำหรับการคำนวณจำนวนรูปภาพมีดังนี้

- คำนวณขนาดหน่วยครอบตัดซึ่งมีค่าประมาณ floor(min(width, height) / 1.5)
- หารแต่ละมิติด้วยขนาดหน่วยครอบตัด แล้วคูณกันเพื่อหาจำนวนรูปภาพ

ตัวอย่างเช่น รูปภาพขนาด 960x540 จะมีขนาดหน่วยครอบตัด 360 หารแต่ละมิติด้วย 360 และจำนวนรูปภาพคือ 3 \* 2 = 6

### ความละเอียดของสื่อ

Gemini 3 มีการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลภาพแบบหลายรูปแบบด้วยพารามิเตอร์ `media_resolution` พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุดที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ**
ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง

ดูรายละเอียดเพิ่มเติมเกี่ยวกับพารามิเตอร์และวิธีที่พารามิเตอร์นี้อาจส่งผลต่อการคำนวณโทเค็นได้ใน
ดู[คู่มือความละเอียดของสื่อ](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th)

## เคล็ดลับและแนวทางปฏิบัติแนะนำ

- ตรวจสอบว่ารูปภาพหมุนอย่างถูกต้อง
- ใช้รูปภาพที่ชัดเจนและไม่เบลอ
- เมื่อใช้รูปภาพเดียวที่มีข้อความ ให้วางพรอมต์ข้อความ *หลัง* ส่วนรูปภาพในอาร์เรย์ `contents`

## ขั้นตอนถัดไป

คู่มือนี้แสดงวิธีอัปโหลดไฟล์รูปภาพและสร้างเอาต์พุตข้อความจากอินพุตรูปภาพ ดูข้อมูลเพิ่มเติมได้จากแหล่งข้อมูลต่อไปนี้

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th): ดูข้อมูลเพิ่มเติมเกี่ยวกับการอัปโหลดและจัดการไฟล์เพื่อใช้กับ Gemini
- [คำแนะนำของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำแนะนำของระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตาม
  ความต้องการและกรณีการใช้งานที่เฉพาะเจาะจง
- [กลยุทธ์การเขียนพรอมต์กับไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide): Gemini API รองรับการเขียนพรอมต์กับข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ หรือที่เรียกว่าการเขียนพรอมต์แบบหลายรูปแบบ
- [คำแนะนำด้านความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=th): บางครั้งโมเดล Generative
  AI จะสร้างเอาต์พุตที่ไม่คาดคิด เช่น เอาต์พุตที่ไม่ถูกต้อง
  มีอคติ หรือไม่เหมาะสม การประมวลผลภายหลังและการประเมินโดยเจ้าหน้าที่เป็นสิ่งสำคัญในการจำกัดความเสี่ยงที่จะเกิดอันตรายจากเอาต์พุตดังกล่าว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-11 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-11 UTC"],[],[]]
