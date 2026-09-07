---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=th
fetched_at: 2026-09-07T05:46:42.444438+00:00
title: "\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e43\u0e2b\u0e21\u0e48\u0e43\u0e19 Gemini 3.8 Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# มีอะไรใหม่ใน Gemini 3.8 Flash

[ดูโมเดลทั้งหมด](https://ai.google.dev/gemini-api/docs/models?hl=th)

Gemini 3.8 Flash (`gemini-3.8-flash`) พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) และพร้อมสำหรับการใช้งานจริงแล้ว โดยเป็นโมเดล Flash ที่ชาญฉลาดที่สุดของเรา ซึ่งออกแบบมาเพื่อการพัฒนาซอฟต์แวร์ในระยะยาว, Agent ที่ทำงานได้ด้วยตัวเอง และเวิร์กโฟลว์ที่ซับซ้อนขององค์กร

คู่มือนี้จะอธิบายสิ่งใหม่ๆ ใน Gemini 3.8 Flash, การเปลี่ยนแปลง API, ตัวอย่างโค้ด และคำแนะนำในการย้ายข้อมูล

## โมเดลใหม่

| รุ่น | รหัสโมเดล | ระดับการคิดเริ่มต้น | ราคา | คำอธิบาย |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash พร้อมให้บริการจนถึงสิ้นปีในราคาช่วงแนะนำที่ $0.75/1M โทเค็นขาเข้า และ $3.75/1M โทเค็นขาออก โปรดดูรายละเอียดเพิ่มเติมเกี่ยวกับ[ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th) | โมเดล Flash ที่ชาญฉลาดที่สุดของเรา ซึ่งออกแบบมาเพื่อการพัฒนาซอฟต์แวร์ในระยะยาว, Agent ที่ทำงานได้ด้วยตัวเอง และเวิร์กโฟลว์ที่ซับซ้อนขององค์กร |

Gemini 3.8 Flash รองรับหน้าต่างบริบทขนาด 1 ล้านโทเค็น, โทเค็นขาออกสูงสุด 64, 000 โทเค็น, ระดับการคิดที่ปรับได้ (`low`, `medium`, `high`) และชุดเครื่องมือในตัวที่ครอบคลุมชุดเดียวกัน

