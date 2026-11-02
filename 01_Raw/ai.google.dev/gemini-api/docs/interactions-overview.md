---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th
fetched_at: 2026-11-02T07:29:30.966376+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Interactions API

Interactions API เป็นวิธีที่ดีที่สุดในการสร้างสรรค์ด้วยโมเดลและ Agent ของ Gemini โดยจะพร้อมให้บริการโดยทั่วไปและแนะนำให้ใช้กับโปรเจ็กต์ใหม่ทั้งหมดตั้งแต่เดือนมิถุนายน 2026 เป็นต้นไป แม้ว่าตอนนี้จะถือว่าเป็น API รุ่นเก่าแล้ว แต่ API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=th)เดิมยังคงได้รับการสนับสนุนอย่างเต็มรูปแบบ

## เหตุใดจึงต้องใช้ Interactions API

- **อินเทอร์เฟซสากลสำหรับแอปพลิเคชันทั้งหมด**: ออกแบบมาให้เป็นอินเทอร์เฟซมาตรฐาน
  สำหรับกรณีการใช้งานทุกกรณี รวมถึงการสร้างข้อความแบบครั้งเดียว
  การทำความเข้าใจแบบมัลติโมดัล เอาต์พุตที่มีโครงสร้าง การจัดระเบียบเครื่องมือ และ
  เวิร์กโฟลว์แบบ Agent
- **API เดียวสำหรับโมเดลและ Agent**: ปลายทางและรูปแบบที่รวมเป็นหนึ่งเดียวสำหรับการ
  เรียกโมเดล Gemini มาตรฐาน รวมถึง Agent เฉพาะทางโดยตรง (เช่น
  Deep Research และ Agent ที่มีการจัดการที่กำหนดเอง)
- **ความสามารถใหม่ที่พร้อมใช้งาน**: ฟีเจอร์ต่างๆ เช่น สถานะการสนทนาฝั่งเซิร์ฟเวอร์ที่ไม่บังคับโดยใช้ `previous_interaction_id`, ขั้นตอนการดำเนินการที่สังเกตได้สำหรับการแก้ไขข้อบกพร่องและการแสดงผล UI รวมถึง[การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)สำหรับงานที่ใช้เวลานานโดยใช้ `background=true`
- **ต้นทุนที่ต่ำลงด้วยอัตราการเข้าถึงแคชที่สูงขึ้น**: เมื่อใช้การสนทนาแบบหลายรอบ
  การจัดการสถานะฝั่งเซิร์ฟเวอร์ที่ไม่บังคับจะช่วยให้การแคชบริบทมีประสิทธิภาพมากขึ้นในแต่ละรอบ ซึ่งช่วยลดต้นทุนโทเค็น
- **ตำแหน่งที่จะเปิดตัวฟีเจอร์ใหม่**: ในอนาคต โมเดลใหม่ทั้งหมด ความสามารถแบบมัลติโมดัล
  เครื่องมือ และฟีเจอร์แบบ Agent จะเปิดตัวใน Interactions
  API

