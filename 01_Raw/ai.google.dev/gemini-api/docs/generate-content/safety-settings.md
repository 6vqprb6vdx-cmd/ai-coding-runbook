---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/safety-settings?hl=th
fetched_at: 2026-10-19T05:43:41.787451+00:00
title: "\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# การตั้งค่าความปลอดภัย

Gemini API มีการตั้งค่าความปลอดภัยที่คุณปรับได้ในระหว่างขั้นตอนการสร้างต้นแบบเพื่อพิจารณาว่าแอปพลิเคชันของคุณต้องมีการกำหนดค่าความปลอดภัยที่เข้มงวดมากขึ้นหรือน้อยลง คุณสามารถปรับการตั้งค่าเหล่านี้ในหมวดหมู่ตัวกรอง 4 หมวดหมู่เพื่อจำกัดหรืออนุญาตเนื้อหาบางประเภท

คู่มือนี้จะอธิบายวิธีที่ Gemini API จัดการการตั้งค่าความปลอดภัยและการกรอง รวมถึงวิธีเปลี่ยนการตั้งค่าความปลอดภัยสำหรับแอปพลิเคชัน

## ตัวกรองความปลอดภัย

ตัวกรองความปลอดภัยที่ปรับได้ของ Gemini API ครอบคลุมหมวดหมู่ต่อไปนี้

| หมวดหมู่ | คำอธิบาย |
| --- | --- |
| การคุกคาม | ความคิดเห็นเชิงลบหรือเป็นอันตรายที่มุ่งเป้าไปที่อัตลักษณ์และ/หรือแอตทริบิวต์ที่ได้รับการคุ้มครอง |
| วาจาสร้างความเกลียดชัง | เนื้อหาที่ไม่สุภาพ ไม่ให้เกียรติ หรือหยาบคาย |
| เกี่ยวกับเรื่องเพศอย่างโจ่งแจ้ง | มีการอ้างอิงถึงการมีเพศสัมพันธ์หรือเนื้อหาลามกอื่นๆ |
| อันตราย | ส่งเสริม สนับสนุน หรือกระตุ้นให้เกิดการกระทำที่เป็นอันตราย |

