---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=hi
fetched_at: 2026-07-20T04:42:46.603675+00:00
title: "\u0907\u092e\u0947\u091c \u0915\u094b \u0938\u092e\u091d\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# इमेज को समझना

Gemini मॉडल को मल्टीमॉडल के तौर पर डिज़ाइन किया गया है. इससे इमेज प्रोसेसिंग और कंप्यूटर विज़न से जुड़े कई काम किए जा सकते हैं. जैसे, इमेज के लिए कैप्शन जनरेट करना, इमेज को अलग-अलग कैटगरी में बांटना, और इमेज से जुड़े सवालों के जवाब देना. इसके लिए, आपको एमएल मॉडल को ट्रेनिंग देने की ज़रूरत नहीं होती.

Gemini मॉडल, मल्टीमॉडल की सामान्य सुविधाओं के साथ-साथ, कुछ खास इस्तेमाल के उदाहरणों के लिए **ज़्यादा सटीक नतीजे** देते हैं. जैसे, [ऑब्जेक्ट का पता लगाने की सुविधा](#object-detection). इसके लिए, उन्हें अतिरिक्त ट्रेनिंग दी जाती है.

## Gemini को इमेज पास करना

Gemini को इनपुट के तौर पर इमेज देने के लिए, इन दो तरीकों का इस्तेमाल किया जा सकता है:

- [इनलाइन इमेज डेटा पास करना](#inline-image): यह छोटी फ़ाइलों के लिए सबसे सही है. इसमें प्रॉम्प्ट के साथ-साथ, कुल अनुरोध का साइज़ 20 एमबी से कम होना चाहिए.
- [File API का इस्तेमाल करके इमेज अपलोड करना](#upload-image): इसका सुझाव बड़ी फ़ाइलों के लिए दिया जाता है. इसके अलावा, इसका इस्तेमाल कई अनुरोधों में इमेज को फिर से इस्तेमाल करने के लिए भी किया जा सकता है.

### इनलाइन इमेज का डेटा पास करना

`generateContent` को किए गए अनुरोध में, इनलाइन इमेज डेटा पास किया जा सकता है. इमेज का डेटा, Base64 एन्कोड की गई स्ट्रिंग के तौर पर दिया जा सकता है. इसके अलावा, सीधे तौर पर स्थानीय फ़ाइलों को पढ़कर भी डेटा दिया जा सकता है. हालांकि, यह भाषा पर निर्भर करता है.

यहां दिए गए उदाहरण में, लोकल फ़ाइल से इमेज को पढ़ने और उसे प्रोसेस करने के लिए `generateContent` API को पास करने का तरीका बताया गया है.

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

### ऐप पर जाएं

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

किसी यूआरएल से इमेज को फ़ेच किया जा सकता है. इसके बाद, उसे बाइट में बदला जा सकता है. साथ ही, उसे `generateContent` में पास किया जा सकता है. ऐसा करने का तरीका यहां दिए गए उदाहरणों में बताया गया है.

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

### ऐप पर जाएं

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

### File API का इस्तेमाल करके इमेज अपलोड करना

बड़ी फ़ाइलों के लिए या एक ही इमेज फ़ाइल का बार-बार इस्तेमाल करने के लिए, फ़ाइल एपीआई का इस्तेमाल करें. इस कोड में, एक इमेज फ़ाइल अपलोड की जाती है. इसके बाद, `generateContent` को कॉल करने के लिए इस फ़ाइल का इस्तेमाल किया जाता है. ज़्यादा जानकारी और उदाहरणों के लिए, [Files API की गाइड](https://ai.google.dev/gemini-api/docs/files?hl=hi) देखें.

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

### ऐप पर जाएं

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

## एक से ज़्यादा इमेज का इस्तेमाल करके प्रॉम्प्ट देना

एक ही प्रॉम्प्ट में कई इमेज दी जा सकती हैं. इसके लिए, `contents` ऐरे में कई इमेज `Part` ऑब्जेक्ट शामिल करें. ये इनलाइन डेटा (स्थानीय फ़ाइलें या यूआरएल) और File API रेफ़रंस का मिक्सचर हो सकते हैं.

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

### ऐप पर जाएं

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

## ऑब्जेक्ट का पता लगाने की सुविधा

मॉडल को इस तरह से ट्रेन किया जाता है कि वे किसी इमेज में मौजूद ऑब्जेक्ट का पता लगा सकें और उनके बाउंडिंग बॉक्स के निर्देशांक पा सकें. इमेज के डाइमेंशन के हिसाब से कोऑर्डिनेट, [0, 1000] के स्केल पर होते हैं. आपको अपनी मूल इमेज के साइज़ के आधार पर, इन कोऑर्डिनेट को कम करना होगा.

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

### ऐप पर जाएं

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

  fmt.Printf("Image size: %d %d\n", width, height)
  fmt.Println("Bounding boxes:")
  for _, box := range boundingBoxes {
    if len(box.Box2D) == 4 {
      absY1 := int(float64(box.Box2D[0]) / 1000.0 * float64(height))
      absX1 := int(float64(box.Box2D[1]) / 1000.0 * float64(width))
      absY2 := int(float64(box.Box2D[2]) / 1000.0 * float64(height))
      absX2 := int(float64(box.Box2D[3]) / 1000.0 * float64(width))
      fmt.Printf("- %s: [%d, %d, %d, %d]\n", box.Label, absX1, absY1, absX2, absY2)
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
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

ज़्यादा उदाहरणों के लिए, [Gemini कुकबुक](https://github.com/google-gemini/cookbook) में मौजूद ये नोटबुक देखें:

- [2D स्पेशल अंडरस्टैंडिंग नोटबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=hi)
- [एक्सपेरिमेंट के तौर पर उपलब्ध 3D पॉइंटिंग नोटबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=hi)

## Google Images पर काम करने वाले फ़ॉर्मैट

Gemini में, इस तरह के इमेज फ़ॉर्मैट वाले एमआईएमई टाइप इस्तेमाल किए जा सकते हैं:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

फ़ाइल इनपुट करने के अन्य तरीकों के बारे में जानने के लिए, [फ़ाइल इनपुट करने के तरीके](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi) गाइड देखें.

## क्षमताएं

Gemini के सभी मॉडल वर्शन मल्टीमॉडल हैं. इनका इस्तेमाल, इमेज प्रोसेसिंग और कंप्यूटर विज़न से जुड़े कई कामों के लिए किया जा सकता है. जैसे, इमेज के लिए कैप्शन जनरेट करना, विज़ुअल से जुड़े सवालों के जवाब देना, इमेज को कैटगरी में बांटना, और ऑब्जेक्ट का पता लगाना. हालांकि, इनके अलावा और भी काम किए जा सकते हैं.

Gemini, आपकी क्वालिटी और परफ़ॉर्मेंस की ज़रूरतों के हिसाब से, खास एमएल मॉडल के इस्तेमाल को कम कर सकता है.

मॉडल के नए वर्शन को खास तौर पर, सामान्य कामों के साथ-साथ खास कामों को ज़्यादा सटीक तरीके से करने के लिए ट्रेन किया गया है. जैसे, [ऑब्जेक्ट का पता लगाने की सुविधा](#object-detection).

## सीमाएं और मुख्य तकनीकी जानकारी

### फ़ाइल की सीमा

Gemini मॉडल, हर अनुरोध के लिए ज़्यादा से ज़्यादा 3,600 इमेज फ़ाइलें इस्तेमाल कर सकते हैं.

### टोकन की गिनती

- अगर दोनों डाइमेंशन 384 पिक्सल से कम या इसके बराबर हैं, तो 258 टोकन.
  बड़ी इमेज को 768x768 पिक्सल वाली टाइल में बांटा जाता है. हर टाइल की कीमत 258 टोकन होती है.

टाइल की संख्या कैलकुलेट करने का सामान्य फ़ॉर्मूला यहां दिया गया है:

- क्रॉप यूनिट के साइज़ का हिसाब लगाएं. यह साइज़, फ़्लोर(min(चौड़ाई, ऊंचाई) / 1.5) के आस-पास होता है.
- टाइल की संख्या पाने के लिए, हर डाइमेंशन को क्रॉप यूनिट के साइज़ से भाग दें और फिर उन्हें आपस में गुणा करें.

उदाहरण के लिए, 960x540 डाइमेंशन वाली इमेज के लिए, क्रॉप यूनिट का साइज़ 360 होगा. हर डाइमेंशन को 360 से भाग दें. टाइल की संख्या 3 \* 2 = 6 है.

### मीडिया रिज़ॉल्यूशन

Gemini 3 में, मल्टीमॉडल विज़न प्रोसेसिंग को ज़्यादा बारीकी से कंट्रोल करने की सुविधा मिलती है. इसके लिए, `media_resolution` पैरामीटर का इस्तेमाल किया जाता है. `media_resolution` पैरामीटर से यह तय होता है कि **हर इनपुट इमेज या वीडियो फ़्रेम के लिए ज़्यादा से ज़्यादा कितने टोकन असाइन किए जा सकते हैं.**
ज़्यादा रिज़ॉल्यूशन से, मॉडल को छोटे टेक्स्ट को पढ़ने या छोटी-छोटी बारीकियों को पहचानने में मदद मिलती है. हालांकि, इससे टोकन का इस्तेमाल और इंतज़ार का समय बढ़ जाता है.

पैरामीटर और इससे टोकन की गिनती पर पड़ने वाले असर के बारे में ज़्यादा जानने के लिए, [मीडिया रिज़ॉल्यूशन](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=hi) गाइड देखें.

## सलाह और सबसे सही तरीके

- पुष्टि करें कि इमेज सही तरीके से घुमाई गई हों.
- साफ़ और बिना धुंधली इमेज का इस्तेमाल करें.
- टेक्स्ट वाली किसी एक इमेज का इस्तेमाल करते समय, `contents` ऐरे में इमेज वाले हिस्से के *बाद* टेक्स्ट प्रॉम्प्ट डालें.

## आगे क्या करना है

इस गाइड में, इमेज फ़ाइलें अपलोड करने और इमेज इनपुट से टेक्स्ट आउटपुट जनरेट करने का तरीका बताया गया है. ज़्यादा जानने के लिए, यहां दिए गए संसाधन देखें:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi): Gemini के साथ इस्तेमाल करने के लिए, फ़ाइलें अपलोड करने और उन्हें मैनेज करने के बारे में ज़्यादा जानें.
- [सिस्टम के लिए निर्देश](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#system-instructions):
  सिस्टम के लिए निर्देश देने की सुविधा की मदद से, अपनी खास ज़रूरतों और इस्तेमाल के उदाहरणों के आधार पर, मॉडल के व्यवहार को कंट्रोल किया जा सकता है.
- [फ़ाइल प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide): Gemini API, टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा देता है. इसे मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सुरक्षा से जुड़ी गाइडलाइन](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=hi): कभी-कभी जनरेटिव एआई मॉडल से ऐसे आउटपुट मिलते हैं जिनकी उम्मीद नहीं होती. जैसे, गलत, पक्षपात करने वाले या आपत्तिजनक आउटपुट. इस तरह के आउटपुट से होने वाले नुकसान के जोखिम को कम करने के लिए, पोस्ट-प्रोसेसिंग और मैन्युअल तरीके से आकलन करना ज़रूरी है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-24 (UTC) को अपडेट किया गया."],[],[]]