ดูข้อมูลจำเพาะทั้งหมดได้ในหน้าโมเดล [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=th) ดูรายละเอียดราคาแนะนำได้ใน[ส่วนราคา](#pricing)ด้านล่างหรือใน[หน้าราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.8-flash)

## คู่มือเริ่มใช้งานฉบับย่อ

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
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
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## สิ่งใหม่ๆ ใน Gemini 3.8 Flash

- **การพัฒนาซอฟต์แวร์ในระยะยาว:** ให้ผลลัพธ์ที่ยอดเยี่ยมในการเปรียบเทียบการเขียนโค้ดในโลกแห่งความเป็นจริง, การปรับโครงสร้างไฟล์หลายไฟล์ที่ซับซ้อน และการดำเนินการเครื่องมือที่กำหนดได้ ดูรายละเอียดได้ใน[ระเบียบวิธีวิจัย](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=th)
- **Agent ที่ทำงานได้ด้วยตัวเอง:** ช่วยให้คุณสร้างเวิร์กโฟลว์การวางแผนและการจัดการเครื่องมือแบบหลายขั้นตอนที่ยืดหยุ่นได้ ซึ่งจะช่วยลดการวนซ้ำและข้อผิดพลาดที่ล้มเหลวลงอย่างมาก
- **เวิร์กโฟลว์ที่ซับซ้อนขององค์กร:** ให้ความแม่นยำที่เหนือกว่า, การให้เหตุผลเชิงลึก และความถูกต้องของข้อเท็จจริงสูงในงานโดเมนที่ต้องใช้ความสามารถสูงและไปป์ไลน์ข้อมูลขนาดใหญ่
- **โมเดลเริ่มต้นสำหรับ Managed Agents:** Agent เริ่มต้นสำหรับ Managed Agents ซึ่งก็คือ Agent ของ [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th) ตอนนี้ใช้ Gemini 3.8 Flash แล้ว นอกจากนี้ [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=th) ยังใช้ Gemini 3.8 Flash เป็นค่าเริ่มต้นด้วย
- **ราคาแนะนำ:** Gemini 3.8 Flash พร้อมให้บริการในราคาแนะนำที่ $0.75/1M โทเค็นขาเข้า และ $3.75/1M โทเค็นขาออกจนถึงวันที่ 31 ธันวาคม 2026 ราคามาตรฐานที่ $1.50/1M โทเค็นขาเข้า และ $7.50/1M โทเค็นขาออกจะมีผลตั้งแต่วันที่ 1 มกราคม 2027

Gemini 3.8 Flash สามารถใช้โทเค็นมากขึ้นในงานที่ใช้เวลานานขึ้นและซับซ้อนขึ้น ซึ่งเป็นไปตามการออกแบบ โมเดลจะใช้ขั้นตอนการให้เหตุผลที่สั้นลง เรียกใช้เครื่องมือซ้ำๆ และตรวจสอบงานไปพร้อมๆ กัน เพื่อให้ได้ผลลัพธ์ที่มีคุณภาพสูงขึ้นสำหรับเป้าหมายที่ยากและมีหลายขั้นตอน เวิร์กโฟลว์บางอย่างอาจไม่จำเป็นต้องมีการตรวจสอบในระดับนี้ สำหรับงานในชีวิตประจำวัน คุณสามารถลดความพยายามในการให้เหตุผลเพื่อลดการใช้โทเค็นได้ หรือจะใช้ Gemini 3.7 Flash ซึ่งยังคงได้รับการสนับสนุนอย่างเต็มที่ก็ได้

## ทำความเข้าใจระดับการให้เหตุผล

Gemini 3.8 Flash ช่วยให้คุณควบคุมเวลาในการตอบสนองและความชาญฉลาดได้อย่างยืดหยุ่นโดยการปรับระดับการคิดของโมเดล

- **การประมวลผลความคิดต่ำ**: ลดเวลาในการตอบสนองสำหรับงานที่สำคัญต่อเวลาในการตอบสนอง เช่น ไปป์ไลน์การตอบสนองต่อเหตุการณ์, การแชทแบบเรียลไทม์, การเขียนฉบับร่าง และการวิเคราะห์ข้อมูลอย่างรวดเร็ว
- **ปานกลาง (ค่าเริ่มต้น):** คุณภาพดีที่สุดสำหรับงานส่วนใหญ่ แนะนำให้ใช้กับโค้ดที่ซับซ้อนและกรณีการใช้งานแบบ Agent ซึ่งจะให้ความแม่นยำในการผ่านครั้งแรกสูงขึ้น
- **ความพยายามในการคิดสูง**: เพิ่มความสามารถในการให้เหตุผลและการจัดการเครื่องมือของโมเดลให้ได้มากที่สุด เหมาะที่สุดสำหรับการให้เหตุผลเชิงลึก, คณิตศาสตร์ และงานที่ซับซ้อนหลายขั้นตอน

ตัวอย่างต่อไปนี้จะตั้งค่า `thinking_level` เป็น `medium` สำหรับคำขอวิเคราะห์โค้ดที่ซับซ้อน

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
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
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Agent ของ Antigravity ที่อัปเดตแล้ว

เนื่องจากประสิทธิภาพและการให้เหตุผลที่ได้รับการปรับปรุง ตอนนี้ Agent ของ [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th) ใน Gemini Managed Agents จึงสร้างขึ้นด้วย Gemini 3.8 Flash เป็นค่าเริ่มต้น

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

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
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

คุณสามารถกำหนดค่าโมเดล Gemini ที่อยู่เบื้องหลัง [ได้](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#model-selection) โดยใช้ `agent_config`

## รายการตรวจสอบการย้ายข้อมูล

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### ย้ายข้อมูลไปใช้ gemini-3.8-flash

- **อัปเดตรหัสโมเดล:** เปลี่ยนสตริงโมเดลเป้าหมายเป็น `gemini-3.8-flash`
- **นำพารามิเตอร์การสุ่มตัวอย่างที่เลิกใช้งานแล้วออก**
  - นำ `temperature`, `top_p` และ `top_k` ออกจากการกำหนดค่าการสร้าง
  - แทนที่ `thinking_budget` ด้วย enum สตริง `thinking_level` โปรดทราบว่า 3.8 Flash ไม่รองรับ `minimal`
  - นำ `candidate_count` ออก (ไม่รองรับใน Gemini 3 ขึ้นไป)
- **บังคับใช้กฎการตรวจสอบเทิร์น**
  - กำหนดการสนทนาไปมาแบบหลายเทิร์นให้เป็นมาตรฐานใน `previous_interaction_id` ฝั่งเซิร์ฟเวอร์
  - นำเทิร์นของโมเดลที่ป้อนไว้ล่วงหน้าออก
- **ตรวจสอบการเรียกฟังก์ชัน**
  - วางเนื้อหาหลายรูปแบบไว้ในเพย์โหลดการตอบกลับ
  - จัดรูปแบบคำแนะนำแบบอินไลน์โดยใช้ `\n\n`
  - หากเห็นข้อผิดพลาด `Malformed_Function_Call` ที่เชื่อมโยงกับข้อความก่อนเครื่องมือ โปรดดู [วิธีแก้ปัญหาสำหรับข้อกำหนดข้อความก่อนเครื่องมือ](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#workarounds-for-pre-tool-text-requirements)
  - เฉพาะในกรณีที่ใช้ generateContent API: ตรวจสอบว่าออบเจ็กต์ `FunctionResponse` ทั้งหมดมี `call_id` และ `name`
- **ข้อกำหนดพื้นฐานของ Gemini 3:** สำหรับการอัปเดต SDK และการเก็บรักษาลายเซ็นความคิด โปรดดู[รายการตรวจสอบการย้ายข้อมูล Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=th#migration)

## ราคา

ใช้ประโยชน์จากราคาแนะนำใน Google AI Studio และแพลตฟอร์ม Agent ของ Gemini Enterprise จนถึงวันที่ 31 ธันวาคม 2026 สำหรับ Gemini 3.8 Flash, Gemini 3.7 Flash และ Gemini 3.6 Flash ราคามาตรฐานจะมีผลตั้งแต่วันที่ 1 มกราคม 2027 ดูระดับราคาทั้งหมดได้ใน[หน้าราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.8-flash)

## ขั้นตอนถัดไป

- ตรวจสอบข้อมูลจำเพาะของ API ใน [ภาพรวมของโมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)
- สำรวจการจัดการ Agent หลายรายการใน[ภาพรวมของ Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
- ทดสอบและปรับแต่งพรอมต์ใน [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-03 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-03 UTC"],[],[]]