หมวดหมู่เหล่านี้กำหนดไว้ใน [`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=th). คุณสามารถใช้ตัวกรองเหล่านี้เพื่อปรับเนื้อหาที่เหมาะสมกับกรณีการใช้งานของคุณ เช่น หากคุณกำลังสร้างบทสนทนาในวิดีโอเกม คุณอาจพิจารณาว่าการอนุญาตเนื้อหาเพิ่มเติมที่ได้รับการจัดประเภทเป็น *อันตราย* นั้นยอมรับได้เนื่องจากลักษณะของเกม

นอกจากตัวกรองความปลอดภัยที่ปรับได้แล้ว Gemini API ยังมีการป้องกันในตัวจากการกระทำที่เป็นอันตรายหลักๆ เช่น เนื้อหาที่อาจเป็นอันตรายต่อความปลอดภัยของเด็ก
ระบบจะบล็อกการกระทำที่เป็นอันตรายประเภทนี้เสมอและไม่สามารถปรับได้

### ระดับการกรองเนื้อหาเพื่อความปลอดภัย

Gemini API จัดประเภทระดับความน่าจะเป็นที่เนื้อหาจะไม่ปลอดภัยเป็น
`HIGH`, `MEDIUM`, `LOW`, หรือ `NEGLIGIBLE`

Gemini API จะบล็อกเนื้อหาตามความน่าจะเป็นที่เนื้อหาจะไม่ปลอดภัย ไม่ใช่ความรุนแรง คุณควรพิจารณาเรื่องนี้เนื่องจากเนื้อหาบางอย่างอาจมีความน่าจะเป็นต่ำที่จะไม่ปลอดภัยแม้ว่าความรุนแรงของอันตรายจะยังสูงอยู่ก็ตาม เช่น การเปรียบเทียบประโยคต่อไปนี้

1. หุ่นยนต์ชกฉัน
2. หุ่นยนต์ฟันฉัน

ประโยคแรกอาจมีความน่าจะเป็นสูงกว่าที่จะไม่ปลอดภัย แต่คุณอาจพิจารณาว่าประโยคที่ 2 มีความรุนแรงสูงกว่าในแง่ของความรุนแรง
ดังนั้น คุณจึงควรทดสอบอย่างละเอียดและพิจารณาว่าจำเป็นต้องมีระดับการบล็อกที่เหมาะสมใดบ้างเพื่อรองรับกรณีการใช้งานหลักๆ ขณะเดียวกันก็ลดอันตรายต่อผู้ใช้ปลายทางให้เหลือน้อยที่สุด

### การกรองเพื่อความปลอดภัยต่อคำขอ

คุณสามารถปรับการตั้งค่าความปลอดภัยสำหรับคำขอแต่ละรายการที่ส่งไปยัง API เมื่อคุณส่งคำขอ ระบบจะวิเคราะห์เนื้อหาและกำหนดการจัดประเภทความปลอดภัย การจัดประเภทความปลอดภัยจะรวมถึงหมวดหมู่และความน่าจะเป็นของการจัดประเภทอันตราย เช่น หากระบบบล็อกเนื้อหาเนื่องจากหมวดหมู่การคุกคามมีความน่าจะเป็นสูง การจัดประเภทความปลอดภัยที่แสดงผลจะมีหมวดหมู่เท่ากับ `HARASSMENT` และความน่าจะเป็นของอันตรายตั้งค่าเป็น `HIGH`

ตัวกรองเพิ่มเติมจะ**ปิด** อยู่โดยค่าเริ่มต้นเนื่องจากความปลอดภัยโดยธรรมชาติของโมเดล
หากเลือกเปิดใช้ คุณสามารถกำหนดค่าระบบให้บล็อกเนื้อหาตามความน่าจะเป็นที่เนื้อหาจะไม่ปลอดภัย ลักษณะการทำงานเริ่มต้นของโมเดลครอบคลุมกรณีการใช้งานส่วนใหญ่ ดังนั้นคุณควรปรับการตั้งค่าเหล่านี้ก็ต่อเมื่อแอปพลิเคชันของคุณต้องใช้การตั้งค่าเหล่านี้อย่างสม่ำเสมอเท่านั้น

ตารางต่อไปนี้อธิบายการตั้งค่าการบล็อกที่คุณปรับได้สำหรับแต่ละหมวดหมู่ เช่น หากคุณตั้งค่าการบล็อกเป็น**บล็อกบางส่วน** สำหรับหมวดหมู่**วาจาสร้างความเกลียดชัง** ระบบจะบล็อกทุกอย่างที่มีความน่าจะเป็นสูงที่จะเป็นเนื้อหาวาจาสร้างความเกลียดชัง แต่จะอนุญาตเนื้อหาที่มีความน่าจะเป็นต่ำกว่า

| เกณฑ์ (Google AI Studio) | เกณฑ์ (API) | คำอธิบาย |
| --- | --- | --- |
| ปิด | `OFF` | ปิดตัวกรองความปลอดภัย |
| ไม่บล็อก | `BLOCK_NONE` | แสดงเสมอไม่ว่าความน่าจะเป็นที่เนื้อหาจะไม่ปลอดภัยจะเป็นเท่าใดก็ตาม |
| บล็อกบางส่วน | `BLOCK_ONLY_HIGH` | บล็อกเมื่อมีความน่าจะเป็นสูงที่เนื้อหาจะไม่ปลอดภัย |
| บล็อกบางส่วน | `BLOCK_MEDIUM_AND_ABOVE` | บล็อกเมื่อมีความน่าจะเป็นปานกลางหรือสูงที่เนื้อหาจะไม่ปลอดภัย |
| บล็อกส่วนใหญ่ | `BLOCK_LOW_AND_ABOVE` | บล็อกเมื่อมีความน่าจะเป็นต่ำ ปานกลาง หรือสูงที่เนื้อหาจะไม่ปลอดภัย |
| ไม่มี | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | ไม่ได้ระบุเกณฑ์ไว้ ให้บล็อกโดยใช้เกณฑ์เริ่มต้น |

หากไม่ได้ตั้งค่าเกณฑ์ เกณฑ์การบล็อกเริ่มต้นจะเป็น**ปิด** สำหรับโมเดล Gemini 2.5 ขึ้นไป

คุณสามารถตั้งค่าเหล่านี้สำหรับคำขอแต่ละรายการที่ส่งไปยังบริการแบบ Generative
ดูรายละเอียดได้ที่เอกสารอ้างอิง API ของ [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=th#harmblockthreshold)

### ความคิดเห็นด้านความปลอดภัย

[`generateContent`](https://ai.google.dev/api/generate-content?hl=th#method:-models.generatecontent)
จะแสดงผล
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=th#generatecontentresponse) ซึ่ง
รวมถึงความคิดเห็นด้านความปลอดภัย

ความคิดเห็นเกี่ยวกับพรอมต์จะรวมอยู่ใน
[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=th#promptfeedback) หากตั้งค่า `promptFeedback.blockReason` ไว้ แสดงว่าระบบบล็อกเนื้อหาของพรอมต์

ความคิดเห็นเกี่ยวกับตัวเลือกคำตอบจะรวมอยู่ใน
[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=th#candidate) และ
[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=th#candidate) หากระบบบล็อกเนื้อหาคำตอบและ `finishReason` เป็น `SAFETY` คุณสามารถตรวจสอบ `safetyRatings` เพื่อดูรายละเอียดเพิ่มเติม ระบบจะไม่แสดงผลเนื้อหาที่ถูกบล็อก

## ปรับการตั้งค่าความปลอดภัย

ส่วนนี้จะอธิบายวิธีปรับการตั้งค่าความปลอดภัยทั้งใน Google AI Studio และในโค้ด

### Google AI Studio

คุณสามารถปรับการตั้งค่าความปลอดภัยใน Google AI Studio

คลิก**การตั้งค่าความปลอดภัย** ในส่วน**การตั้งค่าขั้นสูง** ในแผง**การตั้งค่าการเรียกใช้** เพื่อเปิดโมดัล**การตั้งค่าความปลอดภัยในการเรียกใช้** ในโมดัล คุณสามารถใช้แถบเลื่อนเพื่อปรับระดับการกรองเนื้อหาตามหมวดหมู่ความปลอดภัยได้ดังนี้

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=th)

เมื่อคุณส่งคำขอ (เช่น ถามคำถามกับโมเดล) ข้อความwarning
**ระบบบล็อกเนื้อหา** จะปรากฏขึ้นหากระบบบล็อกเนื้อหาของคำขอ หากต้องการดูรายละเอียดเพิ่มเติม ให้วางตัวชี้เหนือข้อความ**ระบบบล็อกเนื้อหา** เพื่อดูหมวดหมู่และความน่าจะเป็นของการจัดประเภทอันตราย

### ตัวอย่างโค้ด

ข้อมูลโค้ดต่อไปนี้แสดงวิธีตั้งค่าความปลอดภัยในการเรียกใช้ `GenerateContent` ซึ่งจะเป็นการกำหนดเกณฑ์สำหรับหมวดหมู่วาจาสร้างความเกลียดชัง (`HARM_CATEGORY_HATE_SPEECH`) การตั้งค่าหมวดหมู่นี้เป็น `BLOCK_LOW_AND_ABOVE` จะบล็อกเนื้อหาที่มีความน่าจะเป็นต่ำหรือสูงกว่าที่จะเป็นวาจาสร้างความเกลียดชัง หากต้องการทำความเข้าใจการตั้งค่าเกณฑ์ โปรดดู [การกรองเพื่อความปลอดภัย
ต่อคำขอ](#safety-filtering-per-request)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
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

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .category(HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH)
        .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(Arrays.asList(hateSpeechSafety))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Some potentially unsafe prompt.", config);

System.out.println(response.text());
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## ขั้นตอนถัดไป

- ดู[เอกสารอ้างอิง API](https://ai.google.dev/api?hl=th) เพื่อดูข้อมูลเพิ่มเติมเกี่ยวกับ API ทั้งหมด
- อ่าน[คำแนะนำด้านความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=th)เพื่อดูภาพรวมของข้อควรพิจารณาด้านความปลอดภัย
  เมื่อพัฒนาด้วย LLM
- ดูข้อมูลเพิ่มเติมเกี่ยวกับการประเมินความน่าจะเป็นเทียบกับความรุนแรงจากทีม [Jigsaw](https://developers.perspectiveapi.com/s/about-the-api-score)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับผลิตภัณฑ์ที่ช่วยสร้างโซลูชันด้านความปลอดภัย เช่น
  [Perspective
  API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7)
  \* คุณสามารถใช้การตั้งค่าความปลอดภัยเหล่านี้เพื่อสร้างตัวแยกประเภทความเป็นพิษ
  ดูตัวอย่าง[การแยกประเภท
  เพื่อ
  เริ่มต้นใช้งาน](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-15 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-15 UTC"],[],[]]