โดยค่าเริ่มต้น Interactions API จะจัดเก็บคำขอเพื่อให้คุณใช้ประโยชน์จากฟีเจอร์การจัดการสถานะฝั่งเซิร์ฟเวอร์ได้โดยใช้ `previous_interaction_id` คุณเลือกใช้ลักษณะการทำงานแบบไม่เก็บสถานะได้โดยตั้งค่า `store=false` ดูรายละเอียดได้ในส่วน[การเก็บรักษาข้อมูล](#data-storage-retention)

## เริ่มต้นใช้งาน

- **ตั้งค่า Agent การเขียนโค้ด**: เชื่อมต่อกับ **Gemini Docs MCP** และติดตั้ง
  ทักษะ `gemini-api-dev` เพื่อให้ Assistant เข้าถึงเอกสารสำหรับนักพัฒนาแอปและแนวทางปฏิบัติแนะนำล่าสุดได้โดยตรง ดูขั้นตอนโดยละเอียดได้ใน
  [คู่มือการตั้งค่า Agent การเขียนโค้ด](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)
- **ย้ายข้อมูลจาก `generateContent`**: หากคุณมีการผสานรวมอยู่แล้ว ให้ทำตาม[คำแนะนำในการย้ายข้อมูล](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=th)เพื่อเปลี่ยนไปใช้ Interactions API
- **เริ่มต้นใช้งาน**: ทำตามขั้นตอนในคู่มือ[เริ่มต้นใช้งาน Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=th)

### คำแนะนำฟีเจอร์

สำรวจความสามารถเฉพาะของ Interactions API ผ่านคำแนะนำเหล่านี้ คุณสามารถใช้ปุ่มเปิด/ปิดในหน้าเว็บเหล่านี้เพื่อสลับระหว่าง generateContent กับ Interactions API ได้

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)
- [การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)
- [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th)
- [การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)
- [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th)
- [การประมวลผลเอกสาร](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)
- [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
- [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)
- [Agent Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th)
- [Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)
- [Priority Inference](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)

## วิธีการทำงานของ Interactions API

Interactions API มุ่งเน้นไปที่ทรัพยากรหลักอย่าง [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=th#Resource:Interaction) `Interaction` แสดงถึงรอบที่สมบูรณ์ในการสนทนาหรือภารกิจ โดยทำหน้าที่เป็นบันทึกเซสชัน ซึ่งมีประวัติทั้งหมดของการโต้ตอบเป็นลำดับตามเวลาของ**ขั้นตอนการดำเนินการ** ขั้นตอนเหล่านี้รวมถึงความคิดของโมเดล การเรียกใช้เครื่องมือฝั่งเซิร์ฟเวอร์หรือฝั่งไคลเอ็นต์และผลลัพธ์ (เช่น `function_call` และ `function_result`) รวมถึง `model_output` สุดท้าย ทรัพยากรที่จัดเก็บไว้ (ดึงข้อมูลผ่าน `interactions.get`) ยังรวมถึงขั้นตอน `user_input` สำหรับบริบททั้งหมดด้วย แม้ว่าการตอบกลับ `interactions.create` จะแสดงเฉพาะขั้นตอนที่โมเดลสร้างขึ้น

เมื่อคุณเรียกใช้
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=th#CreateInteraction) คุณกำลัง
สร้างทรัพยากร `Interaction` ใหม่:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
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
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
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
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### การจัดการสถานะฝั่งเซิร์ฟเวอร์

คุณสามารถใช้ `id` ของการโต้ตอบที่เสร็จสมบูรณ์แล้วในการเรียกใช้ครั้งถัดไปโดยใช้
`previous_interaction_id` เพื่อสนทนาต่อ เซิร์ฟเวอร์จะใช้รหัสนี้เพื่อดึงข้อมูลประวัติการสนทนา ซึ่งช่วยให้คุณไม่ต้องส่งประวัติการแชททั้งหมดอีกครั้ง

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
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

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
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

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

พารามิเตอร์ `previous_interaction_id` จะเก็บเฉพาะประวัติการสนทนา (อินพุตและเอาต์พุต) โดยใช้ `previous_interaction_id` ส่วนพารามิเตอร์อื่นๆ จะมี**ขอบเขตการโต้ตอบ** และใช้ได้กับการโต้ตอบเฉพาะที่คุณกำลังสร้างเท่านั้น

- `tools`
- `system_instruction`
- `generation_config` (รวมถึง `thinking_level`, `temperature` ฯลฯ)

ซึ่งหมายความว่าคุณต้องระบุพารามิเตอร์เหล่านี้อีกครั้งในการโต้ตอบใหม่แต่ละครั้งหากต้องการให้พารามิเตอร์มีผล การจัดการสถานะฝั่งเซิร์ฟเวอร์นี้เป็นตัวเลือก คุณยังสามารถทำงานในโหมดไม่เก็บสถานะได้โดยส่งประวัติการสนทนาทั้งหมดในคำขอแต่ละรายการ

### การจัดเก็บและการเก็บรักษาข้อมูล

โดยค่าเริ่มต้น API จะจัดเก็บออบเจ็กต์ Interaction ทั้งหมด (`store=true`) เพื่อ
ลดความซับซ้อนในการใช้ฟีเจอร์การจัดการสถานะฝั่งเซิร์ฟเวอร์ (ด้วย
`previous_interaction_id`) [การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th) (โดยใช้ `background=true`) และ
เพื่อวัตถุประสงค์ในการสังเกต

- **ระดับแบบชำระเงิน**: ระบบจะเก็บรักษาการโต้ตอบไว้เป็นเวลา **55 วัน**
- **รุ่นฟรี**: ระบบจะเก็บรักษาการโต้ตอบไว้เป็นเวลา **1 วัน**

หากไม่ต้องการให้เป็นเช่นนี้ คุณสามารถตั้งค่า `store=false` ในคำขอได้ การควบคุมนี้แยกจากการจัดการสถานะ คุณสามารถเลือกไม่จัดเก็บการโต้ตอบใดก็ได้ อย่างไรก็ตาม โปรดทราบว่า
`store=false` ไม่เข้ากันกับ [การดำเนินการเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th) และป้องกันไม่ให้ใช้
`previous_interaction_id` ในรอบถัดไป

สำหรับโปรเจ็กต์ระดับแบบชำระเงิน คุณสามารถกำหนดค่าหน้าต่างการเก็บรักษาใน
[AI Studio](https://aistudio.google.com/logs?hl=th) เพื่อทำเครื่องหมายบันทึกสำหรับการ
ลบออกจากพื้นที่เก็บข้อมูลของโปรเจ็กต์โดยอัตโนมัติหลังจากผ่านไป 7, 14, 28 หรือ 55 วัน การเก็บรักษาที่สั้นลงอาจส่งผลต่อการดึงข้อมูลการสนทนาที่ผ่านมา

คุณสามารถลบการโต้ตอบที่จัดเก็บไว้ได้ทุกเมื่อโดยใช้วิธี
[`delete`](https://ai.google.dev/api/interactions-api?hl=th#deleteInteraction) ผ่านโปรแกรม
ซึ่งต้องใช้รหัสการโต้ตอบ นอกจากนี้ คุณยังดูและจัดการบันทึกการโต้ตอบที่จัดเก็บไว้
รวมถึงการลบออกจากพื้นที่เก็บข้อมูลของโปรเจ็กต์ได้ใน
[AI Studio](https://aistudio.google.com/logs?hl=th)

หลังจากระยะเวลาการเก็บรักษาหมดลง ระบบจะลบข้อมูลของคุณโดยอัตโนมัติ

ระบบจะประมวลผลออบเจ็กต์ Interactions ตาม [ข้อกำหนด](https://ai.google.dev/gemini-api/terms?hl=th)

### ดูการโต้ตอบใน AI Studio

API จะจัดเก็บคำขอ Interactions API ที่ดำเนินการด้วย `store=true` สำหรับโปรเจ็กต์ในระดับแบบชำระเงิน คุณสามารถดูคำขอเหล่านี้ได้โดยตรงจากหน้า
[บันทึกใน Google AI Studio](https://aistudio.google.com/logs?hl=th) ดูข้อมูลเพิ่มเติมได้ในคู่มือ
[บันทึก](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th)

## แนวทางปฏิบัติแนะนำ

- **อัตราการเข้าถึงแคช**: ระบบรองรับการแคชโดยนัยทั้งในโหมดมีสถานะและ
  ไม่มีสถานะ (ดู
  [Quickstart](https://ai.google.dev/gemini-api/docs/get-started?hl=th#4_multi-turn_conversations)) การใช้ `previous_interaction_id` (มีสถานะ) เพื่อสนทนาต่อช่วยให้ระบบใช้การแคชโดยนัยสำหรับประวัติการสนทนาได้ง่ายขึ้น ซึ่งจะช่วยปรับปรุงประสิทธิภาพและลดต้นทุน
- **การโต้ตอบแบบผสม**: คุณสามารถผสมและจับคู่การโต้ตอบของ Agent และ
  โมเดลในการสนทนาได้ตามต้องการ ตัวอย่างเช่น คุณสามารถใช้ Agent เฉพาะทาง เช่น Agent Deep Research สำหรับการเก็บรวบรวมข้อมูลเบื้องต้น แล้วใช้โมเดล Gemini มาตรฐานสำหรับงานติดตามผล เช่น การสรุปหรือการจัดรูปแบบใหม่ โดยลิงก์ขั้นตอนเหล่านี้ด้วย `previous_interaction_id`

## โมเดลและ Agent ที่รองรับ

| ชื่อโมเดล | ประเภท | รหัสโมเดล |
| --- | --- | --- |
| Gemini 4 Argon | โมเดล | `gemini-4-argon` |
| Gemini 3.8 Flash | โมเดล | `gemini-3.8-flash` |
| Gemini 3.6 Flash | โมเดล | `gemini-3.6-flash` |
| Gemini 3.1 Pro (เวอร์ชันตัวอย่าง) | โมเดล | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | โมเดล | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | โมเดล | `gemini-3.1-flash-lite` |
| Gemini 3 Flash (เวอร์ชันตัวอย่าง) | โมเดล | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | โมเดล | `gemini-2.5-pro` |
| Gemini 2.5 Flash | โมเดล | `gemini-2.5-flash` |
| Gemini 2.5 Flash-Lite | โมเดล | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | โมเดล | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | โมเดล | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS (เวอร์ชันตัวอย่าง) | โมเดล | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | โมเดล | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | โมเดล | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | โมเดล | `lyria-3.5` |
| Lyria 3 Clip (เวอร์ชันตัวอย่าง) | โมเดล | `lyria-3-clip-preview` |
| Lyria 3 Pro (เวอร์ชันตัวอย่าง) | โมเดล | `lyria-3-pro-preview` |
| Deep Research (เวอร์ชันตัวอย่าง) | Agent | `deep-research-preview-04-2026` |
| Deep Research (เวอร์ชันตัวอย่าง) | Agent | `deep-research-max-preview-04-2026` |
| Antigravity (เวอร์ชันตัวอย่าง) | Agent | `antigravity-preview-09-2026` |

## SDK

คุณสามารถใช้ Google GenAI SDK เวอร์ชันล่าสุดเพื่อเข้าถึง Interactions API ได้

- ใน Python คือแพ็กเกจ `google-genai` เวอร์ชัน `2.3.0` ขึ้นไป
- ใน JavaScript คือแพ็กเกจ `@google/genai` เวอร์ชัน `2.3.0` ขึ้นไป
- ใน Go คือแพ็กเกจ `google.golang.org/genai`
- ใน Java คือแพ็กเกจ `com.google.genai:google-genai`

ดูข้อมูลเพิ่มเติมเกี่ยวกับวิธีติดตั้ง SDK ได้ในหน้า
[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

## ข้อจำกัด

- **MCP ระยะไกล**: Gemini 3 ไม่รองรับ MCP ระยะไกล ซึ่งจะพร้อมให้บริการเร็วๆ นี้
- **ความเข้ากันได้ของโมเดลแบบหลายรอบ**: เมื่อใช้โมเดลต่างๆ ผสมกันในการสนทนา (ทั้งแบบเก็บสถานะและไม่เก็บสถานะ) โมเดลถัดไปต้องรองรับรูปแบบเอาต์พุตของโมเดลก่อนหน้าเป็นอินพุต ตัวอย่างเช่น หากคุณสร้างรูปภาพโดยใช้ `gemini-3.1-flash-image` คุณจะไม่สามารถสนทนาต่อด้วยโมเดลที่ไม่รับอินพุตรูปภาพ (เช่น โมเดลข้อความเท่านั้นหรือโมเดลการสร้างเพลงอย่าง Lyria)

[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=th) API รองรับฟีเจอร์ต่อไปนี้ แต่ **ยังไม่
พร้อมใช้งาน** ใน Interactions API

- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**
- **[การเรียกใช้ฟังก์ชันอัตโนมัติ (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=th#automatic_function_calling_python_only)**
- **[การแคชอย่างชัดแจ้ง](https://ai.google.dev/gemini-api/docs/caching?hl=th)**: โปรดทราบว่า Interactions API มีการแคชโดยนัยฝั่งเซิร์ฟเวอร์
  ผ่าน `previous_interaction_id`

## ความคิดเห็น

ความคิดเห็นของคุณมีความสำคัญอย่างยิ่งต่อการพัฒนา Interactions API
โปรดแชร์ความคิดเห็น รายงานข้อบกพร่อง หรือขอฟีเจอร์ใน
[ฟอรัมชุมชนนักพัฒนาแอป Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=th)

## ขั้นตอนถัดไป

- ลองใช้ [Notebook Quickstart ของ Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=th)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับ [Agent Deep Research ของ Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-15 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-15 UTC"],[],[]]
