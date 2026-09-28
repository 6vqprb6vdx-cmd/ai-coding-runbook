---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=th
fetched_at: 2026-09-28T06:23:14.384391+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

# Gemini API

Gemini API เป็นเส้นทางที่เร็วที่สุดจากพรอมต์ไปสู่การผลิตด้วย Gemini, Veo,
Nano Banana และอื่นๆ ซึ่งช่วยให้คุณผสานรวมโมเดล Generative เหล่านี้เข้ากับแอปพลิเคชันเพื่อสร้างข้อความและรูปภาพ วิเคราะห์อินพุตหลายรูปแบบ และสร้างเอเจนต์สนทนา

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

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

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[เริ่มสร้าง](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)

---

## พบกับโมเดล

[ดูทั้งหมด](https://ai.google.dev/gemini-api/docs/models?hl=th)

[auto\_awesome
Gemini 3.1 Pro
ใหม่

โมเดลที่ชาญฉลาดที่สุดของเรา ซึ่งเป็นโมเดลที่ดีที่สุดในโลกสำหรับการทำความเข้าใจข้อมูลหลายรูปแบบ ทั้งหมดนี้สร้างขึ้นบนพื้นฐานของการให้เหตุผลที่ล้ำสมัย](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th)
[spark
Gemini 3.6 Flash
ใหม่

โมเดลล่าสุดของเราที่ผสานความเร็วเข้ากับความชาญฉลาดเพื่อมอบประสิทธิภาพที่ยอดเยี่ยมในงานแบบเป็น Agent และงานแบบมัลติโมดัล](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th)
[spark
Gemini 3.5 Flash

ประสิทธิภาพระดับแนวหน้าเทียบเท่าโมเดลขนาดใหญ่กว่าในราคาที่ถูกกว่า](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th)
[graphic\_eq
TTS ของ Gemini 3.8 Flash
ใหม่

โมเดลการอ่านออกเสียงข้อความระดับสตูดิโอที่มีการแสดงออกที่สื่ออารมณ์ การออกแบบเสียงที่กำหนดเอง และการจำลองเสียง](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th)
[spark
Gemini 3.5 Flash-Lite
ใหม่

โมเดลที่มีปริมาณมากและคำนึงถึงต้นทุนซึ่งได้รับการเพิ่มประสิทธิภาพสำหรับงานของตัวแทนย่อยที่มีเวลาในการตอบสนองต่ำและมีปริมาณงานสูง](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th)
[spark
Gemini 3.1 Flash-Lite

โมเดลที่มีปริมาณสูงและคำนึงถึงต้นทุน พร้อมประสิทธิภาพและคุณภาพของซีรีส์ Gemini 3](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th)
[spark
Gemini 3 Flash

ประสิทธิภาพระดับแนวหน้าเทียบเท่าโมเดลขนาดใหญ่กว่าในราคาที่ถูกกว่า](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th)
[🍌
Nano Banana 2 และ Nano Banana Pro

โมเดลการสร้างและแก้ไขรูปภาพที่ล้ำสมัย](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)
[video\_library
Veo 3.1

โมเดลการสร้างวิดีโอสุดล้ำของเราพร้อมเสียงแบบเนทีฟ](https://ai.google.dev/gemini-api/docs/video?hl=th)
[spark
Gemini Robotics

โมเดลวิชันภาษา (VLM) ที่นำความสามารถด้าน Agentic AI ของ Gemini มาใช้กับหุ่นยนต์และช่วยให้การให้เหตุผลขั้นสูงในโลกกายภาพเป็นไปได้](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th)

## สำรวจความสามารถ

[imagesmode

การสร้างรูปภาพโดยตรง (Nano Banana)

สร้างและแก้ไขรูปภาพที่มีบริบทสูงได้โดยตรงด้วย Gemini 2.5 Flash สำหรับรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)
[article

บริบทแบบยาว

ป้อนโทเค็นหลายล้านรายการลงในโมเดล Gemini และรับความเข้าใจจากรูปภาพ วิดีโอ และเอกสารที่ไม่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/long-context?hl=th)
[code

เอาต์พุตที่มีโครงสร้าง

จำกัดให้ Gemini ตอบกลับด้วย JSON ซึ่งเป็นรูปแบบข้อมูลที่มี Structured Data ที่เหมาะสำหรับการประมวลผลอัตโนมัติ](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)
[functions

การเรียกใช้ฟังก์ชัน

สร้างเวิร์กโฟลว์แบบเอเจนต์โดยเชื่อมต่อ Gemini กับ API และเครื่องมือภายนอก](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
[videocam

การสร้างวิดีโอด้วย Veo 3.1

สร้างเนื้อหาวิดีโอคุณภาพสูงจากพรอมต์ข้อความหรือรูปภาพด้วยโมเดลสุดล้ำของเรา](https://ai.google.dev/gemini-api/docs/video?hl=th)
[android\_recorder

เอเจนต์เสียงที่มี Live API

สร้างแอปพลิเคชันและเอเจนต์เสียงแบบเรียลไทม์ด้วย Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)
[build

เครื่องมือ

เชื่อมต่อ Gemini กับโลกภายนอกผ่านเครื่องมือในตัว เช่น Google Search, บริบท URL, Google Maps, การดำเนินการโค้ด และการใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/tools?hl=th)
[stacks

การทำความเข้าใจเอกสาร

ประมวลผลไฟล์ PDF ได้สูงสุด 1,000 หน้าด้วยความสามารถในการทำความเข้าใจข้อมูลหลายรูปแบบอย่างเต็มที่ หรือไฟล์ประเภทอื่นๆ ที่เป็นข้อความ](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)
[cognition\_2

กำลังคิด

ดูว่าความสามารถในการคิดช่วยปรับปรุงการให้เหตุผลสำหรับงานและเอเจนต์ที่ซับซ้อนได้อย่างไร](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

[Google AI Studio

ทดสอบพรอมต์ จัดการคีย์ API ตรวจสอบการใช้งาน และสร้างต้นแบบ](https://aistudio.google.com?hl=th)
[group

ชุมชนนักพัฒนาแอป

ถามคำถามและค้นหาโซลูชันจากนักพัฒนาแอปคนอื่นๆ และวิศวกรของ Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=th)
[menu\_book

เอกสารอ้างอิง API

ดูข้อมูลโดยละเอียดเกี่ยวกับ Gemini API ได้ในเอกสารอ้างอิงอย่างเป็นทางการ](https://ai.google.dev/api?hl=th)
[sensors

สถานะ

ตรวจสอบสถานะของ Gemini API, Google AI Studio และบริการโมเดลของเรา](https://aistudio.google.com/status?hl=th)

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
