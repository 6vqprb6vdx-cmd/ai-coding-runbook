---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=th
fetched_at: 2026-09-28T06:21:15.275043+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e02\u0e2d\u0e07\u0e2a\u0e37\u0e48\u0e2d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ความละเอียดของสื่อ

พารามิเตอร์ `media_resolution` จะควบคุมวิธีที่ Gemini API ประมวลผลอินพุตสื่อ เช่น รูปภาพ วิดีโอ เสียง และเอกสาร PDF โดยการกำหนด**จำนวนโทเค็นสูงสุด**ที่จัดสรรสำหรับอินพุตสื่อ ซึ่งจะช่วยให้คุณปรับสมดุลคุณภาพของคำตอบกับเวลาในการตอบสนองและค่าใช้จ่ายได้ แม้ว่าอินพุตภาพและเอกสารจะปรับขนาดการจัดสรรโทเค็นตามการตั้งค่าความละเอียด แต่อินพุตเสียงจะแปลงเป็นโทเค็นในอัตราคงที่ต่อวินาทีในทุกระดับความละเอียด ดูค่าเริ่มต้นและการเชื่อมโยงกับโทเค็นของการตั้งค่าต่างๆ ได้ที่ส่วน[จำนวนโทเค็น](#token-counts)

คุณสามารถกำหนดค่าความละเอียดของสื่อสำหรับออบเจ็กต์สื่อแต่ละรายการ (รายการเนื้อหา) ภายในคำขอ (Gemini 3 เท่านั้น)

## ความละเอียดของสื่อต่อรายการเนื้อหา (Gemini 3 เท่านั้น)

Gemini 3 ช่วยให้คุณตั้งค่าความละเอียดของสื่อสำหรับออบเจ็กต์สื่อแต่ละรายการภายในคำขอได้ ซึ่งจะช่วยเพิ่มประสิทธิภาพการใช้โทเค็นได้อย่างละเอียด คุณสามารถผสมระดับความละเอียดในคำขอเดียวได้ เช่น ใช้ความละเอียดสูงสำหรับไดอะแกรมที่ซับซ้อน และใช้ความละเอียดต่ำสำหรับรูปภาพตามบริบทอย่างง่าย

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

### JavaScript

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

### REST

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

## ค่าความละเอียดที่ใช้ได้

Gemini API กำหนดระดับความละเอียดของสื่อดังต่อไปนี้

- `unspecified`: การตั้งค่าเริ่มต้น จำนวนโทเค็นสำหรับระดับนี้จะแตกต่างกันอย่างมากระหว่าง Gemini 3 กับโมเดล Gemini รุ่นก่อนหน้า
- `low`: จำนวนโทเค็นน้อยลง ส่งผลให้ประมวลผลได้เร็วขึ้นและมีต้นทุนต่ำลง แต่มีรายละเอียดน้อยลง
- `medium`: ความสมดุลระหว่างรายละเอียด ต้นทุน และเวลาในการตอบสนอง
- `high`: จำนวนโทเค็นที่สูงขึ้น ซึ่งให้รายละเอียดเพิ่มเติมแก่โมเดลในการทำงาน แต่จะทำให้เวลาในการตอบสนองและค่าใช้จ่ายเพิ่มขึ้น
- `ultra_high` (ต่อรายการเนื้อหาเท่านั้น): จำนวนโทเค็นสูงสุดที่จำเป็นสำหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น [การใช้งานคอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

โปรดทราบว่า `high` ให้ประสิทธิภาพสูงสุดสำหรับ Use Case ส่วนใหญ่

จำนวนโทเค็นที่แน่นอนซึ่งสร้างขึ้นสำหรับแต่ละระดับจะขึ้นอยู่กับทั้ง**ประเภทสื่อ** (รูปภาพ วิดีโอ เสียง PDF) และ**เวอร์ชันโมเดล**

## จำนวนโทเค็น

ตารางด้านล่างสรุปจำนวนโทเค็นโดยประมาณสำหรับค่า `media_resolution` และประเภทสื่อแต่ละรายการต่อตระกูลโมเดล

**โมเดล Gemini 3**

| MediaResolution | รูปภาพ | วิดีโอ | เสียง | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (ค่าเริ่มต้น) | 1120 | 70 | 25 (ต่อวินาที) | 560 |
| `low` | 280 | 70 | 25 (ต่อวินาที) | 280 + ข้อความเนทีฟ |
| `medium` | 560 | 70 | 25 (ต่อวินาที) | 560 + ข้อความเนทีฟ |
| `high` | 1120 | 280 | 25 (ต่อวินาที) | 1120 + ข้อความเนทีฟ |
| `ultra_high` | 2240 | ไม่มี | ไม่มี | ไม่มี |

## การเลือกความละเอียดที่เหมาะสม

- **ค่าเริ่มต้น (`unspecified`):** เริ่มต้นด้วยค่าเริ่มต้น โดยได้รับการปรับแต่งให้มีความสมดุลที่ดีระหว่างคุณภาพ เวลาในการตอบสนอง และต้นทุนสำหรับกรณีการใช้งานที่พบบ่อยที่สุด
- **`low`:** ใช้ในสถานการณ์ที่ต้นทุนและเวลาในการตอบสนองมีความสำคัญสูงสุด และรายละเอียดแบบละเอียดมีความสำคัญน้อยกว่า
- **`medium` / `high`:** เพิ่มความละเอียดเมื่องานต้องทำความเข้าใจรายละเอียดที่ซับซ้อนภายในสื่อ ซึ่งมักจำเป็นสำหรับการวิเคราะห์ภาพที่ซับซ้อน การอ่านแผนภูมิ หรือการทำความเข้าใจเอกสารที่มีข้อมูลหนาแน่น
- **`ultra_high`** - ใช้ได้กับการตั้งค่าต่อรายการเนื้อหาเท่านั้น แนะนําสําหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น การใช้คอมพิวเตอร์ หรือในกรณีที่การทดสอบแสดงให้เห็นว่ามีการปรับปรุงที่ชัดเจนเมื่อเทียบกับ `high`
- **การควบคุมต่อรายการเนื้อหา (Gemini 3):** เพิ่มประสิทธิภาพการใช้โทเค็น เช่น ในพรอมต์ที่มีรูปภาพหลายรูป ให้ใช้ `high` สำหรับไดอะแกรมที่ซับซ้อน และ `low` หรือ `medium` สำหรับรูปภาพตามบริบทที่เรียบง่ายกว่า

**การตั้งค่าที่แนะนำ**

รายการต่อไปนี้คือการตั้งค่าความละเอียดของสื่อที่แนะนำสำหรับสื่อแต่ละประเภทที่รองรับ

| ประเภทสื่อ | การตั้งค่าที่แนะนำ | โทเค็นสูงสุด | คำแนะนำในการใช้งาน |
| --- | --- | --- | --- |
| **รูปภาพ** | `high` | 1120 | แนะนำสำหรับงานวิเคราะห์รูปภาพส่วนใหญ่เพื่อให้มั่นใจว่ามีคุณภาพสูงสุด |
| **PDF** | `medium` | 560 | เหมาะสำหรับการทำความเข้าใจเอกสาร โดยปกติคุณภาพจะอิ่มตัวที่ `medium` การเพิ่มเป็น `high` แทบจะไม่ช่วยปรับปรุงผลลัพธ์ OCR สำหรับเอกสารมาตรฐาน |
| **วิดีโอ** (ทั่วไป) | `low` (หรือ `medium`) | 70 (ต่อเฟรม) | **หมายเหตุ:** สำหรับวิดีโอ ระบบจะถือว่าการตั้งค่า `low` และ `medium` เหมือนกัน (70 โทเค็น) เพื่อเพิ่มประสิทธิภาพการใช้บริบท ซึ่งเพียงพอสำหรับงานการจดจำและการอธิบายการกระทำส่วนใหญ่ |
| **วิดีโอ** (มีข้อความจำนวนมาก) | `high` | 280 (ต่อเฟรม) | จำเป็นเฉพาะเมื่อ Use Case เกี่ยวข้องกับการอ่านข้อความหนาแน่น (OCR) หรือรายละเอียดเล็กๆ ภายในเฟรมวิดีโอ |
| **เสียง** | `unspecified` (ค่าเริ่มต้น) | 25 (ต่อวินาที) | ระบบจะแปลงเสียงเป็นโทเค็นในอัตราคงที่ 25 โทเค็นต่อวินาทีในการตั้งค่าความละเอียดที่รองรับทั้งหมด (`unspecified`, `low`, `medium` และ `high`) |

โปรดทดสอบและประเมินผลกระทบของการตั้งค่าความละเอียดต่างๆ ในแอปพลิเคชันเสมอ เพื่อหาจุดสมดุลที่ดีที่สุดระหว่างคุณภาพ เวลาในการตอบสนอง และต้นทุน

## ความสัมพันธ์กับโหมดการประมวลผลวิดีโอ

พารามิเตอร์ `media_resolution` และการประมวลผลจะควบคุมลักษณะต่างๆ ของอินพุตวิดีโอ ดังนี้

- `media_resolution` ควบคุม**ความละเอียด**ของแต่ละเฟรม (จำนวนโทเค็นต่อเฟรม)
- ปุ่มควบคุม `processing` / `media_processing` จะกำหนด**เนื้อหาจากวิดีโอ**ที่จะโหลดลงในบริบท

คุณตั้งค่าทั้ง 2 อย่างได้ในอินพุตวิดีโอเดียวกัน เช่น คุณอาจใช้การประมวลผลแบบเอเจนต์ที่มีความละเอียดของสื่อต่ำเพื่อลดการใช้โทเค็นทั้งหมดสำหรับวิดีโอยาว

ดูรายละเอียดเกี่ยวกับโหมดการประมวลผลวิดีโอได้ในคู่มือ[การทำความเข้าใจวิดีโอแบบเอเจนต์](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#agentic-video-understanding)

## สรุปความเข้ากันได้ของเวอร์ชัน

- การตั้งค่า `resolution` ในเนื้อหาแต่ละรายการ**ใช้ได้กับโมเดล Gemini 3 เท่านั้น**

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับความสามารถแบบมัลติโมดัลของ Gemini API ได้ในคำแนะนำเกี่ยวกับ
  [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th)
  [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th) [การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)
  และ[การทำความเข้าใจเอกสาร](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
