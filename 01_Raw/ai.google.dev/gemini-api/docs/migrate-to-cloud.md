---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=th
fetched_at: 2026-10-19T05:31:07.085331+00:00
title: "Gemini Developer API \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21 Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Gemini Developer API เทียบกับแพลตฟอร์ม Gemini

เมื่อพัฒนาโซลูชัน Generative AI ด้วย Gemini ทาง Google มีผลิตภัณฑ์ API 2 รายการ ได้แก่ [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=th) และ [Gemini Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=th)

Gemini Developer API เป็นเส้นทางที่เร็วที่สุดในการสร้าง ทำให้พร้อมใช้งานจริง และ
ปรับขนาดแอปพลิเคชันที่ทำงานด้วย Gemini นักพัฒนาแอปส่วนใหญ่ควรใช้ Gemini Developer
API เว้นแต่จะจำเป็นต้องใช้การควบคุมเฉพาะสำหรับองค์กร

แพลตฟอร์ม Gemini มีระบบนิเวศที่ครอบคลุมของฟีเจอร์และบริการที่พร้อมใช้งานในองค์กร
สำหรับการสร้างและติดตั้งใช้งานแอปพลิเคชัน Generative AI ที่ขับเคลื่อนโดย
Google Cloud

เมื่อเร็วๆ นี้ เราได้ทำให้การย้ายข้อมูลระหว่างบริการเหล่านี้ง่ายขึ้น ตอนนี้คุณเข้าถึงทั้ง Gemini
Developer API และ Gemini Platform API ได้แล้ว
ผ่าน [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=th) แบบรวมและ
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)

## การเปรียบเทียบโค้ด: Interactions API (แนะนํา)

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) เป็นวิธีที่แนะนําในการสร้างด้วยโมเดลและเอเจนต์ของ Gemini
ตัวอย่างต่อไปนี้
เปรียบเทียบการสร้างข้อความระหว่าง Gemini Developer API กับแพลตฟอร์ม Gemini

### Python

คุณเข้าถึงทั้ง Gemini Developer API และบริการแพลตฟอร์ม Gemini
ได้ผ่านไลบรารี `google-genai` (`>= 2.3.0`) ดูวิธีการติดตั้ง
`google-genai` ได้ในหน้า[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

### Gemini Developer API

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### Gemini Platform API

```
from google import genai

client = genai.Client(
    enterprise=True, project="your-project-id", location="global"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### JavaScript และ TypeScript

คุณสามารถเข้าถึงทั้ง Gemini Developer API และบริการแพลตฟอร์ม Gemini
ผ่านไลบรารี `@google/genai` (`>= 2.3.0`) ดูวิธีการติดตั้ง
`@google/genai` ได้ในหน้า[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### Gemini Platform API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  enterprise: true,
  project: "your_project",
  location: "global",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

## การเปรียบเทียบโค้ด: API ของ generateContent

แม้ว่าเราจะแนะนำให้ใช้ Interactions API สำหรับโปรเจ็กต์ใหม่ แต่ระบบจะยังคงรองรับ `generateContent` API ต่อไป

### Python

คุณสามารถเข้าถึงทั้ง Gemini Developer API และบริการแพลตฟอร์ม Gemini
ได้ผ่านไลบรารี `google-genai` ดูวิธีการติดตั้ง
`google-genai`ได้ที่หน้า[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript และ TypeScript

คุณสามารถเข้าถึงทั้ง Gemini Developer API และบริการแพลตฟอร์ม Gemini
ผ่าน`@google/genai` ได้ ดูวิธีการติดตั้ง
`@google/genai` ได้ที่หน้า[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

คุณสามารถเข้าถึงทั้ง Gemini Developer API และบริการแพลตฟอร์ม Gemini
ผ่าน`google.golang.org/genai` library ดูวิธีการติดตั้ง
`google.golang.org/genai` ได้ที่หน้า[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google Cloud project
const project = "your-project"

// A Google Cloud location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### กรณีการใช้งานและแพลตฟอร์มอื่นๆ

ดูคำแนะนำเฉพาะสำหรับ Use Case ใน[เอกสารประกอบเกี่ยวกับ Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=th)
และ[เอกสารประกอบเกี่ยวกับแพลตฟอร์ม Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=th)
สำหรับแพลตฟอร์มและ Use Case อื่นๆ

## ข้อควรพิจารณาในการย้ายข้อมูล

สิ่งที่จะเกิดขึ้นเมื่อคุณย้ายข้อมูล

- คุณจะต้องใช้บัญชีบริการของ Google Cloud เพื่อตรวจสอบสิทธิ์ ดูข้อมูลเพิ่มเติมได้ที่
  [เอกสารประกอบเกี่ยวกับแพลตฟอร์ม Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=th)
- คุณสามารถใช้โปรเจ็กต์ Google Cloud ที่มีอยู่
  (โปรเจ็กต์เดียวกับที่ใช้สร้างคีย์ API) หรือจะ[สร้างโปรเจ็กต์ Google Cloud ใหม่](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=th)ก็ได้
- ภูมิภาคที่รองรับอาจแตกต่างกันระหว่าง Gemini Developer API กับ
  Gemini Platform API ในระหว่างเวอร์ชันตัวอย่าง [Interactions API ในแพลตฟอร์ม Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=th) รองรับเฉพาะปลายทาง `global` (`location="global"`) โปรดดูรายการ[ภูมิภาคที่รองรับสำหรับ Generative AI ใน Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=th)
- คุณต้องฝึกโมเดลที่สร้างใน Google AI Studio อีกครั้งในแพลตฟอร์ม Gemini

หากไม่จำเป็นต้องใช้คีย์ Gemini API สำหรับ Gemini Developer API อีกต่อไป
โปรดทำตามแนวทางปฏิบัติแนะนำด้านความปลอดภัยและลบคีย์ดังกล่าว

วิธีลบคีย์ API

1. เปิดหน้า
   [ข้อมูลเข้าสู่ระบบของ Google Cloud API](https://console.cloud.google.com/apis/credentials?hl=th)
2. ค้นหาคีย์ API ที่ต้องการลบ แล้วคลิกไอคอน**การดำเนินการ**
3. เลือก**ลบคีย์ API**
4. ในโมดัล**ลบข้อมูลเข้าสู่ระบบ** ให้เลือก**ลบ**

   การลบคีย์ API จะใช้เวลาสักครู่ในการเผยแพร่ หลังจาก
   การเผยแพร่เสร็จสมบูรณ์แล้ว ระบบจะปฏิเสธการเข้าชมที่ใช้คีย์ API ที่ลบไปแล้ว

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมได้ในคู่มือนักพัฒนาซอฟต์แวร์เกี่ยวกับ
  [Interactions API บนแพลตฟอร์ม Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=th)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับโซลูชัน Generative AI บนแพลตฟอร์ม Gemini ได้ที่
  [ภาพรวมของ Generative AI บนแพลตฟอร์ม Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-08 UTC"],[],[]]
