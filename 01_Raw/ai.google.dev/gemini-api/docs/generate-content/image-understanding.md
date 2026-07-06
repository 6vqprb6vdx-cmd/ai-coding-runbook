---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=tr
fetched_at: 2026-07-06T05:11:18.582536+00:00
title: "G\u00f6r\u00fcnt\u00fc anlama \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Görüntü anlama

Gemini modelleri, baştan aşağı çok formatlı olacak şekilde tasarlanmıştır. Bu sayede, özel makine öğrenimi modelleri eğitmenize gerek kalmadan görüntü açıklaması, sınıflandırma ve görsel soru yanıtlama gibi görüntü işleme ve bilgisayarla görme görevlerini yerine getirebilirsiniz.

Gemini modelleri, genel çok formatlı özelliklerinin yanı sıra ek eğitim sayesinde [nesne tespit etme](#object-detection) gibi belirli kullanım alanlarında **daha yüksek doğruluk** sunar.

## Gemini'a görüntü aktarma

Gemini'a giriş olarak iki yöntemle resim sağlayabilirsiniz:

- [Satır içi resim verilerini iletme](#inline-image): Daha küçük dosyalar için idealdir (istemler dahil olmak üzere toplam istek boyutu 20 MB'tan az olmalıdır).
- [File API'yi kullanarak resim yükleme](#upload-image): Daha büyük dosyalar veya resimleri birden fazla istekte yeniden kullanmak için önerilir.

### Satır içi görüntü verilerini iletme

Satır içi resim verilerini `generateContent` isteğinde iletebilirsiniz. Görüntü verilerini Base64 kodlu dizeler olarak veya doğrudan yerel dosyaları okuyarak (dile bağlı olarak) sağlayabilirsiniz.

Aşağıdaki örnekte, yerel bir dosyadan nasıl resim okunacağı ve işlenmesi için `generateContent` API'ye nasıl aktarılacağı gösterilmektedir.

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

Ayrıca bir URL'den resim getirebilir, bunu baytlara dönüştürebilir ve aşağıdaki örneklerde gösterildiği gibi `generateContent`'ye iletebilirsiniz.

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

### File API'yi kullanarak resim yükleme

Büyük dosyalar için veya aynı resim dosyasını tekrar tekrar kullanabilmek için Files API'yi kullanın. Aşağıdaki kod, bir resim dosyasını yükler ve ardından dosyayı `generateContent` çağrısında kullanır. Daha fazla bilgi ve örnek için [Files API kılavuzuna](https://ai.google.dev/gemini-api/docs/files?hl=tr) bakın.

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

## Birden fazla resimle istem oluşturma

`contents` dizisine birden fazla resim `Part` nesnesi ekleyerek tek bir istemde birden fazla resim sağlayabilirsiniz. Bunlar satır içi veriler (yerel dosyalar veya URL'ler) ve File API referanslarının bir karışımı olabilir.

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

## Nesne algılama

Modeller, bir görüntüdeki nesneleri algılayıp sınırlayıcı kutu koordinatlarını almak için eğitilir. Görüntü boyutlarına göre koordinatlar [0, 1000] ölçeğine göre ayarlanır. Bu koordinatları orijinal resim boyutunuza göre ölçeklendirmeniz gerekir.

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

Daha fazla örnek için [Gemini Cookbook](https://github.com/google-gemini/cookbook)'taki aşağıdaki not defterlerine göz atın:

- [2D mekansal anlama not defteri](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=tr)
- [Deneysel 3D işaretleme not defteri](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=tr)

## Desteklenen görsel biçimleri

Gemini aşağıdaki resim biçimi MIME türlerini destekler:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Diğer dosya giriş yöntemleri hakkında bilgi edinmek için [Dosya giriş yöntemleri](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr) kılavuzuna bakın.

## Özellikler

Tüm Gemini modeli sürümleri çok formatlıdır ve görüntü açıklaması oluşturma, görsel soru ve yanıtlama, görüntü sınıflandırma ve nesne tespit etme dahil ancak bunlarla sınırlı olmamak üzere çeşitli görüntü işleme ve bilgisayarla görme görevlerinde kullanılabilir.

Gemini, kalite ve performans gereksinimlerinize bağlı olarak özel ML modelleri kullanma ihtiyacını azaltabilir.

En yeni model sürümleri, [nesne tespit etme](#object-detection) gibi genel özelliklerin yanı sıra uzmanlık gerektiren görevlerin doğruluğunu artırmak için özel olarak eğitilmiştir.

## Sınırlamalar ve temel teknik bilgiler

### Dosya sınırı

Gemini modelleri,istek başına en fazla 3.600 resim dosyasını destekler.

### Jeton hesaplaması

- Her iki boyut da <= 384 piksel ise 258 jeton.
  Daha büyük resimler, her biri 258 jeton değerinde olan 768x768 piksellik bloklar halinde düzenlenir.

Döşeme sayısını hesaplamak için kullanılan yaklaşık formül şöyledir:

- Kırpma birimi boyutunu hesaplayın. Bu boyut yaklaşık olarak floor(min(width, height) / 1.5) olur.
- Her boyutu kırpma birimi boyutuna bölün ve döşeme sayısını elde etmek için sonuçları çarpın.

Örneğin, 960x540 boyutlarındaki bir resmin kırpma birimi boyutu 360 olur. Her boyutu 360'a bölün. Döşeme sayısı 3 \* 2 = 6 olur.

### Medya çözünürlüğü

Gemini 3, `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol sunar. `media_resolution` parametresi, **giriş resmi veya video karesi başına ayrılan maksimum jeton sayısını** belirler.
Daha yüksek çözünürlükler, modelin küçük metinleri okuma veya küçük ayrıntıları tanımlama becerisini artırır ancak jeton kullanımını ve gecikmeyi de artırır.

Parametre ve jeton hesaplamalarını nasıl etkileyebileceği hakkında daha fazla bilgi için [medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=tr) kılavuzuna bakın.

## İpuçları ve en iyi uygulamalar

- Resimlerin doğru şekilde döndürüldüğünü doğrulayın.
- Net ve bulanık olmayan resimler kullanın.
- Metin içeren tek bir resim kullanırken metin istemini `contents` dizisinde resim kısmının *sonrasına* yerleştirin.

## Sırada ne var?

Bu kılavuzda, resim dosyalarını nasıl yükleyeceğiniz ve resim girişlerinden nasıl metin çıkışları oluşturacağınız açıklanmaktadır. Daha fazla bilgi edinmek için aşağıdaki kaynakları inceleyin:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr): Gemini ile kullanılacak dosyaları yükleme ve yönetme hakkında daha fazla bilgi edinin.
- [Sistem talimatları](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#system-instructions):
  Sistem talimatları, modelin davranışını özel ihtiyaçlarınıza ve kullanım alanlarınıza göre yönlendirmenizi sağlar.
- [Dosya istemi stratejileri](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide): Gemini API, çok formatlı istem olarak da bilinen metin, resim, ses ve video verileriyle istemi destekler.
- [Güvenlik yönergeleri](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=tr): Üretken yapay zeka modelleri bazen yanlış, taraflı veya rahatsız edici gibi beklenmedik çıkışlar üretebilir. Bu tür çıkışlardan kaynaklanan zarar riskini sınırlamak için sonradan işleme ve insan değerlendirmesi gereklidir.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-24 UTC."],[],[]]
